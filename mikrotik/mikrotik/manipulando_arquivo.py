import calendar
import re
from time import strptime
from .models import Firewall_Login_Error

def manipulando_arquivo(f):
	for line in f:
		mac = r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})'
        ip = r'[0-9]+(?:\.[0-9]+){3}(:[0-9]+)?'

        find_mes = re.search(r'\b([a-z]){3}\b', line)
        if find_mes is not None:
        	data_convertida = converter_data(find_mes.group(0))

        find_data = re.search(r'/\b\d{2}/\d{4}\b', line)
        print '%s' %find_data

        #data_final = ''.join([data_convertida,find_data.group(0)])
		#find = re.search(mac, line, re.I)
		#find = re.search()
        #print '%s' %find[1]
        
        #if find is not None:
        	#print (find.group(0))
        #else:
        	#print 'nada encontrado'


        #mac = r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})'
        #ip = r'[0-9]+(?:\.[0-9]+){3}(:[0-9]+)?'
       
        #jan/07/1970 03:11:27 system,error,critical 
        #login failure for user admin from 192.168.0.16 via web
        #print '%s' %data_final
        save_login_error = Firewall_Login_Error(

        	)
def converter_data(data):
	converter = strptime(data,'%b').tm_mon
	return converter