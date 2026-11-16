from pwdlib import PasswordHash


class SecurityService:
    def __init__(self, 
                 password_hasher: PasswordHash
                ) -> None:
        
        self.password_hasher = password_hasher

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """проверка хеша с паролем"""
        return self.password_hasher.verify(plain_password, hashed_password)


    def hash_password(self, password: str) -> str:
        """получение хешированного пароля"""
        return self.password_hasher.hash(password)

security_service = SecurityService(
    password_hasher=PasswordHash.recommended(),
)