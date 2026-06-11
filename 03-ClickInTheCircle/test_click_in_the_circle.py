import importlib.util
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).with_name("ClickInTheCircle.py")
spec = importlib.util.spec_from_file_location("click_in_the_circle", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class DistanceTests(unittest.TestCase):
    def test_distance_between_two_points(self):
        self.assertEqual(module.distance((0, 0), (3, 4)), 5.0)

    def test_distance_for_same_point(self):
        self.assertEqual(module.distance((5, 5), (5, 5)), 0.0)


if __name__ == "__main__":
    unittest.main()
