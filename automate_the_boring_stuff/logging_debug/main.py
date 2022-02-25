import logging
"""
调试：异常、断言、Logging模块
    Python记录一个事件的日志时，它都会创建一个LogRecord对象以保存关于该事件的信息。
"""
logging.basicConfig(filename='my_factorial_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# 禁用日志
# logging.disable(logging.CRITICAL)
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f'i is {i}, total is {total}')
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')
