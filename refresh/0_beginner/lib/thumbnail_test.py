from .thumbnail import ThumbnailMakerService, IMG_URLS




def test_thumbnail_maker():
    tn_maker = ThumbnailMakerService()
    tn_maker.make_thumbnails(IMG_URLS)
