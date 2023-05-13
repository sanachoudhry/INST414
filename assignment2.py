import requests
import networkx as nx
import matplotlib.pyplot as plt

endpoint = 'https://restcountries.com/v2/all'

response = requests.get(endpoint)
data = response.json()

countries = []
for country in data:
    name = country.get('name', 'N/A')
    population = country.get('population', 'N/A')
    capital = country.get('capital', 'N/A')
    currencies = country.get('currencies', [])
    languages = country.get('languages', [])

    countries.append({
        'name': name,
        'population': population,
        'capital': capital,
        'currencies': currencies,
        'languages': languages
    })

G = nx.Graph()

for country in countries:
    G.add_node(country['name'], population=country['population'], capital=country['capital'])

for i in range(len(countries)):
    for j in range(i+1, len(countries)):
        if any(currency in countries[j]['currencies'] for currency in countries[i]['currencies']):
            G.add_edge(countries[i]['name'], countries[j]['name'])
        elif any(language in countries[j]['languages'] for language in countries[i]['languages']):
            G.add_edge(countries[i]['name'], countries[j]['name'])

degree_centrality = nx.degree_centrality(G)

top_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:3]

pos = nx.circular_layout(G)

plt.figure(figsize=(12, 12))

nx.draw_networkx(G, pos, node_size=300, font_size=10)

important_nodes = {node: node for node in top_nodes}
nx.draw_networkx_labels(G, pos, labels=important_nodes, font_size=12, font_weight='bold')

plt.axis('off')

plt.title('Web-based Network: Country Connections', fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()





