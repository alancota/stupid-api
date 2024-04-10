from .customers.view import bp as customers_bp
from .orders.view import bp as orders_bp
from sanic import Blueprint

group = Blueprint.group(customers_bp, orders_bp, version=2, version_prefix="/api/v")
