from django.conf.urls import url

from .views import ExportView

urlpatterns = [
    url(r'^export_csv/$', ExportView.as_view()),
]
