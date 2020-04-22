from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework.generics import CreateAPIView, ListAPIView

from MainAPP.serializer import EventSerializerGET, EventSerializerPOST
from MainAPP.models import Event


class EventCreateView(CreateAPIView):
    serializer_class = EventSerializerPOST


class EventListView(ListAPIView):
    serializer_class = EventSerializerGET
    queryset = Event.objects.all()

