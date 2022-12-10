


def team_input():
    team1 = input('What is the name of the home team? -- ')
    try:
        score1 = int(input('How many points did the home team score? -- '))
    except:
        score1 = int(input('Please enter a number for how many points the home team scored -- '))
    team2 = input('What is the name of the visiting team? -- ')
    try:
        score2 = int(input('How many points did the visiting team score? -- '))
    except:
        score2 = int(input('Please enter a number for how many points the visiting team scored -- '))

    team_dictionary = {
        "home_team": team1,
        "home_score": score1,
        "visiting_team": team2,
        "visiting_score": score2
    }

    if score1 > score2:
        return f"{team1} beat {team2} by a score of {score1}-{score2}."
    elif score2 > score1:
        return f"{team2} beat {team1} by a score of {score2}-{score1}."
    elif score1==score2:
        return f"{team1} and {team2} tied with {score1} points each."
    return team_dictionary

# print(team_input())


mountainwest = {'usu':"aggies", "bsu":"broncos","wyoming":"cowboys"}


# print(mountainwest.values())

myfile = open('myfile.txt')

print(myfile.read())