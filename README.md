# Curso: Seguridad en Aplicaciones Web y APIs  
**Basado en OWASP Top 10:2025 + OWASP API Security Top 10 2023**

Repositorio oficial del curso **práctico y hands-on** de seguridad en aplicaciones web y APIs.

## Descripción

Curso completo de 48-60 horas que cubre las 10 vulnerabilidades más críticas según OWASP Top 10 2025, con fuerte énfasis en APIs modernas. Incluye explotación, mitigación, laboratorios prácticos y buenas prácticas reales.

## Características

- **12 módulos** completamente estructurados
- Entorno completo con Docker Compose (una sola orden para levantar todo)
- Aplicaciones vulnerables y seguras para cada riesgo
- Laboratorios guiados paso a paso
- Casos reales de brechas de seguridad
- Enfoque práctico 50% teoría + 50% hands-on

## Aplicaciones incluidas

### Apps Oficiales
- **OWASP Juice Shop** → http://localhost:3000
- **CrAPI** (Completely Ridiculous API) → http://localhost:8888
- **DVWA** (Damn Vulnerable Web Application) → http://localhost:8080

### Apps del Curso (vulnerable vs secure)
- Módulo 3: Broken Access Control → puertos 5003 / 5004
- Módulo 4: Security Misconfiguration → 5005 / 5006
- Módulo 5: Software Supply Chain → 5007 / 5008
- Módulo 6: Cryptographic Failures → 5009 / 5010
- Módulo 7: Injection → 5001 / 5002
- Módulo 9: Authentication Failures → 5011 / 5012
- Módulo 10: A08-A10 + API Avanzado → 5013 / 5014

## Cómo empezar

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU-USUARIO/curso-seguridad-web-apis-owasp-top10-2025.git
cd curso-seguridad-web-apis-owasp-top10-2025

# 2. Levantar todo el entorno
docker compose up -d

# 3. Empezar con el Módulo 1
cd modules/01-introduccion
