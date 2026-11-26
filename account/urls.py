from django.urls import path
from . import views


from .views import StudentCreateView, StudentDetailView, StudentUpdateView,StudentsListView,StudentDeleteView

urlpatterns=[
    path('h/',views.home, name="home"),
    path('reg/',views.register, name="regis"),
    path('log/',views.user_login, name="login"),
    path('studh/',views.studhome, name="student_dashboard"),
    path('upload/',views.upload_file, name="upload_file"),
    path('display/',views.display_file, name="display_file"),
    path('mail/',views.send_email_view, name="send_email"),

    path('s/',views.set_cookie, name="set_cookie"),
    path('g/',views.get_cookie, name="get_cookie"),
    path('d/',views.del_cook, name="del_cook"),

    path('ss/',views.set_sess, name="set_sess"),
    path('gs/',views.get_sess, name="get_sess"),
    path('ds/',views.del_sess, name="del_sess"),




    path('student/create/', StudentCreateView.as_view(), name='student_create'),
    path('student/list/', StudentsListView.as_view(), name='student_list'),
    path('student/detail/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('student/update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),
    path('student/del/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
]