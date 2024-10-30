from rest_framework import serializers
from .models import Room, Pupil, Fan, Teacher


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('name',)

class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = ('name','surname', 'fatherName','password', 'fani','birth')

class FanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fan
        fields = ('name', 'teacher', 'room', 'lesson_time','juftmi',  'price')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('name', 'surname', 'pupilNumber','oyligi', 'foiz')




