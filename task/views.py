from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task.models import Task, Tag


def index(request):
    task_list = Task.objects.all()
    tag_list = Tag.objects.all()

    context = {
        "task_list": task_list,
        "tag_list": tag_list
    }

    return render(request, "task/index.html", context=context)


class TagsListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    queryset = Tag.objects.order_by("name")


class TagCreateView(generic.CreateView):
    model = Tag
    success_url = reverse_lazy("task:tag-list")
    fields = "__all__"


class TagUpdateView(generic.UpdateView):
    model = Tag
    success_url = reverse_lazy("task:tag-list")
    fields = "__all__"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("task:index")
    fields = "__all__"
    template_name = "task/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:index")
    fields = "__all__"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:index")


def complete_task(request, pk: int):
    task = Task.objects.get(pk=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse_lazy("task:index"))

