import unittest
from Code.OOP.Circle import Circle
from Code.OOP.Analysis import Analysis


class TestCircle(unittest.TestCase):
    def test_spawn_circle(self):
        circle = Circle()
        circle.spawn()
        self.assertGreaterEqual(circle.x, circle.radius)
        self.assertLessEqual(circle.x, circle.window_width - circle.radius)

        self.assertGreaterEqual(circle.y, circle.radius)
        self.assertLessEqual(circle.y, circle.window_width - circle.radius)

    def test_update_spawn(self):
        circle = Circle()
        start = circle.radius
        circle.update(1.0)
        self.assertLess(circle.radius, start)

    def test_is_clicked(self):
        circle = Circle()
        circle.x, circle.y = 100, 100
        circle.radius = 100
        self.assertTrue(circle.is_clicked((100, 100)))
        self.assertFalse(circle.is_clicked((200, 200)))


class testAnalysis(unittest.TestCase):
    def test_record_clicks(self):
        analysis = Analysis()
        analysis.record_clicks(100, 100, 110, 110, 250)

        self.assertEqual(len(analysis.distances), 1)
        self.assertEqual(len(analysis.times), 1)
        self.assertEqual(analysis.times[0], 250)
        self.assertAlmostEqual(analysis.distances[0], 14.142, places=3)
