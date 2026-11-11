import unittest

from game import create_player, move_player, collect_item, light_lighthouse


class TestMovement(unittest.TestCase):

    def test_player_can_move_to_jungle(self):
        player = create_player("Alex")

        result = move_player(player, "Jungle")

        self.assertTrue(result)
        self.assertEqual(player["location"], "Jungle")
        self.assertEqual(player["energy"], 4)

    def test_player_cannot_jump_to_lighthouse(self):
        player = create_player("Alex")

        result = move_player(player, "Lighthouse")

        self.assertFalse(result)
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)

    def test_player_cannot_cross_bridge_without_rope(self):
        player = create_player("Alex")
        player["location"] = "Cave"

        result = move_player(player, "Old Bridge")

        self.assertFalse(result)
        self.assertEqual(player["location"], "Cave")
        self.assertEqual(player["energy"], 5)


    def test_player_can_cross_bridge_with_rope(self):
        player = create_player("Alex")
        player["location"] = "Cave"
        player["inventory"].append("Rope")

        result = move_player(player, "Old Bridge")

        self.assertTrue(result)
        self.assertEqual(player["location"], "Old Bridge")
        self.assertEqual(player["energy"], 4)    

class TestItemCollection(unittest.TestCase):

    def test_player_can_collect_rope(self):
        player = create_player("Alex")

        result = collect_item(player, "Rope")

        self.assertTrue(result)
        self.assertIn("Rope", player["inventory"])

    def test_player_can_collect_lantern(self):
        player = create_player("Alex")
        player["location"] = "Cave"

        result = collect_item(player, "Lantern")

        self.assertTrue(result)
        self.assertIn("Lantern", player["inventory"])

    def test_player_cannot_collect_item_from_wrong_location(self):
        player = create_player("Alex")

        result = collect_item(player, "Lantern")

        self.assertFalse(result)
        self.assertEqual(player["inventory"], [])

    def test_player_cannot_collect_same_item_twice(self):
        player = create_player("Alex")

        collect_item(player, "Rope")
        result = collect_item(player, "Rope")

        self.assertFalse(result)
        self.assertEqual(player["inventory"], ["Rope"]) 

class TestLighthouse(unittest.TestCase):

    def test_player_can_light_lighthouse_with_lantern(self):
        player = create_player("Alex")
        player["location"] = "Lighthouse"
        player["inventory"].append("Lantern")

        result = light_lighthouse(player)

        self.assertTrue(result)
        self.assertTrue(player["won"])
        self.assertTrue(player["game_over"])

    def test_player_cannot_light_lighthouse_without_lantern(self):
        player = create_player("Alex")
        player["location"] = "Lighthouse"

        result = light_lighthouse(player)

        self.assertFalse(result)
        self.assertFalse(player["won"])
        self.assertFalse(player["game_over"])

    def test_player_cannot_light_lighthouse_from_wrong_location(self):
        player = create_player("Alex")
        player["inventory"].append("Lantern")

        result = light_lighthouse(player)

        self.assertFalse(result)
        self.assertFalse(player["won"])      

if __name__ == "__main__":
    unittest.main()
