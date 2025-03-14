from django.views.generic import ListView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from custom_user.models import CustomUser


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'project/task_list.html'

    def get_queryset(self):
        user = self.request.user
        if user.user_type in ['staff', 'supplier']:
            return Task.objects.filter(project=user.project)
        return Task.objects.all()