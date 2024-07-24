from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list_app.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list_app:tag-list")
    template_name = "todo_list_app/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list_app:tag-list")
    template_name = "todo_list_app/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list_app:tag-list")
    template_name = "todo_list_app/tag_confirm_delete.html"