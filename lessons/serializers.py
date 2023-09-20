from rest_framework import serializers
from .models import Progress, Lesson


class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ('id', 'lesson_id', 'time_watched', 'status')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ('id', 'lesson_id', 'time_watched', 'status', 'date_last')


class StatsSerializer(serializers.Serializer):
    product_id = serializers.IntegerField() 
    watched_lesson_count = serializers.IntegerField()
    sum_watched_time = serializers.IntegerField()
    user_count = serializers.IntegerField()
    user_percent = serializers.IntegerField()
