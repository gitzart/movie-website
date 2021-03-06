class Movie:
    '''Movie template for individual movies'''
    
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def __str__(self):
        return '%s' % self.title
