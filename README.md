# PostgreSQL Gelato Database

In this project, I design a database of ice cream shops that sell products appropriate for people with dietary requirements.

I decided to create this project to practice PostgreSQL, Database design, Web scraping, and Data Wrangling.

I chose dietary requirement icecream  because people close to me have dietary requirements, so I find the topic interesting (I was also inspired by the [Two Scoops Django book](https://www.feldroy.com/books/two-scoops-of-django-3-x)), and because the dietary requirements allow me to have all three types of relationships in one small project: 
- **many-to-many** for the ice creams that comply with different dietary requirements, 
- **one-to-many** for the reviews done to each icecream flavour, and 
- **one-to-one** for the address of each icecream shop.

I use as a guide [flavours listed in Messina's website](./media/inspiration.jpg), though the information I will fill the database with will be fictitious.

### Preliminary work - DB design 
I used [draw.io](http://draw.io/) to design the schema

<img src="./media/diagram.jpg" width="700" />

### Tables creation
I used postbird client. Below a screenshot of the [queries for creating the tables](./create_tables.sql).

<img src="./media/tables_creation.jpg" width="700" />

### Bibliography
- Learned PostgreSQL at [Design Databases with PostgreSQL by Codecademy](https://www.codecademy.com/learn/paths/design-databases-with-postgresql)
- Diagram notation from https://vertabelo.com/blog/crow-s-foot-notation-in-vertabelo/
- Diagrams drawn with http://draw.io/
- Icecream flavours from https://gelatomessina.com/collections/classic-flavours
