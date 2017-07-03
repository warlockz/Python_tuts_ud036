import webbrowser

class VideoParent():
	def __init__(self,title):
		self.title = title
		#self.duration = duration

class Movie(VideoParent):
	"""docstring for Movie Class"""
	def __init__(self,title,storyline,poster_image_url,trailer_youtube_url):
		#self.title = title
		VideoParent.__init__(self,title)
		self.storyline = storyline
		#storyline = storyline  (It will not create as an class variable just random local variable to fn)
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer():
		webbrowser.open(self.trailer_youtube_url)

class TVShow(VideoParent):
	"""docstring for TVshow"""
	def __init__(self,title):
		VideoParent.__init__(self,title)
		