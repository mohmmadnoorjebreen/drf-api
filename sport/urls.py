from django.urls import path
from .views import SportList, SportDetail

urlpatterns = [
    path('', SportList.as_view(), name='Sport_list'),
    path('<int:pk>/', SportDetail.as_view(), name='Sport_detail'),
]