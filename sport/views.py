from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Sport
from .serializers import SportSerializer
# Create your views here.


class SportList(ListCreateAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

class SportDetail(RetrieveUpdateDestroyAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer