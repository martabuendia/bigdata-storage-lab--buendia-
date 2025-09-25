# bigdata-storage-lab--buendia-
## 📌 Prompts de reflexión — Ejemplo de respuestas

1. **V dominante hoy vs V dominante si 2× tráfico**  
   Hoy la V dominante es **Variedad**, porque integramos CSV heterogéneos de distintos socios.  
   Si el tráfico se duplicara, la **Velocidad** se volvería crítica: habría más ingestas y validaciones en menos tiempo.  
   El diseño debe adaptarse a esa transición de prioridades.

2. **Trade-off elegido (ej.: más compresión vs CPU)**  
   Elegí **más compresión en disco** para reducir coste de almacenamiento.  
   El impacto es mayor uso de CPU al leer, pero lo mediré comparando tiempos de carga y coste de almacenamiento mensual.  
   El balance se evalúa según ahorro económico vs. latencia aceptable en consultas.

3. **Inmutabilidad + linaje = veracidad**  
   - Mejora la veracidad porque cada dataset queda congelado y trazado desde su origen, evitando dudas de manipulación.  
   - El coste añadido es mayor consumo de almacenamiento y complejidad de metadatos.  
   En conjunto se gana confianza y auditoría, aunque se paga con más recursos.

4. **KPI principal y SLA del dashboard**  
   - KPI: **ventas totales por partner y mes**.  
   - Habilita decisiones de priorización comercial y seguimiento de partners estratégicos.  
   - SLA: actualización diaria (24h), suficiente porque las decisiones no son en tiempo real sino de planificación.

5. **Riesgo principal del diseño y mitigación técnica concreta**  
   Riesgo: fallos en la **normalización de columnas** que rompan la cadena Bronze→Silver→Gold.  
   Mitigación: pruebas unitarias de mapeo de columnas + validaciones automáticas en `basic_checks` para detectar errores tempranos.  
   Así se reduce el impacto antes de que afecte a KPIs.
