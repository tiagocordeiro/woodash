from decouple import config
from wordpress import API

# Configurações do WooCommerce
consumer_key = config("WC_CK", False)
consumer_secret = config("WC_CS", False)
woo_commerce_url = config("WC_URL", False)

wpapi = API(
    url=woo_commerce_url,
    api="wp-json",
    version='wc/v3',
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    timeout=10
)


def get_orders():
    orders = wpapi.get("orders")
    return orders.json()
