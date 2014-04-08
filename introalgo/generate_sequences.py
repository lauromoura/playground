"""Helper script to generate sequences"""


import sys
import random

def write_data(filename, data):
	with open(filename, "w") as handle:
		handle.write(" ".join([str(x) for x in data]))


def main(argv=None):
	if (argv is None):
		argv = sys.argv

	size = int(argv[1])
	data = range(size)
	ordered_data = data[:]
	reversed_data = data[:]
	reversed_data.reverse()

	random.shuffle(data)

	write_data("ordered_" + argv[1] + ".txt", ordered_data)
	write_data("random_" + argv[1] + ".txt", data)
	write_data("reversed_" + argv[1] + ".txt", reversed_data)

if __name__ == '__main__':
	main()