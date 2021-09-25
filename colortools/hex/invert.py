from validate import is_hex
from typing import Union
import json
from colortools.hex.validate import is_hex


def invert_hex(hexcode: str, prefix: bool = True) -> Union[bool, str]:
    check_hex = is_hex(hexcode=hexcode)
    if not check_hex:
        return False
    with open('config.json', 'r') as configFile:
        config_data = json.load(configFile)
        configFile.close()
    if prefix:
        inverted_hex = '#'
    else:
        inverted_hex = ''
    for e in list(hexcode):
        inverted_hex_character = config_data[e]
        inverted_hex += inverted_hex_character
    return inverted_hex