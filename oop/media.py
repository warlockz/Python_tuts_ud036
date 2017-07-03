import webbrowser

class Movie:
	def __init__(self,title,storyline,poster_image_url,trailer_youtube_url):
		self.title = title
		self.storyline = storyline
		#storyline = storyline  (It will not create as an class variable just random local variable to fn)
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer():
		webbrowser.open(self.trailer_youtube_url)