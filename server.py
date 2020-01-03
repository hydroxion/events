from flask import Flask


from sensor import sensor


application = Flask(__name__)

application.register_blueprint(sensor)


def start_server():
    application.run(
        host='127.0.0.1',
        port=5000,
        debug=False,  # Use signals
        load_dotenv=False,
        use_reloader=False,  # Use signals
        threaded=False,
        processes=1
        # ssl_context='adhoc' # Requires Py Open SSL
    )
