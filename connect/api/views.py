from rest_framework.generics import CreateAPIView
from connect.api.serializers import LNMOnlineSerializer
from connect.models import LNMOnline




class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer


    def create(self, request):
        print(request.data, name="this is request.data")
