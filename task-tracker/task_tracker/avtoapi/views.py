from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
import django_filters.rest_framework
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination


class PostsViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['post_name']
    ordering_fields = ['post_name']
    filterset_fields = ['post_name']


class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['project_name']
    ordering_fields = ['project_name']
    filterset_fields = ['project_name']


class StatusesViewSet(ModelViewSet):
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']



class ExecutorsPagination(PageNumberPagination):
    page_size = 5
    page_sizer_query_param = 'paginate_by'
    max_page_size = 10


class TasksViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['TaskDesc','ProjectName', 'ExecutorName','StatusName']
    ordering_fields = ['DateStart','DateEnd','StatusName']
    filterset_fields = ['DateStart','DateEnd','StatusName']

    @action(methods=['Delete'], detail=True, url_path='delete') 
    def del_task(self,request, pk=None):
        task=self.queryset.get(id=pk)
        task.delete()
        return Response('Задача была удалена')
    
    @action(methods=['Post'], detail=False, url_path='post') 
    def post_task(self,request, pk=None):
        title=self.queryset.create(TaskDesc=request.data.get('TaskDesc'))
        title.save()
        return Response('Задача была создана')
    
    @action(methods=['GET'], detail=False,url_path='get')
    def get_data(self, request, **kwargs):
        tasks = Tasks.objects.all()
        return Response({'tasks': [task.TaskDesc for task in tasks]})


class ExecutorsViewSet(ModelViewSet):
    queryset = Executors.objects.all()
    serializer_class = ExecutorsSerializer
    pagination_class = ExecutorsPagination
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['executor_name', 'post_name','phone']
    ordering_fields = ['post_name','phone']
    filterset_fields = ['post_name','phone']


class GetTasksView(ListAPIView):
    queryset = Tasks.objects.filter(Q(DateEnd__lte='2022-09-11') | Q(DateStart__lte='2022-08-29'))
    serializer_class = TasksSerializer
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['TaskDesc','ProjectName', 'ExecutorName','StatusName']
    ordering_fields = ['DateStart','DateEnd','StatusName']
    filterset_fields = ['DateStart','DateEnd','StatusName']


class GetExecutorsView(ListAPIView):
    queryset = Executors.objects.order_by('-executor_name')
    serializer_class = ExecutorsSerializer
    pagination_class = ExecutorsPagination
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['executor_name', 'post_name','phone']
    ordering_fields = ['post_name','phone']
    filterset_fields = ['post_name','phone']





