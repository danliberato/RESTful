from django.contrib import admin
from django.urls import path
import core.views
from django.conf.urls import include

admin.site.site_header = 'Admin - RESTful'
admin.site.site_title = "RESTful"
admin.site.index_title = "Gerenciador RESTful"

urlpatterns = [
    path('admin', admin.site.urls),
    path('user/<str:document>', core.views.UserView.as_view())
]