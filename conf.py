# -*- coding: utf-8 -*-
# vi: sts=4 et sw=4

"""Configuration file management."""

import ConfigParser
import os

_systemFile = '/etc/%telepaatti.conf'
_localFile = os.path.expanduser('./telepaatti.conf')

config = ConfigParser.SafeConfigParser()
config.read([_systemFile, _localFile])

class ConfigDict(dict):
    def __init__(self, name):
        #super(ConfigDict, self).__init__(name)
        self.reverses = {}
        print "Parsing conf file for section %s" % name
        try:
            for chandef in config.items(name):
                self[chandef[0]] = chandef[1]
        except ConfigParser.NoSectionError:
            pass # No aliases are set

    def __getitem__(self, key):
            return self.get(key, key)

    def __setitem__(self, key, value):
            print ("Setting alias %s = %s" % (key, value))
            super(ConfigDict, self).__setitem__(key, value)
            self.reverses[value] = key

    def find(self, value):
            return self.reverses.get(value, value)

