from logging import getLogger
from sanic import Blueprint, Request, json
from sanic.views import HTTPMethodView
from sanic_ext import openapi

from stupid_api.common.data.orders import data as orders_data

bp = Blueprint("Orders", url_prefix="/orders")
logger = getLogger("stupid_api")


class OrdersView(HTTPMethodView, attach=bp):
    @openapi.definition(
        summary="Orders data",
        description="Returns a list of orders",
        tag="v1",
    )
    async def get(self, request: Request):
        return json(orders_data)
