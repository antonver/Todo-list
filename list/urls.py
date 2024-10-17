from django.urls import path

from list.views import TaskListView, TaskUpdateView, TaskDeleteView, TagListView, TagUpdateView, TagDeleteView, \
    TagCreateView, TaskCreateView, change

urlpatterns = [path("", TaskListView.as_view(), name="task-list"),
path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
path("tasks/create", TaskCreateView.as_view(), name="task-create"),
path("tags/", TagListView.as_view(), name="tag-list"),
path("tags/create", TagCreateView.as_view(), name="tag-create"),
path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
path("<int:pk>/change/", change, name="change"),
               ]

app_name = 'list'
