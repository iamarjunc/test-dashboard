from django.urls import path
from . import views
urlpatterns = [
    path('',views.login, name='login'),
    path('template1/',views.index1),
    path('template2/',views.index2),
    path('json2/',views.json2),
    path('process_branch/', views.process_branch, name='process_branch'),
]
