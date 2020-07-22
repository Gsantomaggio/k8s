import sys
import time

import requests

url = 'http://{0}/apis/v1beta1/runs'.format(sys.argv[1])

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
    if tentatives >= 10:
        break

if not success:
    raise ValueError('error')
