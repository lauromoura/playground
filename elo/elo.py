import sys
import math
import operator

class Elo(object):
    def __init__(self, k=10):
        Elo.k = k


class Player(object):

    def __init__(self, name, initialElo=1500):
        self.name = name
        self.elo = initialElo

    def expectedScores(self, other):
        homeProb = 1 / (1 + 10**((other.elo - (self.elo + 65))/400.0))
        awayProb = 1 - homeProb
        return homeProb, awayProb

    def __repr__(self):
        return "%s (%s)" % (self.name, self.elo)

    def __cmp__(self, other):
        return int.__cmp__(self.elo, other.elo)

class Match(object):
    def __init__(self, homePlayer, awayPlayer):
        self.homePlayer = homePlayer
        self.awayPlayer = awayPlayer

    def play(self, homeScore, awayScore):
        diffScore = abs(homeScore - awayScore)
        expectedHome, expectedAway = self.homePlayer.expectedScores(self.awayPlayer)
        print self.homePlayer, expectedHome, self.awayPlayer, expectedAway

        outcome = max(min(homeScore - awayScore, 1), -1)

        eloWinner = self.homePlayer.elo
        eloLoser = self.awayPlayer.elo

        if outcome < 0:
            eloWinner, eloLoser = eloLoser, eloWinner

        marginMultiplier = math.log(diffScore+1) * (2.2/((eloWinner - eloLoser)*0.001+2.2))
        print "Margin multiplier", marginMultiplier
        
        if outcome:
            resultDelta = math.trunc((outcome - expectedHome) * Elo.k * marginMultiplier)        
        else: # Ties
            resultDelta = math.trunc((0.5-expectedHome) * Elo.k)
        print "Result delta", resultDelta
        self.homePlayer.elo += int(resultDelta)
        self.awayPlayer.elo += int((-resultDelta))
        print


def Week12Teams():
    teams = {
        'patriots': Player("Patriots", 1707),
        'cardinals': Player("Cardinals", 1654),
        'seahawks': Player("Seahawks", 1639),
        'chiefs': Player("Chiefs", 1602),
        'lions': Player("Lions", 1541),
        'raiders': Player("Raiders", 1261),
    }

    m1 = Match(teams['raiders'], teams['chiefs'])
    m1.play(24, 20)
    m2 = Match(teams['patriots'], teams['lions'])
    m2.play(34, 9)
    m3 = Match(teams['seahawks'], teams['cardinals'])
    m3.play(19, 3)

    return teams
    
def printTeams(teams):
    print
    sorted_teams = sorted(teams.items(), key=operator.itemgetter(1), reverse=True)
    for team in sorted_teams:
        print team
    print

def main(argv=None):

    elo = Elo(k=20)
    panthers = Player("panthers", 1542)
    bengals = Player("bengals", 1578)
    m1 = Match(bengals, panthers)
    m1.play(37, 37)
    print panthers, bengals

    print Week12Teams()

if __name__ == '__main__':
    main()