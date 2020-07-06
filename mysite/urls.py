"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import subscribe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', subscribe, name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('events/', include('events.urls'), name='events'),
    path('groups/', include('groups.urls'), name='groups'),
    path('notifications/', include('actions.urls')),
    path('userprofile/', include('userprofile.urls'), name='userprofile'),
    # path('comments/', include('comments.urls')),

    path('api/', include([
        # path('swagger', schema_view.with_ui('swagger', cache_timeout=0)),
        path('', include('groups.api.urls')),
    ])),

]
