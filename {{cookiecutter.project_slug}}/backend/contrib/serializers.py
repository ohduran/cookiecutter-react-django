from rest_framework import serializers


class CharCountSerializer(serializers.Serializer):
    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return obj.count
