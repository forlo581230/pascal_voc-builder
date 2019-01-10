# -*- coding: utf-8 -*-

from xml.dom.minidom import parse, parseString
from glob import glob
import os
 
path = 'data/prsugar'
files = glob(os.path.join(path, '*.xml'))

for file in files:
    print (file)
    dom=parse(file)
    root=dom.documentElement
    name=root.getElementsByTagName('name')
    #setting new tag name
    name[0].firstChild.data='rsugar'
    #write to xml
    with open(file,'w') as fh:
        dom.writexml(fh)