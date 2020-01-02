from flask import Flask

from sensors import sensors


application = Flask(__name__)

application.register_blueprint(sensors)

application.run(
    host='127.0.0.1',
    port=5000,
    debug=True,
    load_dotenv=False,
    use_reloader=True,
    threaded=False,
    processes=1
    # ssl_context='adhoc' # Requires Py Open SSL
)
