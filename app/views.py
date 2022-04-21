from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import *
def insert_topic(request):
    if request.method=='POST':
        TN=request.POST.get('topic')
        print(TN)
        T=Topic.objects.get_or_create(topic_name=TN)[0]
        T.save()
        return HttpResponse('Topic data is inserted Successfully')
    return render(request,'insert_topic.html')