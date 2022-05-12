<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#inspiration">Inspiration</a></li>
        <li><a href="#major-takeaways">Major Takeaways</a></li>
        <li><a href="#alterations-from-original">Alterations from GlowUp</a></li>
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

<ins>In creating my web app, I worked my way from the backend to frontend.</ins>

<details>
<summary>**Creating the database, using PostgreSQL and SQLAlchemy**</summary>
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
<summary>*What did I learn using PostgreSQL and SQLAlchemy?*</summary>
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
***challenges***:
My main challenges working on my database was coming up with the data structure
model in the first place...

  - figuring out the cardinalities of table relationships. 
    - It helped me greatly to think aloud:
      - What tables do I need in the first place?
      - What data (column names) are needed in said tables?
      - What about table relationships? And the type of relationship?
        - "Business users will have *many* clients, but a client can only have *one* 
        business user, a client can have *many* rewards and rewards can have *many* 
        clients. 
        - Understanding "many-to-many" relationships in my data model presented some 
        difficulties, even more so in practical application.
        - Asking for guidance in the right direction from my instructors helped me
        understand middle/association tables and which I would need to choose depending
        on my design decisions. 

  - factoring in normalization, to avoid the two "primary sins" of data modeling, 
    - repeating dependencies and/or representing multiple data of the same category 
    in columns.
  - remembering the significance in details (e.g.,tablename consistency, choices
  in class names)

My biggest blocker and headache was in seeding the database. I couldn't wrap
my head around how, why, and what variables related to one another. Understanding
data flow among my model.py, crud.py, and seed_database.py files were extremely 
challenging. There really wasn't an instant solution to my challenge, instead
it took time, repeated attempts, and knowing when to step away from my computer
before attempting to tackle the problem again. After a week or so, all the pieces
of the puzzle began to fall into place. 

My challenges taught me a valuable lesson in debugging. Particularly learning to
read raised errors and thinking logically to find the error based on the error 
messages given in the terminal, as opposed to randomly adjusting code here and
there without truly using problem solving techniques.

#### References
* [relational database v. non-relational database](https://www.pluralsight.com/blog/software-development/relational-vs-non-relational-databases)
* [why SQLAlchemy?](https://towardsdatascience.com/here-is-the-reason-why-sqlalchemy-is-so-popular-43b489d3fb00#:~:text=SQLAlchemy%20is%20the%20ORM%20of,of%20SQL%20to%20get%20started.)
* [understanding postgres columns and row orientation](https://www.brianlikespostgres.com/poor-mans-column-oriented-database.html)
* [what is structured data?](https://www.ibm.com/cloud/blog/structured-vs-unstructured-data)
</details>

<details>
<summary>CRUD functions</summary>
After completing and testing by hand my model.py, I moved on to the CRUD functions
that would automate the process of populating my database. As my crud.py deals
with database connections, I added if __name__ == '__main__' block (will only
execute code if the file is run directly and not imported) to the base
of crud.py. I wrote CRUD functions for each table, most of which were complex
queries based on particular variables. I used mock data from mockaroo to populate
my database. Now that my database is complete, it was time to move on to the server!

### Alterations from GlowUp
After creating database tables, CRUD functions, and seed_database.py, I realized
that I needed to make certain changes to cater to its specific purpose as opposed
to the generalized nature of my original application. I've listed
the changes below, along with the dates the changes were made.

5/11/2022
- Changed 'clients' to 'customers' to match data that will be imported from Square
- As this web application will purely have one user, I am adjusting (or possibly
removing) the business user table and dummy data)
--> possibility to create 3 accounts? administrator, business owner, and dummy account 
to test and play with (for people who want to see project in practical application)
- Changing 'rewards' to 'facials'
- Square objects 'transactions' do not list type of booking
- Will need to create 'bookings' table, but also keep transaction --> make relationship
--> if booking has matching transaction, THEN a facial point can be added, else no
(unless there is a way I can ensure that points will not be added if booking is cancelled)
----> blocker...can't figure out how to add booking to sandbox account, keep
coming across error stating "employee_attributions" needed.
### Challenges
Particularly knowing how to write the correct queries when it came to navigating
relationships. Reviewing lecture material repeatedly remedied that difficulty.
</details>

<details>
<summary>server.py, Flask, Jinja2, WTForms, and creating secure login</summary>

The server acted as the bridge between the backend and frontend. 
I first created a simple skeleton of app routes, including homepage, login,
and registration. Using the Flask web framework to define which requests to 
respond to, how to respond to said requests, and generally navigating through
the pre-written functions and classes in Flask to carry out the basics
of what a web application needs to do. 



### Challenges
- flask session
- post v get requests
- creating secure login
- password hashing
- understanding how I could retrieve and output information to the frontend
</details>



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

