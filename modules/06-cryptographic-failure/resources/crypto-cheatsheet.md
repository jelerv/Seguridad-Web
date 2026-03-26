# Crypto Cheatsheet Recomendado

## Hashing de contraseñas
- **Recomendado:** Argon2id o bcrypt (con alto número de rondas)
- **Aceptable:** PBKDF2
- **Prohibido:** MD5, SHA1, SHA256 sin sal

## Algoritmos JWT
- **Recomendado:** RS256 (asymmetric) o HS256 con clave muy larga
- **Prohibido:** algoritmo "none", HS256 con clave débil

## Datos en tránsito
- Siempre usar TLS 1.3
- HSTS + Secure cookies

## Claves
- Nunca hardcodear claves en el código
- Usar secrets managers (AWS Secrets Manager, HashiCorp Vault, etc.)
