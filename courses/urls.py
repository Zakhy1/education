from django.urls import path

from courses import views as courses_views

urlpatterns = [
    path('mine/',
         courses_views.ManageCourseListView.as_view(),
         name='manage_course_list'),
    path('create/',
         courses_views.CourseCreateView.as_view(),
         name='course_create'),
    path('<pk>/edit/',
         courses_views.CourseUpdateView.as_view(),
         name='course_edit'),
    path('<pk>/delete/',
         courses_views.CourseDeleteView.as_view(),
         name='course_delete'),
    path('<pk>/module/',
         courses_views.CourseModuleUpdateView.as_view(),
         name='course_module_update'),
    path('module/<int:module_id>/content/<model_name>/create/',
         courses_views.ContentCreateUpdateView.as_view(),
         name='module_content_create'),
    path('module/<int:module_id>/content/<model_name>/<id>/',
         courses_views.ContentCreateUpdateView.as_view(),
         name='module_content_update'),
    path('content/<int:id>/delete/',
         courses_views.ContentDeleteView.as_view(),
         name='module_content_delete'),
    path('module/<int:module_id>/',
         courses_views.ModuleContentListView.as_view(),
         name='module_content_list'),
    path('module/order/',
         courses_views.ModuleOrderView.as_view(),
         name='module_order'),
    path('content/order/',
         courses_views.ContentOrderView.as_view(),
         name='content_order'),
    path('subject/<slug:subject>/',
         courses_views.CourseListView.as_view(),
         name='course_list_subject'),
    path('<slug:slug>/',
         courses_views.CourseDetailView.as_view(),
         name='course_detail'),
    path('admin_view/', courses_views.AdminCourseListView.as_view(), name='admin_view')
]
