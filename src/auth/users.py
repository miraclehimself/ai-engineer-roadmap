from src.auth.security import hash_password

users = {
    "abiola": {
      "username": "abiola",
      "full_name": "Abiola Aderiye",
      "role": "admin",
      "hashed_password": hash_password("Password123")
    }
}
