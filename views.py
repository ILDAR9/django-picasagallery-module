# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404

from picasagallery.utils import get_albums, get_photos


def gallery(request):
    albums = get_albums()
    return render(request, 'picasagallery/gallery.html', {'albums': albums})


def album_list(request, album_id):
    for album in get_albums():
        if album.gphoto_id.text == album_id:
            photos = get_photos(album)
            return render(request, 'picasagallery/album.html', {'photos': photos, 'album_name':album.title.text})
    raise Http404()