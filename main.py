# MYSTERY ISLAND - THE LOST LIGHTHOUSE

from game import (
    explore_location,
    create_player,
    move_player,
    collect_item,
    light_lighthouse,
    check_surroundings
)


def play_game():
    print("DEBUG: play_game() has started")

    # Display the game title
    print("================================")
    print("       MYSTERY ISLAND")
    print("       THE LOST LIGHTHOUSE")
    print("================================")

    # Ask for the player's name
    player_name = input("Enter your name: ")

    # Create the player's game state
    player = create_player(player_name)

    # Welcome the player
    print(f"\nWelcome to Mystery Island, {player_name}!")

    # Introduce the adventure
    print("\nYou wake up on a mysterious island after a terrible storm.")
    print("Your mission is to restore the lighthouse beacon and escape.")

    print(f"\nYou are currently at: {player['location']}")
    print(f"Your energy level: {player['energy']}")

    print("\nYou can hear the waves crashing against the shore.")
    print("You notice a dense jungle path ahead.")

    game_running = True

    while game_running and not player["game_over"]:

        # Display player's current status
        print("\n================================")
        print(f"Location: {player['location']}")
        print(f"Energy: {player['energy']}")
        print("================================")

        # Display available choices
        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. Check surroundings")
        print("3. Move to another location")
        print("4. Collect an item")
        print("5. Light the lighthouse beacon")
        print("6. Quit")

        choice = input("\nEnter your choice: ").strip()

        print("DEBUG: Choice received =", repr(choice))

        if choice == "1":
            print(explore_location(player))

        elif choice == "2":
            print(check_surroundings(player))

        elif choice == "3":
            print("\nAvailable destinations:")

            destinations = {
                "Beach": ["Jungle"],
                "Jungle": ["Beach", "Cave"],
                "Cave": ["Jungle", "Old Bridge"],
                "Old Bridge": ["Cave", "Lighthouse"],
                "Lighthouse": ["Old Bridge"]
            }

            for destination in destinations[player["location"]]:
                print(destination)

            destination = input("\nWhere would you like to go? ").strip().title()

            if move_player(player, destination):
                print(f"\nYou have successfully moved to {destination}!")
            else:
                print("\nYou cannot move there. Check your destination or energy.")

        elif choice == "4":

            if player["location"] == "Beach":
                item = "Rope"

            elif player["location"] == "Cave":
                item = "Lantern"

            else:
                print("\nThere are no items to collect here.")
                continue

            if collect_item(player, item):
                print(f"\nYou collected the {item}!")
            else:
                print(f"\nYou have already collected the {item}.")

        elif choice == "5":

            if player["location"] != "Lighthouse":
                print("\nYou must be at the Lighthouse to activate the beacon.")

            elif light_lighthouse(player):
                print("\n================================")
                print("       BEACON RESTORED!")
                print("================================")
                print(f"\nCongratulations, {player_name}!")
                print("You have restored the lighthouse beacon.")
                print("A rescue boat spots your signal.")
                print("YOU HAVE ESCAPED MYSTERY ISLAND!")

        elif choice == "6":
            print(f"\nGoodbye, {player_name}! Thanks for playing.")
            game_running = False

        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

    # Check whether the player has run out of energy
    if player["energy"] <= 0:
        print("\n================================")
        print("           GAME OVER")
        print("================================")
        print("You have run out of energy.")
        print("You are stranded on Mystery Island.")


# REPLAY SYSTEM

while True:

    play_game()

    print("\n================================")
    print("       GAME FINISHED")
    print("================================")

    print("\nWould you like to play again?")
    print("1. Yes, start a new game")
    print("2. No, exit game")

    replay_choice = input("\nEnter your choice: ").strip()

    if replay_choice == "1":
        print("\nStarting a new adventure...\n")

    elif replay_choice == "2":
        print("\nThank you for playing Mystery Island!")
        print("See you on your next adventure.")
        break

    else:
        print("\nInvalid choice. Please enter 1 or 2.")