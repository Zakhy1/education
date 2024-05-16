from django import forms
from django.forms.models import inlineformset_factory
from courses.models import Course, Module

ModuleFormSet = inlineformset_factory(Course,
                                      Module,
                                      fields=['title', 'description'],
                                      extra=2,
                                      can_delete=True)


class CourseCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['overview'].label = 'Краткое описание'
        self.fields['overview'].widget.attrs.update({'class': 'form-control danger', 'rows': '3'})
        self.fields['hours'].label = 'Количество часов для освоения курса'
        self.fields['hours'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Course
        fields = ('title', 'subject', 'image', 'overview', 'full_overview', 'hours')


class CourseEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Название:'
        self.fields['title'].widget.attrs.update({'class': 'form-control col'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['overview'].label = 'Краткое описание:'
        self.fields['overview'].widget.attrs.update({'class': 'form-control danger', 'rows': '5'})
        self.fields['full_overview'].label = 'Подробное описание:'
        self.fields['hours'].label = 'Количество часов для освоения курса'
        self.fields['hours'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Course
        fields = ('title', 'overview', 'full_overview', 'image', 'hours')
