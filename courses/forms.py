from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from courses.models import Course, Module


class BaseModuleFormSet(BaseInlineFormSet):
    def clean(self):
        if any(self.errors):
            # Don't bother validating the formset unless each form is valid on its own
            return
        for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
                continue
            title = form.cleaned_data.get("title")
            if title == '':
                raise ValidationError("Поле Наименование не должно быть пустым.")


ModuleFormSet = inlineformset_factory(Course,
                                      Module,
                                      fields=['title', 'description'],
                                      extra=2,
                                      can_delete=True,
                                      formset=BaseModuleFormSet)


class CourseCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Названин:'
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['overview'].label = 'Краткое описание:'
        self.fields['overview'].widget.attrs.update({'class': 'form-control danger', 'rows': '3'})
        self.fields['hours'].label = 'Количество часов для освоения:'
        self.fields['hours'].widget.attrs.update({'class': 'form-control'})
        self.fields['tasks'].label = 'Количество заданий:'
        self.fields['tasks'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Course
        fields = ('title', 'subject', 'image', 'overview', 'full_overview', 'hours', 'tasks')


class CourseEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Название:'
        self.fields['title'].widget.attrs.update({'class': 'form-control col'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['overview'].label = 'Краткое описание:'
        self.fields['overview'].widget.attrs.update({'class': 'form-control danger', 'rows': '5'})
        self.fields['full_overview'].label = 'Подробное описание:'
        self.fields['hours'].label = 'Количество часов для освоения:'
        self.fields['hours'].widget.attrs.update({'class': 'form-control'})
        self.fields['tasks'].label = 'Количество заданий:'
        self.fields['tasks'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Course
        fields = ('title', 'overview', 'full_overview', 'image', 'hours', 'tasks')
