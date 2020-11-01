import flask
# https://flask.palletsprojects.com/en/1.1.x/quickstart/
import requests
# https://requests.readthedocs.io/en/master/user/quickstart/

app = flask.Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  page = requests.get(f'https://{path}').content.decode("UTF-8")
  # page can be manipulated here as a "UTF-8" string
  newpage = page.replace("Bee", "Ya like jazz")
  newerpage = newpage.replace("bee", "ya like jazz")
  return newerpage
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, ssl_context='adhoc')
