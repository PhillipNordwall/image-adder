import re
import flask
# https://flask.palletsprojects.com/en/1.1.x/quickstart/
import requests
# https://requests.readthedocs.io/en/master/user/quickstart/

app = flask.Flask(__name__)
REG = "[bB]ee"
REP = "buzz-buzz<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Vespa_Mandarinia_Magnifica_-_Filippo_Turetta.jpg/220px-Vespa_Mandarinia_Magnifica_-_Filippo_Turetta.jpg'>"


@app.route('/', defaults={'path': 'en.wikipedia.org/wiki/bee'})
@app.route('/<path:path>')
def proxy(path):
  page = requests.get(f'https://{path}').content.decode("UTF-8")
  # page can be manipulated here as a "UTF-8" string
  newpage = re.sub(REG, REP, page)
  return newpage
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, ssl_context='adhoc')
