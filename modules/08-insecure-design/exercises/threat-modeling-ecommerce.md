# Ejercicio: Threat Modeling - Aplicación E-commerce

**Elementos del sistema:**
- Usuario → Frontend → API Gateway → Order Service → Payment Service → Database

**Aplicar STRIDE:**

**Spoofing:** ¿Cómo un atacante podría hacerse pasar por otro usuario?
**Tampering:** ¿Dónde se puede modificar el precio de un producto?
**Information Disclosure:** ¿Qué información sensible se expone en respuestas de error?
**Denial of Service:** ¿Cómo un usuario podría agotar recursos con órdenes masivas?
**Elevation of Privilege:** ¿Cómo un usuario normal podría acceder a funciones de admin?

**Pregunta clave:**  
¿Qué controles de diseño debemos implementar para mitigar estas amenazas?
