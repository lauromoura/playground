from elo import *

def brasilTeams():

    return {k: Player(k) for k in ["Atletico-MG",
                                    "Atletico-PR",
                                    "Bahia",
                                    "Botafogo",
                                    "Chapecoense",
                                    "Corinthians",
                                    "Coritiba",
                                    "Criciuma",
                                    "Cruzeiro",
                                    "Figueirense",
                                    "Flamengo",
                                    "Fluminense",
                                    "Goias",
                                    "Gremio",
                                    "Internacional",
                                    "Palmeiras",
                                    "Santos",
                                    "Sao Paulo",
                                    "Sport",
                                    "Vitoria"]}

def rodada1(teams):
    m = Match(teams["Fluminense"], teams["Figueirense"])
    m.play(3, 0)
    m = Match(teams["Internacional"], teams["Vitoria"])
    m.play(1, 0)
    m = Match(teams["Chapecoense"], teams["Coritiba"])
    m.play(0, 0)
    m = Match(teams["Sao Paulo"], teams["Botafogo"])
    m.play(3, 0)
    m = Match(teams["Atletico-PR"], teams["Gremio"])
    m.play(1, 0)
    m = Match(teams["Atletico-MG"], teams["Corinthians"])
    m.play(0, 0)
    m = Match(teams["Bahia"], teams["Cruzeiro"])
    m.play(1, 2)
    m = Match(teams["Flamengo"], teams["Goias"])
    m.play(0, 0)
    m = Match(teams["Santos"], teams["Sport"])
    m.play(1, 1)
    m = Match(teams["Criciuma"], teams["Palmeiras"])
    m.play(1, 2)
    return

def rodada2(teams):
    m = Match(teams["Coritiba"], teams["Santos"])
    m.play(0, 0)
    m = Match(teams["Palmeiras"], teams["Fluminense"])
    m.play(0, 1)
    m = Match(teams["Botafogo"], teams["Internacional"])
    m.play(2, 2)
    m = Match(teams["Corinthians"], teams["Flamengo"])
    m.play(2, 0)
    m = Match(teams["Cruzeiro"], teams["Sao Paulo"])
    m.play(1, 1)
    m = Match(teams["Vitoria"], teams["Atletico-PR"])
    m.play(2, 2)
    m = Match(teams["Sport"], teams["Chapecoense"])
    m.play(2, 1)
    m = Match(teams["Gremio"], teams["Atletico-MG"])
    m.play(2, 1)
    m = Match(teams["Figueirense"], teams["Bahia"])
    m.play(0, 2)
    m = Match(teams["Goias"], teams["Criciuma"])
    m.play(1, 0)
    return

def main():

    elo = Elo(k=20)
    teams = brasilTeams()

    printTeams(teams)
    # Rodada 1
    rodada1(teams)
    printTeams(teams)
    rodada2(teams)
    printTeams(teams)

if __name__ == '__main__':
    main()
