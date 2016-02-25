#!/usr/bin/python

import sys
import logging
import string
import subprocess

#
# Use logger for debugging
#
#logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

#
# Constants
#
user = ''
passwd = ''
host = '10.0.0.12'
dst = '/volume1/NetworkMusic'
options = '-awh --rsh=ssh --progress --delete-after'

src='/Users/Shared/Music/iTunes/iTunes Media/Music/'
#src='/Users/Shared/Music/iTunes/iTunes Media/Music/The Who'
#src='/Users/Shared/Music/iTunes/iTunes Media/Music/Yes'

#
# Build command
#
# time sshpass -p $pass rsync -aWh --rsh=ssh --progress --delete-after "$src" $user@$host:$dst
command = [ "time" ,
            "sshpass -p" , passwd ,
            "rsync", options , src, user + "@" + host + ":" + dst
]
logging.debug("Command: "+string.join(command))

#
# Execute command
#
#subprocess.call(command)
#logging.debug("Finished!")

sec = 30
x = [ '/bin/sleep' , str(sec) ]
logging.debug("Command: " + str(x))
subprocess.call(x)
logging.debug("Finished!")
