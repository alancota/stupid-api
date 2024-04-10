from typing import Optional, Sequence
from sanic import Sanic

from .autodiscovery import autodiscover

DEFAULT_BLUEPRINTS = [
    "src.stupid_api.blueprints.v1.group",
    "src.stupid_api.blueprints.v2.group",
]


def create_app(
    init_blueprints: Optional[Sequence[str]] = None,
) -> Sanic:
    app = Sanic("TheStupidAPI")

    if not init_blueprints:
        init_blueprints = DEFAULT_BLUEPRINTS

    autodiscover(app, *init_blueprints)

    return app
