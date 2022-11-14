from django.urls import path

from task.views import (
    index,
    TagsListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    complete_task
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/",
         TagsListView.as_view(),
         name="tag-list"),
    path(
        "create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
    path(
        "<int:pk>/",
        complete_task,
        name="complete_task"
    ),
]

app_name = "task"
