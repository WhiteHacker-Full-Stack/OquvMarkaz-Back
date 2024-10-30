from types import SimpleNamespace
import json
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from .models import Room,Pupil,Fan,Teacher
from rest_framework import generics
from django.db.models import Q
from datetime import date,datetime

from .serializers import RoomSerializer, PupilSerializer, FanSerializer,TeacherSerializer


# Create your views here.

# 👉-------------------List Create view --------------------------------👈

class PupilListCreate(generics.ListCreateAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer

class FanListCreate(generics.ListCreateAPIView):
    queryset = Fan.objects.all()
    serializer_class = FanSerializer

class TeacherListCreate(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class RoomListCreate(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

# 👉-------------------List Create view end --------------------------------👈

# 👉------------------------------Create View --------------------------------👈

class FanCreate(generics.CreateAPIView):
    serializer_class = FanSerializer
    def post(self, request):
        fan = Fan.objects.all()
        data = request.data
        juftmi = data.get('juftmi')
        room =data.get('room')
        lesson_time1 = data.get('lesson_time')
        lessons_time = fan.filter(Q(room__exact = room) & Q( juftmi__exact = juftmi) & Q( lesson_time__exact = lesson_time1))
        print(lessons_time, "hoooooooooooooooooooooo")
        if lessons_time:
            return HttpResponse("Fan already exists in this room and time")
        else:
            serializer = FanSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse("ok")


class PupilsCreate(generics.CreateAPIView):
    serializer_class = PupilSerializer
    def post(self, request):
        pupils = Pupil.objects.all()
        data = request.data
        password = data['password']
        # fani = data['fani']
        checkPassword = pupils.filter(password__exact = password)

        # today = date
        birth_date_str = data['birth']
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        difference = today - birth_date
        years = difference.days // 365

        print(years)
        if len(checkPassword)>0 or  years<15:
            if len(checkPassword)>0 and  years<15:
                return HttpResponse("parol 15 yoshdan kichik bo'lishi mumkin emas va oldin kiritilmagan parolni kiriting")
            if len(checkPassword) > 0:
                return HttpResponse("parol oldin kiritilgan  boshqa parol kiriting")
            if years < 15 :
                return HttpResponse("o'qituvchi 15 yoshdan kichik bo'lishi mumkin emas")
        else :
            serializer = PupilSerializer(data=data)
            if serializer.is_valid():
                serializer = serializer.save()
                narxi = serializer.fani.price
                print("narxi -> ", narxi)
                teacher = serializer.fani.teacher
                print("teacher -> ", teacher)
                teacher.pupilNumber += 1
                teacher.oyligi = (teacher.pupilNumber * narxi) * teacher.foiz/100
                teacher.save()
                return HttpResponse("ok")

            else:
                return HttpResponse("error")









# 👉------------------------------Create View  end--------------------------------👈


# ��-------------------Retrieve Update Delete view --------------------------------��





