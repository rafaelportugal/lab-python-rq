# encoding: utf-8
from inflection import camelize


def convert_dict_to_pascalcase(dict_lowercase):
    output = {}
    for k, v in dict_lowercase.items():
        key_pascalcase = camelize(k, False)
        if isinstance(v, dict):
            output[key_pascalcase] = convert_dict_to_pascalcase(v)
        else:
            output[key_pascalcase] = v
    return output
