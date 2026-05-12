print("=== Information Management Expert System ===")

storage = int(input("Enter storage used (%): "))
backup = input("Is backup available? (yes/no): ")
security = input("Is security enabled? (yes/no): ")

print("\n=== Result ===")

if storage > 90:
    print("Warning: Storage Almost Full")
    print("Action: Upgrade Storage")

elif backup == "no":
    print("Warning: Backup Missing")
    print("Action: Create Backup Immediately")

elif security == "no":
    print("Warning: Security Risk")
    print("Action: Enable Security System")

else:
    print("System Working Properly")