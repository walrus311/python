#!/usr/bin/python

#
# imports
#
import os
import exifread

#
# Function to read exif tags
#
def readExif(fn):
    print "Filename: %s" % fn
    fd = open(fn, 'rb')
    print "FD: %r" % fd
    tag = 'EXIF DateTimeDigitized'
    tags = exifread.process_file(fd, details=False, stop_tag=tag)
    print "%s <-> %s" % (tag, tags[tag])


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
os.chdir("data")
files = os.listdir(".")
print "Found files: %d" % len(files)
for x in files:
    print "File: %s" % x
    date = readExifTag(x,'EXIF DateTimeDigitized')
    if date is not None:
        print "\t%s" % date
    else:
        print "\tNo Date Found!"
