#-*- coding: utf-8 -*-
"""
# logging - ведення журналу
В цьому модулі визначені функції і класи, які реалізують гнучку систему реєстрації подій для прикладних програм і бібліотек. Нижче показано найпростіший спосіб використання модуля. Приклад створює файл `mylog.log` з журналом подій.
"""
import logging
logging.basicConfig(format='%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.DEBUG, filename='mylog.log', filemode='w') # конфігурування системи реєстрації подій
logging.debug('Повідомлення налагоджувача')
logging.info('Інформаційне повідомлення')
logging.warning('Попередження')
logging.error('Помилка')
logging.critical('Критичне повідомлення')
"""
    DEBUG    [2018-08-31 14:56:40,039]  Повідомлення налагоджувача
    INFO     [2018-08-31 14:56:40,039]  Інформаційне повідомлення
    WARNING  [2018-08-31 14:56:40,039]  Попередження
    ERROR    [2018-08-31 14:56:40,039]  Помилка
    CRITICAL [2018-08-31 14:56:40,039]  Критичне повідомлення
"""
