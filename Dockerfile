FROM odoo:16.0

USER root

# Instalar dependencias del sistema si las necesitas
RUN apt-get update && apt-get upgrade -y && apt-get install -y nano git && apt-get clean && rm -rf /var/lib/apt/lists/*
