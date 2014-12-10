
teams <- matrix(NA, 0, 1)

probabilities <- function (homeElo, awayElo, homeAdv=TRUE) {
	if (homeAdv)
		homeElo <- homeElo + 65

	1 / (1 + 10^((awayElo - homeElo)/400))
}

marginMultiplier <- function(eloWinner, eloLoser, diffScore) {
	log(diffScore + 1) * (2.2/((eloWinner - eloLoser)*0.001+2.2))
}

playMatch <- function (homeElo, awayElo, homeScore, awayScore, k=20, ignoreHome=FALSE, debug=FALSE) {
	diffScore <- abs(homeScore - awayScore)
	expectedHome <- probabilities(homeElo, awayElo, homeAdv=!ignoreHome)

	# Pos: Home win. Neg: away win. 0: tie.
	outcome <- max(min(homeScore - awayScore, 1), -1)

	eloWinner <- homeElo
	eloLoser <- awayElo

	if (outcome < 0) {
		eloWinner <- awayElo
		eloLoser <- homeElo
	}


	if (outcome) {
		margMult <- marginMultiplier(eloWinner, eloLoser, diffScore)
		resultDelta <- trunc((outcome - expectedHome) * k * margMult)
	} else {
		resultDelta <- trunc((0.5 - expectedHome) * k)
	}

	if (debug) {
		print(c("Home elo: ", homeElo))
		print(c("Away elo: ", awayElo))
		print(c("Expected prob of home win:", expectedHome))
		if(outcome) {
			margMult <- marginMultiplier(eloWinner, eloLoser, diffScore)
			print(c("Margin multiplier", margMult))
		}
		print(c("Result delta: ", resultDelta))
	}

	c(homeElo + resultDelta, awayElo - resultDelta)
}