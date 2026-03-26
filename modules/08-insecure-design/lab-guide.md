# Guía del Laboratorio – Insecure Design

## 1. Ejercicio Principal: Threat Modeling

**Caso de estudio:** Plataforma de E-commerce (Web + API)

**Descripción del sistema:**
- Usuarios pueden registrarse, iniciar sesión y comprar productos.
- API maneja órdenes, pagos y gestión de productos.
- Existe un panel administrativo.
- Se utiliza JWT para autenticación y un servicio externo de pagos.

**Instrucciones:**
1. Dibuja un **Data Flow Diagram (DFD)** simple del sistema.
2. Identifica los principales elementos: Usuario, Frontend, API, Base de datos, Servicio de pagos.
3. Aplica la metodología **STRIDE** a cada flujo y elemento:
   - **S**poofing (suplantación)
   - **T**ampering (manipulación)
   - **R**epudiation (repudio)
   - **I**nformation Disclosure (divulgación de información)
   - **D**enial of Service (denegación de servicio)
   - **E**levation of Privilege (elevación de privilegios)

4. Para cada amenaza identificada, propone controles de seguridad que deberían implementarse **en la fase de diseño**.

## 2. Análisis de código de ejemplo
- Revisa la aplicación en `vulnerable/` e identifica decisiones de diseño inseguras.
- Compara con la versión `secure/`.

## 3. Tarea final
- Redacta un documento corto titulado **"Secure Design Requirements"** para la plataforma de e-commerce.
- Incluye mínimo 8 controles de seguridad que deben estar presentes desde el diseño.

**Herramientas recomendadas:**
- draw.io, Lucidchart o Miro (para diagramas)
- Plantilla STRIDE (disponible en exercises/)
