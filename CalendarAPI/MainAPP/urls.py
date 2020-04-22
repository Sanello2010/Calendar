from django.urls import path
from MainAPP.views import EventCreateView, EventListView

urlpatterns = [
   path("create/", EventCreateView.as_view(), name="create_url"),
   path("list/", EventListView.as_view(), name="list_url"),
]