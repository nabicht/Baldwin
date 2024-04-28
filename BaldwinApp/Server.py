import flask

app = flask.Flask('Baldwin', 
				  static_url_path='/assets',
				  static_folder='BaldwinApp/assets',
				  template_folder='BaldwinApp/templates')



@app.route('/')
def index():
	return flask.render_template('index.html')


