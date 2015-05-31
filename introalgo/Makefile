
FLAGS=-pedantic-errors -std=c99

all: sorting


sorting: sorting.c numgen.c numgen.h
	gcc -o sorting $(FLAGS) numgen.c sorting.c

input:
	python generate_sequences.py 10
	python generate_sequences.py 1000
	python generate_sequences.py 1000000
