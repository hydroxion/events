from flask import Flask

from sensor import sensor

from process import process


application = Flask(__name__)

application.register_blueprint(sensor)

application.register_blueprint(process)


def start_server():
    print(' * Server start')

    application.run(
        host='0.0.0.0',
        port=5000,
        debug=False,  # Use signals, which 'breaks' in the thread
        load_dotenv=False,
        use_reloader=False,  # Use signals, which 'breaks' in the thread
        threaded=True,  # Required
        processes=1
        # ssl_context='adhoc' # Requires Py Open SSL
    )
