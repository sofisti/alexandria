import os
import errno
from typing import Optional, Type

import pydantic

from models import get_models, get_models_map


def write_to_path(path: str, content: str) -> None:
    """
    Writes to a path, even when the parent path doesn't exist.
    See: https://stackoverflow.com/a/12517490
    """
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(path, "w") as fp:
        fp.write(content)


def generate_model(
    model: Type[pydantic.BaseModel],
    path: str = "",
    indent: Optional[int] = 2,
) -> None:
    schema = model.schema_json(
        indent=indent,
        ref_template="https://github.com/sofisti/sopymodels/schemas/{model}.json",
    )

    if path:
        write_to_path(f"{path}/{model.__name__}.json", schema)

    else:
        print(schema)


def generate_models(model: str, path: str, indent: int) -> None:
    models = []

    if model:
        models = [get_models_map()[model.lower()]]

    else:
        models = list(get_models())

    for item in models:
        generate_model(item, path, indent or None)
