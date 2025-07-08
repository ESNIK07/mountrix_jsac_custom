# Customer Profitability Report

Este módulo permite visualizar la rentabilidad por cliente a partir de las órdenes de venta confirmadas. Calcula:

- Total de ventas por cliente.
- Costo total (basado en `purchase_price` y `qty_delivered`).
- Utilidad.
- Margen porcentual.

## Tecnologías

- Odoo 16
- Python
- SQL View
- Docker Ready

## Instalación

1. Copiar este módulo en el path de `addons`.
2. Reiniciar Odoo y activar el módulo desde Apps.
3. Ir al menú “Customer Profitability”.

## Docker

Este módulo está diseñado para correr en entorno Docker. Ver `docker-compose.yml`.
