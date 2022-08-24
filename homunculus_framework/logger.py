import logging
import os
import sys


class Logger:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __call__(self, *args, **kwargs):
        # LOGGER_NAME = 'client'

        # задаем форматирование сообщений
        CLIENT_FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

        # выводим все в stderr
        STREAM_HANDLER = logging.StreamHandler(sys.stderr)
        # подключаем форматирование к обработчику
        STREAM_HANDLER.setFormatter(CLIENT_FORMATTER)
        # события не ниже ошибок (ERROR, CRITICAL)
        STREAM_HANDLER.setLevel(logging.DEBUG)

        # путь до папки исполняемого файла
        LOG_PATH = os.path.dirname(os.path.abspath(__file__))
        # путь до файла логов
        LOG_PATH = os.path.join(LOG_PATH, 'logs', f'{self.name}.txt')
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        LOG_FILE = logging.FileHandler(LOG_PATH, mode='w', encoding='utf-8')
        LOG_FILE.setFormatter(CLIENT_FORMATTER)

        # создаем новый экземпляр, т.к. ранее такой логгер не определялся
        LOGGER = logging.getLogger(self.name)
        LOGGER.addHandler(STREAM_HANDLER)
        LOGGER.addHandler(LOG_FILE)
        LOGGER.setLevel(logging.DEBUG)

        return LOGGER
