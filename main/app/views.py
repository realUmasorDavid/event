from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def event_form(request):
    info = Event.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        organizer = request.POST['organizer']
        image = request.POST['image']
        date = request.POST['date']
        time = request.POST['time']
        category = request.POST['category']
        event_info = Event(title=title, description=description, organizer=organizer, image=image, time=time, date=date, category=category)
        event_info.save()
    else:
        print('Request not sent')
    return render(request, 'index.html', {'info': info})

def qrcode(request, model_name, pk):
    if model_name == 'event':
        model = get_object_or_404(Event, pk=pk)
    context = {'model': model}
    return render(request, 'code.html', context)