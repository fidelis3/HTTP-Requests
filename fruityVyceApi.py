#In this notebook, we will be using the Fruityvice API. Fruityvice is a free API that provides information about fruits, including their nutritional content, family, genus, and more. The API allows you to retrieve data about specific fruits or get a list of all available fruits. You can also filter the results based on various criteria such as sugar content, calories, and more. The Fruityvice API is a great resource for anyone interested in learning more about fruits and their nutritional value. More information on the Fruityvice API can be found here.

import requests
import json
import pandas as pd
data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)#retrieving data using json.loads() method to convert the JSON string into a Python object (in this case, a list of dictionaries).
print(results)
df = pd.DataFrame(results)#converting the python object(dictionary of fruits to a dataframe)
print(df)

df2 = pd.json_normalize(results)#The pd.json_normalize() function is used to flatten nested JSON data into a flat table (DataFrame). In this case, it takes the list of dictionaries (results) and creates a DataFrame where each dictionary's keys become column names and their corresponding values become the row values. This is particularly useful when dealing with nested JSON structures, as it allows you to easily work with the data in a tabular format.eg in this case it splits the nested nutrition column into separate columns for each nutrient (carbohydrates, protein, fat, calories, sugar) and their corresponding values.
print(df2)