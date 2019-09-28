from django.db import models

class Thread(models.Model):
    title = models.CharField('', max_length = 50)
    content = models. TextField('', max_length = 255)
    
    def __str__(self):
        return self.title
