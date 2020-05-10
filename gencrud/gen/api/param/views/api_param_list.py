from rest_framework import generics
from gen.api.param.serializers import ParamAllListSerializer
from param.models import Param


class ParamAllListAPIView(generics.ListAPIView):
    queryset = Param.objects.all()
    serializer_class = ParamAllListSerializer



