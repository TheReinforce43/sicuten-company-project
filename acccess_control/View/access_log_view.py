from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from acccess_control.Model.accces_log_model import AccessLog
from acccess_control.Serializer.access_log_serializer import AccessLogSerializer




class AccessLogCreateGetAPIView(ListCreateAPIView):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer


class AccessLogDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer

class AccessLogListView(ListAPIView):
    
    serializer_class = AccessLogSerializer


    def get_queryset(self):

        queryset = AccessLog.objects.all()
        card_id = self.request.query_params.get('card_id', None)
        if card_id is not None:
            queryset = queryset.filter(card_id=card_id)
        return queryset
        