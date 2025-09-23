def validate_secury_password(password: str) -> str:
    """Valida que la contraseña cumpla las reglas de seguridad."""
    if not any(c.isupper() for c in password):
        raise ValueError("Password must contain at least one uppercase letter")
    if not any(c.islower() for c in password):
        raise ValueError("Password must contain at least one lowercase letter")
    if not any(c.isdigit() for c in password):
        raise ValueError("Password must contain at least one number")
    if not any(c in "@$!%*?&." for c in password):
        raise ValueError("Password must contain at least one special character (@$!%*?&.)")
    return password