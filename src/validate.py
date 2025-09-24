# Validación de calidad de datos
def validate_dataframe(df):
    # TODO: Implementar validaciones (nulos, duplicados, tipos de datos, etc.)
    pass

import pandas as pd
from typing import List

def basic_checks(df: pd.DataFrame) -> List[str]:
    """
    Realiza validaciones mínimas sobre el DataFrame canónico.
    - Verifica columnas canónicas presentes.
    - Verifica amount numérico y >= 0.
    - Verifica date en datetime.
    Devuelve lista de errores detectados.
    """
    errors: List[str] = []

    # Columnas requeridas
    required = {"date", "partner", "amount"}
    missing = required - set(df.columns)
    if missing:
        errors.append(f"Faltan columnas requeridas: {missing}")

    # amount numérico y >= 0
    if "amount" in df.columns:
        if not pd.api.types.is_numeric_dtype(df["amount"]):
            errors.append("La columna 'amount' no es numérica.")
        elif (df["amount"] < 0).any():
            errors.append("Existen valores negativos en 'amount'.")

    # date en datetime
    if "date" in df.columns:
        if not pd.api.types.is_datetime64_any_dtype(df["date"]):
            errors.append("La columna 'date' no está en formato datetime.")

    return errors
