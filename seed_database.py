"""Script to seed database."""

import os 
import json
from random import choice, randint
from datetime import datetime 

import crud 
import model 
import server 

os.system("dropdb rewardsprogram")
os.system("createdb rewardsprogram")

model.connect_to_db(server.app)
model.db.create_all()

#################################################
###############    business      ################
#################################################

with open('data/bUser_dummydata.json') as b:
    business_data = json.loads(b.read())

business_in_db = []

for business in business_data:
    bUser_email, bUser_username, bUser_password_original, bUser_name, bUser_business, bUser_avatar = (
       business['bUser_email'],
       business['bUser_username'],
       business['bUser_password_original'], 
       business['bUser_name'],
       business['bUser_business'],
       business['bUser_avatar']
    )

    db_business = crud.create_bUser(bUser_email, 
                                    bUser_username, 
                                    bUser_password_original, 
                                    bUser_name, 
                                    bUser_business, 
                                    bUser_avatar)
    
    business_in_db.append(db_business)


#################################################
###############     clients      ################
#################################################

with open('data/client_dummydata.json') as c:
    client_data = json.loads(c.read())

client_in_db = []

for client in client_data:
    client_name, client_email, business, reward_point = (
        client['client_name'],
        client['client_email'],
        choice(business_in_db),
        client['reward_point']
    )

    db_client = crud.create_client(client_name, 
                                client_email, 
                                business, 
                                reward_point)
    
    client_in_db.append(db_client)

#################################################
###############   transactions   ################
#################################################

with open('data/transaction_dummydata.json') as t:
    transaction_data = json.loads(t.read())

    transaction_in_db = []

    for transaction in transaction_data:
        trans_appt, trans_date, trans_cost, client = (
            transaction['trans_appt'],
            transaction['trans_date'],
            transaction['trans_cost'],
            choice(client_in_db)
        )

    db_transaction = crud.create_trans(trans_appt, 
                                        trans_date, 
                                        trans_cost, 
                                        client)

    transaction_in_db.append(db_transaction)

#################################################
###############     rewards       ###############
#################################################

with open('data/rewards_dummydata.json') as r:
    reward_data = json.loads(r.read())

reward_in_db = []

for reward in reward_data:
    reward_type, reward_cost, business = (
        reward['reward_type'],
        reward['reward_cost'],
        choice(business_in_db)
    )

    db_reward = crud.create_reward(reward_type, reward_cost, business)

    reward_in_db.append(db_reward)

for client in client_in_db:
    crud.create_client_reward(client.client_id, randint(1, 30))