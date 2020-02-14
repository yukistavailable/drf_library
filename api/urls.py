from django.urls import path, include
from .views import BookAPIView, BookAPIViewSet, FortuneView, FortuneGETView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('books', BookAPIViewSet)

urlpatterns = [
    path('', BookAPIView.as_view()),
    path('', include(router.urls)),
    path('fortune', FortuneView.as_view()),
    path('fortuneget<pk>', FortuneGETView.as_view()),
    
]