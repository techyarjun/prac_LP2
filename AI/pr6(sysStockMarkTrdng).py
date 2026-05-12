print("=== Stock Market Expert System ===")

price = float(input("Enter current stock price: "))
moving_avg = float(input("Enter moving average price: "))

print("\n=== Suggestion ===")

if price > moving_avg:
    print("Suggestion: BUY Stock")

elif price < moving_avg:
    print("Suggestion: SELL Stock")

else:
    print("Suggestion: HOLD Stock")