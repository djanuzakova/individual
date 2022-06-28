from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from applications.review.models import Review, Like
from applications.review.permissions import IsReviewAuthor
from .serializers import ReviewSerializer
from rest_framework.response import Response


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = IsReviewAuthor

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.action == 'like':
            permissions = [IsAuthenticated, ]
        elif self.action == 'create':
            permissions = [IsReviewAuthor, ]
        else:
            permissions = [IsReviewAuthor, ]
        return [permission() for permission in permissions]

    @action(detail=True, methods=['Post'])
    def like(self, request, *args, **kwargs):
        review = self.get_object()
        like_obj, _ = Like.objects.get_or_create(review=review, user=request.user)
        like_obj.like = not like_obj.like
        like_obj.save()
        status = 'like'
        if not like_obj.like:
            status = 'unlike'
        return Response({'status': status})


