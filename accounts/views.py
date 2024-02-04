
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
from .emails import send_otp_via_email

class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)

            if serializer.is_valid():
                user = serializer.save()
                send_otp_via_email(user.email)
                return Response({
                    'status': 200,
                    'message': 'Registration successful. Check your email.',
                    'data': serializer.data,
                })
            else:
                return Response({
                    'status': 400,
                    'message': 'Validation error. Please check the data.',
                    'data': serializer.errors
                })

        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({
                'status': 500,
                'message': f'Internal Server Error: {str(e)}',
                'data': None
            })
