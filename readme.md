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