from stupid_api.common.utils.app_factory import create_app
from sanic.log import logger
from textwrap import dedent

app = create_app()

app.ext.openapi.describe(
    "Stupid API",
    version="0.1.1",
    description=dedent(
        """
        # Info
        I ran out of names for my lab and testing APIs, so I'm calling this one "Stupid API".
        Feel free to use it in your labs and projects.
        """
    ),
)


@app.main_process_start
def display_routes(app, _):
    logger.info("Registered routes:")
    for route in app.router.routes:
        logger.info(f"> /{route.path}")
