
import gtk


class Model(object):

	def __init__(self, numPlayers, timePerPlayer=300):

		self.players = [timePerPlayer]*numPlayers
		self.currentPlayer = 0

	def tick(self, elapsed=1):
		"""Count a tick, updating the player times"""

		self.players[self.currentPlayer] -= elapsed

	def next(self):
		self.currentPlayer = (self.currentPlayer + 1) % len(self.players)

	def previous(self):
		self.currentPlayer = (self.currentPlayer - 1) % len(self.players)

	def printData(self):
		print "currentPlayer: %s" % self.currentPlayer
		print "players: %s" % self.players


def quit_function():
	gtk.main_quit()

	return False

def loop_function(model):
	model.tick()
	model.printData()

	return True

def main():

	model = Model(5)
	gtk.timeout_add(1000, loop_function, model)

	gtk.main()

if __name__ == '__main__':
	main()