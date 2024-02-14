import csv



def create_hof():

    with open("Scripts/data/hof.csv", "w", newline='') as file:
        fieldnames = ['name', 'rating', 'gamesPlayed',
                     'goalDifference', 'wins', 'draws', 'points',]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'name': "Invincible Gunners", 'rating': 95, 'gamesPlayed': 38,
                     'goalDifference': "+47", 'wins': 26, 'draws': 12, 'points': 90})
        writer.writerow({'name': "Silver Knights", 'rating': 94, 'gamesPlayed': 30,
                         'goalDifference': "+40", 'wins': 20, 'draws': 10, 'points': 70})
        writer.writerow({'name': "Bronze Satisfiers", 'rating': 92, 'gamesPlayed': 28,
                         'goalDifference': "+30", 'wins': 14, 'draws': 14, 'points': 56})
        writer.writerow({'name': "Rusty Warriors", 'rating': 90, 'gamesPlayed': 24,
                         'goalDifference': "+25", 'wins': 15, 'draws': 9, 'points': 54})
        writer.writerow({'name': "Squanchy Punishers", 'rating': 89, 'gamesPlayed': 22,
                         'goalDifference': "+24", 'wins': 14, 'draws': 8, 'points': 50})
        writer.writerow({'name': "Forward Pushers", 'rating': 87, 'gamesPlayed': 18,
                         'goalDifference': "+19", 'wins': 13, 'draws': 5, 'points': 44})
        writer.writerow({'name': "Fast Boys", 'rating': 86.5, 'gamesPlayed': 14,
                         'goalDifference': "+17", 'wins': 10, 'draws': 4, 'points': 34})
        writer.writerow({'name': "Meer Cats", 'rating': 85, 'gamesPlayed': 12,
                         'goalDifference': "+14", 'wins': 8, 'draws': 4, 'points': 27})
        writer.writerow({'name': "Crazy Puckers", 'rating': 83.69, 'gamesPlayed': 10,
                         'goalDifference': "+12", 'wins': 7, 'draws': 3, 'points': 24})
        writer.writerow({'name': "Simple Jacks", 'rating': 80, 'gamesPlayed': 6,
                         'goalDifference': "+7", 'wins': 4, 'draws': 2, 'points': 14})


def table_hof():
    tabHoF = []
    with open("Scripts/data/hof.csv", "r", newline='') as file:
        fieldnames = ['name', 'rating', 'gamesPlayed',
                     'goalDifference', 'wins', 'draws', 'points']
        reader = csv.DictReader(file, fieldnames=fieldnames)
        next(reader)
        for row in reader:
            team = {'name': row['name'], 'rating': row['rating'], 'gamesPlayed': int(row['gamesPlayed']),
                    'goalDifference': row['goalDifference'], 'wins': int(row['wins']), 'draws': int(row['draws']),
                    'points': int(row['points'])}

            tabHoF.append(team)
    return tabHoF

def compare_results(team , hof_table):
    if team['Games'] > hof_table[-1]['gamesPlayed']:
        hof_table.pop(-1)
        hof_table.append({'name': team['name'], 'rating': team['Rating'], 'gamesPlayed': team['Games'],
                    'goalDifference': team['+/-'], 'wins': team['W'], 'draws': team['D'],
                    'points': team['P']})
        hof_table.sort(reverse=True, key=Myfunc)

        with open("Scripts/data/hof.csv", "w", newline='') as file:
            fieldnames = ['name', 'rating', 'gamesPlayed',
                          'goalDifference', 'wins', 'draws', 'points', ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for team in hof_table:
                writer.writerow(team)



def Myfunc(e):
    """sort list with dictionary by one of values"""
    return e['gamesPlayed']


