def is_valid_token(token:str)->bool:
    return token.startswith("cli_") and len(token)==68