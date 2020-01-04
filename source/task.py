from time import sleep


import schedule


from cache import client


from threading import Thread


from ast import literal_eval


from requests import post, Timeout

from requests.exceptions import MissingSchema


def request(data):
    try:
        response = post(data.get('url'), json=data, timeout=data.get('seconds')).json()

        if response.get('status'):
            return schedule.CancelJob
    except Timeout:
        pass
    except MissingSchema:
        return schedule.CancelJob


def channel_webhook(message):
    data = literal_eval(message.get('data', {}).decode('utf-8'))

    schedule.every(data.get('seconds')).seconds.do(lambda: request(data)).tag('webhook', data.get('trace'))


def start_schedule():
    while True:
        schedule.run_pending()

        sleep(1)


def start_message(pubsub):
    while True:
        message = pubsub.get_message()

        if message:
            print(message)

        sleep(0.001)


def start_task():
    print(' * Task start')

    Thread(target=start_schedule, name='Schedule').start()

    pubsub = client.pubsub()

    pubsub.subscribe(**{'webhook': channel_webhook})

    Thread(target=start_message, name='Message', args=(pubsub,)).start()
