from rest_framework import serializers
from param.models import ParamValue


class ParamValueAllListSerializer(serializers.ModelSerializer):
    val = serializers.SerializerMethodField()

    class Meta:
        model = ParamValue
        fields = ('id', 'val')

    def get_val(self, obj):
        if obj.int_value is not None:
            return obj.int_value
        elif obj.bool_value is not None:
            return obj.bool_value
        elif obj.decimal_value:
            return obj.decimal_value
        return obj.str_value


