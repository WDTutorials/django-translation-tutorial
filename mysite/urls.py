"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path, reverse
from blog.models import Post
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from django.views.generic import TemplateView
from django.conf.urls.static import static
from mysite import settings
from django.conf.urls.i18n import i18n_patterns 
from django.utils.translation import gettext_lazy as _ 

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['about']

    def location(self, item):
        return reverse(item)

sitemaps = {
    'blog': GenericSitemap({
        'queryset': Post.objects.all(),
        'date_field': 'modified',
    }),
    'static': StaticViewSitemap,
}

urlpatterns = i18n_patterns(
    path('blog/', include('blog.urls')),
    # path('admin/', admin.site.urls),
    path(_('admin/'), admin.site.urls), # here
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('sitemap.xml', sitemap,
         {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    prefix_default_language=False
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


