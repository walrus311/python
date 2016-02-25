#!/usr/bin/python

import sys
import os
import time
import logging

#
# Setup logging
#
logging.basicConfig(level=logging.DEBUG,   #Default to INFO
                    format='%(asctime)s %(name)-5s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/Users/eric/code/python/filename/filename.log',
                    filemode='w')
log = logging.getLogger()

#
# Process files
#
#def process_files():
    


#
# Main
#
log.debug("Mark 1: %s" % sys.executable)
log.debug("Mark 2: %s" % os.path.dirname(sys.executable))
log.debug("Mark 5: %s" % sys.argv[0])
log.debug("Mark 6: %s" % os.path.dirname(sys.argv[0]))



time.sleep(11)
