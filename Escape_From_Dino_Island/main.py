# ==========================================
# Escape From Dino Island (Version 2.0)
# Text Adventure Game
# ==========================================

import time
import sys
import os
from colorama import init, Fore, Style

init(autoreset=True)

# ==========================================
# GAME STATE (INVENTORY)
# ==========================================

has_backpack = False
has_flashlight = False
has_boat_key = False


# ==========================================
# CORE UTILITIES
# ==========================================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause(seconds=1.2):
    time.sleep(seconds)


def type_text(text, color=Fore.WHITE, speed=0.02):
    print(color, end="")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print(Style.RESET_ALL)


def scene(title):
    print()
    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + f" {title.upper()}")
    print(Fore.CYAN + "=" * 60)
    print()


def menu(question, options):
    print(Fore.CYAN + "━" * 60)
    print(Fore.YELLOW + "🦖 " + question)
    print(Fore.CYAN + "━" * 60)

    print()

    colors = [Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.BLUE]

    for i, opt in enumerate(options):
        print(colors[i % len(colors)] + f" [{i+1}] {opt}")

    print()
    print(Fore.CYAN + "━" * 60)

    return input(Fore.WHITE + "➜ Your Choice: ")


def show_inventory():
    print(Fore.MAGENTA + "\n🎒 INVENTORY")
    print(Fore.MAGENTA + "-" * 25)
    print("Backpack   :", "✅" if has_backpack else "❌")
    print("Flashlight :", "✅" if has_flashlight else "❌")
    print("Boat Key   :", "✅" if has_boat_key else "❌")
    print(Fore.MAGENTA + "-" * 25)


# ==========================================
# TITLE SCREEN
# ==========================================

def title_screen():
    clear()

    print(Fore.GREEN + r"""
███████╗███████╗ ██████╗ █████╗ ██████╗ ███████╗
██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
█████╗  ███████╗██║     ███████║██████╔╝█████╗
██╔══╝  ╚════██║██║     ██╔══██║██╔═══╝ ██╔══╝
███████╗███████║╚██████╗██║  ██║██║     ███████╗
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝

██████╗ ██╗███╗   ██╗ ██████╗
██╔══██╗██║████╗  ██║██╔═══██╗
██║  ██║██║██╔██╗ ██║██║   ██║
██║  ██║██║██║╚██╗██║██║   ██║
██████╔╝██║██║ ╚████║╚██████╔╝
╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝
""")

    print(Fore.YELLOW + r"""
                 __
                / _)
       _.----._/ /
      /         /
   __/ (  | (  |
  /__.-'|_|--|_|

   ESCAPE FROM DINO ISLAND
""")

    print(Fore.CYAN + "=" * 60)

    type_text(
        "A stranded island. Dinosaurs roam freely. Can you escape?",
        Fore.YELLOW,
        0.03
    )

    print(Fore.CYAN + "=" * 60)

    input(Fore.GREEN + "\nPress ENTER to begin...")
    clear()


# ==========================================
# GAME OVER / WIN
# ==========================================

def lose(reason):
    clear()
    print(Fore.RED + "=" * 60)
    type_text("GAME OVER", Fore.RED, 0.05)
    print(reason)
    print("=" * 60)

    while True:
        again = input("\nPlay again? (yes/no): ").lower()

        if again == "yes":
            start_game()
            return
        elif again == "no":
            quit()


def win():
    clear()
    print(Fore.GREEN + "=" * 60)
    type_text("YOU ESCAPED DINO ISLAND!", Fore.GREEN, 0.04)
    print(Fore.GREEN + "=" * 60)

    type_text("You reach the dock and start the boat...", Fore.YELLOW)
    pause()

    type_text("The engine roars to life!", Fore.GREEN)
    pause()

    type_text("You escape just as the dinosaurs roar behind you!", Fore.CYAN)
    pause()

    quit()


# ==========================================
# GAME START
# ==========================================

def start_game():
    global has_backpack, has_flashlight, has_boat_key

    has_backpack = False
    has_flashlight = False
    has_boat_key = False

    title_screen()
    beach()


# ==========================================
# BEACH (START)
# ==========================================

def beach():
    scene("The Beach")
    show_inventory()

    type_text("You wake up on a strange sandy beach...", Fore.YELLOW)
    pause()

    type_text("Your boat is destroyed. Something is wrong here.", Fore.RED)
    pause()

    choice = menu(
        "Where do you go?",
        [
            "🌴 Enter the jungle",
            "⛰️ Climb the cliffs"
        ]
    )

    if choice == "1":
        jungle()
    elif choice == "2":
        lose("You slip on the cliffs... Velociraptors were hiding there!")
    else:
        beach()


# ==========================================
# JUNGLE
# ==========================================

def jungle():
    global has_backpack

    scene("The Jungle")
    show_inventory()

    type_text("The jungle is loud... something is moving nearby.", Fore.GREEN)
    pause()

    type_text("A trapped Triceratops is stuck under a fallen tree!", Fore.YELLOW)
    pause()

    choice = menu(
        "What do you do?",
        [
            "🦕 Help the Triceratops",
            "🏃 Run away"
        ]
    )

    if choice == "1":
        type_text("The Triceratops frees itself and gives you a backpack!", Fore.YELLOW)
        has_backpack = True
        pause()
        river()
    elif choice == "2":
        lose("You run straight into a pack of Velociraptors!")
    else:
        jungle()


# ==========================================
# RIVER
# ==========================================

def river():
    scene("The River")
    show_inventory()

    type_text("A fast river blocks your path.", Fore.CYAN)
    pause()

    choice = menu(
        "How do you cross?",
        [
            "🌊 Swim across",
            "🪵 Build a log bridge"
        ]
    )

    if choice == "1":
        lose("A T-Rex was waiting in the water... bad idea.")
    elif choice == "2":
        type_text("You safely cross the river.", Fore.GREEN)
        pause()
        cave()
    else:
        river()


# ==========================================
# CAVE
# ==========================================

def cave():
    global has_flashlight

    scene("The Cave")
    show_inventory()

    type_text("A dark cave blocks your path.", Fore.WHITE)
    pause()

    choice = menu(
        "What do you do?",
        [
            "🔦 Enter quietly",
            "📢 Shout into the cave"
        ]
    )

    if choice == "1":
        type_text("You find a flashlight inside the cave!", Fore.YELLOW)
        has_flashlight = True
        pause()
        camp()
    elif choice == "2":
        lose("A sleeping dinosaur wakes up instantly...")
    else:
        cave()


# ==========================================
# CAMP
# ==========================================

def camp():
    global has_boat_key

    scene("Abandoned Camp")
    show_inventory()

    type_text("You find an old abandoned campsite.", Fore.YELLOW)
    pause()

    choice = menu(
        "What do you do?",
        [
            "⛺ Search the tent",
            "🚶 Keep moving"
        ]
    )

    if choice == "1":
        type_text("You found a BOAT KEY!", Fore.GREEN)
        has_boat_key = True
        pause()
        dock()
    elif choice == "2":
        lose("You miss the key... and get stuck on the island forever.")
    else:
        camp()


# ==========================================
# DOCK (FINAL AREA)
# ==========================================

def dock():
    scene("The Dock")
    show_inventory()

    type_text("You finally reach the old dock.", Fore.CYAN)
    pause()

    type_text("A boat is waiting... your only chance to escape.", Fore.YELLOW)
    pause()

    choice = menu(
        "What do you do?",
        [
            "🗝️ Use the Boat Key",
            "🚤 Push the boat into the water"
        ]
    )

    if choice == "1":
        if has_boat_key:
            win()
        else:
            lose("You don't have the key... the boat won't start.")
    elif choice == "2":
        lose("The boat drifts away without you...")
    else:
        dock()


# ==========================================
# RUN GAME
# ==========================================

start_game()