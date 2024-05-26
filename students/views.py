from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth import authenticate, login
from django.views.generic.detail import DetailView

from courses.models import Course, Module
from users.forms import CustomUserCreationForm
from .forms import CourseEnrollForm


class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['email'],
                            password=cd['password1'])
        if user is not None:
            login(self.request, user)
        return result


class StudentsEnrollCourseView(LoginRequiredMixin,
                               FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_course_detail', args=[self.course.id])


class StudentsUnrollCourseView(LoginRequiredMixin,
                               FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.remove(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_course_list')


class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user]).annotate(
            total_modules=Count('modules')
        )


class StudentCourseDetailView(DetailView):
    model = Course
    template_name = 'students/course/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        if 'module_id' in self.kwargs:
            module = course.modules.get(id=self.kwargs['module_id'])
        else:
            module = course.modules.all()[0]
        context['unroll_form'] = CourseEnrollForm(
            initial={'course': self.object}
        )
        context['module'] = module
        next_module = module.get_next_module()
        prev_module = module.get_prev_module()
        context['next_module_id'] = next_module.id if next_module else module.id
        context['prev_module_id'] = prev_module.id if prev_module else module.id

        return context
