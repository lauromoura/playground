import os
import sys

from collections import defaultdict

import gexf

def main():
	
	gfile = gexf.Gexf("Lauro Moura", "A hello world! file");

	graph = gfile.addGraph("undirected", "static", "a hello world graph")

	handle = open(sys.argv[1])
	#aliancas key = PA/PB , value = lista de cidades em que sao aliados
	partidos = {}
	partido_id = 0

	relacoes = defaultdict(list)

	for line in handle:
		tokens = line.split(";")

		cidade = tokens[7]
		partido = tokens[12].strip('"')
		coligacao = [x.strip() for x in tokens[16].split("/")]
		coligacao = [x.strip('"') for x in coligacao]

		if partido not in partidos:
			print "adding", partido
			partidos[partido] = str(partido_id)
			partido_id += 1

		for partido2 in coligacao:
			if partido == partido2:
				continue

			if partido2 > partido:
				partido, partido2 = partido2, partido

			dupla = partido, partido2

			if "#NE#" in dupla or '' in dupla:
				"skipping"
				continue

			if (dupla not in relacoes) or (cidade not in relacoes[dupla]):
				relacoes[dupla].append(cidade)
		


	print partidos
	# for relacao in relacoes:
	# 	print relacao, len(relacoes[relacao])

	for partido, codigo in partidos.items():
		graph.addNode(codigo, partido)

	edge_id = 0
	for relacao, cidades in relacoes.items():
		partidoA, partidoB = relacao
		total = len(cidades)

		graph.addEdge(str(edge_id), partidos[partidoA], partidos[partidoB])
		edge_id += 1


	output_file = open("hellowrld.gexf", "w")
	gfile.write(output_file)


if __name__ == '__main__':
	main()