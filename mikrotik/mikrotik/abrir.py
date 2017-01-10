import glob
import os
import re
from django.http import HttpResponse

#def arquivo(f):
	#for file in glob.glob('mikrotik/*.log'):
	#for line in open(f):
		#linha = line
	#with open()
	#
def arquivo(f):
    destination = open(f, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()