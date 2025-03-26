print("Welcome to Leaf Pharmacy Management System")

class Medicine:
    def __init__(self, name, mrp, expiration_date, quantity):
        self.name = name
        self.mrp = mrp
        self.expiration_date = expiration_date
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity -= quantity

class Pharmacy:
    def __init__(self):
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
            self.medicines[name].quantity += quantity
            print(f"Stock for '{name}' updated successfully.")
            if self.medicines[name].quantity < 50:
                print(f"Alert: Stock for '{name}' is less than 50.")
        else:
            print(f"Medicine '{name}' not found in the inventory.")

    def place_order(self, order):
        total_cost = 0
        for name, quantity in order.items():
            if name in self.medicines:
                if self.medicines[name].quantity >= quantity:
                    cost = self.medicines[name].mrp * quantity
                    total_cost += cost
                    self.medicines[name].update_quantity(quantity)
                    print(f"Order for '{quantity}' units of '{name}' placed successfully. Cost: {cost:.2f}")
                else:
                    print(f"Insufficient stock for '{name}'. Available stock: {self.medicines[name].quantity}")
            else:
                print(f"Medicine '{name}' not found in the inventory.")
        print(f"Total cost of the order: {total_cost:.2f}")
        return total_cost

    def display_inventory(self):
        print("Pharmacy Inventory:")
        for name, med_info in self.medicines.items():
            print(f"Name: {med_info.name}, MRP: {med_info.mrp}, Expiration Date: {med_info.expiration_date}, Quantity: {med_info.quantity}")

# Creating a Pharmacy instance
pharmacy = Pharmacy()
pharmacy.add_medicine("Paracetamol", 100, "2025-12-31", 200)
pharmacy.add_medicine("Crocin", 75, "2026-8-1", 200)
pharmacy.add_medicine("Dolo", 60, "2026-7-18", 200)
pharmacy.add_medicine("Allegra", 100, "2026-2-4", 200)
pharmacy.add_medicine("Pentacid", 200, "2025-7-12", 200)
pharmacy.add_medicine("Avomine", 90, "2026-3-6", 200)
pharmacy.add_medicine("Aspirin", 80, "2027-7-8", 200)

# Interactive menu for adding or removing medicines
while True:
    print("\nChoose an option: ")
    print("1. Add Medicine")
    print("2. Remove Medicine")
    print("3. Place Order")
    print("4. Update Stock")
    print("5. Display Inventory")
    print("6. Quit")

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
        order = {}
        while True:
            name = input("Enter medicine name to order (or type 'done' to finish): ")
            if name.lower() == 'done':
                break
            quantity = int(input("Enter quantity to order: "))
            order[name] = quantity
        total_cost = pharmacy.place_order(order)
        print(f"Total cost of the order: {total_cost:.2f}")
    elif choice == '4':
        name = input("Enter medicine name to update stock: ")
        quantity = int(input("Enter quantity to add to stock: "))
        pharmacy.update_stock(name, quantity)
    elif choice == '5':
        pharmacy.display_inventory()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
