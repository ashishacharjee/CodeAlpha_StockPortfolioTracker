# Stock Portfolio Tracker 📈

A feature-rich command-line stock portfolio tracker built with Python as part of the **CodeAlpha Python Programming Internship**.

## How to Run

```bash
python stock_tracker.py
```

> No external libraries needed. Works with Python 3.x out of the box.

## Features

- **View Available Stocks** — 15 stocks across NASDAQ, NYSE, and NSE (Indian markets)
- **Add Stocks** — Enter symbol, quantity, and buy price (or use current price)
- **Smart Averaging** — Automatically calculates average buy price if you add more of an existing stock
- **Live Portfolio View** — Displays quantity, buy price, current price, total value, and P&L per stock
- **Profit & Loss Tracking** — Shows gain/loss in USD and overall portfolio P&L percentage
- **Update Quantity** — Edit how many shares you hold for any stock
- **Remove Stock** — Delete a holding from your portfolio with confirmation
- **CSV Export** — Save your full portfolio with P&L data to a timestamped `.csv` file
- **Full Menu System** — Clean numbered menu for all actions

## Menu Options

```
1. View available stocks
2. Add stock to portfolio
3. View my portfolio & P&L
4. Update stock quantity
5. Remove stock from portfolio
6. Save portfolio to CSV
7. Exit
```

## Sample Portfolio View

```
  STOCK    QTY   BUY PRICE   CUR PRICE   VALUE        P&L
  AAPL      10    $200.00     $213.32     $2133.20    +$133.20
  TSLA       5    $260.00     $248.50     $1242.50    -$57.50
  ─────────────────────────────────────────────────────────
  TOTAL                                  $3375.70    +$75.70
```

## Concepts Used

`dict`, `csv`, `datetime`, `input/output`, arithmetic, functions, file handling

## Project Structure

```
CodeAlpha_StockPortfolioTracker/
└── stock_tracker.py
```

## Internship Details

- **Organization:** CodeAlpha
- **Domain:** Python Programming
- **Student ID:** CA/DF1/75758
- **Duration:** 20th May 2026 – 20th June 2026
