import sys, os, inspect
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(Path(__file__).parent.parent), "src"))
import numpy as np

from app_lib_py import ClassCurves as cc


# ---------------------------------------------------------------------------
def _test_squared():
    print(f"Testing utility: {inspect.stack()[0][3]}")
    # x^2
    sq = cc.Quadratic(1, 0, 0)
    ys = sq.get_ys([0, 1, 2, 3])
    assert ys == [0.0, 1.0, 4.0, 9.0], ys

    # x^2 + bx
    sq = cc.Quadratic(1, 1, 0)
    ys = sq.get_ys([0, 1, 2, 3])
    assert ys == [0.0, 2.0, 6.0, 12.0], ys

    # x^2 + 1
    sq = cc.Quadratic(1, 0, 1)
    ys = sq.get_ys([0, 1, 2, 3])
    assert ys == [1.0, 2.0, 5.0, 10.0], ys


# ---------------------------------------------------------------------------
def _test_exponent():
    # y = ae^bx + c
    print(f"Testing utility: {inspect.stack()[0][3]}")
    # e^0
    ep = cc.Exponential(1, 0, 0)
    ys = ep.get_ys([0, 1, 2, 3])
    assert ys == [1.0, 1.0, 1.0, 1.0], ys
    # e^x
    ep = cc.Exponential(1, 1, 0)
    ys = np.round(np.array(ep.get_ys([0, 1, 2, 3])))
    assert ys == [1.0, 1.0, 1.0, 1.0], ys


###########################################################################
if __name__ == "__main__":
    _test_exponent()
    # _test_squared()
