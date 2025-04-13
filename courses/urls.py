from django.urls import path
from django.contrib.auth import views as auth_views
from courses import views
from .views import CourseCreateView  # Added 
from .views import CourseListAPI, CourseDetailAPI, EnrollStudentAPI

urlpatterns = [
    path('', views.CourseListView.as_view(), name='course_list'),  # Updated 
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),  # Updated 
    path('course/create/', CourseCreateView.as_view(), name='course_create'),  # Updated 
    path('course/update/<int:course_id>/', views.course_update, name='course_update'),
    path('course/delete/<int:course_id>/', views.course_delete, name='course_delete'),
    path('course/<int:course_id>/lesson/create/', views.lesson_create, name='lesson_create'),
    path('lesson/update/<int:lesson_id>/', views.lesson_update, name='lesson_update'),
    path('lesson/delete/<int:lesson_id>/', views.lesson_delete, name='lesson_delete'),
    path('students/', views.student_list, name='student_list'),
    path('enroll/', views.enroll_student, name='enroll_student'),
    path('course/<int:course_id>/students/', views.course_students, name='course_students'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='courses/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='courses/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='courses/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='courses/password_reset_complete.html'), name='password_reset_complete'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='courses/password_change.html'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='courses/password_change_done.html'), name='password_change_done'),
     # API endpoint for listing all courses
    path('api/courses/', CourseListAPI.as_view(), name='api_course_list'),
    
    # API endpoint for getting course details
    path('api/courses/<int:pk>/', CourseDetailAPI.as_view(), name='api_course_detail'),
    
    # API endpoint for enrolling a student
    path('api/enroll/', EnrollStudentAPI.as_view(), name='api_enroll_student'),
]
