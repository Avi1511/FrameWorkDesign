import inspect
import logging

class Log:

    @staticmethod
    def logs_generation():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(r'C:\Users\x257555\PycharmProjects1\FrameWorkDesign\Logs\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        logger.info("hkmj,kk,jl,k,")
        return logger



