from ast import literal_eval

def get_stopwords(in_path):
	with open(in_path, 'r') as f:
		res = literal_eval(f.read())

	return set(res)

def serialise_object(obj):
	res = {
		'paper_id': obj.paper_id,
		'title': obj.title,
		'url': obj.url,
		'author': obj.author,
		'date': obj.date,
		'topic': obj.topic,
		'tags': obj.tags
	}
	return res