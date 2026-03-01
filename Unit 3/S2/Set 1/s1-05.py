# ------------------------------------------------
#  *                    Problem 5: Teemo's Attack
#
#    In League of Legends, Teemo attacks Ashe with poison arrows. Write a function
#    find_poisoned_duration() that takes in time_series (a list of times Teemo attacks)
#    and duration (how long the poison lasts) as parameters. The function returns the
#    total time Ashe is in a poisoned state.
#
#    If Teemo hits Ashe while she is still poisoned, the poison duration resets.
#    Example: attacks at times [1, 4] with duration 3:
#      Time 1: attacked (poisoned for 3s)
#      Time 4: attacked again (poison resets to 3s)
#      Total poisoned time = (4-1) + 3 = 6


def find_poisoned_duration(time_series, duration):
    pass


time_series = [1, 4, 9]
damage = find_poisoned_duration(time_series, 3)
print(damage)

# Example Output: 8
#
# ------------------------------------------------
