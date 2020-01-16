import requests
import json
import time

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def console_print(text):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    # print(text)
    r = requests.post('http://localhost:5000/api/pending_client_actions', json={'response': str(text), 'response_required': 'n'})
    # print(r.status_code)

def input(prompt):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    # print(prompt)
    r = requests.post('http://localhost:5000/api/pending_client_actions', json={'response': str(prompt), 'response_required': 'y'})
    # print(r.status_code)
    r = requests.get('http://localhost:5000/api/pending_server_actions')
    while r.status_code != 200:
        r = requests.get('http://localhost:5000/api/pending_server_actions')
        # print(r.status_code)
        time.sleep(1)
        # print("Input Response: ")
        # print(r.content)
    j = json.loads(r.content)
    return j[0]['response']

def get_num_options(num_options):
    J = None
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post('http://localhost:5000/api/pending_client_actions', json={'response': "Please Enter a Number", 'response_required': 'y'})
    # print(r.status_code)
    r = requests.get('http://localhost:5000/api/pending_server_actions')
    while True:
        if r.status_code == 200:
            j = json.loads((r.content))
            if is_number(j[0]['response']):
                if 0 <= int(j[0]['response']) < num_options: 
                    return int(j[0]['response'])
        r = requests.get('http://localhost:5000/api/pending_server_actions')
        # print(r.status_code)
        time.sleep(1)

