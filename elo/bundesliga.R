
filenames <- c(
	"bundesliga/9394.csv",
	"bundesliga/9495.csv",
	"bundesliga/9596.csv",
	"bundesliga/9697.csv",
	"bundesliga/9798.csv"
	)

for (i in seq_along(filenames)) {
	data <- read.table(filenames[i])
	validData <- data[data$Div == "D1",]
}