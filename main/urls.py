from django.urls import include, path
from rest_framework.routers import DefaultRouter

from main.views import LikesView, AddStarRatingView, SavedView

router = DefaultRouter()
router.register('like', LikesView)
router.register('rating', AddStarRatingView)
urlpatterns = [
    path('saved-list/', SavedView.as_view()),
    path('', include(router.urls)),
]