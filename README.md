<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#inspiration">Inspiration</a></li>
        <li><a href="#major-takeaways">Major Takeaways</a></li>
        <li><a href="#challenges">Challenges</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

What you see before you is not just my coding bootcamp capstone project, but the
very first of many I intend to build in time as I develop my career in tech.
Please keep in mind that this project was never merely a graduation requirement
to me—rather, it was proof to myself that I am fully capable of achieving more
than I could have ever expected of myself. I am currently redeveloping my
original project, to include features from my 3.0 that I didn’t have the time to
include as well as those that I had come up with long after I graduated from
Hackbright Academy. 

Seoulful Glam is a points-based rewards system in which business owners can
keep track of client transactions, so as to tally redeemable points for
promotional rewards. 

### Inspiration

The name of my project is actually the name of my sister's business. My sister,
an aesthetician and small business owner, told me about a rewards program she
created to promote further business. For every 10 facials (a very popular 
service in her business) booked, a client is eligible for a freebie. She kept
tally of her clients' appointments in a little notebook. I told her, "Toss the notebook!
I'll create a web application so that you can store this information safely and 
increase the efficiency by automating such a manual task." 

### Major Takeaways
##### i.e, What did I learn?
Seoulful Glam (or GlowUp, as my initial project was originally named), reinforced
all that I had learned throughout my coding bootcamp. The Hackbright Academy
curriculum taught me how to use the technologies needed to create a fullstack web app.

In creating my web app, I worked my way from the backend to frontend.

<details>
<summary>Creating the database, using PostgreSQL and SQLAlchemy</summary>
I began my first establishing a relational database (RDBMS)^ using PostgreSQL. 
Using SQLAlchemy, as opposed to raw SQL, I used classes to create tables in
the database, each of which held columns of data I wanted to include in said tables.
Each column included specifications, such as default, primary key, and autoincrement.
Relationships among the proper tables were establishing using backref. In my prior
'edition' of my project (aka GlowUp), I used db.relationship in both tables
as opposed to backref. At the time I didn't understand the difference between the two
besides the fact that db.relationship took more time to implement the relationships.
I now understand that db.relationship is used if the relationship goes one way
and backref is used if the relationship goes both ways. This time around I used 
backref, including comments between tables with relationships to remember which table
related to which.

<details>
<summary>What did I learn using PostgreSQL and SQLAlchemy?</summary>
A relational database links information from multiple tables by using primary
and foreign keys, which uniquely identifies a row of data. The connection of primary
and foreign keys are what creates the 'relationships' between records contained
throughout existing tables. Relational databases are ideal for working with structured
data, highly organized quantitative data easily used to input, search, and manipulate. 
Because of the relationship constraints created by the referential integrity of 
relational databases, it means that data will be accurate and consistent. 
While RDBMS isn't as easily scalable and flexible as non-relational databases,
that really isn't an issue for the purpose of my project. From what I have been
able to glean and understand, non-relational databases would be preferable
for document data. 
</details>
</details>

After completing and testing by hand my model.py, I moved on to the CRUD functions
that would automate the process of populating my database. As my crud.py deals
with database connections, I added if __name__ == '__main__' block (will only
execute code if the file is run directly and not imported) to the base
of crud.py. I wrote CRUD functions for each table, most of which were complex
queries based on particular variables. I used mock data from mockaroo to populate
my database. Now that my database is complete, it was time to move on to the server!

The server


### Challenges
seeding database
### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [JavaScript](https://www.javascript.com/)
* [jQuery](https://jquery.com/)
* [WTForms](https://wtforms.readthedocs.io/en/3.0.x/)
* [Bootstrap](https://getbootstrap.com/)
#### Other Code & Libraries
* HTML/CSS
* AJAX
* bCrypt


<p align="right">(<a href="#top">back to top</a>)</p>

