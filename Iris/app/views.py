"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
# Clases del analisis
from app.getFrame import GetFrame as gf
from app.faceAPI import sendToAPI as fa
from app.parseData import parseData as pd

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def analysis(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/analysis.html',
        {
            'title':'Comenzar análisis',
            'year':datetime.now().year,
        }
    )

def result(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST' and request.FILES['videourl']:
        # Guardar el video en la aplicacion
        myfile = request.FILES['videourl']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # Invocar el video
        osPath = r'%s' % os.getcwd().replace('\\','/')
        path = osPath + '/media/'
        videopath = osPath + uploaded_file_url
        gf.getFrames(videopath)
        # Inicializar el JSON [
        out_file = open("response.json", "a+")
        out_file.write("[\n")
        out_file.close()
        # Llamar el API
        for filename in os.listdir(path):
            if (filename[-3:] == 'jpg'):
                imgurl = path + filename
                fa.imgToAPI(path, filename)
        # Cerrar el JSON con ]
        with open("response.json","rb+") as filehandle:
            filehandle.seek(-3, os.SEEK_END)
            filehandle.truncate()
        with open("response.json","a+") as filehandle:
            filehandle.write("]")
        # Formatear datos y crear el grafico
        pd.printData()
        os.remove("response.json")
        os.remove(videopath)
        for filename in os.listdir(path):
            if (filename[-3:] == 'jpg'):
                os.remove(path + filename)
    return render(
        request,
        'app/result.html',
        {
            'title':'Resultado del análisis',
            'uploaded_file_url': uploaded_file_url,
            'year':datetime.now().year,
        }
    )