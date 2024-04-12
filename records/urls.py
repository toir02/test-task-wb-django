from django.urls import path

from records.apps import RecordsConfig
from records.views import RecordCreateAPIView

app_name = RecordsConfig.name

urlpatterns = [
    path('record/', RecordCreateAPIView.as_view(), name="create-record"),
]
