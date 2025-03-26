print("WELCOME TO LEAF PHARMACY")

class Medicine:
    def __init__(self, name, mrp, expiration_date, quantity):
        self.name = name
        self.mrp = mrp
        self.expiration_date = expiration_date
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity += quantity

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

# Adding medicines to the inventory with initial quantities
pharmacy.add_medicine("Paracetamol", 10.5, "2025-12-31", 100)
pharmacy.add_medicine("Aspirin", 8.75, "2024-08-15", 50)
pharmacy.add_medicine("Ibuprofen", 15, "2026-04-30", 75)

# Displaying the current inventory
pharmacy.display_inventory()

# Updating stock for a medicine
pharmacy.update_stock("Paracetamol", 50)

# Displaying the updated inventory
pharmacy.display_inventory()
