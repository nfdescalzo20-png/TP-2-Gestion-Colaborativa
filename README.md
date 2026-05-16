
# ANÁLISIS DE VENTAS - CÉLULA DE DESARROLLO

# Integrantes del Equipo

P1 - Líder y Organizador (Hugo) = Gobernanza del repositorio y estructura inicial.
P2 - Desarrollador Técnico (Paco) = Scripts de análisis estadístico.
P3 - Revisor y QA (Luis) = Peer review, documentación y Pull Requests.

# Escenario Elegido

Escenario B – Análisis de Ventas de una Pequeña Empresa

# Dataset Utilizado

- Archivo = `datos/dataset.csv`
- Registros = 100 filas
- Columnas = fecha, producto, cantidad, precio, venta_total

# Instrucciones para Ejecutar el Script en Google Colab

1. Clonar el repositorio:

   !git clone https://github.com/nfdescalzo20-png/TP-2-Gestion-Colaborativa.git

2. Navegar a la carpeta del proyecto:

   %cd TP-2-Gestion-Colaborativa

3. Ejecutar el script de análisis:

   !python scripts/analisis_ventas.py

4. Los resultados se guardan automáticamente en `/resultados/grafico_ventas_mensuales.png`

# Indicadores que genera el análisis

- Ventas totales del período
- Producto más vendido por cantidad
- Ventas agrupadas por mes
- Gráfico de evolución de ventas mensual

# Gestión del Proyecto

Las tareas de este proyecto fueron gestionadas mediante Jira bajo la clave `ADVT2O`.
Cada commit del repositorio incluye el ID del Issue correspondiente para garantizar la trazabilidad entre la gestión y el código.
    