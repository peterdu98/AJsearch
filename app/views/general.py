from flask import render_template, request, url_for, jsonify, session
from app import model, stopwords, const_store, temp_store
from app.search import search_papers
from app.models import Paper
from app.views import mod
import math
import sys


@mod.route('/', methods=['GET', 'POST'])
def index():
	topics = const_store['topics']

	# Get query params
	page = request.args.get('page', 1, type=int)	

	# Filter papers
	if session.get('topic', None) is not None:
		topic = session['topic']
		data = Paper.query.filter_by(topic=topic)
	else:
		data = Paper.query

	# Order and Paginate papers
	data = data.order_by(
			Paper.paper_id.desc()
		).paginate(page, 5, False)

	prev_page = data.prev_num
	next_page = data.next_num

	return render_template(
		'general/index.html',
		data = data.items,
		topics = topics,
		prev_page = prev_page,
		next_page = next_page
	)

@mod.route('/select/<topic>/<page>')
def select(topic, page):
	data = Paper.query.filter_by(topic=topic).order_by(
			Paper.paper_id.desc()
		).paginate(int(page), 5, False).items

	# Add data into session
	session['topic'] = topic

	# Serialisation
	res = []
	for entry in data:
		res.append({
			'paper_id': entry.paper_id,
			'title': entry.title,
			'url': entry.url,
			'author': entry.author,
			'date': entry.date,
			'topic': entry.topic,
			'tags': entry.tags
		})

	return jsonify(json_list=res)

@mod.route('/search/', methods=['GET', 'POST'])
def search():
	global temp_store
	topics = const_store['topics']

	# Get topic
	query = request.form.get('query')
	topic = request.form.get('topic', None)
	page = request.args.get('page', 1, type=int)

	if query is not None:
		# If there no selected topic
		if topic is not None:
			data = Paper.query.filter_by(topic=topic).all()
		else: # Otherwise
			data = Paper.query.all()

		# Preprocess query and fetch results
		query = query.lower()
		query = ' '.join([word for word in query.split() if word not in stopwords])

		if query != '':
			temp_store = search_papers(model, query, data)

	num_pages = math.ceil(len(temp_store) / 5)
	if page == num_pages:
		prev_page = page - 1 
		next_page = None
	elif page == 1:
		prev_page = None

		if len(temp_store) == 0:
			next_page = None
		else:
			next_page = page + 1
	else:	
		prev_page = page - 1 
		next_page = page + 1

	start = (page * 5) - 5
	end = page * 5 + 1

	return render_template(
		'general/index.html',
		data = temp_store[start:end:],
		topics = topics,
		prev_page = prev_page,
		next_page = next_page
	)