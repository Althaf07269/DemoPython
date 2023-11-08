from django.urls import path
from . import views
app_name='todoapp'
urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id1>/', views.update, name='update'),
    path('cbvhome/',views.tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.taskdetailview.as_view(),name='cbvdetail'),
    path('cupdate/<int:pk>/',views.taskupdateview.as_view(),name='cupdate'),
    path('cdelete/<int:pk>/',views.taskdeleteview.as_view(),name='cdelete'),
]