def save_scoreboard(score):
    # Read the existing scores
    try:
        with open('data/scores.txt', 'r') as f:
            scores = [int(line.strip()) for line in f]
    except FileNotFoundError:
        scores = []

    # Add the current score if it's higher than the lowest score or if there are less than 10 scores
    if len(scores) < 10 or score > min(scores):
        scores.append(score)

    # Sort the scores in descending order and keep only the top 10
    scores = sorted(scores, reverse=True)[:10]

    # Write the scores back to the file
    with open('data/scores.txt', 'w') as f:
        for score in scores:
            f.write(str(score) + '\n')

def get_high_score():
    try:
        with open('data/scores.txt', 'r') as f:
            scores = [int(line.strip()) for line in f]
    except FileNotFoundError:
        return 0

    return max(scores)