# Módulo 1: Introducción a la Seguridad en Aplicaciones Web y APIs

**Objetivos de aprendizaje:**
- Comprender la importancia crítica de la seguridad en aplicaciones web y APIs modernas.
- Diferenciar los conceptos de vulnerabilidad, amenaza y riesgo.
- Conocer la arquitectura típica de aplicaciones web y APIs (cliente-servidor, microservicios, API-first).
- Entender el funcionamiento del protocolo HTTP/HTTPS y sus implicaciones de seguridad.
- Conocer los principales proyectos OWASP relevantes para desarrollo seguro.
- Introducir el concepto de Secure Software Development Lifecycle (Secure SDLC) y Shift-Left Security.

**Duración recomendada:** 3 horas (2 horas teoría + 1 hora discusión y laboratorio básico).

**Relación con OWASP Top 10:2025**
Este módulo sienta las bases para entender por qué el OWASP Top 10:2025 sigue siendo la referencia principal para identificar y priorizar riesgos de seguridad en aplicaciones web y APIs.

**Cambios clave en OWASP Top 10:2025**
- Dos categorías nuevas: Software Supply Chain Failures (A03) y Mishandling of Exceptional Conditions (A10).
- Consolidación de SSRF dentro de Broken Access Control (A01).
- Security Misconfiguration subió al puesto #2.
- Injection bajó al #5, pero sigue afectando al 100% de las aplicaciones probadas.

**Referencias oficiales:**
- OWASP Top 10:2025 – Introducción oficial: https://owasp.org/Top10/2025/
- OWASP API Security Top 10 2023

## Entorno de Laboratorio

El curso incluye un **docker-compose.yml** centralizado que levanta:

- **Juice Shop** (Web + API moderna)
- **CrAPI** (Completely Ridiculous API – OWASP)
- **DVWA** (Damn Vulnerable Web Application)
- Apps vulnerables y seguras de cada módulo (Injection, Broken Access Control, etc.)
