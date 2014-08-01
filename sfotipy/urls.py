from django.conf.urls   import patterns, include, url
from django.conf        import settings
from django.contrib     import admin
from artists.views      import ArtistDetailView, ArtistListView, ArtistViewSet
from albums.views       import AlbumViewSet
from tracks.views       import TrackViewSet
from rest_framework     import routers
admin.autodiscover()

router      = routers.DefaultRouter()
router.register(r'artists',ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'tracks', TrackViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfotipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracks/(?P<title>[\w\-\w]+)/', 'tracks.views.track_view', name='track_view'),
    url(r'^signup/','userprofiles.views.signup', name='signup'),
    url(r'^signin/','userprofiles.views.signin', name='signin'),
    url(r'^artists/(?P<pk>[\d]+)', ArtistDetailView.as_view()),
    url(r'^artists/', ArtistListView.as_view()),
    url(r'^api/', include(router.urls)),

)

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
	)