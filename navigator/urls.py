from django.urls import include, path
from rest_framework import serializers, viewsets, routers

from . import views
from .models import Item

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['update_date', 'content']

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
