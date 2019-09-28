from django.db import models
from django.urls import reverse

class Thread(models.Model):
    title = models.CharField('', max_length = 50)
    content = models. TextField('', max_length = 255)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('view_thread', kwargs = { 'id': self.id })

class Reply(models.Model):
    thread = models.ForeignKey(Thread, on_delete = models.CASCADE)
    content = models. TextField('', max_length = 255)
    
    def __str__(self):
        return self.content
