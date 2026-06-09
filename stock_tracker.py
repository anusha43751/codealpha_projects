# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total_investment = 0

print("Available Stocks:")
for stock, price in stocks.items():
    print(stock, ":", price)

n = int(input("\nEnter number of stocks you want to buy: "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))
        investment = stocks[stock_name] * quantity
        total_investment += investment
    else:
        print("Stock not found!")

print("\nTotal Investment Value = $", total_investment)

# Optional: Save result to file
with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value = $" + str(total_investment))

print("Result saved in portfolio.txt")