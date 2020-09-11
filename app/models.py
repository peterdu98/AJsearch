from app import db
from datetime import datetime

class Paper(db.Model):
	# Properties
	paper_id = db.Column(db.Integer, index=True, primary_key=True)
	title = db.Column(db.String)
	url = db.Column(db.String)
	author = db.Column(db.String)
	_date = db.Column(db.DateTime(), index=True, default=datetime.now)
	topic = db.Column(db.String)
	_tags = db.Column(db.String, default='')

	# Getter and Setter for tags
	@property
	def tags(self):
		return [tag for tag in self._tags.split(';')]
	@tags.setter
	def tags(self, value):
		self._tags = ''
		for tag in value:
			if self._tags != '':
				self._tags += ';{}'.format(tag)
			else:
				self._tags += tag

	# Getter and Setter for tags
	@property
	def date(self):
		months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
			'October', 'Novembre', 'December']
		month = months[self._date.date().month - 1]

		return '{} {}'.format(month, self._date.date().year)
	@date.setter
	def date(self, value):
		self._date = datetime.strptime(value, '%m/%Y')