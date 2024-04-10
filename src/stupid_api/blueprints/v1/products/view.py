from logging import getLogger
from sanic import Blueprint, Request, json
from sanic.views import HTTPMethodView
from sanic_ext import openapi

from stupid_api.common.data.products import data as products_data

bp = Blueprint("Products", url_prefix="/products")
logger = getLogger("stupid_api")


class ProductView(HTTPMethodView, attach=bp):
    @openapi.definition(
        summary="Products",
        description="Returns a list of products",
        tag="v1",
    )
    async def get(self, request: Request):
        return json(products_data)
