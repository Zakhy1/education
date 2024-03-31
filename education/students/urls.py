from django.urls import path
from django.views.decorators.cache import cache_page

from students import views as student_views

urlpatterns = [
    path('register/',
         student_views.StudentRegistrationView.as_view(),
         name='student_registration'),
    path('enroll-course/',
         student_views.StudentsEnrollCourseView.as_view(),
         name='student_enroll_course'),
    path('courses/',
         student_views.StudentCourseListView.as_view(),
         name='student_course_list'),
    path('courses/<pk>/',
         cache_page(60 * 15)
         (student_views.StudentCourseDetailView.as_view()),
         name='student_course_detail'),
    path('courses/<pk>/<module_id>/',
         cache_page(60 * 15)
         (student_views.StudentCourseDetailView.as_view()),
         name='student_course_detail_module'),

]
