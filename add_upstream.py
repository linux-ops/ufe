#!/usr/bin/env python
import json,sys
filename = sys.argv[1]
utree_list=open(filename,'r')

for f in  utree_list:

 f = f.strip('\n')
 rst = json.dumps(body,indent=4, separators=(',', ': '))
 print rst+','
utree_list.close()
