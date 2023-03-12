from rest_framework import serializers
from .models import *

class PostsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Posts
        fields = ['url', 'post_name']


class ProjectsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Projects
        fields = ['url','project_name']


class StatusesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statuses
        fields = '__all__'


class TasksSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tasks
        fields = ['url', 'TaskDesc', 'DateStart','DateEnd','ProjectName', 'ExecutorName','StatusName']


class ExecutorsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Executors
        fields = ['url', 'executor_name', 'post_name','phone']
