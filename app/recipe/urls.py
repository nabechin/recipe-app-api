from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views


app_name = 'recipe'
router = DefaultRouter()
router.register('tag', views.TagViewSet)
router.register('ingredient', views.IngredientViewSet)

urlpatterns = [
    path('', include(router.urls))
]
