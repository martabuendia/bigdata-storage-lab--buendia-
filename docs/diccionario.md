# Diccionario de Datos

> Completar con la descripción de campos, tipos, dominios y reglas de negocio.
# 📖 Diccionario de Datos

## Esquema Canónico
El modelo de datos consolidado se basa en un **esquema canónico** que homogeniza los distintos orígenes en tres campos principales:

| Campo   | Tipo        | Formato / Unidad | Descripción                                           |
|---------|-------------|------------------|-------------------------------------------------------|
| date    | Date        | `YYYY-MM-DD`     | Fecha de la transacción o registro.                   |
| partner | String      | Texto libre      | Identificador o nombre de la contraparte (cliente/proveedor). |
| amount  | Float (EUR) | Euros            | Monto monetario asociado, siempre expresado en EUR.   |

---

## Mapeos Origen → Canónico
Ejemplos típicos de cómo distintos orígenes de CSV se normalizan al esquema canónico:

| Origen (columna CSV) | Transformación / Normalización | Campo Canónico |
|-----------------------|--------------------------------|----------------|
| `fecha`, `dt`, `transaction_date` | Parsear a formato `YYYY-MM-DD` (considerar zona horaria si aplica). | **date** |
| `cliente`, `partner_id`, `vendor` | Normalizar a texto plano sin caracteres especiales. | **partner** |
| `importe`, `monto`, `value_eur` | Convertir a tipo float en euros. | **amount** |
| `amount_usd` | Conversión a EUR usando tipo de cambio definido en parámetros. | **amount** |
| `sociedad`, `empresa` | Mapear al campo canónico **partner** si representa la contraparte. | **partner** |
| `date_time` | Extraer solo la parte de fecha y convertir a `YYYY-MM-DD`. | **date** |

---

> ⚠️ Nota: cualquier nueva fuente debe documentar explícitamente su **mapeo origen → canónico** antes de incorporarse al pipeline.
