from django.shortcuts import render
import re
from .manipulando_arquivo import manipulando_arquivo
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        manipulando_arquivo(request.FILES['myfile'])        
        return render(request, 'mikrotik/upload.html')
    return render(request, 'mikrotik/upload.html')

