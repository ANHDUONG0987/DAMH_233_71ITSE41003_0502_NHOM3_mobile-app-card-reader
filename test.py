import json

class Card:
    def __init__(self, account_number, account_holder, open_date):
        self.account_number = account_number
        self.account_holder = account_holder
        self.open_date = open_date

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "account_holder": self.account_holder,
            "open_date": self.open_date
        }

class PhoneStorage:
    def __init__(self, storage_file):
        self.storage_file = storage_file
        self.data = self.load_storage()

    def load_storage(self):
        try:
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_storage(self):
        with open(self.storage_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_card_info(self, card):
        self.data[card.account_number] = card.to_dict()
        self.save_storage()
        print(f"Saved card info: {card.to_dict()}")

# Simulated function to read card info from a chip-enabled card
def read_card_info():
    # In a real scenario, this function would interact with hardware to read the card info
    return Card("123456789", "John Doe", "2024-01-01")

# Example usage
storage = PhoneStorage("phone_storage.json")

# Read card info from a chip-enabled card
card_info = read_card_info()

# Add card info to phone storage
storage.add_card_info(card_info)

# Verify saved data
print("\nCurrent Storage Data:")
print(json.dumps(storage.data, indent=4))
