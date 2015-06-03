
FLAGS=-pedantic-errors -std=c99

all: sorting


sorting: sorting.h sorting.c numgen.c numgen.h util.h util.c main.c
	gcc -o sorting $(FLAGS) numgen.c sorting.c util.c main.c

input:
	python generate_sequences.py 10
	python generate_sequences.py 1000
	python generate_sequences.py 1000000
