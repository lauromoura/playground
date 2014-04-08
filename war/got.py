import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge("Castle Black", "Winterfell")
G.add_edge("Castle Black", "Karhold")
G.add_edge("Castle Black", "The Shivering Sea")
G.add_edge("Castle Black", "Bay of Ice")

G.add_edge("Winterfell", "Karhold")
G.add_edge("Winterfell", "The Shivering Sea")
G.add_edge("Winterfell", "Bay of Ice")
G.add_edge("Winterfell", "White Harbor")
G.add_edge("Winterfell", "Moat Cailin")
G.add_edge("Winterfell", "The Stony Shore")

G.add_edge("Karhold", "The Shivering Sea")

G.add_edge("The Stony Shore", "Bay of Ice")

G.add_edge("White Harbor", "Widow's Watch")
G.add_edge("White Harbor", "The Shivering Sea")
G.add_edge("White Harbor", "The Narrow Sea")
G.add_edge("White Harbor", "Moat Cailin")

G.add_edge("Widow's Watch", "The Shivering Sea")
G.add_edge("Widow's Watch", "The Narrow Sea")

G.add_edge("Bay of Ice", "Sunset Sea")
G.add_edge("Bay of Ice", "Flint's Finger")
G.add_edge("Bay of Ice", "Greywater Watch")

G.add_edge("The Narrow Sea", "Shipbreaker Bay")

G.add_edge("Shipbreaker Bay", "Blackwater Bay")
G.add_edge("Shipbreaker Bay", "East Summer Sea")

G.add_edge("East Summer Sea", "Sea of Dorne")
G.add_edge("East Summer Sea", "West Summer Sea")

G.add_edge("West Summer Sea", "Redwyne Straights")
G.add_edge("West Summer Sea", "Sunset Sea")

G.add_edge("Sunset Sea", "The Golden Sound")
G.add_edge("Sunset Sea", "Flint's Finger")
G.add_edge("Sunset Sea", "Ironman's Bay")
G.add_edge("Sunset Sea", "The Golden Sound")





nx.draw(G)

plt.savefig("blah.png")
plt.show()

