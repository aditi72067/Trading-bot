import argparse

from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price)

        print("\n----- Order Request -----")
        print(f"Symbol     : {symbol}")
        print(f"Side       : {side}")
        print(f"Type       : {order_type}")
        print(f"Quantity   : {quantity}")

        if price:
            print(f"Price      : {price}")

        if order_type == "MARKET":
            response = place_market_order(symbol, side, quantity)

        else:
            if price is None:
                raise ValueError("Price is required for LIMIT orders.")

            response = place_limit_order(
                symbol,
                side,
                quantity,
                price,
            )

        print("\n----- Order Response -----")
        print(f"Order ID       : {response.get('orderId')}")
        print(f"Status         : {response.get('status')}")
        print(f"Executed Qty   : {response.get('executedQty')}")
        print(f"Average Price  : {response.get('avgPrice', 'N/A')}")

        print("\nOrder placed successfully!")

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()