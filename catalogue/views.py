from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from catalogue.forms import TagForm, TaskForm
from catalogue.models import Task, Tag


# Create your views here.


class TaskListView(ListView):
    model = Task

    def get_queryset(self):
        return Task.objects.order_by("is_completed", "-date")


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "catalogue/task_form.html"
    success_url = reverse_lazy("catalogue:task-catalogue")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "catalogue/task_form.html"
    success_url = reverse_lazy("catalogue:task-catalogue")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "catalogue/task_confirm_delete.html"
    success_url = reverse_lazy("catalogue:task-catalogue")


class TagListView(ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "catalogue/tag_list.html"


class TagCreateView(CreateView):
    template_name = "catalogue/tag_form.html"
    model = Tag
    success_url = reverse_lazy("catalogue:tag-catalogue")
    form_class = TagForm


class TagUpdateView(UpdateView):
    model = Tag
    template_name = "catalogue/tag_form.html"
    success_url = reverse_lazy("catalogue:tag-catalogue")
    form_class = TagForm


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "catalogue/tag_confirm_delete.html"
    success_url = reverse_lazy("catalogue:tag-catalogue")


def change(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("catalogue:task-catalogue")
