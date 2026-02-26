import os
import json

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
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
    oracle_text = input("Card Text: ")
    
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
            print("\n-------------------------")
            print("English Name:", card["eng_name"])
            print("Japanese Name:", card["jpn_name"])
            print("Mana cost:", card["mana_cost"])
            print("Type:", card["card_type"])
            print("Card Text:", card["oracle_text"])
            print("-------------------------\n")
            found = True
    if not found:
        print("Card not found.\n")
        
def list_cards():
    if not cards:
        print("No cards in database.")
        return
    
    print("\n-----Card List-----")
    for card in sorted(cards.values(), key=lambda x: x["eng_name"]):
        print("-", card["eng_name"])
    print("-------------------\n")

def main():
    clear_screen()
    print("-----MAGIC THE GATHERING Quick Search Tool-----\n")
    while True:
        print("Choose and option:")
        print("1 - Search")
        print("2 - Add Card")
        print("3 - Delete Card")
        print("4 - View card list")
        print("0 - Quit")
        user_input = input("Enter choice: ").strip()
        
        if  user_input == "0":
            print("Shutting down.")
            break
        elif user_input == "1":
            card_search = input("Search: ")
            search(card_search)
        elif user_input == "2":
            add_card()
        elif user_input == "3":
            delete_card()
        elif user_input == "4":
            list_cards()
        else:
            print("Invalid option. PLease select number from menu.")
        
        input("\nPress ENTER to continue.")
        clear_screen()
            
if __name__ == "__main__":
    main()