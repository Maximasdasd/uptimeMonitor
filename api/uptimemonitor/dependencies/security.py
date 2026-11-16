from pwdlib import PasswordHash
from uptimemonitor.core.security import SecurityService


def get_security_service() -> SecurityService:
    return SecurityService(
        password_hasher=PasswordHash.recommended(),
    )