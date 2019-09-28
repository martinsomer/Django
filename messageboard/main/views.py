from django.shortcuts import render
from .forms import *
from .models import *

def create_thread(request):
    form = NewThreadForm()
    
    if request.method == 'POST':
        form = NewThreadForm(request.POST)
    
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            
            thread = Thread(title = title, content = content)
            thread.save()
    
    return render(request, 'newthread.html', { 'form': form })

def index(request):
    threads = Thread.objects.all().order_by('-id')
    return render(request, 'index.html', { 'threads': threads })

def view_thread(request, id):
    thread = Thread.objects.get(id = id)    
    return render(request, 'viewthread.html', { 'thread': thread })
