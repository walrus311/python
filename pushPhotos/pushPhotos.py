#!/usr/bin/python

#
# Imports
#
import subprocess
import logging
import string
from datetime import datetime

#
# Setup logging
#
logging.basicConfig(level=logging.INFO,   #Default to INFO
                    format='%(asctime)s %(name)-5s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/Users/eric/bin/pushPhotos.log',
                    filemode='w')
log = logging.getLogger()

#
# Function to load password from a file
#
def loadPass(pwfile):
    try:
        fo = open(pwfile)
        pw = fo.read().strip()
        fo.close()
        return pw
    except Exception as e:
        log.warn("Caught exception: %r" % e)
        log.warn("Output: %s" % e.output)
        return None

#
# Function to wrap the rsync call
#
def syncToNAS(usr,pwd,hst,src,dst):
    cmd = ["/usr/local/bin/sshpass","-p",pwd,"/usr/bin/rsync","-aWh","--rsh=ssh","--progress","--delete-after",src,usr+"@"+hst+":"+dst]
    try:
        log.debug("Command: %s" % string.join(cmd))
        output = subprocess.check_output( cmd , stderr=subprocess.STDOUT )
        log.debug("Output: %r" % output)
    except OSError as e:
        log.warn("Caught exception: %r" % e)
        log.warn("Filename: %s" % e.filename)
        log.warn("Errno: %d" % e.errno)
        log.warn("Strerror: %s" % e.strerror)
    except Exception as e:
        log.warn("Caught exception: %r" % e)
        log.warn("While running command: %s" % e.cmd)
        log.warn("Return code: %d" % e.returncode)
        log.warn("Output: %s" % e.output)
    return

#
# Main
#
xTime = datetime.now()

# Load the password
pw = loadPass("pushPhotos.pass")
if pw is None:
    log.warn("Failed to load password . . . exiting")
    exit

src='/Users/ftpuser/CameraSync/'
log.info("Syncing: %s" % src)
yTime = datetime.now()
syncToNAS('admin',pw,'10.0.0.12',src,'/volume1/PhotoSync/ftpuser/CameraSync/')
runtime = datetime.now() - yTime
log.info("Runtime: %s" % runtime)

src='/Users/Shared/Pictures/'
log.info("Syncing: %s" % src)
yTime = datetime.now()
syncToNAS('admin',pw,'10.0.0.12',src,'/volume1/PhotoSync/Shared/Pictures/')
runtime = datetime.now() - yTime
log.info("Runtime: %s" % runtime)

runtime = datetime.now() - xTime
log.info("Total Runtime: %s\n\n" % runtime)
