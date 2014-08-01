from django.shortcuts 				import render
from .models 						import Artist
from django.views.generic.detail 	import DetailView
from django.views.generic 			import ListView
from rest_framework 				import viewsets
from .serializers 					import ArtistSerializer

# Create your views here.
class ArtistDetailView(DetailView):
	model = Artist
	context_object_name = 'fav_artist'
	template_name = 'artist.html'

class ArtistListView(ListView):
	model = Artist
	context_object_name = 'artists'
	template_name = 'artist.html'



class ArtistViewSet(viewsets.ModelViewSet):
	model = Artist
	serializer_class = ArtistSerializer