#!/usr/bin/env python
"""

Telepaatti, IRC to Jabber/XMPP gateway.

Copyright (C) 2007-2009 Petteri Klemola

Telepaatti is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License version 3 as
published by the Free Software Foundation.

Telepaatti is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.

For more information about Telepaatti see http://23.fi/telepaatti

"""

import socket
import time, datetime
import exceptions
from threading import *
from xmpp import *
import getopt, sys

STATUSSTATES = ['AVAILABLE','CHAT', 'AWAY', 'XA', 'DND', 'INVISIBLE']
TELEPAATTIVERSION = 1

def usage():
    """Usage function for showing commandline options """
    print "Usage: telepaatti [OPTION]..."
    print "OPTIONS"
    print "-h, --help\t telepaatti help"
    print "-p, --port\t port which telepaatti listens"
    print "-u, --user\t Jabber/XMPP username in the format name@xmppserver.tld"
    print "-w, --password\t Password for Jabber/XMPP account"
    print "-d, --debug\t turn debug messages on"

def main():
    """Main function where the control flow stars """
    port = 6667
    user = ''
    password = ''
    debug = False
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   "u:p:w:h:d",
                                   ["user=",
                                    "port=",
                                    "password=",
                                    "help",
                                    "debug"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    if len(opts) == 0:
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        if o in ("-p", "--port"):
            try:
                port = int(a)
            except:
                print "port should be an integer"
                sys.exit()
        if o in ("-u", "--user"):
            if a.find('@') < 1:
                print "user name should be in form user@xmppserver.tld"
                sys.exit()
            else:
                user = a
        if o in ("-w", "--password"):
            password = a
        if o in ("-d", "--debug"):
            print "debug messages on"
            debug = True

    service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    service.bind(("", port))
    service.listen(1)

    print "listening on port", port

    (clientsocket, address ) = service.accept()
    ct = ClientThread(clientsocket, port, user, password, debug)
    ct.start()
    service.shutdown(socket.SHUT_RDWR)

if __name__ == "__main__":
    main()
