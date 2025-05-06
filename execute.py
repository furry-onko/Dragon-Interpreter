from os import system as cmd
import re

def assign(code: list) -> dict:
    # print(code)
    result: dict = {
        "stdbyte": None,
        "encoding": "ascii",
    }
    context: list = []
    variables: dict = {}

    for l, line in enumerate(code):
        for t, token in enumerate(line):
            if l == 0:
                if t == 0 and token == "int":
                    context.append("int")
                elif t == 1 and token == "cat64" and "int" in context:
                    result["stdbyte"] = token
                    context.remove("int")
                elif t == 1 and token != "cat64" and "int" in context:
                    raise ValueError(f"Error. Stdbyte is invalid ({token})\nLine: {l +1}")
                elif t > 1:
                    raise ValueError(f"Error. Unexpected: {token}\nLine: {l +1}")
                else:
                    raise ValueError(f"Error. Stdbyte instruction not found.\nLine: {l +1}")

            elif l == 1:
                if t == 0 and token == "str":
                    context.append("str")
                elif t == 1 and token.lower() in ("utf8", "ascii") and "str" in context:
                    result["encoding"] = token
                    context.remove("str")
                elif t > 1:
                    raise ValueError(f"Error. Unexpected: {token}\nLine: {l +1}")
                elif t == 0 and token == "section":
                    t == 0
                    l += 1
                elif t == 0:
                    raise ValueError(f"Error. Invalid encoding {token}\nLine: {l +1}")

            elif l >= 1:
                if t == 0 and token == "section":
                    context.append(token)
                elif t == 1 and token == ".":
                    pass
                elif t == 1 and token != ".":
                    raise ValueError(f"Error. Every section must start from \".\"\nLine: {l +1}")
                elif t == 2:
                    if token == 'main':
                        try:
                            context.remove("section")
                            context.append(".main")
                        except:
                            context.append(".main")

                    elif token == 'data':
                        try:
                            context.remove("section")
                            context.append(".data")
                        except:
                            context.append(".data")
                    else:
                        raise ValueError(f"Error. Section must be either \".main\" or \".data\"\nLine: {l +1}")

                if context[0] == '.data':
                    if t == 0 and token and re.match(r"\_[A-Za-z_]+[A-Za-z0-9_]*", token):
                        context.append(f"var|{token}")
                    elif t == 1 and context[1] == "var" and token == ":":
                        context[1] += token
                    elif t == 2 and context[1] == "var:" and token in ("integer", "string", "bool", "float", "long", "array"):
                        context[1] += token
                    elif t == 3 and token == '=' and re.match(r"var\:(integer|string|bool|float|long|array)", context):
                        context[1] += token
                    elif t == 4 and token:
                        variables[context] = token
    print(variables)
    return result