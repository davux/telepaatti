# -*- coding: utf-8 -*-
# vi: sts=4 et sw=4

"""Configuration file management."""

import ConfigParser
import os

_systemFile = '/etc/%telepaatti.conf'
_localFile = os.path.expanduser('./telepaatti.conf')

config = ConfigParser.SafeConfigParser()
config.read([_systemFile, _localFile])
