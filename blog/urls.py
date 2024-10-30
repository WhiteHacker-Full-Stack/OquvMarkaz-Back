from django.urls import path

from blog.views import RoomListCreate, PupilListCreate, FanListCreate, TeacherListCreate, FanCreate,PupilsCreate

urlpatterns = [
    path('pupilListCreate/', PupilListCreate.as_view()),
    path('fanListCreate/', FanListCreate.as_view()),
    path('roomListCreate/', RoomListCreate.as_view()),
    path('teacherListCreate/',TeacherListCreate.as_view()),

    path('fanCreate/', FanCreate.as_view()),
    path('pupilscreate/', PupilsCreate.as_view())
]