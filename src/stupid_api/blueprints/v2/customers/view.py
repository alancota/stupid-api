from logging import getLogger
from sanic import Blueprint, Request, json
from sanic.views import HTTPMethodView
from sanic_ext import openapi

from stupid_api.common.data.customers_v2 import data as customers_data

bp = Blueprint("Customersv2", url_prefix="/customers")
logger = getLogger("stupid_api")


class CustomerView(HTTPMethodView, attach=bp):
    @openapi.definition(
        summary="Customer data",
        description="Returns a list of customers",
        tag="v2",
    )
    async def get(self, request: Request):
        return json(customers_data)
