
class UrlManager(object):
	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()


	def add_new_url(self, url):
		if url is None:
			return None
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)

	def get_new_url(self):
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url

	def has_new_url(self):
		return len(self.new_urls) != 0
		