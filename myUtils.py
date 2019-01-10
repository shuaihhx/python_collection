import logging
import os

class Logger:
    def __init__(self, path=None):
        if path:
            self.path = path
        else:
            self.path = 'logs'
        
    def getLogger(self, name=None):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        
        if name:
            if not os.path.exists(self.path):
                os.makedirs(self.path)
            path = os.path.join(self.path, name+'.log')
        
            fh = logging.FileHandler(path)
            fh.setLevel(logging.INFO)
            fh.setFormatter(formatter)
            logger.addHandler(fh)

        return logger