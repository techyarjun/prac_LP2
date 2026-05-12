print("=== Hospital Expert System ===")

fever = input("Do you have fever? (yes/no): ")
cough = input("Do you have cough? (yes/no): ")
headache = input("Do you have headache? (yes/no): ")
stomach = input("Do you have stomach pain? (yes/no): ")

print("\n=== Diagnosis ===")

if fever == "yes" and cough == "yes":
    print("Possible Disease: Flu")
    print("Department: General Medicine")

elif headache == "yes":
    print("Possible Disease: Migraine")
    print("Department: Neurology")

elif stomach == "yes":
    print("Possible Disease: Gastric Problem")
    print("Department: Gastroenterology")

else:
    print("Consult General Physician")