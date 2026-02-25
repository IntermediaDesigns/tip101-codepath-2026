# ------------------------------------------------
#  *                    Problem 4: Sleep Assessment
#
#    Write a function sleep_assessment() that takes in an integer parameter hours
#    indicating the number of hours the user slept.
#    If hours is less than 8, print "Oof, go back to bed!".
#    If hours is >= 8 and <= 10, print "You got a good night's rest!".
#    If hours is greater than 10, print "You're a sleep prodigy!".


def sleep_assessment(hours):
    if hours < 8:
        print("Oof, go back to bed!")
    elif hours <= 10:
        print("You got a good night's rest!")
    else:
        print("You're a sleep prodigy!")


sleep_assessment(10)
sleep_assessment(4)
sleep_assessment(12)
sleep_assessment(9)

# Example Output:
# You got a good night's rest!
# Oof, go back to bed!
# You're a sleep prodigy!
# You got a good night's rest!
#
# ------------------------------------------------
