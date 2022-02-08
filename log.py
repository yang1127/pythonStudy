import logging

logging.basicConfig(filename='log.txt', format='%(asctime)s %(message)s', filemode='w')

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)  # 设置层级

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This iss warning message')
logger.error('This is error message')
logger.critical('This is critical message')
