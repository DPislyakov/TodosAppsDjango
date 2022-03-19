from rest_framework import serializers
from .models import Todos, Tasks


class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = Todos
        fields = ('id', 'title', 'color', 'tasks_ids',)
        read_only_fields = ('id', 'tasks_ids',)

    def update(self, instance, validated_data):
        list_data = {}
        for key, val in self.get_fields().items():
            if isinstance(val, serializers.ListSerializer) and not val.read_only:
                list_data[key] = validated_data.pop(key, [])
        instance = super().update(instance, validated_data)
        for key, data in list_data.items():
            serializer = self.get_fields()[key]
            serializer.set_parent_data(data, instance)
            serializer.update(getattr(instance, key).all(), data)
        return instance


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = Tasks
        fields = ('id', 'todos', 'task', 'color', 'completed')
        read_only_fields = ('id',)
