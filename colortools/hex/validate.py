def is_hex(hexcode: str) -> bool:
    if hexcode.startswith('#'):
        if len(hexcode) != 7 and len(hexcode) != 4:
            return False
        else:
            hex_check = hexcode.replace('#', '')
    else:
        if len(hexcode) != 6 and len(hexcode) != 3:
            return False
        else:
            hex_check = hexcode
    for e in list(hex_check):
        if e >= "g":
            return False
    return True