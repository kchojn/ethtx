def match_dict(parameters: dict, arguments: list):
    for index, (k, _) in enumerate(parameters.items()):
        parameters[k] = arguments[index]

    return parameters
