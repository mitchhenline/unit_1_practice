


def team_input():
    team1 = input('What is the name of the home team? -- ')
    try:
        score1 = float(input('How many points did the home team score? -- '))
    except:
        score1 = float(input('Please enter a number for how many points the home team scored -- '))
    team2 = input('What is the name of the visiting team? -- ')
    try:
        score2 = float(input('How many points did the visiting team score? -- '))
    except:
        score2 = float(input('Please enter a number for how many points the visiting team scored -- '))

    team_dictionary = {
        "home_team": team1,
        "home_score": score1,
        "visiting_team": team2,
        "visiting_score": score2
    }

    return team_dictionary

team_input()