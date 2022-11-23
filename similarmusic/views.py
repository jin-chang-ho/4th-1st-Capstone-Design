import csv
import numpy as np
import librosa
import pandas as pd
import sklearn

from django.shortcuts import render
from django.http import HttpResponse
from . import models

from .models import Dataset, Music  # DB 모델 사용 가능하도록 import

from compare_newmusic import compare_music

# Create your views here.

def data_view(request):
    data = Dataset.objects.all()
    music = Music.objects.all()
    return render(request, 'similarmusic/index.html', {"data": data})


def play_music(request):
    documents = models.Document.objects.all()
    filename, musics, cosines = compare_music(documents)
    return render(request, 'similarmusic/show-files.html', context={
        'filename': filename,
        'music1': musics[0], "cosine1": cosines[0],
        'music2': musics[1], "cosine2": cosines[1],
        'music3': musics[2], "cosine3": cosines[2],
        'music4': musics[3], "cosine4": cosines[3],
        'music5': musics[4], "cosine5": cosines[4]

    })

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST.get("fileTitle")
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "similarmusic/upload-file.html", context={
        "files": documents
    })