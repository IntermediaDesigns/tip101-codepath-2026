# ------------------------------------------------
#  *                    Problem 7: Best Team
#
#    Write a function team_with_best_average_score() that returns the team with the
#    highest average score over a season. The function accepts a list of dictionaries
#    named games, each with "team_name" and "score" keys. The function calculates
#    the average score for each team across all games and returns the team name with
#    the highest average score.


def team_with_best_average_score(games):
    pass


games = [
    {"team_name": "Lions", "score": 23},
    {"team_name": "Tigers", "score": 30},
    {"team_name": "Lions", "score": 27},
    {"team_name": "Bears", "score": 20},
    {"team_name": "Tigers", "score": 24},
    {"team_name": "Bears", "score": 22}
]
print(team_with_best_average_score(games))

# Example Output: Tigers
#
# ------------------------------------------------
