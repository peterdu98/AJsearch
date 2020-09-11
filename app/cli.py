import json
from app import app, models, db

# Command lines for testing
@app.cli.command('db_create')
def db_create():
	db.create_all()
	print('Database created!')

@app.cli.command('db_drop')
def db_drop():
	db.drop_all()
	print('Database dropped!')

@app.cli.command('db_seed')
def db_seed():
	with open('./app/data/data.json', 'r') as f:
		data = json.load(f)

		for entry in data:
			paper = models.Paper(**entry)

			db.session.add(paper)
			db.session.commit()

		print('Database seeded!')