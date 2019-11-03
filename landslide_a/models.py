from django.db import models
from django.db.models import Q
# Create your models here.

class main_block(models.Model):
    first_block_title=models.TextField(default="enter first block title here")
    first_block_text = models.TextField(default="enter first block text here")
    second_block_title = models.TextField(default="enter second block title here")
    second_block_text = models.TextField(default="enter second block text here")
    first_block_title_ua = models.TextField(default="Заголовок першого блоку")
    first_block_text_ua = models.TextField(default="Текст першого блоку")
    second_block_title_ua = models.TextField(default="Заголовок другого блоку")
    second_block_text_ua = models.TextField(default="Текст другого блоку")
    def __str__(self):
        return "%s %s %s %s"% (self.first_block_title,self.second_block_title,self.first_block_title_ua,self.second_block_text_ua)


class ArticleManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (Q(title__icontains=query) | Q(text__icontains=query))
            qs = qs.filter(or_lookup)

        return qs
    def search_ua(self,query=None):
        qs_ua = self.get_queryset()
        if query:
            or_lookup_ua = (Q(title_ua__icontains=query) | Q(text_ua__icontains=query))
            qs_ua = qs_ua.filter(or_lookup_ua)

        return qs_ua

class Articles(models.Model):
    objects = ArticleManager()
    image = models.ImageField(upload_to="landslide_a/static/img")
    title = models.CharField(max_length=1000)
    text = models.TextField(default="Enter text here")
    title_ua = models.CharField(max_length=1000 , default="Введіть заголовк статті")
    text_ua = models.TextField(default="Введіть текст")
    date = models.DateField()
    link_facebook = models.TextField(default="#")
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return "%s"% (self.title_ua)
    def short_text(self):
        if len(self.text)>150:
            return self.text[:150]+'...'
        else:
            return self.text
    def short_text_ua(self):
        if len(self.text_ua)>150:
            return self.text_ua[:150]+'...'
        else:
            return self.text_ua

class About(models.Model):
    title = models.TextField(max_length=1000)
    text = models.TextField(max_length=100000)
    title_ua = models.TextField(max_length=1000,default="Заголовок")
    text_ua = models.TextField(max_length=100000, default="Текст")
    icon = models.TextField(max_length=100)
    image_about = models.ImageField(upload_to="landslide_a/static/img",default="landslide_a/static/img/1502775784-80580920_cQVDkIC.jpg")
    short = models.TextField(default="enter please")
    link_to_website = models.TextField(default="enter e-mail here", max_length=100)
    def __str__(self):
        return "%s"% (self.title)

class outputs(models.Model):
    title = models.TextField(max_length=100,default="Write your title here")
    text = models.TextField(max_length=10000,default="Write your text here")
    def __str__(self):
        return "%s"% (self.title)


class case_of_study(models.Model):
    title = models.TextField(max_length=100,default="Write your title here")
    main_text = models.TextField(max_length=10000,default="Write your text here")
    title_ua = models.TextField(max_length=100, default="Введіть заголовок")
    main_text_ua = models.TextField(max_length=10000, default="Введіть текст")
    foto_object = models.ImageField(upload_to="landslide_a/static/img",default="landslide_a/static/img/1502775784-80580920_cQVDkIC.jpg")
    date = models.DateField()
    location = models.TextField(default="Write location heres")

class person(models.Model):
    first_name = models.TextField(default="enter your name please")
    last_name = models.TextField(default="enter your last name please")
    first_name_ua = models.TextField(default="Введіть ім'я")
    last_name_ua = models.TextField(default="Введіть прізвище")
    personal_image = models.ImageField(upload_to="landslide_a/static/img",default="landslide_a/static/img/1502775784-80580920_cQVDkIC.jpg")
    email = models.TextField(default="enter your e-mail")
    link_okid = models.TextField(default="enter link on your facebook page")
    interests = models.TextField(default="Enter your interests here")
    interests_ua = models.TextField(default="Enter your interests here")
    cur_pos = models.TextField(default="Enter position")
    cur_pos_ua = models.TextField(default="Enter position")
    current_position = models.TextField(default="Enter current position here")
    current_position_ua = models.TextField(default="Enter current position here")

    def __str__(self):
        return "%s%s"% (self.first_name,self.last_name)

class foto_news(models.Model):
    foto_header = models.TextField(default="Enter header of foto")
    foto = models.ImageField(upload_to="landslide_a/static/img",default="landslide_a/static/img/1502775784-80580920_cQVDkIC.jpg")
    type = models.ForeignKey(Articles,on_delete=models.CASCADE)

class main_object(models.Model):
    image = models.ImageField(upload_to="landslide_a/static/img",default="landslide_a/static/img/1502775784-80580920_cQVDkIC.jpg")
    type = models.TextField(default="")
    type_ua = models.TextField(default="")

    def _get_FIELD_display(self, field):
        return super()._get_FIELD_display(field)


class geological_background(models.Model):
    name = models.TextField(default="Enter header")
    name_ua = models.TextField(default="Enter header")
    description = models.TextField(default="Enter description of object")
    description_ua = models.TextField(default="Enter description of object")
    geol_image = models.ImageField(upload_to="landslide_a/static/img",default="landslide_a/static/img/1502775784-80580920_cQVDkIC.jpg")
    type = models.ForeignKey(main_object,on_delete=models.CASCADE)
    def __str__(self):
        return "%s%s"% (self.name,self.type)

class geological_objects(models.Model):
    name = models.TextField(default="Enter name of object")
    name_ua = models.TextField(default="Enter name of object")
    x_coord = models.FloatField(default=2.3)
    y_coord = models.FloatField(default=2.3)
    adress = models.TextField(default="Enter adress here")
    adress_ua = models.TextField(default="Enter adress here")
    desciption = models.TextField(default="Enter  here")
    desciption_ua = models.TextField(default="Enter  here")
    type_id = models.ForeignKey(main_object,on_delete=models.CASCADE)
    def __str__(self):
        return "%s%s%s"% (self.name,self.x_coord,self.y_coord)
