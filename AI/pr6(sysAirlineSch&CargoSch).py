print("=== Airline Scheduling Expert System ===")

weather = input("Is weather good? (yes/no): ")
cargo = int(input("Enter cargo weight in tons: "))

print("\n=== Scheduling Result ===")

if weather == "no":
    print("Flight Delayed Due to Bad Weather")

elif cargo > 100:
    print("Use Cargo Aircraft")

else:
    print("Flight Scheduled Successfully")