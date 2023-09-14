import requests
import json

SHOW_ALL = 'http://127.0.0.1:8000/all'
GET_RANDOM_USER = ' http://127.0.0.1:8000/random_user'
UPDATE_USERS_NAME = 'http://127.0.0.1:8000/update'
CREATE_USER = 'http://127.0.0.1:8000/adduser'
GET_SPECIFIC_USER = 'http://127.0.0.1:8000/user'
DELETE_SPECIFIC_USER = 'http://127.0.0.1:8000/delete'

# just checking if endpoint working, useless test we can just check in http-client
def test_can_call_endpoint():
    response = requests.get(GET_RANDOM_USER)
    assert response.status_code == 200

# test if we can get all users
def test_can_get_all_users():
    response = requests.get(SHOW_ALL)
    assert response.status_code == 200

# This test fails if the exact payload exists in the database
# def test_cal_create_new_user():
#     payload={
#         "name": "Garo Doom Goblin",
#         "email": "DOOGoblinM@email.com",
#         "password": "010101010",
#         "membership_status": "DOOM",
#         "weight_value": "130",
#         "weight_unit": "kg",
#         "height_value": "184",
#         "height_unit": "cm"
#     }
#     pass


