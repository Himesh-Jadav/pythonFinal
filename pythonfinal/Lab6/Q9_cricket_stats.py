# Team: list of tuples (player, runs, wickets)
teams = {'Team A': [('P1', 80, 1), ('P2', 20, 3)], 'Team B': [('P3', 90, 0), ('P4', 30, 4)]}
best_batsman = max((p for players in teams.values() for p in players), key=lambda x: x[1])
best_bowler = max((p for players in teams.values() for p in players), key=lambda x: x[2])
team_score = {team: sum(p[1] + p[2]*10 for p in players) for team, players in teams.items()}
print("Best batsman:", best_batsman)
print("Best wicket taker:", best_bowler)
print("Best team:", max(team_score, key=team_score.get), team_score)
