#!/usr/bin/env python
import json,sys
filename = sys.argv[1]
utree_list=open(filename,'r')

for f in  utree_list:

 f = f.strip('\n')
 body = {"m_name":f,"m_loadbalanceStrategyName": "round","m_health_check": {"interval": "3000", "check_keepalive_requests": "5", "timeout": "3000", "rise": "1", "enable_health_check":  'true', "check_http_send": "GET /healthCheck.jsp  HTTP/1.0\\r\\n\\r\\n", "default_down": 'false', "fall": "3", "check_http_expect_alive": ["http_2xx", "http_3xx"], "type": "http", "port": "80"}}
 rst = json.dumps(body,indent=4, separators=(',', ': '))
 print rst+','
utree_list.close()
