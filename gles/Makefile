# Straight forward Makefile to compile all examples in a row

INCDIR=
LIBS=-lGLESv2 -lEGL -lm -lX11 -lxcb


default: all

all: ./play

clean:
	rm play

./play: main.cpp
	g++ main.cpp -o $@ ${INCDIR} ${LIBS}
