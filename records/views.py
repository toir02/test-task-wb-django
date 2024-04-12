from rest_framework import (
    generics,
    status
)
from rest_framework.response import Response

from records.models import Record
from records.serializers import RecordSerializer


class RecordCreateAPIView(generics.CreateAPIView):
    serializer_class = RecordSerializer

    def post(self, request, *args, **kwargs):
        data = self.request.data.get("data")
        if not data:
            return Response(
                data={
                    "error": "data field is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        instance = Record.objects.create(
            data=data
        )

        serializer = self.serializer_class(instance)
        return Response(serializer.data)
