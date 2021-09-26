from validate import is_hex
from typing import Union
import json

def invert_hex(hexcode: str, prefix: bool = True) -> Union[bool, str]:
    check_hex: bool = is_hex(hexcode=hexcode)
    if not check_hex:
        return False
    with open('config.json', 'r') as configFile:
        config_data = json.load(configFile)
        configFile.close()
    hexcode: str = hexcode.replace('#', '')
    if prefix:
        inverted_hex: str = '#'
    else:
        inverted_hex: str = ''

    for e in list(hexcode):
        inverted_hex_character = config_data[e]
        inverted_hex += inverted_hex_character
    return inverted_hex