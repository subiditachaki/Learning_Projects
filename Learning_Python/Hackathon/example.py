from .read_inshorts_new import ReadNews

news_source = ReadNews(url) 
def get_api(request):
	body = request.body
	news_source.play_news()
	return response({'message': 'ok'})


def pause_api(request):
	news_source.pause()
	return response()
	