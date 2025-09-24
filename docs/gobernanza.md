# Gobernanza de Datos

- Roles y responsabilidades.
- Normas de seguridad y cumplimiento.
- Reglas de acceso a datos.
- Ciclo de vida de los datasets.

# 🔐 Gobernanza de Datos

## Origen y Linaje
- **Origen**: todos los CSV provienen de fuentes públicas o sintéticas.
- **Linaje**: cada dataset debe trazar su paso por las zonas → raw → bronze → silver → gold.
- Se documenta en metadatos: fecha de carga, nombre de archivo, hash de integridad.

---

## Validaciones mínimas
- `date`: formato válido `YYYY-MM-DD` y rango coherente (no futuro > 1 año).
- `partner`: no nulo, sin caracteres prohibidos.
- `amount`: numérico, distinto de nulo, en rango definido por reglas de negocio.
- Integridad: conteo de filas pre/post transformación.

---

## Política de mínimos privilegios
- Acceso a datos según necesidad:
  - **Raw/Bronze** → restringido a ingenieros de datos.
  - **Silver/Gold** → accesibles a analistas y consumidores de BI.
- Credenciales y secretos nunca deben estar versionados en el repositorio.
- Todo acceso debe estar autenticado y registrado.

---

## Trazabilidad
- Cada transformación debe dejar un **log** con:
  - Fuente de datos original.
  - Fecha/hora de ejecución.
  - Regla aplicada.
  - Resultados (número de filas afectadas, errores detectados).
- Los KPIs en gold deben poder rastrearse hasta sus registros en silver.

---

## Roles
- **Ingeniero de Datos**: ingesta, validación, normalización, mantenimiento del pipeline.
- **Analista de Datos**: explotación de silver/gold, definición de KPIs.
- **Administrador de Datos**: políticas de acceso, seguridad y cumplimiento.
- **Owner del Negocio**: validación de reglas de negocio y uso final de KPIs.
