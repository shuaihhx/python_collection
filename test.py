from myUtils import Logger


def testLogger():
    logger = Logger().getLogger('test')
    logger.debug('debug')
    logger.info('info')

if __name__ == '__main__':
    testLogger()