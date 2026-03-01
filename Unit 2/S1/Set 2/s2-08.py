# ------------------------------------------------
#  *                    Problem 8: Quality Control
#
#    Write a function quality_control() that takes in a dictionary product_scores
#    and an integer threshold as parameters. The dictionary maps product IDs to
#    their quality ratings. If a product's score >= threshold, categorize it as
#    "pass". If a product's score < threshold, categorize it as "fail".
#    The function returns a new dictionary mapping product IDs to "pass" or "fail".


def quality_control(product_scores, threshold):
    pass


product_scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
threshold = 60
print(quality_control(product_scores, threshold))

# Example Output: {'x0123': 'pass', 'x0124': 'fail', 'x0125': 'pass', 'x0126': 'fail'}
#
# ------------------------------------------------
