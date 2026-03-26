# 🚀 Configuración del Entorno de Laboratorio

Bienvenido al curso **Seguridad en Aplicaciones Web y APIs basado en OWASP Top 10:2025**.

Este documento te guiará paso a paso para configurar todo el entorno necesario para aprovechar al máximo el curso.

## Requisitos mínimos del sistema

- **Docker Desktop** (versión 24 o superior) + Docker Compose
- **Python 3.11 o superior** (para ejecutar scripts locales)
- **8 GB de RAM** recomendados (12 GB o más ideal)
- **20 GB de espacio libre** en disco
- Sistema operativo: Windows 10/11, macOS o Linux

## Herramientas recomendadas

| Herramienta              | Propósito                              | Enlace de descarga                          |
|--------------------------|----------------------------------------|---------------------------------------------|
| **Burp Suite Community** | Proxy y testing manual                 | portswigger.net/burp/community              |
| **OWASP ZAP**            | Escaneo automatizado y proxy           | zaproxy.org                                 |
| **Postman**              | Testing de APIs                        | postman.com                                 |
| **sqlmap**               | Automatización de SQL Injection        | sqlmap.org                                  |
| **Nuclei**               | Escaneo rápido de vulnerabilidades     | nuclei.projectdiscovery.io                  |
| **jwt_tool**             | Análisis y explotación de JWT          | GitHub - ticarpi/jwt_tool                   |

## Pasos de instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/curso-seguridad-web-apis-owasp-top10-2025.git
cd curso-seguridad-web-apis-owasp-top10-2025
