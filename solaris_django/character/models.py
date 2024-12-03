from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(blank=True,null=True)
    image = models.ImageField(upload_to='uploads/',blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/',blank=True, null=True)
    background = models.CharField(max_length=255, blank=True,null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    martialStyle = models.CharField(max_length=255, blank=True, null=True)
    body = models.IntegerField(default=0)
    agility = models.IntegerField(default=0)
    mind = models.IntegerField(default=0)
    hp = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    resistance  = models.IntegerField(default=0)
    deadlift = models.IntegerField(default=0)
    dodge = models.IntegerField(default=0)
    actions = models.IntegerField(default=0)
    deadeye = models.IntegerField(default=0)
    critical_reduction = models.IntegerField(default=0)
    willpower = models.IntegerField(default=0)
    skillpoints = models.IntegerField(default=0)
    skillcap = models.IntegerField(default=0)
    skillnumber = models.IntegerField(default=0)
    skillsadded = models.JSONField(default=list, blank=True, null=True)
    level = models.IntegerField(default=0)
    actives = models.JSONField(default=list, blank=True, null=True)
    joblevel = models.IntegerField(default=0)
    jobtoken = models.IntegerField(default=0)
    jobtalents = models.JSONField(default=list, blank=True, null=True)
    jobskills = models.JSONField(default=list, blank=True, null=True)
    martialStylelevel = models.IntegerField(default=0)
    martialStyletoken =  models.IntegerField(default=0)
    martialStyletalents =  models.JSONField(default=list,blank=True, null=True)
    backgroundskills = models.JSONField(default=list, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127:0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
            
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        
        thumbnail = File(thumb_io, name=image.name)
        
        return thumbnail