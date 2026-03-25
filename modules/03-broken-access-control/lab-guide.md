# Laboratorio: Broken Access Control

1. Levantar la app: `docker compose up vulnerable-flask`
2. Acceder a http://localhost:5000/api/user/1 (sin login → BOLA)
3. Intentar SSRF: /api/proxy?url=http://169.254.169.254/latest/meta-data/
4. Corregir con el código de la carpeta secure/
5. Verificar que ahora devuelve 403 correctamente
