import pandas as pd
from googletrans import Translator

# Load dataset
df = pd.read_csv(
    'Images-Book.csv',
    usecols=[
        'Identifier', 'Edition Statement', 'Place of Publication',
        'Date of Publication', 'Publisher', 'Title',
        'Author', 'Contributors', 'Shelfmarks'
    ],
    keep_default_na=False,
    nrows=200
)

# Clean text
df['Place of Publication'] = df['Place of Publication'].str.lower()
df['Place of Publication'] = df['Place of Publication'].replace(r'[^\w\s]', '', regex=True)

df['Date of Publication'] = df['Date of Publication'].replace(r'[^\w\s]', '', regex=True)

# Load reference dataset
cities = pd.read_csv('world-cities.csv', usecols=['name'])
cities['name'] = cities['name'].str.lower()

# Merge with cities
merged = df.merge(cities, how='left', left_on='Place of Publication', right_on='name')

matched = merged[merged['name'].notnull()].copy()
unmatched = merged[merged['name'].isnull()].copy()

# Translate unmatched rows
translator = Translator()

unmatched['Place of Publication'] = unmatched['Place of Publication'].apply(
    lambda x: translator.translate(x, dest='en').text if x else x
).str.lower()

# Re-match after translation
merged_2 = unmatched.merge(cities, how='left', left_on='Place of Publication', right_on='name')

matched_2 = merged_2[merged_2['name'].notnull()]

# Combine final dataset
final_df = pd.concat([matched, matched_2], ignore_index=True).drop_duplicates()

final_df['Place of Publication'] = final_df['Place of Publication'].str.title()

# Export
final_df.to_excel('cleaned_books.xlsx', sheet_name='Cleansed Data', index=False)
