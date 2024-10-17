from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, UpdateView, DeleteView

from list.models import Task


# Create your views here.

class TaskListView(ListView):
    model = Task


class TaskUpdateView(UpdateView):
    model = Task
    success_url = reverse("list:task_list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "list/task_confirm_delete.html"
    success_url = reverse("list:task_list")


class TagListView(ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "list/task_list.html"


class TagUpdateView(UpdateView):
    model = Task
    success_url = reverse("list:tag_list")


class TagDeleteView(DeleteView):
    model = Task
    success_url = reverse("list:tag_list")
