#!/usr/bin/python

#
# imports
#
import os
import sys
import exifread

#
# Function to read exif tags
#
def printExifTags(fn):
    fd = open(fn, 'rb')
    #tags = exifread.process_file(fd, details=False, stop_tag=tag)
    tags = exifread.process_file(fd, details=False)
    print "Found %d tags in file: %s" % (len(tags),fn)
    for t in tags:
        print "%s:  %s" % (t, tags[t])

#
# Function to retrieve a named EXIF tag
#
def readExifTag(fn,tag_name):
    fd = open(fn, 'rb')
    tags = exifread.process_file(fd, details=False, stop_tag=tag_name)
    if tag_name in tags:
        return tags[tag_name]
    else:
        return None

#
# Main
#
if len(sys.argv) < 2:
    print "Usage: %s filename [filenames]" % sys.argv[0]
    sys.exit(1)

files = sys.argv[1:]
for f in files:
    try:
        printExifTags(f)
    except IOError as ex:
        print "Exception %r" % ex
        
