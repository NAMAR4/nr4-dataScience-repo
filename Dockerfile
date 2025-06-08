# Basis-Image definieren
FROM python:3.12-slim

# Arbeitsverzeichnis setzen
WORKDIR /app

# Python-Pakete installieren
RUN pip install --no-cache-dir numpy pandas matplotlib seaborn pytest
