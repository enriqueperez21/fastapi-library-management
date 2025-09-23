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


# Data for Author tests
valid_author = {"name": "Robert Martin", "birthdate": "21/11/2002"}

invalid_author_create_inputs = [
    {"input": {"birthdate": "21/11/2002"}, "msg": "Field required"},
    {"input": {"name": "Test User", "birthdate": "21-11-2002"}, "msg": "Value error, The date must be in format dd/mm/yyyy (21/11/2002)"},
    {"input": {"name": "Test User", "birthdate": "40/11/2002"}, "msg": "Value error, The date must be in format dd/mm/yyyy (21/11/2002)"},
]

invalid_author_update_inputs = [
    {"birthdate": "21-11-2002", "msg": "Value error, The date must be in format dd/mm/yyyy (21/11/2002)"},
    {"birthdate": "40/11/2002", "msg": "Value error, The date must be in format dd/mm/yyyy (21/11/2002)"},
]