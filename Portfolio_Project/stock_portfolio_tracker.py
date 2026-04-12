import datetime
import pandas as pd


def view_stock(stock_portfolio):
    df = pd.DataFrame.from_dict(stock_portfolio, orient='index')

    # ADD: total investment column
    df["total_investment"] = df["price"] * df["quantity"]

    df.index.name = "Symbol"
    print(df)


def add_stock(myStock):

    symbol = input("Enter the stock's company symbol: ").upper()

    if symbol in myStock:
        current_quan = myStock[symbol]["quantity"]
        print(f"Current Quantity of {myStock[symbol]['name']}: {current_quan}")

        addQuan = int(input("How much quantity you want to add: "))
        myStock[symbol]["quantity"] += addQuan

        print(f"Stock quantity updated from {current_quan} to {myStock[symbol]['quantity']}")

    else:
        name = input("Enter the name of new company: ")
        price = float(input("Enter the price of new product: "))
        quantity = int(input("Enter the quantity: "))

        myStock[symbol] = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        print("New stock is added!")


def calculate_purchase(myStock, symbol, user_quantity):
    return myStock[symbol]["price"] * user_quantity


def purchase_stock(myStock):

    if all(stock["quantity"] == 0 for stock in myStock.values()):
        print("All stocks are sold out. Cannot purchase anything.")
        return

    view_stock(myStock)

    while True:
        try:
            symbol = input("Enter company's symbol: ").upper()

            if symbol in myStock:
                quantity = myStock[symbol]["quantity"]

                if quantity != 0:
                    break
                else:
                    print("Stock is empty!")
                    return
            else:
                print("Symbol not found.")
                return

        except Exception:
            print("Invalid entry!")

    while True:
        try:
            user_quantity = int(input(f"Enter quantity (1-{quantity}): "))
            if 1 <= user_quantity <= quantity:
                break
            else:
                print("Invalid range.")
        except ValueError:
            print("Enter a number.")

    total_price = calculate_purchase(myStock, symbol, user_quantity)

    myStock[symbol]["quantity"] -= user_quantity

    print(f"Purchase successful! Total cost = {total_price}")

    today = datetime.date.today()

    record = {
        "symbol": symbol,
        "quan": user_quantity,   
        "total": total_price,
        "date": today
    }

    return record


# portfolio investment calculator
def portfolio_investment(myStock):
    total = 0
    for stock in myStock.values():
        total += stock["price"] * stock["quantity"]
    return total


# save full portfolio summary
def save_portfolio_summary(myStock):
    total_investment = portfolio_investment(myStock)

    with open("Portfolio.txt", "a") as file:
        file.write(f"\nDate: {datetime.date.today()}\n")
        file.write("PORTFOLIO SUMMARY\n")

        for symbol, data in myStock.items():
            inv = data["price"] * data["quantity"]
            file.write(f"{symbol} | Investment: {inv}\n")

        file.write(f"TOTAL INVESTMENT: {total_investment}\n")
        file.write("-" * 40 + "\n")


def Save_purchase_history(record):
    with open("Total.txt", "a") as file:
        file.write(f"\nDate: {record['date']}\n")
        file.write(f"Total Price: {record['total']}\n")
        file.write(f"Quantity: {record['quan']}\n")
        file.write("-" * 30 + "\n")


def main_menu(myStock):

    while True:
        while True:
            try:
                print("\n1.Add Stock\n2.Purchase\n3.View Stock\n4.Save Portfolio\n5.Exit")
                choose = int(input("Enter: "))

                if 1 <= choose <= 5:
                    break
                else:
                    print("Invalid option.")
            except ValueError:
                print("Wrong input.")

        if choose == 1:
            add_stock(myStock)

        elif choose == 2:
            record = purchase_stock(myStock)
            if record:
                Save_purchase_history(record)

        elif choose == 3:
            view_stock(myStock)

        elif choose == 4:
            save_portfolio_summary(myStock)
            print("Portfolio saved.")

        else:
            print("Exiting...")
            break


if __name__ == "__main__":

    stock_portfolio = {
        "AAPL": {"name": "Apple", "price": 175.50, "quantity": 10},
        "MSFT": {"name": "Microsoft", "price": 330.00, "quantity": 5},
        "GOOGL": {"name": "Google", "price": 2800.75, "quantity": 2},
        "TSLA": {"name": "Tesla", "price": 900.25, "quantity": 3},
        "AMZN": {"name": "Amazon", "price": 3500.10, "quantity": 7}
    }

    main_menu(stock_portfolio)