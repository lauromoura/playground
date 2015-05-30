
FLAGS=-pedantic-errors -std=c99

all: sorting input


sorting: sorting.c
	gcc -o sorting $(FLAGS) sorting.c

input:
	python generate_sequences.py 10
	python generate_sequences.py 1000
	python generate_sequences.py 1000000