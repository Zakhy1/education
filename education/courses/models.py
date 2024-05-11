from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.loader import render_to_string
from django_ckeditor_5.fields import CKEditor5Field
from froala_editor.fields import FroalaField
from pytils.translit import slugify

from courses.fields import OrderField


class Subject(models.Model):
    title = models.CharField(max_length=128, verbose_name='Наименование')
    slug = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Course(models.Model):
    owner = models.ForeignKey(get_user_model(),
                              related_name='courses_created',
                              on_delete=models.CASCADE, verbose_name='Владелец')
    subject = models.ForeignKey(Subject,
                                related_name='courses',
                                on_delete=models.CASCADE, verbose_name='Дисциплина')
    title = models.CharField(max_length=128, verbose_name='Название')
    slug = models.SlugField(max_length=128)
    overview = models.TextField(verbose_name='Краткое описание')
    full_overview = CKEditor5Field('Text', config_name='extends')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    students = models.ManyToManyField(get_user_model(),
                                      related_name='courses_joined',
                                      blank=True, verbose_name='Студенты')
    image = models.ImageField(upload_to='course_images', blank=True, verbose_name='Изображение')

    def save(self, *args, **kwargs):
        """
        Метод сохранения экземпляра
        """
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE, verbose_name='Курс')
    title = models.CharField(max_length=200, verbose_name='Название', blank=True)
    description = CKEditor5Field(verbose_name='Описание', config_name='default', blank=True)
    order = OrderField(blank=True, for_fields=['course'], verbose_name='Порядок')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}. {self.title}'


class Content(models.Model):
    module = models.ForeignKey(Module,
                               related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': (
                                         'text',
                                         'video',
                                         'image',
                                         'file'
                                     )})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']


class ItemBase(models.Model):
    owner = models.ForeignKey(get_user_model(),
                              related_name='%(class)s_related',
                              on_delete=models.CASCADE, verbose_name='Владелец')
    title = models.CharField(max_length=128, verbose_name='Название')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Редактировано')

    def __str__(self):
        return self.title

    def render(self):
        return render_to_string(
            f'courses/content/{self._meta.model_name}.html',
            {'item': self}
        )

    class Meta:
        abstract = True


class Text(ItemBase):
    content = CKEditor5Field(config_name='extends', verbose_name='Описание')


class File(ItemBase):
    file = models.FileField(upload_to='files', verbose_name='Файл')


class Image(ItemBase):
    file = models.FileField(upload_to='images', verbose_name='Изображение')


class Video(ItemBase):
    url = models.URLField(verbose_name='Видео')
