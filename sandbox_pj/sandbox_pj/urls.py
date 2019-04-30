from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # admin関連
    url(r'^admin/', admin.site.urls),

    # basic_practice_1のルート
    url(r'^basic_practice_1/', include('basic_practice_1.urls')),
    url(r'^', include('basic_practice_1.urls', namespace='basic_practice_1')),
]
