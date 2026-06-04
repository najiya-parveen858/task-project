from django.contrib import admin
from django.urls import path
from student.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup',signupview.as_view(),name='signup'),
    path('shome',studenthomeview.as_view(),name='shome'),
    path('student_Add',addstudentview.as_view(),name='studentadd'),



    path('edit/<int:id>', editstudentview.as_view(), name='editstud'),
    path('delete/<int:id>', deletestudview.as_view(), name='delstud'),
] 
































    # path('addteach',studentaddview.as_view(),name="addstudent"),
    # path('studentlist',studentlistview.as_view(),name="studlist"),
    # path('delteach/<int:id>',deletestudentview.as_view(),name="delstudent"),
    # path('editteacher/<int:id>',editstudentview.as_view(),name="editstudent"),
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

   
