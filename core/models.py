from django.db import models


class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")
    
    class Meta:
        verbose_name = 'About me'
        verbose_name_plural = 'About me'
        
        def __str__(self):
            return "About me"
        
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Service name', null=True, blank=False)
    description = models.TextField(verbose_name='About Service')

    def __str__(self):
        return "{}".format(self.name)
    
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name='Work title')
    image = models.ImageField(upload_to='works')

    def __str__(self):
        return "{}".format(self.title)
    
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Client name')
    description = models.TextField(verbose_name='Client say')
    image = models.ImageField(upload_to='client', default='default.png')

    def __str__(self):
        return "{}".format(self.name)
