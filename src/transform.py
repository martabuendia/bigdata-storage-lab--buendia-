# Normalización y construcción de zonas bronze/silver
def transform_to_bronze(df):
    # TODO: Guardar versión cruda en zona bronze
    pass

def transform_to_silver(df):
    # TODO: Normalizar datos y guardar en zona silver
    pass

import pandas as pd
from typing import Dict

def normalize_columns(df: pd.DataFrame, mapping: Dict[str, str]) -> pd.DataFrame:
    """
    Normaliza un DataFrame hacia el esquema canónico.
    - Renombra columnas según mapping (origen -> canónico).
    - Parsea fechas a datetime (ISO).
    - Normaliza amount (quita símbolos €, comas europeas, convierte a float).
    - Limpia espacios en partner.
    """
    # Renombrar columnas
    df = df.rename(columns=mapping)

    # Fecha a datetime
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce", format="%Y-%m-%d")

    # Partner: quitar espacios alrededor
    if "partner" in df.columns:
        df["partner"] = df["partner"].astype(str).str.strip()

    # Amount: eliminar € y comas europeas, convertir a float
    if "amount" in df.columns:
        df["amount"] = (
            df["amount"]
            .astype(str)
            .str.replace("€", "", regex=False)
            .str.replace(".", "", regex=False)  # miles
            .str.replace(",", ".", regex=False)  # decimales
        )
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    return df


def to_silver(bronze: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega datos bronze → silver:
    - Agrupa por partner y mes (periodo → timestamp).
    - Suma amount.
    """
    if "date" not in bronze.columns or "partner" not in bronze.columns or "amount" not in bronze.columns:
        raise ValueError("El DataFrame bronze no contiene columnas canónicas necesarias.")

    # Crear columna month (primer día del mes como timestamp)
    bronze = bronze.copy()
    bronze["month"] = bronze["date"].dt.to_period("M").dt.to_timestamp()

    silver = (
        bronze.groupby(["partner", "month"], as_index=False)
        .agg({"amount": "sum"})
    )

    return silver
