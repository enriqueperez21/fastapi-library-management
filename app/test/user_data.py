# Data for User tests
valid_user = {
    "name": "Test User",
    "email": "test@mail.com",
    "password": "Strong@123"
}

invalid_user_create_inputs = [
    {"name": "Test User", "password": "Strong@123"},
    {"name": "Test User","email": "test@mail.com"},
    {"password": "Strong@123"},
]

invalid_user_passwords = [
    {"password": "strong",      "msg":"String should have at least 8 characters"},
    {"password": "stroooong",   "msg":"Value error, Password must contain at least one uppercase letter"},
    {"password": "stroooongS",  "msg":"Value error, Password must contain at least one number"},
    {"password": "stroooongS1", "msg":"Value error, Password must contain at least one special character (@$!%*?&.)"},
]