from django.urls import path
from course.apps import CourseConfig
from rest_framework.routers import DefaultRouter
from course.views import (CourseViewSet,
                          LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView,
                          LessonDestroyAPIView,
                          PaymentListAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView,
                          SubscriptionRetrieveAPIView, SubscriptionListAPIView)

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [

      path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
      path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
      path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
      path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
      path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delet'),
      path("payment/", PaymentListAPIView.as_view(), name="PAY"),
      path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription-create'),
      path('subscription/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(),
           name='subscription-delete'),
      path('subscription/<int:pk>/', SubscriptionRetrieveAPIView.as_view(),
           name='subscription-get'),
      path('subscription/', SubscriptionListAPIView.as_view(),
           name='subscription-list'),

  ] + router.urls
