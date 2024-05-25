import pandas as pd
import datetime
from os.path import dirname, abspath
import sys

DIR = dirname(abspath(__file__))
sys.path.append(dirname(dirname(DIR)))
print("Loading to path", dirname(dirname(DIR)))

ITERS = 1000000
FACTOR_MIN = 0.1
FACTOR_MAX = 1.5


def get_iterations():
    return ITERS


def get_last_speed(function_name):
    df_speeds = pd.read_csv(f"{DIR}/data/speed_log.csv")
    df_speeds["timedelta"] = pd.to_timedelta(df_speeds["timedelta"])
    rows = df_speeds[df_speeds["function"] == function_name]
    rows = rows[rows["iterations"] == ITERS]
    if len(rows) == 0:
        print("Function not yet run", function_name)
        return datetime.timedelta(0), datetime.timedelta(0), False
    else:
        min_row = min(rows["timedelta"])
        max_row = max(rows["timedelta"])
        print("Min entry=", min_row, "Max entry=", max_row)
        return min_row, max_row, True


def get_start():
    return datetime.datetime.today()


def get_speed(start):
    end = datetime.datetime.today()
    return end - start


def is_it_error(function_name, speed):
    min_last, max_last, exists = get_last_speed(function_name)
    print(f"min:{min_last} now:{speed} max:{max_last}")
    # we don't want the difference in speed to be more than FACTOR of the speed itself
    if not exists:
        return True
    if speed < min_last * FACTOR_MIN:
        print(
            f"Failing min because {min_last} < {FACTOR_MIN}*{min_last}={FACTOR_MIN*min_last}"
        )
        return False
    if speed > max_last * FACTOR_MAX:
        print(
            f"Failing max because {speed} > {FACTOR_MAX}*{max_last}={FACTOR_MAX*max_last}"
        )
        return False
    return True


def update_speed(function_name, speed, date):
    print(function_name, date, speed)
    with open(f"{DIR}/data/speed_log.csv", "a") as fa:
        fa.write(f"{date},{function_name},{ITERS},{speed}\n")
