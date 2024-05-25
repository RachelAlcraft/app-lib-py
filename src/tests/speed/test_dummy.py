"""
Test the speed of dummy functionality
"""
from os.path import dirname, abspath
import sys

DIR = dirname(abspath(__file__))
sys.path.append((DIR))
print("Loading to path", (DIR))
import help_speed as hs  # noqa: E402
from app_lib_py import ClassCurves as cc  # noqa: E402


def test_numpy():
    start = hs.get_start()
    for i in range(hs.get_iterations()):
        if i % 100000 == 0:
            print(f"{i}/{hs.get_iterations()}", "load_quadratic")
        sq = cc.Quadratic(1, 0, 0)
        ys = sq.get_ys([0, 1, 2, 3])
    total_speed = hs.get_speed(start)
    assert hs.is_it_error("test_numpy", total_speed), f"test_numpy, {total_speed}"
    hs.update_speed("test_numpy", total_speed, start)


if __name__ == "__main__":
    test_numpy()
