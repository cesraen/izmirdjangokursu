from django.db import models

# Create your models here.
class Category(models.Model):
    STATUS = (('True', 'Evet'), ('False', 'Hayir'))
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choice=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children',
                               on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title