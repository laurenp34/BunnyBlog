#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/BunnyBlog/")
sys.path.insert(0,"/var/www/BunnyBlog/BunnyBlog/")

import logging
logging.basicConfig(stream=sys.stderr)

from BunnyBlog import app as application

