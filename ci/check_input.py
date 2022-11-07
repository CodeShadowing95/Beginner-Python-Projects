def validate_input(s):
    if not s.isnumeric() or not s:
        return False
    return int(s)