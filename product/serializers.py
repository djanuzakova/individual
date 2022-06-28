from rest_framework import serializers
from .models import Product, ProductImage
from ..review.serializers import ReviewSerializer


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            requests = self.context.get("requests")
            if requests is not None:
                url = requests.build_absolute_uri(url)
        else:
            url = ""
        return url

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = self._get_image_url(instance)
        return rep


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = ProductImageSerializer(ProductImage.objects.filter(product=instance.id), many=True).data
        rep['review'] = ReviewSerializer(instance.review.filter(product=instance.id), many=True).data
        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) != 0:
            rep["total_rating"] = sum(total_rating)/len(total_rating)
        else:
            rep['total_rating'] = ""
        return rep




