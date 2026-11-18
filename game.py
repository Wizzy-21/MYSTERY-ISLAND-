# MYSTERY ISLAND - GAME LOGIC

def explore_location(player):

    location = player["location"]

    discoveries = {
        "Beach": """
You begin exploring the beach.

You notice footprints leading towards the jungle.
Nearby, you spot a piece of rope washed ashore.
It might prove useful during your adventure.
""",

        "Jungle": """
You begin exploring the jungle.

You notice broken branches along a narrow path.
Something appears to have passed through recently.
You also discover a path leading towards a dark cave.
""",

        "Cave": """
You begin exploring the cave.

You notice strange markings on the cave walls.
A dusty Lantern lies near a pile of rocks.
You wonder whether it could help you later.
""",

        "Old Bridge": """
You begin examining the Old Bridge.

Several wooden planks are damaged.
The bridge looks dangerous to cross without proper equipment.
You notice the Lighthouse standing beyond it.
""",

        "Lighthouse": """
You begin exploring the Lighthouse.

You discover that the beacon is switched off.
The lighthouse appears to need a source of light.
Perhaps the Lantern you found earlier can help.
"""
    }

    return discoveries.get(
        location,
        "There is nothing interesting to discover here."
    )

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
        player["game_over"] = True
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


def check_surroundings(player):

    location = player["location"]

    surroundings = {
        "Beach": """
You look around the beach.

You notice footprints leading towards the jungle.
Something useful appears to have washed ashore.
The jungle path is your only visible route forward.
""",

        "Jungle": """
You examine the jungle carefully.

Tall trees surround you.
You notice a narrow path leading deeper into the jungle.
You can also see the beach behind you and a cave ahead.
""",

        "Cave": """
You look around the dark cave.

The cave is cold and unusually quiet.
You notice an old Lantern lying near the cave wall.
A path leads back towards the jungle, while another leads to the Old Bridge.
""",

        "Old Bridge": """
You inspect the old bridge.

The bridge looks unstable and dangerous.
Your Rope could help you cross safely.
Beyond the bridge, you can see the Lighthouse.
""",

        "Lighthouse": """
You examine the lighthouse.

The lighthouse beacon is currently switched off.
A powerful light could attract the attention of rescue boats.
You are very close to escaping the island.
"""
    }

    return surroundings.get(location, "There is nothing interesting here.")

