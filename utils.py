# -*- coding: utf-8 -*-
from gdata.photos.service import PhotosService
from ftsrt import settings


def get_albums():
    pws = PhotosService()
    uf = pws.GetUserFeed(user=settings.PICASAGALLERY_USER)
    feed = '{uri}&thumbsize={thumbsize}'.format(
        uri=uf.GetAlbumsUri(), thumbsize=settings.PICASAGALLERY_ALBUM_THUMBSIZE
    )
    print feed
    return pws.GetFeed(feed).entry


def get_photos(album):
    feed = '{uri}&imgmax={imgmax}&thumbsize={thumbsize}'.format(
        uri=album.GetPhotosUri(), imgmax=settings.PICASAGALLERY_PHOTO_IMGMAXSIZE,
        thumbsize=settings.PICASAGALLERY_PHOTO_THUMBSIZE
    )
    return PhotosService().GetFeed(feed).entry
