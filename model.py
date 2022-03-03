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
    # client = db.relationship('Client', back_populates='business_user')
    # It appears that foreign key IDs are not assigned because that is done w/seed.py
    # BACKREF
    client = db.relationship('Client', backref='business_users')
    client_reward = db.relationship('ClientReward', backref='business_users')
    # reward = db.relationship('Reward', backref='business_user')


#################################################
#################################################
###############  clients         ################
###############    table       ##################
#################################################
#################################################

class Client(db.Model):
    """A client."""

    __tablename__ = 'clients'

    client_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    client_name = db.Column(db.Text, nullable=False)
    client_email = db.Column(db.String(254), nullable=False, unique=True)
    reward_point = db.Column(db.Integer, nullable=True)
    bUser_id = db.Column(db.Integer, db.ForeignKey('business_users.bUser_id'))

    # TEMPORARY TEST CASE(create test file after creating CRUD functions)
    # test_client = Client(client_name='Client Name', client_email='client@email.com', reward_point=0)
    # db.session.add(test_client)
    # db.session.commit()
    # client = Client.query.first()
    # client
    def __repr__(self):
        return f"""<Client client_id={self.client_id}, client_name={self.client_name},
        client_email={self.client_email}, reward_point={self.reward_point}, 
        id={self.bUser_id}>"""

    # BACK_POPULATES
    # business_user = db.relationship('BusinessUser', back_populates='client')
    # BACKREF
    # business_user = list of BusinessUser objects (backref)
    client_reward = db.relationship('ClientReward', backref='clients')
    transaction = db.relationship('Transaction', backref='clients')


#################################################
#################################################
###############  transactions.   ################
###############    table       ##################
#################################################
#################################################

class Transaction(db.Model):
    """A client transaction."""
    __tablename__='transactions'

    trans_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    trans_appt = db.Column(db.Text, nullable=False)
    trans_date = db.Column(db.Date, nullable=False)
    trans_cost = db.Column(db.Float, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'))

    # TEMPORARY TEST CASE(create test file after creating CRUD functions)
    # test_trans = Transaction(trans_appt='facial', trans_date=datetime.now(), trans_cost=100.00)
    # db.session.add(test_trans)
    # db.session.commit()
    # trans = Transaction.query.first()
    # trans

    def __repr__(self):
        return f"""<Transaction trans_id={self.trans_id,} trans_appt={self.trans_appt},
        trans_date={self.trans_date}, client_id={self.client_id}>"""

    # client = list of Client objects (backref)


#################################################
#################################################
###############  client_rewards  ################
###############    table       ##################
#################################################
#################################################

class ClientReward(db.Model):
    """A client-reward association table (to establish many-to-many relationship)."""

    __tablename__ = 'client_rewards'
    cReward_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'))
    reward_id = db.Column(db.Integer, db.ForeignKey('rewards.reward_id'))
    bUser_id = db.Column(db.Integer, db.ForeignKey('business_users.bUser_id'))

    def __repr__(self):
        return f"""<ClientReward cReward_id={self.cReward_id}, 
        client_id={self.client_id}, reward_id={self.reward_id}>"""
    
    # BACKREF
    reward = db.relationship('Reward', backref='client_rewards')
    # client = list of Client objects
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
    # client_reward = list of ClientReward objects
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
