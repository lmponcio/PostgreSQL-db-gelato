""" Script for writing the SQL statements to fill the tables "icecream" and "icecream_dietr"
"""
import openpyxl
from dataclasses import dataclass

wb = openpyxl.load_workbook("web_scraped.xlsx")
ws = wb.active


@dataclass
class Flavour:
    id: int
    name: str
    description: str
    is_vegan: bool
    is_alcohol_free: bool
    is_egg_free: bool
    is_gluten_free: bool
    is_nut_free: bool

    def get_insert_query_icecream(self):
        return f"""INSERT INTO icecream VALUES (
        {self.id},
        '{self.name}',
        '{self.description}'
        );"""

    def get_insert_query_icecream_dietr(self):
        print(f"testing dietrs from {self.name}")
        print(self.get_dietr_id_list())
        print(self.is_alcohol_free)
        all_queries = ""
        try:
            for dietr_id in self.get_dietr_id_list():
                this_query = f"""INSERT INTO icecream_dietr VALUES (
                '{self.id}',
                '{dietr_id}'
                );"""
                all_queries += "\n" + this_query
        except:
            pass
        return all_queries

    def get_dietr_id_list(self):
        dietrs_list = []
        if self.is_vegan:
            dietrs_list.append(1)
        if self.is_alcohol_free:
            dietrs_list.append(2)
        if self.is_egg_free:
            dietrs_list.append(3)
        if self.is_gluten_free:
            dietrs_list.append(4)
        if self.is_nut_free:
            dietrs_list.append(5)
        return dietrs_list


columns_mapping = {
    "name": 0,
    "description": 1,
    "is_vegan": 2,
    "is_alcohol_free": 3,
    "is_egg_free": 4,
    "is_gluten_free": 5,
    "is_nut_free": 6,
}


def get_diet_bool(cell_content):
    if cell_content == "X":
        return True
    else:
        return False


flavours = []
id = 1
for row in ws.iter_rows(min_row=2, max_col=7):
    name = row[columns_mapping["name"]].value
    description = row[columns_mapping["description"]].value
    is_vegan = get_diet_bool(row[columns_mapping["is_vegan"]].value)
    is_alcohol_free = get_diet_bool(row[columns_mapping["is_alcohol_free"]].value)
    is_egg_free = get_diet_bool(row[columns_mapping["is_egg_free"]].value)
    is_gluten_free = get_diet_bool(row[columns_mapping["is_gluten_free"]].value)
    is_nut_free = get_diet_bool(row[columns_mapping["is_nut_free"]].value)
    this_flavour = Flavour(
        id,
        name,
        description,
        is_vegan,
        is_alcohol_free,
        is_egg_free,
        is_gluten_free,
        is_nut_free,
    )
    flavours.append(this_flavour)
    id += 1


with open("insert_icecreams.sql", "w") as file:
    for flavour in flavours:
        file.write(flavour.get_insert_query_icecream() + "\n")


with open("insert_icecream_dietrs.sql", "w") as file:
    for flavour in flavours:
        file.write(flavour.get_insert_query_icecream_dietr() + "\n")
