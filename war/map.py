import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge("Brasil", "Argentina")
G.add_edge("Brasil", "Bolivia")
G.add_edge("Brasil", "Colombia")
G.add_edge("Brasil", "Nigeria")

G.add_edge("Argentina", "Bolivia")

G.add_edge("Bolivia", "Mexico")

G.add_edge("Mexico", "Nova York")
G.add_edge("Mexico", "California")

G.add_edge("Nova York", "Ottawa")
G.add_edge("Nova York", "Labrador")

G.add_edge("California", "Nova York")
G.add_edge("California", "Ottawa")
G.add_edge("California", "Vancouver")

G.add_edge("Vancouver", "Alaska")
G.add_edge("Vancouver", "Mackenzie")
G.add_edge("Vancouver", "Ottawa")

G.add_edge("Alaska", "Vladivostok")
G.add_edge("Alaska", "Mackenzie")

G.add_edge("Mackenzie", "Ottawa")
G.add_edge("Mackenzie", "Groelandia")

G.add_edge("Ottawa", "Labrador")

G.add_edge("Labrador", "Groelandia")

G.add_edge("Groelandia", "Islandia")

G.add_edge("Islandia", "Inglaterra")

G.add_edge("Inglaterra", "Suecia")
G.add_edge("Inglaterra", "Alemanha")
G.add_edge("Inglaterra", "Franca")

G.add_edge("Franca", "Alemanha")
G.add_edge("Franca", "Nigeria")
G.add_edge("Franca", "Polonia")
G.add_edge("Franca", "Egito")

G.add_edge("Suecia", "Moscou")

G.add_edge("Alemanha", "Polonia")

G.add_edge("Polonia", "Moscou")
G.add_edge("Polonia", "Egito")
G.add_edge("Polonia", "Oriente Medio")

G.add_edge("Moscou", "Omsk")
G.add_edge("Moscou", "Aral")
G.add_edge("Moscou", "Oriente Medio")

G.add_edge("Nigeria", "Egito")
G.add_edge("Nigeria", "Sudao")
G.add_edge("Nigeria", "Congo")

G.add_edge("Egito", "Sudao")
G.add_edge("Egito", "Oriente Medio")

G.add_edge("Sudao", "Congo")
G.add_edge("Sudao", "Madagascar")
G.add_edge("Sudao", "Africa do Sul")

G.add_edge("Congo", "Africa do Sul")

G.add_edge("Africa do Sul", "Madagascar")

G.add_edge("Oriente Medio", "India")
G.add_edge("Oriente Medio", "Aral")

G.add_edge("Aral", "India")
G.add_edge("Aral", "China")
G.add_edge("Aral", "Omsk")

G.add_edge("Omsk", "Dudinka")
G.add_edge("Omsk", "Mongolia")
G.add_edge("Omsk", "China")

G.add_edge("Dudinka", "Siberia")
G.add_edge("Dudinka", "Tchita")
G.add_edge("Dudinka", "Mongolia")

G.add_edge("India", "Sumatra")
G.add_edge("India", "Vietna")
G.add_edge("India", "China")

G.add_edge("China", "Vietna")
G.add_edge("China", "Japao")
G.add_edge("China", "Vladivostok")
G.add_edge("China", "Tchita")
G.add_edge("China", "Mongolia")

G.add_edge("Mongolia", "Tchita")

G.add_edge("Tchita", "Siberia")
G.add_edge("Tchita", "Vladivostok")

G.add_edge("Siberia", "Vladivostok")

G.add_edge("Vladivostok", "Japao")

G.add_edge("Vietna", "Borneo")

G.add_edge("Sumatra", "Australia")

G.add_edge("Borneo", "Nova Guine")
G.add_edge("Borneo", "Australia")

G.add_edge("Australia", "Nova Guine")




nx.draw(G)

plt.savefig("blah.png")
plt.show()

