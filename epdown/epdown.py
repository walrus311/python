#!/usr/bin/python

#
# Imports
#
#import subprocess
import logging
#import string
from datetime import datetime
import sys
import requests



#
# Setup logging
#
logging.basicConfig(level=logging.DEBUG,   #Default to INFO - raise to DEBUG for development and troubleshooting
                    format='%(asctime)s %(name)-5s %(levelname)-8s %(funcName)s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename= str(sys.argv[0]+".log") ,
                    filemode='w')
log = logging.getLogger()



#
def foo():
    log.debug("Try one")
    response = requests.get("http://reddit.com/api/v1/me")
    log.debug("Response: %s",response.headers)



#
# Main
#
start = datetime.now()
log.info("Script start . . .")
foo()
log.info("Runtime: %s\n" % str(datetime.now() - start))
