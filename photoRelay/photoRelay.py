#!/usr/bin/python

#
# Imports
#
#import subprocess
import logging
#import string
from datetime import datetime
import sys
import os
import imghdr
import exifread
import string
import subprocess
import shutil
import uuid


#
# Fallout directory for unprocessable files
#
fallout_dir = "/Users/Shared/Pictures/fallout"


#
# Setup logging
#
logging.basicConfig(level=logging.INFO,   #Default to INFO - raise to DEBUG for development and troubleshooting
                    format='%(asctime)s %(name)-5s %(levelname)-8s %(funcName)s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename= str(sys.argv[0]+".log") ,
                    filemode='w')
log = logging.getLogger()


#
# Function to scan and route list of files in src_dir
#
def processDir(src_dir,arc_dir,token):
    log.debug("Directory: %s Token: %s" % (src_dir,token))
    files = os.listdir(src_dir)
    # Cap file list at three files for testing
#    files = files[0:500]
    log.debug("Files: %d" % len(files))
    # filenames in files are not full paths, so chdir to avoid mass string concatenation
    os.chdir(src_dir)
    for f in files:
        # ignore dot files
        ext = os.path.splitext(f)[1].lower()
        if ext == ".jpg":
            archiveJPG(f,arc_dir,token)
        elif ext == ".mov":
            archiveMOV(f,arc_dir,token)
        else:
            # Move to fallout directory
            log.info("No process for type. Moveing %s to %s" % (f,fallout_dir))
            archiveFile(f,fallout_dir,token)
    return


#
# Function to archive JPG to archive_dir
#
def archiveJPG(f,arc_dir,token):
    log.debug("File: %s Archive Directory: %s" % (f,arc_dir))
    
    if not isPhoto(f):
        log.warn("Not a photo, exiting")
        return
    log_level = log.getEffectiveLevel()
    log.setLevel(logging.INFO)
    ifd_tag = readExifTag(f,'EXIF DateTimeDigitized')
    log.setLevel(log_level)
    if ifd_tag is None:
        log.warn("No Exif date found: %s, moving to %s" % (f,fallout_dir))
        archiveFile(f,fallout_dir,token)
        return
    log.debug("Date: %s" % ifd_tag)
    # Expecting a string like: '2014:11:12 20:26:33'
    (y,m,d) = str(ifd_tag).split(" ")[0].split(":")
    archiveFile(f,cat_arc_dir(arc_dir,y,m,d),token)
    return


#
# Function to retrieve a named EXIF tag
#
def readExifTag(fn,tag_name):
    log.debug("Filename: %s Tagname: %s",(fn,tag_name))
    fd = open(fn, 'rb')
    tags = exifread.process_file(fd, details=False, stop_tag=tag_name)
    if tag_name in tags:
        return tags[tag_name]
    else:
        return None
    

#
# Predicate to determine if file is a photo
#
def isPhoto(f):
    log.debug("File: %r" % f)
    ft = imghdr.what(f)
    log.debug("File type: %s" % ft)
    if ft is None:
        return False
    else:
        return True


#
# Function to archive MOV to archive_dir
#
def archiveMOV(f,arc_dir,token):
    log.debug("File: %s Archive Directory: %s" % (f,arc_dir))
    cr_date = getMovCreateDate(f)
    if cr_date is None:
        log.warn("\tGot None type from date function")
        archiveFile(f,fallout_dir,token)        
    else:
        log.debug("Create date: %s" % cr_date)
        (y,m,d) = cr_date.split("-")
        archiveFile(f,cat_arc_dir(arc_dir,y,m,d),token)


#
# Function to parse create date from hachoir output
#
def getMovCreateDate(f):
    log.debug("File: %s",f)

    cmd = ["/usr/local/bin/hachoir-metadata",f]
    try:
        log.debug("Command: %s" % string.join(cmd))
        output = subprocess.check_output( cmd , stderr=subprocess.STDOUT )
        words = output.split()
        idx = words.index('Creation')
        idx += 2
        return words[idx]
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
# Function to concatenate archive directory name
#
def cat_arc_dir(arc_dir,y,m,d):
    return arc_dir+"/"+y+"/"+y+"-"+m+"-"+d


#
# Function to archive file in date named directory
#
def archiveFile(f,ad,token):
    log.debug("File: %s Archive Directory: %s" % (f,ad))
    try:
        if not os.path.exists(ad):
            log.debug("makedirs() %s" % ad)
            os.makedirs(ad)
        # Add token first, reduces chances of conflict later
        nfn = token + f
        log.debug("Filename w/ token: %s" % f)
        os.rename(f,nfn)
        f = nfn
        move_uniq(f,ad)
    except Exception as e:
        log.warn("Caught exception: %r" % e)


#
# Function to move and rename for uniqness if necessary
#
def move_uniq(f,ad):
    # Check for conflict at dst, insert uuid if needed (overkill)
    if os.path.isfile(ad+"/"+f):
        log.warn("Move conflict detected, inserting uuid")
        nfn = uniq_fn(f)
        log.info("rename %s %s" % (f,nfn))
        os.rename(f,nfn)
        f = nfn
    log.info("move %s %s" % (f,ad))
    shutil.move(f,ad)


#
# Function to insert UUID in a filename
#
def uniq_fn(fn):
    log.debug("Filename: %s" % fn)
    fnln = len(fn)
    nfn = fn[0:fnln-3]+str(uuid.uuid4())+"."+fn[fnln-3:fnln]
    log.debug("New Filename: %s" % nfn)
    return nfn


#
# Main
#
start = datetime.now()
log.info("Script start . . .")
#processDir("/Users/eric/code/python/photoRelay/data/src","/Users/eric/code/python/photoRelay/data/dst","t")
processDir("/Users/ftpuser/CameraSync/eric","/Users/Shared/Pictures/Sorted Pictures","e")
processDir("/Users/ftpuser/CameraSync/erica","/Users/Shared/Pictures/Sorted Pictures","a")
processDir("/Users/ftpuser/CameraSync/ipad","/Users/Shared/Pictures/Sorted Pictures","i")
log.info("Runtime: %s\n" % str(datetime.now() - start))
