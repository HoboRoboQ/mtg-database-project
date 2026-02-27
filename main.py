import card_functions
import ui_functions

def main():
    ui_functions.clear_screen()
    ui_functions.line()
    print("MAGIC THE GATHERING Quick Search Tool")
    ui_functions.line()
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
            ui_functions.clear_screen()
            card_functions.search(card_search)
        elif user_input == "2":
            ui_functions.clear_screen()
            card_functions.add_card()
        elif user_input == "3":
            ui_functions.clear_screen()
            card_functions.delete_card()
        elif user_input == "4":
            ui_functions.clear_screen()
            card_functions.list_cards()
        else:
            print("Invalid option. Please select number from menu.")
        
        input("\nPress ENTER to continue.")
        ui_functions.clear_screen()
            
if __name__ == "__main__":
    main()