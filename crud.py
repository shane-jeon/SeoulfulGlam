"""CRUD ('CREATE, READ, UPDATE, DELETE') operations."""

# make variables from files within nested directories available

# CRUD.py acts as a bridge from db tables to python server

# import from model.py module
from model import db, BusinessUser, Customer, Transaction, CustomerReward, Reward, connect_to_db
import bcrypt


#################################################
###########    BUSINESS_USERS     ###############
#################################################

################  def create_bUser #######################
def create_bUser(bUser_email, bUser_username, bUser_password_original, 
                bUser_name, bUser_business, 
                bUser_avatar='/static/img/pusheen.jpg'):

    """Create, add, & return new Business User."""
    bUser_password_hash = bcrypt.hashpw(bUser_password_original.encode('utf-8'), bcrypt.gensalt())
    bUser_password = bUser_password_hash.decode('utf-8')
    bUser = BusinessUser(bUser_email=bUser_email,
                        bUser_username=bUser_username,
                        bUser_password=bUser_password,
                        bUser_name=bUser_name,
                        bUser_business=bUser_business,
                        bUser_avatar=bUser_avatar)

    db.session.add(bUser)
    db.session.commit()

    return bUser


################  def show_all_bUser() ######################
def show_all_bUser():
    """Query all Business Users."""

    return BusinessUser.query.all()


################  def get_bUser_by_id(bUser_id) ######################
def get_bUser_by_id(bUser_id):
    """Queries Business User by bUser_id."""

    bUser = BusinessUser.query.get(bUser_id)

    return bUser

################  def get_bUser_by_username(bUser_username) ################
def get_bUser_by_username(bUser_username):
    """Gets BusinessUser by username."""
    
    bUser = BusinessUser.query.filter_by(bu_username=bUser_username).first()

    return bUser

################  def get_bUser_by_email(bUser_email) ################
def get_bUser_by_email(bUser_email):
    """Gets Business User by email."""

    bUser = BusinessUser.query.filter_by(bUser_email=bUser_email).first()

    return bUser

################  def update_bUser() #######################
def update_bUser(bUser_id):
    """Update Business User profile."""

    bUser = BusinessUser.query.get(bUser_id)
    new_bUser_name = request.form['bUser_name']
    bUser.bUser_name = new_bUser_name 

    db.session.commit()

    return bUser


#################################################
###############    CUSTOMERS     ##################
#################################################

#######################  def create_customer(...) #########################
def create_customer(customer_name,
                customer_email,
                business,
                reward_point=0):
    """Creates new customer for Business User."""

    customer = Customer(customer_name=customer_name,
                    customer_email=customer_email,
                    bUser_id=business.bUser_id,
                    reward_point=reward_point
                    )
    
    db.session.add(customer)
    db.session.commit()

    return customer

#######################  def show_all_customer() ########################
def show_all_customer():
    """Query all Customerss."""

    return Customer.query.all()

####################  def get_customer_by_id(customer_id) ######################
def get_customer_by_id(customer_id):
    """Query for customer by customer_id."""
    
    customer = Customer.query.get(customer_id)

    return customer 

###################  def get_customer_by_email(customer_email) #######################
def get_customer_by_email(customer_email):
    """Queries for and gets customer using customer_email."""

    customer = Customer.query.filter_by(customer_email=customer_email).first()

    return customer 

#############  def adjust_customer_points(customer_id, reward_point) ###############
def adjust_customer_points(customer_id, reward_point):
    """Increment or decrement customer reward point."""

    customer = Customer.query.get(customer_id)

    customer.reward_point += reward_point 

    db.session.commit()

    return customer.reward_point

#################################################
##############   TRANSACTIONS     ################
#################################################

####################  def create_transaction(...) ##################
def create_trans(trans_appt, trans_date, trans_cost, customer):
    """Create a customer transaction."""

    transaction = Transaction(trans_appt=trans_appt,
                        trans_date=trans_date,
                        trans_cost=trans_cost,
                        customer_id=customer.customer_id)

    db.session.add(transaction)
    db.session.commit()

    return transaction

###################  def SHOW_ALL_TRANSACTION #######################
def show_all_transaction():
    """Show all customer transactions."""

    return Transaction.query.all()

###################  def get_transaction_by_id(trans_id) ##################
def get_transaction_by_id(trans_id):
    """Display Transaction by transaction_id."""
    
    transaction = Transaction.query.get(trans_id)

    return transaction

#################################################
###########    REWARDS/POINTS     ###############
#################################################

###################  def create_customer_reward ######################
def create_customer_reward(customer_id, reward_id):
    """Create customer reward."""

    customer_reward = CustomerReward(customer_id=customer_id, reward_id=reward_id)

    db.session.add(customer_reward)
    db.session.commit()

    return customer_reward

##################  def get_customer_reward(customer_id)  ######################
def get_customer_reward(customer_id):
    """Query for customer reward account."""
    customer_point = CustomerReward.query.filter_by(customer_id=customer_id).first()

    return customer_point

##########  def create_reward(reward_type, rewarrd_cost, business) #########
def create_reward(reward_type, reward_cost, bUser_id):
    """Create new Reward."""

    reward = Reward(reward_type=reward_type,
                    reward_cost=reward_cost,
                    bUser_id=bUser_id.bUser_id)

    db.session.add(reward)
    db.session.commit()

    return reward

######################  def delete_reward(reward_id) #####################
def delete_reward(reward_id):
    """Delete a Reward."""

    reward = Reward.query.get(reward_id)

    db.session.delete(reward)
    db.session.commit()

#######################  def show_all_reward() #######################
def show_all_reward():
    """Query all rewards."""

    return Reward.query.all()

###################  def get_reward_by_id(reward_id) ####################
def get_reward_by_id(reward_id):
    """Get reward by reward_id."""

    reward = Reward.query.get(reward_id)

    return reward

if __name__ == '__main__':
    from model import connect_to_db
    from server import app
    connect_to_db(app)