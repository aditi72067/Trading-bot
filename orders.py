from binance.enums import *
from binance.exceptions import BinanceAPIException

from bot.client import get_client
from bot.logging_config import setup_logger

logger = setup_logger()
client = get_client()

def place_market_order(symbol, side, quantity):
    try:
        logger.info(f"Placing MARKET order: {symbol} {side} {quantity}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_MARKET,
            quantity=quantity,
        )
        import time 
        time.sleep(0.5)
        order = client.futures_get_order(symbol=symbol, orderId=order['orderId'])

        logger.info(
    f"ORDER SUCCESS | symbol={symbol} | side={side} | "
    f"type={order['type']} | qty={order['origQty']} | "
    f"status={order['status']} | orderId={order['orderId']}"
)
        return order
    
    except BinanceAPIException as e:
        logger.error(e)
        raise

def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(f"Placing LIMIT order: {symbol} {side} {quantity} @ {price}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC,
        )

        logger.info(
            f"ORDER SUCCESS | symbol={symbol} | side={side} | "
            f"type={order['type']} | qty={order['origQty']} | "
            f"status={order['status']} | orderId={order['orderId']}"
        )
        return order

    except BinanceAPIException as e:
        logger.error(e)
        raise