from django.contrib import admin
from django.urls import path
from laundry.views import (
    WasherView,
    DryerView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('washer/<int:washer_id>', WasherView.as_view(), name='washer'),
    path('dryer/<int:dryer_id>', DryerView.as_view(), name='dryer')
]
