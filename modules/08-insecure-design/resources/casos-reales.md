# Casos Reales de Insecure Design

- **Capital One (2019)**: Configuración incorrecta de WAF + diseño deficiente de permisos en AWS → exposición de 100 millones de registros.
- **Twitter (2022)**: Vulnerabilidad masiva por diseño incorrecto de una API interna.
- **Equifax (2017)**: Falta de segmentación de red y threat modeling inadecuado.
- **ChatGPT Plugins (2023)**: Diseño inseguro permitió que plugins accedieran a datos de otros usuarios.
- **MOVEit Transfer (2023)**: Lógica de autenticación progresiva mal diseñada.

**Lección principal:**  
Corregir un problema de diseño en producción cuesta 10–100 veces más que prevenirlo durante la fase de diseño.
