from django.http import HttpResponse, Http404
#from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

'''
def index(request):
	all_album = Album.objects.all()
	html=''
	for album in all_album:
		url = '/music/'+ str(album.id) + '/'
		html += '<a href="'+ url + '">'+ album.album_title+'</a><br>'
	return HttpResponse(html)

def index(request):
	all_album = Album.objects.all()
	template = loader.get_template('music/index.html')
	context = {
		'all_album' : all_album,
	}
	return HttpResponse(template.render(context,request))
'''
def index(request):
	all_album = Album.objects.all()
	return render(request, 'music/index.html',{ 'all_album' : all_album})

def detail(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'music/detail.html',{'album':album})

def favorite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song=album.song_set.get(pk=request.POST['song'])
	except(KeyError, Song.DoesNotExist):
		return render(request, 'music/detail.html',{	'album':album,
			'error_message':"You did not select a valid song"
		})
	else:
		selected_song.is_favorite = True
		selected_song.save()
		return render(request,'music/detail.html',{'album':album})
'''return HttpResponse('<h2>Album id is ' + str(album_id) +'</h2>') 
 try:
		album = Album.objects.get(pk=album_id)
	except Album.DoesNotExist:
		raise Http404("Album does not exist")'''
	