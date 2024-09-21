import pandas as pd

# Load both datasets
matches_df = pd.read_csv("Indian Premier League/matches.csv")
players_df = pd.read_csv("Indian Premier League/deliveries.csv")

# Check the structure of both datasets
print(matches_df.info())
print(players_df.info())

# Display the first few rows of each dataset
print(matches_df.head())
print(players_df.head())

# Merge the two datasets on 'match_id' (or other relevant columns)
ipl_df = pd.merge(matches_df, players_df, on='match_id', how='inner')

# Display the merged dataset
print(ipl_df.head())


# Display the first few rows and summary
print(ipl_df.head())
print(ipl_df.info())
print(ipl_df.describe())
# Analyzing the total number of wins per team
wins_per_team = ipl_df['winner'].value_counts().head(10)
print(wins_per_team)

# Visualizing the results
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,6))
sns.barplot(x=wins_per_team.values, y=wins_per_team.index, palette='viridis')
plt.title('Most Successful IPL Teams (by wins)')
plt.xlabel('Number of Wins')
plt.ylabel('Teams')
plt.show()
# Top performing players based on 'Man of the Match' awards
top_players = ipl_df['player_of_match'].value_counts().head(10)
print(top_players)

# Visualizing top players
plt.figure(figsize=(10,6))
sns.barplot(x=top_players.values, y=top_players.index, palette='plasma')
plt.title('Top Players based on Man of the Match Awards')
plt.xlabel('Number of Awards')
plt.ylabel('Players')
plt.show()

# Analyzing the impact of toss decision on match result
toss_effect = ipl_df.groupby(['toss_decision', 'result']).size().unstack()
print(toss_effect)

# Visualizing toss decision impact
toss_effect.plot(kind='bar', stacked=True, figsize=(10,6))
plt.title('Impact of Toss Decision on Match Result')
plt.xlabel('Toss Decision')
plt.ylabel('Number of Matches')
plt.show()
# Recommending teams based on success
endorsement_teams = wins_per_team.head(5)
print("Recommended Teams for Endorsements:", endorsement_teams)
# Recommending players based on 'Man of the Match' awards
endorsement_players = top_players.head(5)
print("Recommended Players for Endorsements:", endorsement_players)



import plotly.express as px

# Sample data for team wins
team_wins = ipl_df['winner'].value_counts().reset_index()
team_wins.columns = ['winner', 'Wins']

# Creating an interactive bar chart with annotations
fig = px.bar(team_wins, x='winner', y='Wins', title='Most Successful Teams in IPL')

# Adding annotations for top-performing teams
fig.update_traces(marker_color='teal')
fig.update_layout(
    annotations=[
        dict(
            x=team_wins['winner'][0],  # Top team
            y=team_wins['Wins'][0],
            text="Top Team",  # Annotation text
            showarrow=True,
            arrowhead=2,
            ax=0, ay=-40
        ),
        dict(
            x=team_wins['winner'][1],
            y=team_wins['Wins'][1],
            text="2nd Best Team",
            showarrow=True,
            arrowhead=2,
            ax=0, ay=-40
        )
    ]
)

fig.show()
