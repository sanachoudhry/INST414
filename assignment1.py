import requests
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://www.fruityvice.com/api/fruit/all'

response = requests.get(url)

data = response.json()

fruit_data = []

for fruit_info in data:
    fruit = fruit_info['name']
    nutrients = fruit_info['nutritions']
    fruit_info = {
        'Name': fruit,
        'Sugar': nutrients['sugar'],
        'Calories': nutrients['calories'],
        'Fat': nutrients['fat'],
        'Carbohydrates': nutrients['carbohydrates'],
        'Protein': nutrients['protein']
    }
    fruit_data.append(fruit_info)

df = pd.DataFrame(fruit_data)

df['Sugar-to-Nutrition Ratio'] = df['Sugar'] / (df['Calories'] + df['Protein'] + df['Fat'] + df['Carbohydrates'] + df['Protein'])

df = df.sort_values(by='Sugar-to-Nutrition Ratio', ascending=False)

top_fruits = df.head(10)

print(top_fruits)

plt.figure(figsize=(10, 6))
plt.bar(top_fruits['Name'], top_fruits['Sugar-to-Nutrition Ratio'])
plt.xlabel('Fruit')
plt.ylabel('Sugar-to-Nutrition Ratio')
plt.title('Sugar-to-Nutrition Ratio for Select Fruits')
plt.xticks(rotation=45)
plt.show()