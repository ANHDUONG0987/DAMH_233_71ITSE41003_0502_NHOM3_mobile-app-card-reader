import json

class Card:
    def __init__(self, card_id, account_holder, account_number):
        self.card_id = card_id
        self.account_holder = account_holder
        self.account_number = account_number

    def to_dict(self):
        return {
            "card_id": self.card_id,
            "account_holder": self.account_holder,
            "account_number": self.account_number
        }

class CardManager:
    def __init__(self, storage_file):
        self.storage_file = storage_file
        self.cards = self.load_cards()

    def load_cards(self):
        try:
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_cards(self):
        with open(self.storage_file, 'w') as file:
            json.dump(self.cards, file, indent=4)

    def add_card(self, card):
        self.cards[card.card_id] = card.to_dict()
        self.save_cards()
        print(f"Added card: {card.to_dict()}")

    def delete_card(self, card_id):
        if card_id in self.cards:
            del self.cards[card_id]
            self.save_cards()
            print(f"Deleted card with ID: {card_id}")
        else:
            print(f"Card with ID: {card_id} not found")

    def list_cards(self):
        for card_id, card_info in self.cards.items():
            print(f"Card ID: {card_id}, Account Holder: {card_info['account_holder']}, Account Number: {card_info['account_number']}")

    def select_card(self, card_id):
        if card_id in self.cards:
            print(f"Selected card: {self.cards[card_id]}")
            return self.cards[card_id]
        else:
            print(f"Card with ID: {card_id} not found")
            return None

# Example usage
manager = CardManager("cards_storage.json")

# Add some cards
manager.add_card(Card("1", "John Doe", "123456789"))
manager.add_card(Card("2", "Jane Smith", "987654321"))

# List all cards
print("All cards:")
manager.list_cards()

# Select a card to interact with
print("\nSelecting card with ID '1':")
selected_card = manager.select_card("1")

# Delete a card
print("\nDeleting card with ID '2':")
manager.delete_card("2")

# List all cards after deletion
print("\nAll cards after deletion:")
manager.list_cards()
