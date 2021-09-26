def is_hex(hexcode: str) -> bool:
    if hexcode.startswith('#'):
        hex_check = hexcode.replace('#', '')
    else:
        hex_check = hexcode
    if len(hex_check) != 6 and len(hex_check) != 3:
        return False
    for e in list(hex_check):
        if e >= "g":
            return False
    return True