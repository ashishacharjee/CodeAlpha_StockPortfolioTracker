import csv
import os
from datetime import datetime

# ─────────────────────────────────────────────
#  Hardcoded stock prices (USD)
# ─────────────────────────────────────────────
STOCK_PRICES = {
    "AAPL":  213.32,
    "TSLA":  248.50,
    "GOOGL": 175.80,
    "MSFT":  425.60,
    "AMZN":  198.40,
    "NFLX":  645.20,
    "META":  540.10,
    "NVDA":  131.50,
    "INFY":   21.30,
    "TCS":    38.90,
    "RELIANCE": 29.10,
    "HDFC":   18.70,
    "WIPRO":  10.50,
    "UBER":   80.20,
    "SONY":   20.40,
}

# Portfolio: { symbol: {"qty": int, "buy_price": float} }
portfolio = {}


# ─────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────
def separator(char="─", width=56):
    print("  " + char * width)


def show_available_stocks():
    print("\n  ┌─────────────────────────────────────────┐")
    print("  │         Available Stocks (USD)           │")
    print("  ├──────────┬──────────────┬───────────────┤")
    print("  │  Symbol  │  Price       │  Exchange      │")
    print("  ├──────────┼──────────────┼───────────────┤")
    exchange = {
        "AAPL": "NASDAQ", "TSLA": "NASDAQ", "GOOGL": "NASDAQ",
        "MSFT": "NASDAQ", "AMZN": "NASDAQ", "NFLX": "NASDAQ",
        "META": "NASDAQ", "NVDA": "NASDAQ", "UBER": "NYSE",
        "SONY": "NYSE",   "INFY": "NSE",    "TCS": "NSE",
        "RELIANCE": "NSE","HDFC": "NSE",    "WIPRO": "NSE",
    }
    for sym, price in STOCK_PRICES.items():
        print(f"  │  {sym:<8} │  ${price:<11.2f} │  {exchange.get(sym,''):<13} │")
    print("  └──────────┴──────────────┴───────────────┘")


def show_portfolio():
    if not portfolio:
        print("\n  Your portfolio is empty. Add stocks first.")
        return

    total_invested = 0
    total_current  = 0

    print("\n  ┌──────────┬───────┬────────────┬────────────┬────────────┬──────────┐")
    print("  │  Stock   │  Qty  │  Buy Price │  Cur Price │  Value     │  P&L     │")
    print("  ├──────────┼───────┼────────────┼────────────┼────────────┼──────────┤")

    for sym, data in portfolio.items():
        qty        = data["qty"]
        buy_price  = data["buy_price"]
        cur_price  = STOCK_PRICES[sym]
        invested   = qty * buy_price
        current    = qty * cur_price
        pnl        = current - invested
        pnl_pct    = ((cur_price - buy_price) / buy_price) * 100
        pnl_str    = f"+${pnl:.2f}" if pnl >= 0 else f"-${abs(pnl):.2f}"
        arrow      = "▲" if pnl >= 0 else "▼"

        total_invested += invested
        total_current  += current

        print(f"  │  {sym:<8} │  {qty:<5} │  ${buy_price:<9.2f} │  ${cur_price:<9.2f} │  ${current:<9.2f} │ {arrow}{pnl_str:<7} │")

    print("  ├──────────┴───────┴────────────┴────────────┼────────────┼──────────┤")
    total_pnl = total_current - total_invested
    pnl_sign  = "+" if total_pnl >= 0 else "-"
    print(f"  │  {'TOTAL':>40}   │  ${total_current:<9.2f} │ {pnl_sign}${abs(total_pnl):<6.2f}  │")
    print("  └─────────────────────────────────────────────┴────────────┴──────────┘")
    print(f"\n  Total Invested : ${total_invested:.2f}")
    print(f"  Current Value  : ${total_current:.2f}")
    pnl_pct_total = ((total_current - total_invested) / total_invested * 100) if total_invested else 0
    sign = "+" if pnl_pct_total >= 0 else ""
    print(f"  Overall P&L    : {sign}{pnl_pct_total:.2f}%")


def add_stock():
    show_available_stocks()
    print()
    symbol = input("  Enter stock symbol to add: ").upper().strip()

    if symbol not in STOCK_PRICES:
        print(f"  '{symbol}' not found in the available stock list.")
        return

    try:
        qty = int(input(f"  Quantity of {symbol}: ").strip())
        if qty <= 0:
            print("  Quantity must be a positive number.")
            return
    except ValueError:
        print("  Invalid quantity.")
        return

    cur_price = STOCK_PRICES[symbol]
    buy_input = input(f"  Buy price per share (press Enter to use current ${cur_price:.2f}): ").strip()
    buy_price = float(buy_input) if buy_input else cur_price

    if symbol in portfolio:
        # Average down/up if already exists
        existing     = portfolio[symbol]
        total_qty    = existing["qty"] + qty
        avg_price    = ((existing["qty"] * existing["buy_price"]) + (qty * buy_price)) / total_qty
        portfolio[symbol] = {"qty": total_qty, "buy_price": round(avg_price, 2)}
        print(f"\n  Updated {symbol}: {total_qty} shares @ avg ${avg_price:.2f}")
    else:
        portfolio[symbol] = {"qty": qty, "buy_price": buy_price}
        print(f"\n  Added {qty} x {symbol} @ ${buy_price:.2f}")


def remove_stock():
    if not portfolio:
        print("\n  Portfolio is empty.")
        return

    print("\n  Current holdings:", ", ".join(portfolio.keys()))
    symbol = input("  Enter symbol to remove: ").upper().strip()

    if symbol not in portfolio:
        print(f"  '{symbol}' is not in your portfolio.")
        return

    confirm = input(f"  Remove all {portfolio[symbol]['qty']} shares of {symbol}? (yes/no): ").lower()
    if confirm == "yes":
        del portfolio[symbol]
        print(f"  {symbol} removed from portfolio.")
    else:
        print("  Removal cancelled.")


def update_quantity():
    if not portfolio:
        print("\n  Portfolio is empty.")
        return

    print("\n  Current holdings:", ", ".join(portfolio.keys()))
    symbol = input("  Enter symbol to update: ").upper().strip()

    if symbol not in portfolio:
        print(f"  '{symbol}' is not in your portfolio.")
        return

    print(f"  Current quantity: {portfolio[symbol]['qty']}")
    try:
        new_qty = int(input("  New quantity: ").strip())
        if new_qty <= 0:
            print("  Quantity must be positive.")
            return
        portfolio[symbol]["qty"] = new_qty
        print(f"  Updated {symbol} to {new_qty} shares.")
    except ValueError:
        print("  Invalid input.")


def save_to_csv():
    if not portfolio:
        print("\n  Nothing to save.")
        return

    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    total_invested = sum(d["qty"] * d["buy_price"] for d in portfolio.values())
    total_current  = sum(d["qty"] * STOCK_PRICES[s] for s, d in portfolio.items())

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Qty", "Buy Price (USD)", "Current Price (USD)", "Value (USD)", "P&L (USD)", "P&L (%)"])
        for sym, data in portfolio.items():
            qty       = data["qty"]
            buy_p     = data["buy_price"]
            cur_p     = STOCK_PRICES[sym]
            value     = qty * cur_p
            pnl       = value - (qty * buy_p)
            pnl_pct   = ((cur_p - buy_p) / buy_p) * 100
            writer.writerow([sym, qty, f"{buy_p:.2f}", f"{cur_p:.2f}", f"{value:.2f}", f"{pnl:.2f}", f"{pnl_pct:.2f}%"])
        writer.writerow([])
        writer.writerow(["", "", "Total Invested", f"${total_invested:.2f}"])
        writer.writerow(["", "", "Current Value",  f"${total_current:.2f}"])
        writer.writerow(["", "", "Net P&L",        f"${total_current - total_invested:.2f}"])

    print(f"\n  Portfolio saved to '{filename}'")


def show_menu():
    print("\n  ╔══════════════════════════════════════╗")
    print("  ║   Stock Portfolio Tracker — Menu     ║")
    print("  ╠══════════════════════════════════════╣")
    print("  ║  1. View available stocks            ║")
    print("  ║  2. Add stock to portfolio           ║")
    print("  ║  3. View my portfolio & P&L          ║")
    print("  ║  4. Update stock quantity            ║")
    print("  ║  5. Remove stock from portfolio      ║")
    print("  ║  6. Save portfolio to CSV            ║")
    print("  ║  7. Exit                             ║")
    print("  ╚══════════════════════════════════════╝")


def main():
    print("\n" + "═" * 56)
    print("      CodeAlpha — Stock Portfolio Tracker")
    print("  Track your investments and monitor gains/losses")
    print("═" * 56)

    actions = {
        "1": show_available_stocks,
        "2": add_stock,
        "3": show_portfolio,
        "4": update_quantity,
        "5": remove_stock,
        "6": save_to_csv,
    }

    while True:
        show_menu()
        choice = input("\n  Choose an option (1-7): ").strip()

        if choice == "7":
            print("\n  Goodbye! Happy investing! 📈\n")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("  Invalid option. Please choose 1–7.")


if __name__ == "__main__":
    main()
