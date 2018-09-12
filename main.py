from game import Game

if __name__ == "__main__":
	game = Game()
	try:
		game.new_round()
	except KeyboardInterrupt:
		print "Exiting program"