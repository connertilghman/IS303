# Video Game Catalog Manager
# Reads csv, lets the user update status, adds a recommended column, and saves everything to a new file.

import pandas as pd

# Read the original file
games = pd.read_csv("video_games_raw.csv")

# Ask for a row number and make sure it is valid
while True:
    try:
        row_number = int(input("Enter a row number to inspect: "))
        if 0 <= row_number < len(games):
            break
        print(f"Please enter a number between 0 and {len(games) - 1}.")
    except ValueError:
        print("Please enter a whole number.")

# iloc accesses a row by its position
game = games.iloc[row_number]
print("\nSelected Game:")
print(f"Title: {game['Title']}")
print(f"Platform: {game['Platform']}")
print(f"Genre: {game['Genre']}")
print(f"Rating: {game['Rating']}")
print(f"Current Status: {game['Status']}")

# Ask for the new status
new_status = input("\nEnter a new status: ").strip()

# The default index matches the row position, so row_number works as the label
games.at[games.index[row_number], "Status"] = new_status

# Start every game as "No", then use .loc[] to change multiple rows at once
games["Recommended"] = "No"
games.loc[(games["Rating"] >= 8) & (games["Price"] <= 40), "Recommended"] = "Yes"

# query filters the DataFrame to only the recommended games
print("Recommended Games:")
recommended = games.query("Recommended == 'Yes'")
print(recommended[["Title", "Platform", "Price", "Rating"]])

# to_csv saves the updated data to a new file
games.to_csv("video_games_cleaned.csv", index=False)
