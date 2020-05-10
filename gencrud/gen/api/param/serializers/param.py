from rest_framework import serializers
from gen.api.param.serializers.value import ParamValueAllListSerializer
from param.models import Param, ParamValue


class ParamAllListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Param
        fields = ('id', 'title', 'typeof', 'decor', 'values')

    values = serializers.SerializerMethodField(read_only=True)

    def get_values(self, obj):
        param_values = ParamValue.objects.filter(param_id=obj.pk)
        param_value_serializer = ParamValueAllListSerializer(param_values, many=True)
        return param_value_serializer.data
