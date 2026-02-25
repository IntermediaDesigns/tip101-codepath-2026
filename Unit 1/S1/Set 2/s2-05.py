# ------------------------------------------------
#  *                    Problem 5: Calculate Tip
#
#    Write a function calculate_tip() that takes in a float bill and a string
#    service_quality as parameters.
#    If service_quality is "poor", return 10% of the bill value.
#    If service_quality is "average", return 15% of the bill value.
#    If service_quality is "excellent", return 20% of the bill value.
#    If service_quality is any other value, return None.


def calculate_tip(bill, service_quality):
    if service_quality == "poor":
        return bill * 0.1
    elif service_quality == "average":
        return bill * 0.15
    elif service_quality == "excellent":
        return bill * 0.2
    else:
        return None


tip1 = calculate_tip(44.53, "average")
print(tip1)

tip2 = calculate_tip(44.53, "poor")
print(tip2)

tip3 = calculate_tip(44.53, "excellent")
print(tip3)

# Example Output:
# 6.6795
# 4.453
# 8.906
#
# ------------------------------------------------
