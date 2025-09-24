# Streamlit App - bigdata-storage-lab-<apellido>
import streamlit as st

st.title("Big Data Storage Lab - <apellido>")
st.write("App de visualización de KPIs y exploración de datos.")

import streamlit as st
import pandas as pd
from io import BytesIO

# Importar funciones del pipeline
from src.transform import normalize_columns, to_silver
from src.ingest import tag_lineage, concat_bronze
from src.validate import basic_checks

st.set_page_config(page_title="Big Data Storage Lab", layout="wide")

st.title("📊 Big Data Storage Lab")
st.write("De CSVs heterogéneos a un almacén analítico confiable.")

# --- Configuración en sidebar ---
st.sidebar.header("Configuración de columnas origen")
date_col = st.sidebar.text_input("Columna fecha (origen)", "fecha")
partner_col = st.sidebar.text_input("Columna partner (origen)", "cliente")
amount_col = st.sidebar.text_input("Columna amount (origen)", "importe")

mapping = {
    date_col: "date",
    partner_col: "partner",
    amount_col: "amount",
}

# --- Subida de archivos ---
uploaded_files = st.file_uploader(
    "Sube uno o varios CSVs", type="csv", accept_multiple_files=True
)

bronze_frames = []

if uploaded_files:
    for uploaded_file in uploaded_files:
        try:
            df = pd.read_csv(uploaded_file)
        except UnicodeDecodeError:
            df = pd.read_csv(uploaded_file, encoding="latin-1")

        # Normalización y linaje
        df = normalize_columns(df, mapping)
        df = tag_lineage(df, uploaded_file.name)
        bronze_frames.append(df)

    if bronze_frames:
        bronze = concat_bronze(bronze_frames)

        st.subheader("📂 Datos Bronze (unificados)")
        st.dataframe(bronze.head(20))

        # Validaciones
        errors = basic_checks(bronze)
        if errors:
            st.error("❌ Validaciones fallidas:")
            for e in errors:
                st.write(f"- {e}")
        else:
            st.success("✅ Validaciones correctas")

            # Derivar Silver
            silver = to_silver(bronze)

            st.subheader("🥈 Datos Silver (agregados)")
            st.dataframe(silver.head(20))

            # KPIs simples
            st.subheader("📈 KPIs")
            total_amount = silver["amount"].sum()
            total_partners = silver["partner"].nunique()
            st.metric("Total Amount (EUR)", f"{total_amount:,.2f}")
            st.metric("Partners únicos", total_partners)

            # Gráfico
            st.subheader("📊 Evolución mensual (Amount)")
            chart_data = silver.groupby("month")["amount"].sum().reset_index()
            st.bar_chart(chart_data, x="month", y="amount")

            # Descargas
            st.subheader("⬇️ Descargas")
            def convert_df(df):
                return df.to_csv(index=False).encode("utf-8")

            bronze_csv = convert_df(bronze)
            silver_csv = convert_df(silver)

            st.download_button(
                "Descargar Bronze CSV",
                data=bronze_csv,
                file_name="bronze.csv",
                mime="text/csv",
            )
            st.download_button(
                "Descargar Silver CSV",
                data=silver_csv,
                file_name="silver.csv",
                mime="text/csv",
            )
