import logger as log

def calculate():
    calc = input('Введите математическое выражение:\n')
    log.input_logger(calc)
    answer = str(eval(calc))
    return answer