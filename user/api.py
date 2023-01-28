from django.http import JsonResponse
from .models import Test, User
from .serializers import TestSerializer, UserSerializer


def test_list(request):
    test = Test.objects.all()
    serializer = TestSerializer(test, many=True)
    return JsonResponse({'test':serializer.data})


def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse({'users':serializer.data})
