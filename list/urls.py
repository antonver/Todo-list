from django.urls import path

from list.views import TaskListView, TaskUpdateView, TaskDeleteView, TagListView, TagUpdateView, TagDeleteView

urlpatterns = [path("", TaskListView.as_view(), name="task-list"),
path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
path("tags/", TagListView.as_view(), name="tag-list"),
path("<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
path("<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
               ]
