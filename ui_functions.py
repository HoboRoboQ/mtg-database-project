import os
import textwrap

def line():
    print("=" * 50)
    
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
def multiline_input(prompt):
    print(prompt)
    print("(Type 'END' on a new line to finish.\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    
    return "\n".join(lines)

def display_card(card):
    width = 50
    print()
    line()
    print(f"{card["eng_name"]} | {card["jpn_name"]}")
    print("-" * width)
    print(f"Mana cost: {card["mana_cost"]}")
    print(f"Type: {card["card_type"]}")
    print()
    
    print("Card text:")
    for paragraph in card["oracle_text"].split("\n"):
        wrapped = textwrap.fill(paragraph, width=width)
        print(wrapped)
    line()