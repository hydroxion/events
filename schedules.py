from time import sleep

import schedule


schedule.every(5).seconds.do(webhook)


while True:
    schedule.run_pending()

    sleep(1)