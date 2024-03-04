import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'results.csv'
data = pd.read_csv(file_path)


data['date'] = pd.to_datetime(data['date'])
data['year'] = data['date'].dt.year


matches_per_year = data['year'].value_counts().sort_index()

plt.figure(figsize=(15, 7))
sns.lineplot(x=matches_per_year.index, y=matches_per_year.values)
plt.title('Number of Matches Played Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Matches')
plt.grid(True)
plt.show()


hosted_matches = data['country'].value_counts()

top_10_hosted = hosted_matches.head(10)


plt.figure(figsize=(12, 6))
sns.barplot(x=top_10_hosted.values, y=top_10_hosted.index, palette="Blues_d")
plt.title('Top 10 Countries with the Most Hosted Matches')
plt.xlabel('Number of Matches Hosted')
plt.ylabel('Country')
plt.show()

# Creating a new column for match score
data['match_score'] = data['home_score'].astype(str) + '-' + data['away_score'].astype(str)

# Getting the top 10 most common match scores
top_scores = data['match_score'].value_counts().head(10)

# Plotting the most common match scores
plt.figure(figsize=(12, 6))
sns.barplot(x=top_scores.index, y=top_scores.values, palette="mako")
plt.title('Top 10 Most Common Match Scores')
plt.xlabel('Match Score')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

team = 'England'

# Identifying wins, losses, and draws for the selected team
wins = data[(data['home_team'] == team) & (data['home_score'] > data['away_score'])].shape[0] + \
       data[(data['away_team'] == team) & (data['away_score'] > data['home_score'])].shape[0]

losses = data[(data['home_team'] == team) & (data['home_score'] < data['away_score'])].shape[0] + \
         data[(data['away_team'] == team) & (data['away_score'] < data['home_score'])].shape[0]

draws = data[(data['home_team'] == team) & (data['home_score'] == data['away_score'])].shape[0] + \
        data[(data['away_team'] == team) & (data['away_score'] == data['home_score'])].shape[0]

# Data for plotting
labels = 'Wins', 'Losses', 'Draws'
sizes = [wins, losses, draws]

# Plotting the win-loss-draw ratio in a pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.title(f'Win-Loss-Draw Ratio for {team}')
plt.show()

# Counting the number of matches by tournament type
tournament_counts = data['tournament'].value_counts()

# Selecting the top 10 most frequent tournaments for a clearer visualization
top_tournaments = tournament_counts.head(10)

# Plotting the frequency of different tournament types
plt.figure(figsize=(12, 6))
sns.barplot(x=top_tournaments.values, y=top_tournaments.index, palette="cubehelix")
plt.title('Top 10 Most Frequent Tournament Types')
plt.xlabel('Number of Matches')
plt.ylabel('Tournament Type')
plt.show()

home_wins = data[data['home_score'] > data['away_score']].shape[0]
away_wins = data[data['home_score'] < data['away_score']].shape[0]

# Data for plotting
categories = ['Home Wins', 'Away Wins']
values = [home_wins, away_wins]

# Plotting the comparison of home wins vs away wins
plt.figure(figsize=(8, 6))
sns.barplot(x=categories, y=values, palette="pastel")
plt.title('Home vs Away Wins')
plt.ylabel('Number of Wins')
plt.show()