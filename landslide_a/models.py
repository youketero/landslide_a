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
    short = models.TextField(default="enter please")
    def __str__(self):
        return "%s"% (self.title)

class outputs(models.Model):
    title = models.TextField(max_length=100,default="Write your title here")
    text = models.TextField(max_length=10000,default="Write your text here")
    def __str__(self):
        return "%s"% (self.title)
