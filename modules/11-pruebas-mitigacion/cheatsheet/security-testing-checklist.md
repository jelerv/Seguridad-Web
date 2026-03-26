# Checklist de Pruebas de Seguridad

### Autenticación y Sesiones
- [ ] Pruebas de brute force y credential stuffing
- [ ] Validación de JWT / tokens
- [ ] Rate limiting en login

### Autorización
- [ ] Broken Object Level Authorization (BOLA)
- [ ] Privilege Escalation
- [ ] IDOR testing

### Datos e Input
- [ ] SQL/NoSQL Injection
- [ ] XSS, CSRF, SSRF
- [ ] XML/JSON Injection

### API Specific
- [ ] Broken Object Property Level Authorization
- [ ] Unrestricted Resource Consumption
- [ ] Mass Assignment

### Configuración
- [ ] Security Headers
- [ ] CORS configuration
- [ ] Error messages

### Supply Chain
- [ ] SCA scan (Dependency-Check / Trivy)
- [ ] SBOM review
