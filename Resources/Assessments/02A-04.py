# Get Top Player

# The following function accepts a dictionary which maps player names to their score and wants to return the name of the highest scoring player. However, its not working as intended. How do we modify this function to actually return the player with the highest score?

dictionary = {"Audrey": 90, "Char": 60, "Mario": 95, "Kyra": 12}

# Expected output: "Mario"

def get_top_player(dictionary):
    high_score = 0
    top_player = ""
    
    for name, score in dictionary.items():
        if score > high_score:
            high_score= score
            top_player = name
    return top_player

print(get_top_player(dictionary))  # Should print "Mario"

# Pick ONE of the following options to fix the function:

# 1. Replace high_score += score with high_score = score

# 2. Replace top_player = "" with top_player = dictionary[0]

# 3. Replace return top_player with return high_score

# 4. Replace top_placer = name with name = top_player


# The correct answer is option 1. We need to replace high_score += score with high_score = score. This way, we update high_score to be the current player's score when we find a new high score, instead of adding the current player's score to the existing high_score.