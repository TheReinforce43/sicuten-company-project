from django.urls import path 


from acccess_control.View.access_log_view import  (
    AccessLogCreateGetAPIView, AccessLogDetailUpdateDeleteAPIView

)

urlpatterns = [
    path('access_logs/', AccessLogCreateGetAPIView.as_view(), name='access_log'),
    path('access_logs/<int:pk>/', AccessLogDetailUpdateDeleteAPIView.as_view(), name='access_log_details'),
]
