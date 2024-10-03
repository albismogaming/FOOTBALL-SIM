import numpy as np
import pandas as pd

def mini_football_game():
    home_score = []
    away_score = []
    quarters = 4
    overtime = False

    # Scoring options and their probabilities
    scores = [0, 3, 7]
    probs = [0.65, 0.15, 0.20]

    # Define random possessions for each quarter
    possessions_per_qtr = {
        1: np.random.randint(2, 3),  # Fewer possessions in early quarters
        2: np.random.randint(2, 4),
        3: np.random.randint(2, 3),
        4: np.random.randint(3, 5)   # More possessions in the 4th quarter
    }

    # Simulate 4 quarters with random possessions for each
    for qtr in range(1, quarters + 1):
        home_qtr = []
        away_qtr = []
        
        for _ in range(possessions_per_qtr[qtr]):
            home = np.random.choice(scores, p=probs)
            away = np.random.choice(scores, p=probs)
            home_qtr.append(home)
            away_qtr.append(away)

        home_score.append(sum(home_qtr))
        away_score.append(sum(away_qtr))

    # Calculate total scores after 4 quarters
    home_total = sum(home_score)
    away_total = sum(away_score)

    # Check for overtime if the scores are tied
    if home_total == away_total:
        overtime = True
        print("Overtime!")
        while overtime:
            home_ot = np.random.choice(scores, p=probs)
            away_ot = np.random.choice(scores, p=probs)
            home_total += home_ot
            away_total += away_ot
            home_score.append(home_ot)
            away_score.append(away_ot)

            # End overtime if scores are no longer tied
            if home_total != away_total:
                overtime = False

    # Append final scores
    home_score.append(home_total)
    away_score.append(away_total)

    # Define columns dynamically based on whether there's overtime
    if len(home_score) == 6:  # If there's overtime
        columns = ["1", "2", "3", "4", "OT", "F"]
    else:
        columns = ["1", "2", "3", "4", "F"]

    # Create DataFrame and print
    print(pd.DataFrame([home_score, away_score], index=["HOME", "AWAY"], columns=columns))

mini_football_game()
