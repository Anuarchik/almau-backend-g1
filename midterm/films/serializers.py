from rest_framework import serializers
from films.models import Film


class FilmSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(min_length=5, max_length=200, allow_null=False)
    description = serializers.CharField(min_length=5, max_length=200, allow_null=False)
    duration = serializers.IntegerField(allow_null=False)

    def create(self, validated_data):
        films = Film(**validated_data)
        films.save()
        return films

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
