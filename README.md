# Customer Profitability Report

Este módulo permite visualizar y analizar la rentabilidad por cliente a partir de las órdenes de venta confirmadas en Odoo.

## Funcionalidades

- Cálculo de:
  - Total de ventas por cliente.
  - Costo total (basado en `standard_price` y `product_uom_qty`).
  - Utilidad (ganancia).
  - Margen porcentual de rentabilidad.
- Vista tipo **árbol** con un botón por fila para imprimir el reporte PDF del cliente.
- **Vistas gráficas** interactivas:
  - Gráfico de barras por cliente:
    - Ventas totales
    - Costos
    - Ganancia
    - Margen
  - Gráfico de pastel para ventas totales
- **Reporte PDF por cliente**:
  - Incluye datos financieros resumidos
  - Incluye un gráfico de barras generado dinámicamente con [QuickChart](https://quickchart.io)

## Tecnologías utilizadas

- Odoo 16
- Python 3.10+
- SQL View (`customer_profitability_report`)
- QuickChart para gráficos externos
- Docker Ready

## Instalación

1. Copiar este módulo en el directorio de `addons`.
2. Reiniciar el servidor Odoo.
3. Instalar el módulo desde el menú **Apps**.
4. Acceder al menú **Customer Profitability** para comenzar a usarlo.

## Requisitos adicionales

Para que el reporte PDF genere correctamente el gráfico con QuickChart:

- El servidor Odoo debe tener acceso a Internet (para cargar las imágenes desde quickchart.io).
- No se requieren dependencias externas adicionales.

## Docker

Este módulo está diseñado para funcionar correctamente en entornos Docker.  
Consulta el archivo `docker-compose.yml` del proyecto para integrarlo con tu entorno.

## Créditos

Desarrollado por JSAC
