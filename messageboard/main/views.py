from django.shortcuts import render, redirect
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
            
            return redirect(thread.get_absolute_url())
    
    return render(request, 'newthread.html', { 'form': form })

def index(request):
    threads = Thread.objects.all().order_by('-id')
    return render(request, 'index.html', { 'threads': threads })

def view_thread(request, id):
    thread = Thread.objects.get(id = id)
    replies = Reply.objects.filter(thread = thread)
    
    form = NewReplyForm()
    
    if request.method == 'POST':
        form = NewReplyForm(request.POST)
        
    
        if form.is_valid():
            content = form.cleaned_data['content']
            
            reply = Reply(thread = thread, content = content)
            reply.save()
            return redirect('.')

    return render(request, 'viewthread.html', { 'thread': thread, 'replies': replies, 'form': form })
