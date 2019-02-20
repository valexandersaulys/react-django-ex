from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (   # specify the fields we care to expose
            'id',
            'title',
            'description'
        )
