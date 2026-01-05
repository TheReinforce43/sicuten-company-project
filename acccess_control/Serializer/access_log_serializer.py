from rest_framework import serializers 
from acccess_control.Model.accces_log_model import AccessLog 



class AccessLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessLog
        fields = "__all__"