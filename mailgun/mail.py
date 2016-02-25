#!/usr/bin/python

#
# Learnng the MailGun API as well as restul serivce interraction.
#

import requests

def send_simple_message():
    
    auth=("api", "key-zbc123")

    data={"from": "Mailgun Sandbox <postmaster@sandbox293847556.mailgun.org>",
          "to": "Foo <foo@bar.com>",
          "subject": "Mailgun Test 2",
          "text": "Test message body v2"}
    
    rv = requests.post(
        "https://api.mailgun.net/v2/sandbox1029384756.mailgun.org/messages",
        auth,
        data
    )
      
    print "Return value: %r" % rv
    print "Type: %r" % type(rv)

send_simple_message()
