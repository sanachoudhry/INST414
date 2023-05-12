import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
df = pd.read_csv("best-selling video games of all time.csv")

# Clean the data and preprocess the features for similarity calculation
# (e.g., handle missing values, convert data types, etc.)

# Concatenate the relevant columns into a single text column for similarity calculation
text_data = df['Title'] + ' ' + df['Series'] + ' ' + df['Platform(s)'] + ' ' + df['Developer(s)'] + ' ' + df['Publisher(s)']

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the text data
tfidf_matrix = vectorizer.fit_transform(text_data)

# Define the queries
queries = ['popular action games',
           'best-selling games for Xbox',
           'top games by Electronic Arts']

# Transform the query data using the TF-IDF vectorizer
query_vectors = vectorizer.transform(queries)

# Calculate the cosine similarity between queries and the dataset
cosine_similarities = cosine_similarity(query_vectors, tfidf_matrix)

# Get the top 10 most similar entities for each query
num_similar_entities = 10
similar_entities = []
for i, query in enumerate(queries):
    similarities = cosine_similarities[i]
    top_similar_indices = similarities.argsort()[:-num_similar_entities-1:-1]
    top_similar_games = df.iloc[top_similar_indices]['Title'].tolist()
    similar_entities.append(top_similar_games)

# Print the results
for i, query in enumerate(queries):
    print(f"Query: {query}")
    print("Similar Games based on Cosine Similarity:")
    for j, game in enumerate(similar_entities[i]):
        print(f"{j+1}. {game}")
    print()