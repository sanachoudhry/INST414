import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('best-selling video games of all time.csv')

titles = df['Title'].tolist()

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(titles)

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_similar_games(query, top_n=10):
    index = titles.index(query)
    
    sim_scores = list(enumerate(cosine_sim[index]))
    
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    top_similar_games = sim_scores[1:top_n+1]
    
    return top_similar_games


query1 = "Grand Theft Auto V"
query2 = "Minecraft"
query3 = "FIFA 18"


similar_games1 = get_similar_games(query1)
similar_games2 = get_similar_games(query2)
similar_games3 = get_similar_games(query3)

print(f"Top 10 games similar to '{query1}':")
for game in similar_games1:
    print(f"- {titles[game[0]]}")

print(f"\nTop 10 games similar to '{query2}':")
for game in similar_games2:
    print(f"- {titles[game[0]]}")

print(f"\nTop 10 games similar to '{query3}':")
for game in similar_games3:
    print(f"- {titles[game[0]]}")