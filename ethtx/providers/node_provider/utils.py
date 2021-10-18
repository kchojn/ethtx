from typing import Dict, Any

from pydantic import BaseModel


def match_dict(parameters: dict, arguments: list):
    for index, (k, _) in enumerate(parameters.items()):
        parameters[k] = arguments[index]

    return parameters


def update_model(base_model: BaseModel, additional_data: Dict[str, Any]) -> BaseModel:
    for k, v in additional_data.items():
        setattr(base_model, k, v)

    return base_model
