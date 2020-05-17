
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.student_form,name='Student_insert' ),#get nd post insert opartion
    path('<int:id>/',views.student_form,name='Student_update'),#get nd post req. update opration
    path('delete/<int:id>/',views.student_delete,name='student_delete'),
    path('list/',views.student_list,name='student_list') #get req. to the retrive nd display all records
]