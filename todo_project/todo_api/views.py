from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_extensions.mixins import NestedViewSetMixin
from .models import Todos, Tasks
from .serializers import (TodosSerializer, TasksSerializer)


class TodosView(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

    def update(self, request, category_pk=None, *args, **kwargs):

        ids = get_object_or_404(Todos.objects, id=kwargs['pk'])
        field_names = ["id", "title", "color"]
        for attribute in field_names:
            if attribute not in request.data.keys():
                request.data[attribute] = getattr(ids, attribute)

        return super(TodosView, self).update(request, *args, **kwargs)


class TasksView(NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

    def create(self, request, *args, **kwargs):
        todos_id = kwargs['parent_lookup_todos']
        new_data = request.data.copy()
        new_data['todos'] = todos_id
        serializer = self.get_serializer(data=new_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, category_pk=None, *args, **kwargs):

        ids = get_object_or_404(Tasks.objects, id=kwargs['pk'])
        field_names = ["id", "task", "color", "completed"]
        for attribute in field_names:
            if attribute not in request.data.keys():
                request.data[attribute] = getattr(ids, attribute)
        request.data['todos'] = kwargs['parent_lookup_todos']

        return super(TasksView, self).update(request, *args, **kwargs)
