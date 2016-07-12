import requests
from time import sleep as sleep

while(1):
    response = requests.get('http://www.eastereggdevelopment.com/private/new-data')
    data = response.json()

    print data['new-data']

    if data['new-data'] == 'NONE':
        sleep(1)

    elif data['new-data'] == 'COFFEE':
        coffeeresponse = requests.get('http://www.eastereggdevelopment.com/private/queue')
        coffeedata = response.json()
        print data['queue']

        sleep(1)

    elif data['new-data'] == 'STATUS':
        print data
        sleep(1)

    elif data['new-data'] == 'BOTH':
        response = requests.get('http://www.eastereggdevelopment.com/private/queue')
        data = response.json()
        print data['queue']

        sleep(1)
    print '------------'
