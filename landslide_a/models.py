from django.db import models
# Create your models here.
class main_block(models.Model):
    first_block_title=models.TextField(default="enter first block title here")
    first_block_text = models.TextField(default="enter first block text here")
    second_block_title = models.TextField(default="enter second block title here")
    second_block_text = models.TextField(default="enter second block text here")
    def __str__(self):
        return "%s %s"% (self.first_block_title,self.second_block_title)



class Articles(models.Model):
    image = models.ImageField(upload_to="landslide_a/static/img")
    title = models.CharField(max_length=1000)
    text = models.TextField()
    date = models.DateField()
    link_facebook = models.TextField(default="#")
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return "%s %s %s"% (self.date,self.title,self.image)
    def short_text(self):
        if len(self.text)>500:
            return self.text[:500]+'...'
        else:
            return self.text
    def all_articles(self):
        return  Articles.objects.order_by('id').reverse()[:5]
class About(models.Model):
    title = models.TextField(max_length=1000)
    text = models.TextField(max_length=100000)
    icon = models.TextField(max_length=100)
    image_about = models.ImageField(upload_to="landslide_a/static/img",default="landslide_a/static/img/1502775784-80580920_cQVDkIC.jpg")
    short = models.TextField(default="enter please")
    def __str__(self):
        return "%s"% (self.title)

class outputs(models.Model):
    title = models.TextField(max_length=100,default="Write your title here")
    text = models.TextField(max_length=10000,default="Write your text here")
    def __str__(self):
        return "%s"% (self.title)

class event(models.Model):
    title = models.TextField(max_length=100,default="Write your title here")
    main_text = models.TextField(max_length=10000,default="Write your text here")
    date = models.DateField()
    time  = models.TimeField(auto_now=True)
    location = models.TextField(default="Write location heres")
    type_of_event = models.TextField(default="Write type of your event")

class person(models.Model):
    first_name = models.TextField(default="enter your name please")
    last_name = models.TextField(default="enter your last name please")
    personal_image = models.ImageField(upload_to="landslide_a/static/img",default="landslide_a/static/img/1502775784-80580920_cQVDkIC.jpg")
    email = models.TextField(default="enter your e-mail")
    link_facebook = models.TextField(default="enter link on your facebook page")

