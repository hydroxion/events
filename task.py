from time import sleep


import schedule


from cache import pubsub


def url():
    print('Url')


def task_url(message):  # message.get('data')
    schedule.every(1).seconds.do(url)


def start_task():
    pubsub.subscribe(**{'url': task_url})

    while True:
        schedule.run_pending()

        sleep(1)
