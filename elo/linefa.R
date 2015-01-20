source("elo.R")

teams <- read.table("teamsPE2015.txt", header=TRUE, stringsAsFactors=FALSE)

loadSeason <- function(filename, teams) {
	print(filename)
	print(teams)
	matches <- read.table(filename, header=TRUE, stringsAsFactors=FALSE)
	for (i in seq(nrow(matches))) {
		homeElo <- teams[teams$Name == matches[i,"HomeTeam"] ,"Rating"]
		awayElo <- teams[teams$Name == matches[i,"AwayTeam"] ,"Rating"]
		homeScore <- matches[i, "HomeScore"]
		awayScore <- matches[i, "AwayScore"]
		shouldIgnoreHome <- matches[i, "IgnoreHome"]
		if (is.na(shouldIgnoreHome)){
			shouldIgnoreHome <- FALSE
		}
		print(matches[i,])
		newElo <- playMatch(homeElo, awayElo, homeScore, awayScore, ignoreHome=shouldIgnoreHome, debug=TRUE)
		teams[teams$Name == matches[i,"HomeTeam"] ,"Rating"] <- newElo[1]
		teams[teams$Name == matches[i,"AwayTeam"] ,"Rating"] <- newElo[2]
		print(teams[sort(teams$Rating, decreasing=TRUE, index.return=TRUE)$ix,])
	}
}

teams <- loadSeason("PE2015.txt", teams)
# teams <- loadSeason("linefa2012.txt", teams)
# teams <- loadSeason("linefa2014.txt", teams)