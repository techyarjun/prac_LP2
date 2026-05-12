print("=== Employee Performance Expert System ===")

attendance = int(input("Enter attendance percentage: "))
tasks = int(input("Enter completed tasks: "))

print("\n=== Evaluation ===")

if attendance >= 90 and tasks >= 8:
    print("Performance: Excellent")

elif attendance >= 75 and tasks >= 5:
    print("Performance: Good")

elif attendance >= 60:
    print("Performance: Average")

else:
    print("Performance: Poor")