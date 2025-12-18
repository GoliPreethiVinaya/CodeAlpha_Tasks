
stock_prices = {
    "APPLE": 180,
    "TSLA": 250,
    "GOOGLE": 120,
    "AMAZON": 100,
    "MICROSOFT": 150
}

portfolio = {}

num_stocks = int(input("How many different stocks do you want to enter? "))

for _ in range(num_stocks):
    stock_name = input("Enter stock symbol (e.g., AAPL): ").upper()
    quantity = int(input(f"Enter number of shares for {stock_name}: "))
    portfolio[stock_name] = quantity

total_investment = 0
print("\nYour Portfolio:")
for stock, quantity in portfolio.items():
    price = stock_prices.get(stock, 0)
    value = price * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares x ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

save_file = input("Do you want to save this portfolio to a file? (yes/no): ").lower()
if save_file == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Your Portfolio:\n")
        for stock, quantity in portfolio.items():
            price = stock_prices.get(stock, 0)
            value = price * quantity
            file.write(f"{stock}: {quantity} shares x ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("Portfolio saved to portfolio.txt")
