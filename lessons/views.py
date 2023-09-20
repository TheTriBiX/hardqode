from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from .models import Lesson, Product, Progress
from .serializers import ProgressSerializer, LessonSerializer, StatsSerializer
from django.db.models import Count, Sum


# Create your views here.


class ProgressAPIView(APIView):
    def get(self, request, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            user = request.user.id
            lesson = Lesson.objects.filter(product=pk).values('id')
            query = Progress.objects.filter(user=user, lesson__in=lesson)

            return Response({'data': LessonSerializer(query, many=True).data})

        else:
            user = request.user.id
            query = Progress.objects.filter(user=user)
            return Response({'data': ProgressSerializer(query, many=True).data})


class StatsAPIView(APIView):
    def get(self, request):
        all_products = Product.objects.all().values('id')
        User = get_user_model()
        users = len(list(User.objects.all()))
        data = []
        for product in all_products:
            lessons = Lesson.objects.filter(product=product['id']).values('id')
            count = len(list(Progress.objects.filter(status='Просмотрено', lesson__in=lessons)))
            sum_watch_query = Progress.objects.filter(lesson__in=lessons).values('time_watched')
            sum_watch = 0
            for query in sum_watch_query:
                sum_watch += query['time_watched']
            user_count = Product.objects.all().annotate(user_count=Count('users'))[0].user_count
            user_percent = user_count / users * 100
            data.append({'product_id': product['id'],
                         'watched_lesson_count': count,
                         'sum_watched_time': sum_watch,
                         'user_count': user_count,
                         'user_percent': user_percent
                         })
        return Response({'data': StatsSerializer(data, many=True).data})
