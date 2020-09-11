
from app import utils

def search_papers(model, query, data, alpha=0.85, n_tags=10):
	''' This function searches papers based on the similarity between the query
	and each paper's tags.

	Paramaeters
	-----------
	model: A pre-trained model
	query: A searched query
	data: A list of papers
	alpha: A threshold for the similarity score
	n_tags: A number of tags that are used to select tags for each paper

	Return
	------
	A list of paper ids from the highest similar score to the lowest similar score (above alpha)
	'''
	res = []

	words = query.split()
	for entry in data:
		score = model.n_similarity(words, entry.tags[:n_tags:])
		if score >= alpha:
			res.append((entry, score))

	res = [utils.serialise_object(entry[0]) for entry in sorted(res, key=lambda x: x[1], reverse=True)]

	return res
