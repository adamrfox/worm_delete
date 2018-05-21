#!/usr/bin/python

import os
import sys

for dirname, subdirList, filelist in os.walk (sys.argv[1]):
  for fname in filelist:
    full_path = '"' + dirname + "/" + fname + '"'
    full_path = full_path.replace("$", "\$")
    cmd_str = "isi worm files delete -f " + full_path
    print cmd_str
    os.system (cmd_str)
