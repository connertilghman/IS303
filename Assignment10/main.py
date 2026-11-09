# College Football Season
# This program lets the user pick a season from cfb.csv and shows
# the teams from that season sorted into groups by number of wins.

import pandas as pd

# Column names from the CSV file 
season_column = "Season"
team_column = "Team"
wins_column = "Win"

def categorize_teams(season_data):
    # Dictionary where each key is a category and each value is a list of teams
    categories = {
        "10 or more wins": [],
        "8-9 wins": [],
        "6-7 wins": [],
        "Fewer than 6 wins": [],
    }
 # Go through each row (team) in the season's data
    for _, row in season_data.iterrows():
        team = row[team_column]
        win = row[wins_column]
 # Check the wins from highest to lowest and add the team to the right list
        if win >= 10:
            categories["10 or more wins"].append((team, win))
        elif win >= 8:
            categories["8-9 wins"].append((team, win))
        elif win >= 6:
            categories["6-7 wins"].append((team, win))
        else:
            categories["Fewer than 6 wins"].append((team, win))
 
    return categories

def display_categories(season, categories):
    print(f"\n{season} Season")
    # Loop through each category and its list of teams
    for label, teams in categories.items():
        print(f"\n{label} ({len(teams)} teams):")
        if not teams:
            print("  (none)")
        # Sort by most wins first, then alphabetically if wins are tied
        for team, win in sorted(teams, key=lambda t: (-t[1], t[0])):
            print(f"  {team}: {int(win)} wins")

def main():
    # Read the CSV file into a Pandas DataFrame
    data = pd.read_csv("cfb.csv")
 
    for col in (season_column, team_column, wins_column):
        if col not in data.columns:
            print(f"Column '{col}' not found in cfb.csv.")
            return
 # Get a sorted list of every season in the file (no hard-coded years)
    seasons = sorted(data[season_column].unique())
    print(f"Seasons available: {seasons[0]} to {seasons[-1]}")
 
    while True:
        choice = input("Which season would you like to analyze? (or 'q' to quit): ").strip()
        if choice.lower() == "q":
            print("Goodbye!")
            break
 
        try:
            season = int(choice)
        except ValueError:
            print("Please enter a valid year, like 2015.")
            continue
 # Keep only the rows that match the chosen season
        season_data = data[data[season_column] == season]
        if season_data.empty:
            print(f"Season {season} was not found in the data.")
        else:
            display_categories(season, categorize_teams(season_data))

main()