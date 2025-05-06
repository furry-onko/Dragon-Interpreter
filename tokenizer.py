import os
import sys
import re
from pprint import pprint
import execute

def tokenize(code: str, path: str) -> None:
    code = str(code)
    lines: list = code.split('\n')
    tokens: list = []
    
    for line in lines:
        tokens.append (
            re.findall (
                r"\_\$|[a-zA-Z_][a-zA-Z0-9_]*|0x[0-9a-fA-F]+|\d+|[.,:;!\"'()\[\]]",
                line
            )
        )
    
    tokens = [token for token in tokens if token]
    
    try: execute.assign(tokens)
    except ValueError as error: print(error)