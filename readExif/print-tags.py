#!/usr/bin/python

#
# imports
#
import os
import sys
import subprocess
import exifread

#
# Function to read exif tags from a .jpg file
#
def printExifTags(fn):
    fd = open(fn, 'rb')
    #tags = exifread.process_file(fd, details=False, stop_tag=tag)
    tags = exifread.process_file(fd, details=False)
    print "Found %d tags in file: %s" % (len(tags),fn)
    for t in tags:
        print "%s:  %s" % (t, tags[t])

#
# Function to read metadata from a .mov file
#
def printMovTags(fn):
    cmd = ["/usr/local/bin/hachoir-metadata",fn]
    try:
        output = subprocess.check_output( cmd , stderr=subprocess.STDOUT )
        lines = output.split("\n")[1:]
        print "Found %d tags in file: %s" %(len(lines),fn)
        for line in lines:
            print line
    except OSError as e:
        print("Caught exception: %r" % e)
        print("Filename: %s" % e.filename)
        print("Errno: %d" % e.errno)
        print("Strerror: %s" % e.strerror)
    except Exception as e:
        print("Caught exception: %r" % e)
        #print("While running command: %s" % e.cmd)
        #print("Return code: %d" % e.returncode)
        #print("Output: %s" % e.output)
    return

#
# Funciton to detect JPGs by file extension
#
def isJPG(fn):
    ext = os.path.splitext(fn)[1].lower()
    if ext == ".jpg":
        return 1
    else:
        return 0

#
# Function to detect MOVs by file extension
#
def isMOV(fn):
    ext = os.path.splitext(fn)[1].lower()
    if ext == ".mov":
        return 1
    else:
        return 0

#
# Main
#
if len(sys.argv) < 2:
    print "Usage: %s filename [filenames]" % sys.argv[0]
    sys.exit(1)

files = sys.argv[1:]
for f in files:
    try:
        if isJPG(f):
            printExifTags(f)
            next
        if isMOV(f):
            printMovTags(f)
            next
    except IOError as ex:
        print "Exception %r" % ex
        
