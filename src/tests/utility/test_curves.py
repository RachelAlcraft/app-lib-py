import sys
import os
import inspect
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(Path(__file__).parent.parent), ""))
from app_lib_py import ClassCurves as cc


# ---------------------------------------------------------------------------
def test_squared():
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
def test_exponent():
    # y = ae^bx + c
    print(f"Testing utility: {inspect.stack()[0][3]}")
    # e^0
    ep1 = cc.Exponential(1, 0, 0)
    ys1 = ep1.get_ys([0, 1, 2, 3])
    assert ys1 == [1.0, 1.0, 1.0, 1.0], "1" + str(ys1)
    # e^x
    ep2 = cc.Exponential(1, 1, 0)
    ys2 = ep2.get_ys([0, 1, 2, 3])
    ys2 = [int(round(x, 0)) for x in ys2]
    assert ys2 == [1, 3, 7, 20], "2" + str(ys2)

    # 2e^x + 1
    ep3 = cc.Exponential(2, 1, 1)
    ys3 = ep3.get_ys([0, 1, 2, 3])
    ys3 = [int(round(x, 0)) for x in ys3]
    assert ys3 == [3, 6, 16, 41], "3" + str(ys3)


###########################################################################
if __name__ == "__main__":
    test_exponent()
    # test_squared()
