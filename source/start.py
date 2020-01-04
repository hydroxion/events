from threading import Thread


from task import start_task

from server import start_server


if __name__ == '__main__':
    Thread(target=start_task, name='Task').start()

    Thread(target=start_server, name='Server').start()
