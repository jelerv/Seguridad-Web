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

#### 2. Levantar el entorno

Opción recomendada (todo el laboratorio):

```bash
docker compose up -d

Opción ligera (solo Juice Shop + apps del módulo actual):

```bash
docker compose up -d juice-shop

### 3. URLs principales del laboratorio

| Aplicación           | URL                         | Uso principal                               |
|----------------------|-----------------------------|---------------------------------------------|
| **Juice Shopy**      | http://localhost:3000       | Broken Access, XSS, Insecure Designy        |
| **DVWA**             | http://localhost:8080       | SQL Injection y niveles de dificultad       |
| **CrAP**             | http://localhost:8888       | Seguridad de APIs puras                     |
| **Apps del curso**   | Ver tabla de abajo          | Demostración vulnerable vs secure           |

Credenciales por defecto:

Juice Shop: admin@juice-sh.op / admin123
DVWA: admin / password

Tabla de Aplicaciones del Curso

| Módulo | Vulnerabilidad            | Vulnerable URL | Secure URL |
| 3      | Broken Access Control     | :5003          | :5004      |
| 4      | Security Misconfiguration | :5005          | :5006      |
| 5      | Software Supply Chain     | :5007          | :5008      |
| 6      | Cryptographic Failures    | :5009          | :5010      |
| 7      | Injection                 | :5001          | :5002      |
| 9      | Authentication Failures   | :5011          | :5012      |
| 10     | A08-A10 + API Avanzado    | :5013          | :5014      |

Comandos útiles
```bash
# Levantar todo
docker compose up -d

# Levantar solo Juice Shop + una app específica
docker compose up -d juice-shop vulnerable-injection secure-injection

# Ver estado de los contenedores
docker compose ps

# Ver logs de una aplicación
docker logs -f vulnerable-injection

# Reconstruir después de modificar código
docker compose up -d --build

# Detener todo
docker compose down
