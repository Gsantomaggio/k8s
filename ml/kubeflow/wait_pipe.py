import time

import requests

url = 'http://localhost:8080/apis/v1beta1/runs'

success = False
tentatives = 0

while not success:
    response = requests.get(url)
    runs = response.json()["runs"]
    last = runs[(len(runs) - 1)]
    print(
        "{0} - {1} - {2} - {3} - {4}".format(last["id"], last["created_at"], last["status"], last["name"], tentatives))
    success = last["status"] == "Succeeded"
    time.sleep(2.4)
    tentatives += 1
    if tentatives >= 30:
        break
