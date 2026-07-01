# Trading Bot - Binance Futures Testnet

A simplified Python CLI application that places **Market** and **Limit** orders on Binance Futures Testnet (USDT-M), with input validation, structured logging, and clean console output.

---

## Setup

1. Register for a Binance Futures Testnet account at
   https://testnet.binancefuture.com

2. Generate an API Key and Secret from the testnet dashboard.

3. Clone/download this project and create a virtual environment:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root with your credentials:

   ```text
   API_KEY=your_key_here
   API_SECRET=your_secret_here
   ```

   Replace the values with your Binance Futures Testnet API credentials.

---

## How to Run

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

---

## Assumptions

- Only USDT-M Futures pairs are supported (e.g. `BTCUSDT`).
- `LIMIT` orders use `timeInForce=GTC` (Good-Til-Cancelled).
- After placing an order, the app fetches updated status from Binance because the initial response may not reflect final execution.

---

## Logging

All order requests, responses, and errors are logged to:

```
logs/trading_bot.log
```

for auditing purposes.