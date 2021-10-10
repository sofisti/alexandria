from typing import Iterator, Optional, Type
from uuid import UUID

import pydantic


class Domain(pydantic.BaseModel):
    """
    Describes a domain of knowledge
    """

    uuid: UUID = pydantic.Field(
        title="UUID",
        description="Primary Identifier",
    )
    name: str
    description: str
    parent: Optional[UUID]
    dependencies: list[UUID] = pydantic.Field(
        title="Domain Dependencies",
        description="Domains required to understand this domain",
        default_factory=list,
    )


class Resource(pydantic.BaseModel):
    """
    Describes a resource to get to know one or more domains
    """

    uuid: UUID = pydantic.Field(
        title="UUID",
        description="Primary Identifier",
    )
    domains: list[UUID] = pydantic.Field(
        title="Domains",
        description="Related domains",
    )


class Question(pydantic.BaseModel):
    """
    A question
    """

    uuid: UUID = pydantic.Field(
        title="UUID",
        description="Primary Identifier",
    )
    resource: UUID = pydantic.Field(
        title="Resource UUID",
        description="Related resource UUID",
    )
    text: str = pydantic.Field(
        title="Text",
        description="Question content",
    )


class Answer(pydantic.BaseModel):
    """
    An answer
    """

    uuid: UUID = pydantic.Field(
        title="UUID",
        description="Primary Identifier",
    )
    question: UUID = pydantic.Field(
        title="Question UUID", description="Related question UUID"
    )
    text: str = pydantic.Field(
        title="Text",
        description="Answer content",
    )
    is_correct: bool = pydantic.Field(
        title="Is Correct",
        description="Whether the answer is correct",
    )


class User(pydantic.BaseModel):
    """
    User model
    """

    uuid: UUID = pydantic.Field(
        title="UUID",
        description="Primary Identifier",
    )
    full_name: str = pydantic.Field(
        title="Full Name",
        description="Full name of the user",
    )
    pref_name: str = pydantic.Field(
        title="Preferred Name",
        description="Short name used in friendly communications with the user",
    )
    email_address: pydantic.EmailStr = pydantic.Field(
        title="Email Address",
        description="Current email address associated with the user",
    )


def get_models() -> Iterator[Type[pydantic.BaseModel]]:
    for item in globals().values():
        try:
            if issubclass(item, pydantic.BaseModel) and not getattr(
                item, "__private__", False
            ):
                yield item
        except TypeError:
            continue


def get_models_map() -> dict[str, Type[pydantic.BaseModel]]:
    return {model.__name__.lower(): model for model in list(get_models())}
