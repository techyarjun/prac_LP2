print("=== Help Desk Expert System ===")

issue = input("Enter issue (network/software/password): ")

print("\n=== Solution ===")

if issue == "network":
    print("Restart Router and Check Connection")

elif issue == "software":
    print("Reinstall or Update Software")

elif issue == "password":
    print("Reset Password Using Recovery Option")

else:
    print("Contact Technical Support")