from rest_framework import serializers
from course.models import Course, Lesson, Payment, Subscription
from course.services import get_payment
from users.validators import VideoValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

    validators = [VideoValidator(field='description'),
                  serializers.UniqueTogetherValidator(fields=['title', 'description'], queryset=Lesson.objects.all())]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        return obj.subscription_set.filter(user=user).exists()

    def get_lesson_count(self, obj):
        return obj.title.count('10')

    class Meta:
        model = Course
        fields = '__all__'

    def get_payment_url(self, obj):
        price = obj.course.price
        title = obj.course.title
        pk = obj.course.pk
        url = get_payment(price, title, pk)
        return url


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    payment_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Subscription
        fields = '__all__'



    def get_payment_url(self, obj):
        price = obj.course.price
        title = obj.course.title
        pk = obj.course.pk
        url = get_payment(price, title, pk)
        return url


