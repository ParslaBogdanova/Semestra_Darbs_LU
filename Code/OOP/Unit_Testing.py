import unittest
import numpy as np
from OOP.Circle import Circle
from OOP.Analysis import Analysis


# Vēl tiek piestrādāts un testēts, kods vēl nestrādā.
class Circle:
    def __init__(
            self, x=100, y=100, radius=10, window_width=720, window_height=720):
        self.x = x
        self.y = y
        self.radius = radius
        self.window_width = window_width
        self.window_height = window_height

    def __call__(self, dx, dy):
        x = self.x
        y = self.y
        radius = self.radius
        window_width = self.window_width
        window_height = self.window_height

        dx = window_width-radius
        dy = window_height-radius
        d = np.sqrt(dx**2+dy**2)
        return d


class TestCircle(unittest.TestCase):
    def test_spawn_circle(self):
        circle = Circle()
        circle.spawn()
        self.assertGreaterEqual(circle.x, circle.radius)
        self.assertLessEqual(circle.x, circle.window_width - circle.radius)

        self.assertGreaterEqual(circle.y, circle.radius)
        self.assertLessEqual(circle.y, circle.window_height - circle.radius)

    def test_update_spawn(self):
        circle = Circle()
        start = circle.radius
        circle.update(1)
        self.assertLess(circle.radius, start)

    def test_is_clicked(self):
        circle = Circle()
        circle.x, circle.y = 100, 100
        circle.radius = 100
        self.assertTrue(circle.is_clicked((100, 100)))
        self.assertFalse(circle.is_clicked((200, 200)))


if __name__ == "__main__":
    unittest.main()
