from string import punctuation


def is_hex(hexcode: str) -> bool:
    if hexcode.startswith('#'):
        hex_check: str = hexcode.replace('#', '')
    else:
        hex_check: str = hexcode
    if len(hex_check) != 8 and len(hex_check) != 6 and len(hex_check) != 3:
        return False
    for e in list(hex_check):
        if e >= "g" or e in punctuation:
            return False
    return True


def is_in_vga(hexcode: str) -> bool:
    if hexcode.startswith('#'):
        hex_check: str = hexcode.replace('#', '')
    else:
        hex_check: str = hexcode
    if len(hex_check) != 6 and len(hex_check) != 3:
        return False
    if hex_check.lower() in __config_is_vga():
        return True
    return False


def __config_is_vga() -> list:
    return ['000000', '800000', '008000', '808000', '000080', '800080', '008080', 'c0c0c0', '808080', 'ff0000',
            '00ff00', 'ffff00', '0000ff', 'ff00ff', '00ffff', 'ffffff']
