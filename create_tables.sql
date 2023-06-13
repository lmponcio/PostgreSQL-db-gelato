CREATE TABLE shop (
    id integer PRIMARY KEY,
    name varchar(20),
    description varchar(100),
    telephone char(10)
);

CREATE TABLE address (
    id integer PRIMARY KEY,
    street_number varchar(10),
    street_name varchar(20),
    city  varchar(20),
    shop_id integer REFERENCES shop(id) UNIQUE -- one-to-one relationship
);

CREATE TABLE dietr (
    id integer PRIMARY KEY,
    name varchar(50),
    description varchar(200)
);

CREATE TABLE icecream (
    id integer PRIMARY KEY,
    name varchar(50),
    description varchar(200)
);

CREATE TABLE review (
    id integer PRIMARY KEY,
    rating decimal,
    date date,
    icecream_id integer REFERENCES icecream(id) -- one-to-many relationship
);

-- many-to-many relationship (cross reference table)
CREATE TABLE icecream_dietr (
 icecream_id integer REFERENCES icecream(id),
 dietr_id integer REFERENCES dietr(id),
 PRIMARY KEY (icecream_id, dietr_id)
);