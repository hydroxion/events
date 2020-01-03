from time import sleep


import schedule


from cache import client


def url():
    print('Url')


def task_url(message):  # message.get('data')
    schedule.every(1).seconds.do(url)


def start_task():
    print(' * Task start')

    pubsub = client.pubsub()

    pubsub.subscribe(**{'url': task_url})

    while True:
        # This log is not 100% accurate, once it doesn't
        # read all the messages before sleep
        message = pubsub.get_message()

        if message:
            print('Message: ', message)

        schedule.run_pending()

        sleep(1)
