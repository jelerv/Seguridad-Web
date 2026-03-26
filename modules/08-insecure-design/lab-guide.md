# Guía del Laboratorio – Insecure Design

## 1. Ejercicio principal: Threat Modeling

### Caso práctico: Aplicación de E-commerce (API + Web)

**Descripción del sistema:**
- Usuarios pueden registrarse, iniciar sesión y realizar compras.
- Existe un panel de administración.
- La API maneja pagos y gestión de productos.
- Se usa JWT para autenticación.

**Tarea (en grupos o individual):**
Usa la metodología **STRIDE** para identificar amenazas de diseño.

**Pasos recomendados:**
1. Dibuja el diagrama de flujo de datos (Data Flow Diagram - DFD).
2. Identifica los elementos: Usuarios, API, Base de datos, Servicio de pagos.
3. Aplica STRIDE a cada elemento y flujo:
   - **S**poofing
   - **T**ampering
   - **R**epudiation
   - **I**nformation Disclosure
   - **D**enial of Service
   - **E**levation of Privilege

4. Propón controles de seguridad para mitigar las amenazas identificadas.

## 2. Análisis de la aplicación de ejemplo
- Analiza la versión `vulnerable/` → identifica decisiones de diseño inseguras.
- Compara con la versión `secure/`.

## 3. Tarea final
- Redacta un documento corto de "Secure Design Requirements" para la aplicación de e-commerce.
- Incluye al menos 5 controles de seguridad que deben estar presentes desde la fase de diseño.

**Herramientas recomendadas:**
- draw.io / Lucidchart / Miro (para diagramas)
- Plantilla STRIDE (incluida en exercises/)
