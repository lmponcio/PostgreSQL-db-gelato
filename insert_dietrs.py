dietary_requirements = {
    "vegan": "no animal products or byproducts",
    "alcohol_free": "without any alcohol content or presence",
    "egg_free": "not containing eggs or egg-based ingredients",
    "gluten_free": "not containing gluten",
    "nut_free": "not containing nuts or nut-based ingredients",
}

queries = []
id = 1
for dietr in dietary_requirements.keys():
    this_query = f"""INSERT INTO dietr VALUES (
    {id},
    '{dietr}',
    '{dietary_requirements[dietr]}'
    );"""
    id += 1
    queries.append(this_query)

with open("insert_dietrs.sql", "w") as file:
    for query in queries:
        file.write(query + "\n")
