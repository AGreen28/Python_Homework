from datetime import datetime as dt

def input_logger(data):
    time = dt.now()
    with open('log.txt', 'a') as file:
        file.write('{} - Input: {}\n'.format(time, data))

def answer_logger(data):
    time = dt.now()
    with open('log.txt', 'a') as file:
        file.write('{} - Answer: {}\n'.format(time, data))