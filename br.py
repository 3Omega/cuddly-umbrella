import pandas as pd

url = 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html'
dfs = pd.read_html(url)

# dfs is a list of dataframes, one for each table on the page
df = dfs[0]
df.drop_duplicates(inplace=True)

# Drop the second row and reset the index
df = df[df.Player != 'Player'].reset_index(drop=True)

df.to_csv("br.csv", index=False)
