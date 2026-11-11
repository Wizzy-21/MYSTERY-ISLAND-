# MYSTERY ISLAND - GAME LOGIC

def explore_beach():
    description = """
    You begin exploring the beach.

    You notice footprints leading towards the jungle.
    Nearby, you also spot something washed ashore.
    """

    return description

# Create the player's state
def create_player(name):

    player = {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False
    }

    return player

# Move the player between locations
def move_player(player, destination):

    # Define the island map
    paths = {
        "Beach": ["Jungle"],
        "Jungle": ["Beach", "Cave"],
        "Cave": ["Jungle", "Old Bridge"],
        "Old Bridge": ["Cave", "Lighthouse"],
        "Lighthouse": ["Old Bridge"]
    }

    # Check whether the destination is accessible
    if destination not in paths[player["location"]]:
        return False
    if destination == "Old Bridge" and "Rope" not in player["inventory"]:
        return False

    # Check whether the player has enough energy
    if player["energy"] <= 0:
        return False

    # Update the player's location
    player["location"] = destination

    # Reduce the player's energy
    player["energy"] -= 1

    return True        

# Collect items during the adventure
def collect_item(player, item):

    # Define where each item can be found
    item_locations = {
        "Rope": "Beach",
        "Lantern": "Cave"
    }

    # Check whether the item exists
    if item not in item_locations:
        return False

    # Check whether the player is at the correct location
    if player["location"] != item_locations[item]:
        return False

    # Prevent the player from collecting the same item twice
    if item in player["inventory"]:
        return False

    # Add the item to the player's inventory
    player["inventory"].append(item)

    return True    

def light_lighthouse(player):
    if player["location"] != "Lighthouse":
        return False

    if "Lantern" not in player["inventory"]:
        return False

    player["won"] = True
    player["game_over"] = True

    return True