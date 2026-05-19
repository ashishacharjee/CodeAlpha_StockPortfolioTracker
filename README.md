# Stock Portfolio Tracker 📈

A simple command-line stock portfolio tracker built with Python as part of the **CodeAlpha Python Programming Internship**.

## How to Run

```bash
python stock_tracker.py
```

> No external libraries needed. Works with Python 3.x out of the box.

## How It Works

- Displays a list of 10 available stocks with hardcoded prices (AAPL, TSLA, GOOGL, MSFT, NVDA, and more)
- You enter stock symbols and quantities you hold
- It calculates the total value of each holding and your overall portfolio
- Optionally saves the result to a timestamped `.csv` file

## Features

- 10 pre-loaded stocks including Indian and US markets (TCS, INFY, AAPL, NVDA, etc.)
- Clean tabular summary of your portfolio
- CSV export with timestamp
- Input validation for stock symbols and quantities

## Sample Output

```
  STOCK    QTY        PRICE        VALUE
  ----------------------------------------
  AAPL      10      $213.32     $2133.20
  TSLA       5      $248.50     $1242.50
  ----------------------------------------
  TOTAL               $3375.70
```

## Concepts Used

- Dictionaries
- User input and output
- Basic arithmetic
- File handling (`csv` module)
- Functions

## Project Structure

```
CodeAlpha_StockPortfolioTracker/
│
└── stock_tracker.py
```

## Internship Details

- **Organization:** CodeAlpha
- **Domain:** Python Programming
- **Student ID:** CA/DF1/75758
