from os import system as cmd
import re
from pprint import pprint

def assign(code: list) -> list:
    result: dict = {
        "stdbyte": None,
        "encoding": "ascii",
    }
    context: list = []
    variables: dict = {}

    for line in code:
        if len(line) >= 4 and (line[0], line[1], line[2]) == ('section', '.', 'data'):
            if line[3] == ':':
                if 'section.data' not in context and 'section.main' not in context:
                    context.append('section.data')
                else:
                    raise ValueError("Error. Section duplicate found.")
            else:
                raise ValueError("Error. Missing ':' in section.")
        
        if len(line) >= 5 
        
        


def removeComments(code: list) -> list:
    result: list = []

    for line in code:
        if len(line) == 0:
            continue

        if len(line) >= 2 and (line[0], line[1]) in [('/', '/'), ('*', '*')]:
            continue

        if line[0] == ';':
            continue

        comment_index: int = None
        
        for i in range(len(line)):
            if line[i] == ';':
                comment_index = i
                break
            if i + 1 < len(line) and (line[i], line[i+1]) in [('/', '/'), ('*', '*')]:
                comment_index = i
                break

        if comment_index is not None:
            line = line[:comment_index]

        if line:
            result.append(line)

    return result

def init(code: list) -> dict:
    clean_code: list = removeComments(code)
    pprint(clean_code)
    assign(clean_code)