from .forms import SignupForm
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    status = 'success'

    form = SignupForm({
        'first_name': data.get('first_name'), 'last_name': data.get('last_name'),
        'email': data.get('email'), 'username': data.get('username'),
        'password1': data.get('password1'), 'password2': data.get('password2'),
    })

    if form.is_valid():
        form.save()
    else:
        status = 'error'

    return JsonResponse({'data': status}, safe=False)
