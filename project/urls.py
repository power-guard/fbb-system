from django.urls import path
from .views import TaskListView

urlpatterns = [
    path('task_list/', TaskListView.as_view(), name='task_list'),
]