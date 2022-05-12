"""Models for GlamUp web app"""

from datetime import datetime 
# importing SQLAlchemy constructor function
from flask_sqlalchemy import SQLAlchemy

# instantiation, create SQLAlchemy instance at the variable db
db = SQLAlchemy()

#################################################
#################################################
###############  business_users  ################
###############    table       ##################
#################################################
#################################################

class BusinessUser(db.Model):
    """Business user."""

    __tablename__ = 'business_users'

    # table fields
    bUser_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    bUser_email = db.Column(db.String(120), nullable=False, unique=True)
    bUser_username = db.Column(db.String(30), nullable=False, unique=True)
    bUser_password = db.Column(db.String, nullable=False)
    bUser_name = db.Column(db.String, nullable=False)
    bUser_business = db.Column(db.String, nullable=False, unique=True)
    bUser_avatar = db.Column(db.String)

    # TEMPORARY TEST CASE(create test file after creating CRUD functions)
    # test_bUser = BusinessUser(bUser_email='bUser@email.com', bUser_username='test_user', bUser_password='password1', bUser_name='Test Name', bUser_business='Test Business')
    # db.session.add(test_bUser)
    # db.session.commit()
    # bUser = BusinessUser.query.first()
    # bUser

    def __repr__(self):
        return f"""<bUser_id={self.bUser_id} bUser_email={self.bUser_email}
        bUser_username={self.bUser_username} bUser_business={self.bUser_business}>"""
    
    # BACK_POPULATES
    # customer = db.relationship('Customer', back_populates='business_user')
    # It appears that foreign key IDs are not assigned because that is done w/seed.py
    # BACKREF
    customer = db.relationship('Customer', backref='business_users')
    customer_reward = db.relationship('CustomerReward', backref='business_users')
    reward = db.relationship('Reward', backref='business_user')


#################################################
#################################################
###############  customers         ################
###############    table       ##################
#################################################
#################################################
# might need to change customers to customers
class Customer(db.Model):
    """A customer."""

    __tablename__ = 'customers'

    customer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    customer_name = db.Column(db.Text, nullable=False)
    customer_email = db.Column(db.String(254), nullable=False, unique=True)
    reward_point = db.Column(db.Integer, nullable=True)
    bUser_id = db.Column(db.Integer, db.ForeignKey('business_users.bUser_id'))

    # TEMPORARY TEST CASE(create test file after creating CRUD functions)
    # test_customer = Customer(customer_name='Customer Name', customer_email='customer@email.com', reward_point=0)
    # db.session.add(test_customer)
    # db.session.commit()
    # customer = Customer.query.first()
    # customer
    def __repr__(self):
        return f"""<Customer customer_id={self.customer_id}, customer_name={self.customer_name},
        customer_email={self.customer_email}, reward_point={self.reward_point}, 
        id={self.bUser_id}>"""

    # BACK_POPULATES
    # business_user = db.relationship('BusinessUser', back_populates='customer')
    # BACKREF
    # business_user = list of BusinessUser objects (backref)
    customer_reward = db.relationship('CustomerReward', backref='customers')
    transaction = db.relationship('Transaction', backref='customers')


#################################################
#################################################
###############  transactions.   ################
###############    table       ##################
#################################################
#################################################

class Transaction(db.Model):
    """A customer transaction."""
    __tablename__='transactions'

    trans_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    trans_appt = db.Column(db.Text, nullable=False)
    trans_date = db.Column(db.Date, nullable=False)
    trans_cost = db.Column(db.Text, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))

    # TEMPORARY TEST CASE(create test file after creating CRUD functions)
    # test_trans = Transaction(trans_appt='facial', trans_date=datetime.now(), trans_cost=100.00)
    # db.session.add(test_trans)
    # db.session.commit()
    # trans = Transaction.query.first()
    # trans

    def __repr__(self):
        return f"""<Transaction trans_id={self.trans_id,} trans_appt={self.trans_appt},
        trans_date={self.trans_date}, customer_id={self.customer_id}>"""

    # customer = list of Customer objects (backref)


#################################################
#################################################
###############  customer_rewards  ################
###############    table       ##################
#################################################
#################################################

class CustomerReward(db.Model):
    """A customer-reward association table (to establish many-to-many relationship)."""

    __tablename__ = 'customer_rewards'
    cReward_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'))
    reward_id = db.Column(db.Integer, db.ForeignKey('rewards.reward_id'))
    bUser_id = db.Column(db.Integer, db.ForeignKey('business_users.bUser_id'))

    def __repr__(self):
        # return f"""<CustomerReward cReward_id={self.cReward_id}
        return f"""<CustomerReward Reward_id={self.Reward_id}, 
        customer_id={self.customer_id}, reward_id={self.reward_id}>"""
    
    # BACKREF
    reward = db.relationship('Reward', backref='customer_rewards')
    # customer = list of Customer objects
    # business_user = list of BusinessUser objects

#################################################
#################################################
###############    rewards       ################
###############    table       ##################
#################################################
#################################################

class Reward(db.Model):

    __tablename__ = 'rewards'

    reward_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    reward_type = db.Column(db.Text, nullable=False)
    reward_cost = db.Column(db.Integer, nullable=False)
    bUser_id = db.Column(db.Integer, db.ForeignKey('business_users.bUser_id'))

    # TEMPORARY TEST CASE(create test file after creating CRUD functions)
    # test_reward = Reward(reward_type='free facial', reward_cost=10)
    # db.session.add(test_reward)
    # db.session.commit()
    # reward = Reward.query.first()
    # reward

    def __repr__(self):
        return f"""<Reward reward_id={self.reward_id},
        reward_type={self.reward_type}>"""
    
    # BACKREF relationships
    # customer_reward = list of CustomerReward objects
    # business_user = list of BusinessUser objects

def connect_to_db(flask_app, db_uri="postgresql:///rewardsprogram", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
