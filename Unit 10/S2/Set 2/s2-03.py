# ------------------------------------------------
#  *                    Problem 3: Buildings with an Ocean View
#
#    Given a list of integers heights representing building heights (ocean is
#    to the right), return a sorted list of indices of buildings that have an
#    ocean view. A building has an ocean view if all buildings to its right are
#    shorter.

def find_buildings(heights):
    pass


print(find_buildings([4, 2, 3, 1]))  # Expected Output: [0, 2, 3]
# Building 1 (height=2) is blocked by building 2 (height=3)

print(find_buildings([4, 3, 2, 1]))  # Expected Output: [0, 1, 2, 3]
# All buildings can see the ocean

print(find_buildings([1, 3, 2, 4]))  # Expected Output: [3]
# Only the last building can see the ocean

# ------------------------------------------------
