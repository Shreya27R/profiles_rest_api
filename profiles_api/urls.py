from django.urls import path,include
from rest_framework.routers import DefaultRouter
#for viewset
from profiles_api import views



router = DefaultRouter()
router.register("hello-viewset",views.HelloViewSet,base_name='hello-viewset')
#register view set
router.register('profile',views.UserProfileViewSet)



urlpatterns=[
   path('hello-view/',views.HelloApiView.as_view()),
   path('',include(router.urls))
]
