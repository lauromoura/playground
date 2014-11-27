from elo import *
import csv

def main(argv=None):

    if argv is None:
        argv = sys.argv

    elo = Elo(k=13)

    teams = {}

    for filename in argv[1:]:
        with open(filename, 'rb') as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                if row['Div'] != "D1":
                    continue

                home = row['HomeTeam']
                away = row['AwayTeam']

                # FIXME DefaultDict
                if home not in teams:
                    teams[home] = Player(home)
                if away not in teams:
                    teams[away] = Player(away)

                home = teams[home]
                away = teams[away]
                match = Match(home, away)
                match.play(int(row['FTHG']), int(row['FTAG']))


    printTeams(teams)

if __name__ == '__main__':
    main()