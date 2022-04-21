from rest_framework import viewsets, mixins
from .models import User
from .serializers import UserSerializer
import codecs
import smtplib
import os
import dotenv
from rest_framework import status
from rest_framework.response import Response


class UserCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = [UserSerializer]

    class Mailer:
        def __init__(self, from_email, from_password, to_email):
            self.from_email = from_email
            self.from_password = from_password
            self.to_email = to_email
            subject = 'Welcome to the Wall App'
            message = 'Thank you for registering to the Wall App, now you can add a post it to the wall, and alter the ones already on it!'
            self.body = f"Subject:{subject}\n\n{message}".encode('utf-8')

        def send_email(self, email):
            with smtplib.SMTP(
                "smtp-mail.outlook.com", 587
            ) as server:
                server.ehlo()
                server.starttls()
                server.login(self.from_email, self.from_password)
                try:
                    server.sendmail(self.from_email, email, self.body)
                except (smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused):
                    raise ValueError

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            dotenv.load_dotenv()
            from_email = os.getenv("EMAIL_HOST_USER")
            from_password = os.getenv("EMAIL_HOST_PASSWORD")
            to_email = request.data['email']
            mailer = self.Mailer(from_email, from_password, to_email)
            mailer.send_email(to_email)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
