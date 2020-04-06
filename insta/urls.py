"""insta URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from gatekeeper import views as gatekeeper
from insta import settings
from scrapbook import views as scrap
from infoapp import views as info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', gatekeeper.register, name='signup'),
    path('home/', scrap.ScrapListView.as_view(), name='scraplist'),
    path('home/<slug:slug>/', scrap.ScrapDetailView.as_view(), name='scrap-detail'),
    path('home/scrap/create/', scrap.ScrapCreatView.as_view(), name='scrap-create'),
    path('userpost/', scrap.UserScrapListView.as_view(), name='user-post'),
    path('news/',info.index,name = "info"),
    path('stock',info.stockpredic,name = 'stock')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
