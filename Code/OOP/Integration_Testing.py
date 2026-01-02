# import unittest
# from Code.OOP.Game import Game


# class TestGame(unittest.TestCase):
#     def test_click_miss(self):
#         game = Game()
#         game.circle.radius = 0
#         game.check_miss()
#         self.assertEqual(game.miss_count, 0)
#         self.assertFalse(game.game_over)

#     def test_game_over(self):
#         game = Game()
#         game.max_misses = 10
#         game.circle.radius = 0

#         for _ in range(10):
#             game.check_miss()

#         self.assertEqual(game.miss_count, 10)
#         self.assertTrue(game.game_over)
