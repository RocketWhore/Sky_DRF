from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# from django_filters.rest_framework import DjangoFilterBackend

# from rest_framework.filters import OrderingFilter

from course.models import Course, Lesson, Payment, Subscription
from course.paginators import LessonPaginator, CoursePaginator
from course.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, SubscriptionSerializer

from rest_framework.permissions import IsAuthenticated, BasePermission, AllowAny

from users.permissions import IsOwnerOrStaff, NotModeratorPermissionsAll, IsUserOrStaff


class IsModerator(BasePermission):
    """
    Проверка на принадлежность пользователя к группе модераторов.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Модераторы').exists()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = [CoursePaginator]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def get_queryset(self):
    if self.request.user.groups.filter(name='moderator').exists():
        return Course.objects.all()

    return Course.objects.filter(user=self.request.user)


def get_permissions(self):
    permission_classes = (IsAuthenticated,)

    if self.action == 'create':
        permission_classes = (IsModerator,)

    elif self.action == 'destroy':
        permission_classes = (IsModerator, IsUserOrStaff)

    elif self.action == 'update' or self.action == 'partial_update':
        permission_classes = (IsModerator | IsUserOrStaff,)

    return [permission() for permission in permission_classes]



class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    # permission_classes = [NotModeratorPermissionsAll]
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff, IsAuthenticated]
    pagination_class = [LessonPaginator]

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff, IsAuthenticated]

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('item', 'lesson_name', 'payment_method')
    ordering_fields = ('date_of_pay',)

class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_subscription = serializer.save()
        new_subscription.user = self.request.user
        new_subscription.is_subscribed = False
        new_subscription.save()


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    permission_classes = [IsUserOrStaff, IsAuthenticated]


class SubscriptionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsUserOrStaff, IsAuthenticated]


class SubscriptionListAPIView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsUserOrStaff, IsAuthenticated]
