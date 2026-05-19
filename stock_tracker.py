import csv
from datetime import datetime

stock_prices = {
    "AAPL": 213.32,
    "TSLA": 248.50,
    "GOOGL": 175.80,
    "MSFT": 425.60,
    "AMZN": 198.40,
    "NFLX": 645.20,
    "META": 540.10,
    "NVDA": 131.50,
    "INFY": 21.30,
    "TCS": 38.90,
}


def show_available_stocks():
    print("\n Available Stocks:")
    print(f"  {'Symbol':<8} {'Price (USD)':>12}")
    print("  " + "-" * 22)
    for symbol, price in stock_prices.items():
        print(f"  {symbol:<8} ${price:>11.2f}")
    print()


def get_portfolio():
    portfolio = []
    print(" Enter your holdings. Type 'done' when finished.\n")

    while True:
        symbol = input(" Stock symbol: ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in stock_prices:
            print(f" '{symbol}' not found. Choose from: {', '.join(stock_prices)}\n")
            continue

        try:
            qty = int(input(f" Quantity of {symbol}: ").strip())
            if qty <= 0:
                print(" Quantity must be a positive number.\n")
                continue
        except ValueError:
            print(" Invalid input. Enter a whole number.\n")
            continue

        portfolio.append({"symbol": symbol, "qty": qty, "price": stock_prices[symbol]})
        print(f" Added {qty} x {symbol} @ ${stock_prices[symbol]:.2f}\n")

    return portfolio


def display_summary(portfolio):
    if not portfolio:
        print("\n Your portfolio is empty.")
        return 0

    total = 0
    print("\n" + "=" * 48)
    print(f"  {'STOCK':<8} {'QTY':>5} {'PRICE':>12} {'VALUE':>12}")
    print("  " + "-" * 40)

    for item in portfolio:
        value = item["qty"] * item["price"]
        total += value
        print(f"  {item['symbol']:<8} {item['qty']:>5} ${item['price']:>11.2f} ${value:>11.2f}")

    print("  " + "-" * 40)
    print(f"  {'TOTAL':>26} ${total:>11.2f}")
    print("=" * 48)
    return total


def save_to_csv(portfolio, total):
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price (USD)", "Value (USD)"])
        for item in portfolio:
            value = item["qty"] * item["price"]
            writer.writerow([item["symbol"], item["qty"], f"{item['price']:.2f}", f"{value:.2f}"])
        writer.writerow([])
        writer.writerow(["", "", "Grand Total", f"{total:.2f}"])
    print(f"\n Saved to '{filename}'")


def main():
    print("\n" + "=" * 48)
    print("    CodeAlpha — Stock Portfolio Tracker")
    print("=" * 48)

    show_available_stocks()
    portfolio = get_portfolio()
    total = display_summary(portfolio)

    if portfolio:
        save = input("\n Save to CSV? (yes/no): ").lower().strip()
        if save == "yes":
            save_to_csv(portfolio, total)

    print("\n Thanks for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
