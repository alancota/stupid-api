from logging import getLogger
from sanic import Blueprint, Request, json
from sanic.views import HTTPMethodView
from sanic_ext import openapi

from stupid_api.common.data.shipping import data as shipping_data

bp = Blueprint("Shipping", url_prefix="/shipping")
logger = getLogger("stupid_api")


class ShippingView(HTTPMethodView, attach=bp):
    @openapi.definition(
        summary="Shipping data",
        description="Returns a list of shipments",
        tag="v1",
    )
    async def get(self, request: Request):
        return json(shipping_data)
