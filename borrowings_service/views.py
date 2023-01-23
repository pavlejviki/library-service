from django.shortcuts import render

# class MovieViewSet(
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     viewsets.GenericViewSet,
# ):
#     queryset = Movie.objects.all().prefetch_related("genres", "actors")
#     serializer_class = MovieSerializer
#     permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)