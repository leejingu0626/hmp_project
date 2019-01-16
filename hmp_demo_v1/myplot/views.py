from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, HttpResponse, render_to_response
import json

from .models import RawData
import csv

# Call upload.html for upload file
def upload_file(request):
    return render(request, "myplot/upload.html", {})

# View db
def upload_file_to_html(request):
    file = request.FILES['files']
    name = file.name
    BASE_DIR= "C:/Users/leejingu/Desktop"
    f = BASE_DIR+"/"+name
    with open(f) as fp:
        reader = csv.reader(fp,delimiter=',')
        iter_readers = iter(reader)
        next(iter_readers)
        for value in iter_readers:
            created = RawData.objects.get_or_create(
                column_1=value[0],
                column_2=value[1],
                column_3=value[2],
                column_4=value[3],
                column_5=value[4],
            )

    rawdatas = RawData.objects.all()
    rawdata = {'rawdatas':rawdatas}
    return render(request, 'myplot/index.html', rawdata)

def data_json(request):
    rawdatas = RawData.objects.all()
    data = [{"x":0, "column3":0, "column4":0, "column5":0}]
    for rawdata in rawdatas:
        index = int(rawdata.column_2)
        column3_data = float(rawdata.column_3)
        column4_data = float(rawdata.column_4)
        column5_data = float(rawdata.column_5)
        # print(column3_data)
        data.append({"x":index,
                     "column3":column3_data,
                     "column4":column4_data,
                     "column5":column5_data})

    return JsonResponse(data, safe=False)

# html test code(2019. 01. 14 jglee)
def index_html(request):
    rawdatas = RawData.objects.all()
    rawdata = {'rawdatas':rawdatas}
    return render(request, 'myplot/index.html', rawdata)