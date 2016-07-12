#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

# log configuration
log_filename = 'test.log'
log_filemode = 'a'
log_format = '%(asctime)s %(filename)s[line:%(lineno)d] [%(levelname)s] %(message)s'
log_datefmt = '%Y-%m-%d %H:%M:%S'
log_level = logging.DEBUG


logging.basicConfig(level=log_level, format=log_format, datefmt=log_datefmt, 
                    filename=log_filename, filemode=log_filemode)
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')

log = logging.getLogger()
log.debug('debug')
