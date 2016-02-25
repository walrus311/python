#!/usr/bin/python

#from subprocess import check_output
import subprocess

#cmd = ['ls','-l','/bin','2>&1']
cmd = ['ls','-l','/binxx']

output = ''
e = ''
try:
    print "Mark 1"
    print "Running: " , cmd
    output = subprocess.check_output( cmd , stderr=subprocess.STDOUT )
    print "Mark 2"
#except Exception as e:
except Exception as e:
    print "Return code: %r" % output
    print "Exception: %r" % e
    print "Exception: Command: %s" % e.cmd
    print "Exception: Returncode: %d" % e.returncode
    print "Exception: Output: %s" % e.output

    
#print 'Have %d bytes in output' % len(output)
#print "Output: %r" % output
print "Output: %s" % output
try:
    print "Exception: e.output: %s " % e.output
except NameError as en:
    print
