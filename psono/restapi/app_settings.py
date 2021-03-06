from django.conf import settings

from importlib import import_module

from .serializers import (
    UploadSerializer as DefaultUploadSerializer,
    DownloadSerializer as DefaultDownloadSerializer,
)

def import_callable(path_or_callable):
    if hasattr(path_or_callable, '__call__'):
        return path_or_callable
    else:
        package, attr = path_or_callable.rsplit('.', 1)
        return getattr(import_module(package), attr)

serializers = getattr(settings, 'RESTAPI_SERIALIZERS', {})

UploadSerializer = import_callable(
    serializers.get('UPLOAD_SERIALIZER', DefaultUploadSerializer)
)
DownloadSerializer = import_callable(
    serializers.get('DOWNLOAD_SERIALIZER', DefaultDownloadSerializer)
)


