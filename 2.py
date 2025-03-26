class Medicine:
    def _init_(self, name, mrp, expiration_date, quantity):
        self.name = name
        self.mrp = mrp
        self.expiration_date = expiration_date
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity += quantity

class Pharmacy:
    def _init_(self):
        self.medicines = {}

    def add_medicine(self, name, mrp, expiration_date, quantity):
        if name not in self.medicines:
            self.medicines[name] = Medicine(name, mrp, expiration_date, quantity)
            print(f"Medicine '{name}' added successfully.")
        else:
            print(f"Medicine '{name}' already exists in the inventory.")

    def remove_medicine(self, name):
        if name in self.medicines:
            del self.medicines[name]
            print(f"Medicine '{name}' removed successfully.")
        else:
            print(f"Medicine '{name}' not found in the inventory.")

    def update_stock(self, name, quantity):
        if name in self.medicines:
            self.medicines[name].update_quantity(quantity)
            print(f"Stock for '{name}' updated successfully.")
        else:
            print(f"Medicine '{name}' not found in the inventory.")

    def display_inventory(self):
        print("Pharmacy Inventory:")
        for name, med_info in self.medicines.items():
            print(f"Name: {med_info.name}, MRP: {med_info.mrp}, Expiration Date: {med_info.expiration_date}, Quantity: {med_info.quantity}")

# Creating a Pharmacy instance
pharmacy = Pharmacy()

# Interactive menu for adding or removing medicines
while True:
    print("\nChoose an option:")
    print("1. Add Medicine")
    print("2. Remove Medicine")
    print("3. Display Inventory")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter medicine name: ")
        mrp = float(input("Enter MRP: "))
        expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
        quantity = int(input("Enter quantity: "))
        pharmacy.add_medicine(name, mrp, expiration_date, quantity)
    elif choice == '2':
        name = input("Enter medicine name to remove: ")
        pharmacy.remove_medicine(name)
    elif choice == '3':
        pharmacy.display_inventory()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        