from django.contrib import admin
from django.urls import path
from .viewsFolder.employeeviews import *
from .viewsFolder.deviceviews import *
from .viewsFolder.deviceReportViews import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='Employee-list'),
    path('employees/<int:ps_no>',EmployeeDetail.as_view(),name='employee detail list'),
    path('devices/', DeviceList.as_view(), name='Device-list'),
    path('devices/<int:AssetNo>',DeviceDetail.as_view(),name='Device detail list'),
    path('devicereport/view/',DeviceReportList.as_view(),name='Device report detail list'),
    path('devicereport/borrowdevice/',BorrowOrReturn.as_view(),name='Device report detail list'),
    path('devicereport/returndevice/',BorrowOrReturn.as_view(),name='Deivce report detail list'),
    path('devicereport/checkin/', DeviceReturn.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('try2/',try2)
]
