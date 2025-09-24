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