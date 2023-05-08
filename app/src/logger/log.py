import os
import logging
import sys
from config import debug

os.makedirs('./logs', exist_ok=True)
_error_log_file = os.path.expanduser('./logs/error.log')
_critical_log_file = os.path.expanduser('./logs/critical.log')

formatter = logging.Formatter('[%(asctime)s %(name)s] %(levelname)s: %(message)s')
default_handler = logging.StreamHandler(sys.stdout)
default_handler.setFormatter(formatter)

# 错误级别
error_handler = logging.FileHandler(_error_log_file, encoding='utf8')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

# 关键级别
critical_handler = logging.FileHandler(_critical_log_file, encoding='utf8')
critical_handler.setLevel(logging.CRITICAL)
critical_handler.setFormatter(formatter)


def new_logger(name):
    logger = logging.getLogger(name)
    logger.addHandler(default_handler)
    logger.addHandler(error_handler)
    logger.addHandler(critical_handler)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    return logger

