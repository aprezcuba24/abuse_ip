def get_parameters(text: str):
    parts = text.split(" ")
    return [item for item in parts[1:] if item != " "]
