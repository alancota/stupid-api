from .products.view import bp as products_bp
from .orders.view import bp as orders_bp
from .customers.view import bp as customers_bp
from .shipping.view import bp as shipping_bp
from sanic import Blueprint

api = Blueprint.group(
    products_bp,
    orders_bp,
    customers_bp,
    shipping_bp,
    version=1,
    version_prefix="/api/v",
)
