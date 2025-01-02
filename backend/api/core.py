"""
Module init.
Contains function for starting up the flask process
"""
from api.routes import RouteManager
from api.server import WaitressAPIServer
from api.app import FlaskApp
from microlab.interface import MicrolabInterface
from util.logger import MultiprocessingLogger


def run_flask(in_queue, out_queue, logging_queue):

    # The initialize_logger call only needs to happen once when a new process is started.
    # Logs from this point on will just require a call to MultiprocessingLogger.get_logger(<logger_name>)
    # within the same process.
    MultiprocessingLogger.initialize_logger(logging_queue)

    logger = MultiprocessingLogger.get_logger(__name__)
    logger.info("### STARTING API ###")

    microlab_interface = MicrolabInterface(in_queue, out_queue)

    flask_app = FlaskApp()

    # This handles the routes and registering them to the flask_app instance
    RouteManager(flask_app, microlab_interface)

    server = WaitressAPIServer(flask_app.get_flask_app())
    server.set_microlab_interface(microlab_interface)
    server.run()
