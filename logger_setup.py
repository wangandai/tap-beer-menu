import logging


def setup_logger(logFile):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    fl = logging.FileHandler(logFile)
    fl.setLevel(logging.DEBUG)
    sl = logging.StreamHandler()
    sl.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fl.setFormatter(formatter)
    sl.setFormatter(formatter)
    logger.addHandler(fl)
    logger.addHandler(sl)