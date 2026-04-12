# 📊 Portfolio Tracker (Python)

A simple Python-based stock portfolio tracker that allows users to manage stocks, simulate purchases, and track total investment value. The system also saves portfolio summaries and transaction history into text files.

---

## 🚀 Features

- Add new stocks to portfolio
- Update existing stock quantities
- Purchase stocks with quantity validation
- View current portfolio in tabular format
- Automatically calculate:
  - Total investment per stock
  - Overall portfolio investment
- Save:
  - Transaction history (`Total.txt`)
  - Portfolio summary (`Portfolio.txt`)

---

## 🧠 How It Works

Each stock contains:
```python
{
  "name": "Company Name",
  "price": 100.0,
  "quantity": 10
}
Investment = Price × Quantity

Total Portfolio Value = Sum of all individual stock investments

---

## 📂 File Structure

project/
│── main.py
│── Total.txt
│── Portfolio.txt

File descriptions:
- main.py → Main program logic (stock management + portfolio operations)
- Total.txt → Stores purchase history (date, quantity, total cost)
- Portfolio.txt → Stores portfolio snapshots and total investment values

---

## ▶️ How Program Runs

1. The program starts with a predefined stock portfolio.
2. A menu is displayed with options:
   - Add Stock
   - Purchase Stock
   - View Portfolio
   - Save Portfolio Summary
   - Exit
3. Based on user input:
   - Stocks are added or updated
   - Purchases reduce stock quantity and calculate total cost
   - Portfolio can be viewed in table form
   - Data can be saved into files
4. The program runs in a loop until the user exits.

---

## 💾 Data Storage

Total.txt:
- Stores purchase records
- Includes date, quantity, and total cost

Portfolio.txt:
- Stores portfolio snapshots
- Shows each stock’s investment value
- Stores total portfolio value with date

---

## 📌 Summary

This project simulates a basic stock portfolio system with:
- Investment calculation
- Stock management
- File-based storage
- Portfolio tracking over time
