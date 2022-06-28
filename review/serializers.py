from rest_framework import serializers
from .models import Review, Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        try:
            review = Review.objects.create(**validated_data)
        except ValueError:
            raise serializers.ValidationError('Вы не авторизованы')
        return review

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['like'] = instance.like.filter(like=True).count()
        rep['product'] = str(instance)
        return rep
