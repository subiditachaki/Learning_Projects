import os
import urllib2
from HTMLParser import HTMLParser
import time

class ReadNews:
	def __init__(self, url):
		news_url =  urllib2.urlopen(url) 
		self.page_source = news_url.read()
		# self.new_series = []
		self.news_read_count = 0

	def play_news(self):
		page = self.page_source
		start_news = 0
		while(start_news != -1):
			start_news = page.find('<div itemprop="articleBody">')
			end_news = page.find('</div>', start_news)
			news = page[start_news+28:end_news]
			news_text = self.parse_news(news)
			# time.sleep(2)
			os.system("say %s" %("news" + str(self.news_read_count + 1)))
			os.system("say %s" %(news_text))
			page = page[end_news+1:]
			self.news_read_count +=1

	def parse_news(self, news):
		u_news = news.decode("utf-8")
		ascii_news=u_news.encode("ascii","ignore")

		parser = HTMLParser() #Initializes parser
		parsed_news_text = parser.unescape(ascii_news) #Parses HTML Numeric characters
		quote_removed_news_text = parsed_news_text.replace('"', '').replace("'", '') #Removes single and double quotes
		return(quote_removed_news_text)

	
	# def pause_news(self):

	# def revind_news(self):

	# def forward_news(self):

	def stop_news(self):
		self.new_series = []
		self.news_read_count = 0

if __name__=='__main__':
	news_source = ReadNews("https://www.inshorts.com/en/read")
	news_source.play_news()

