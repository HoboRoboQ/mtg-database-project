import json
from ui_functions import line
from ui_functions import multiline_input
from ui_functions import display_card

def load_cards():
    try:
        with open("cards.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

cards = load_cards()

def save_cards():
    with open("cards.json", "w", encoding="utf-8") as file:
        json.dump(cards, file, ensure_ascii=False, indent=4)
        
def add_card():
    eng_name = input("English Name: ")
    
    if not eng_name.strip():
        print("English name cannot be empty.")
        return
    
    jpn_name = input("Japanese Name: ")
    mana_cost = input("Mana Cost: ")
    card_type = input("Card Type: ")
    oracle_text = multiline_input("Enter Card text:")
    
    key = eng_name.lower()
    
    if key in cards:
        print("This card already exists.")
        return
    
    cards[key] = {
        "eng_name": eng_name,
        "jpn_name": jpn_name,
        "mana_cost": mana_cost,
        "card_type": card_type,
        "oracle_text": oracle_text
    }
    
    save_cards()
    print("Card added successfully!")
    display_card(cards[key])
    
def delete_card():
    deleting_card = input("What card would you like to delete?: ").lower()
    
    if deleting_card not in cards:
        print("This card does not exist.")
        return
    
    confirm = input(f"Are you sure you want to delete "
                    f"{cards[deleting_card]['eng_name']}? Yes (1) No (2): ")
    if confirm == "1":
        del cards[deleting_card]
        save_cards()
        print("The card has been deleted.")
    else:
        print("Card has not been deleted.")
        return

def search(search_input):
    search_input = search_input.lower()
    found = False
    
    for key, card in cards.items():
        if search_input in key or search_input in card["jpn_name"].lower():
            display_card(card) 
                
            found = True
    if not found:
        print("Card not found.\n")
        
def list_cards():
    if not cards:
        print("No cards in database.")
        return
    
    line()
    print("CARD LIST")
    line()
    for card in sorted(cards.values(), key=lambda x: x["eng_name"]):
        print("-", card["eng_name"])
    line()

