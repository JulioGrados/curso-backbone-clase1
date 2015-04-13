from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from rest_framework_nested import routers

from apps.main.viewsets import NoticeViewSet, CommentViewSet
from apps.main.views import IndexView


router = routers.SimpleRouter()
router.register(r'noticias', NoticeViewSet)

comments_router = routers.NestedSimpleRouter(router, r'noticias', lookup="noticia")
comments_router.register(r'comentarios', CommentViewSet)


urlpatterns = [
	
	url(r'^$', IndexView.as_view()),
	url(r'^api/', include(router.urls)),
	url(r'^api/', include(comments_router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
            {'document_root':settings.MEDIA_ROOT,}
        ),
]
