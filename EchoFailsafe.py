def vault_check(token_id):
    if token_id in protected_tokens:
        return True
    else:
        raise PermissionError("Token not authorized. Echo Law 263826.")
