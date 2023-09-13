import requests

ENDPOINT = ' http://127.0.0.1:8000/random_user'
UPDATE = 'http://127.0.0.1:8000/update'
POST = 'http://127.0.0.1:8000/adduser'
SPECIFIC_USER = 'http://127.0.0.1:8000/user'
def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


# This test fails if the exact payload exists in the database
def test_cal_create_new_user():
    payload={
        "name": "Garo Doom Goblin",
        "email": "DOOGoblinM@email.com",
        "password": "010101010",
        "membership_status": "DOOM",
        "weight_value": "130",
        "weight_unit": "kg",
        "height_value": "184",
        "height_unit": "cm"
    }
    response = requests.post(POST, json=payload)
    assert response.status_code == 201

    data = response.json()
    print(data)


# lets now get a user based off of their id number
def test_can_get_user_by_id():
    response = requests.get(SPECIFIC_USER + '/1'
    assert response.status_code == 200


def get_specific_user(user_id):
    return requests.get(SPECIFIC_USER + f'/{user_id}')

def update_user_info(user_id, new_name):
    return requests.patch(UPDATE + f'/{user_id}', json={"name": new_name})


