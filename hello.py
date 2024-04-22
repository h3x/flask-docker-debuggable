# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/
try: 
    import debugpy
except:
    debugpy = None
import logging
logger = logging.getLogger(__name__)

from flask import Flask
app = Flask(__name__)
logging.log(logging.INFO, 'ADAM: Entering File')

@app.route('/')
def hello_world():
    app.logger.log(logging.INFO, 'ADAM: hello_worldk')
    retval = 'Hello World!!!!'
    return retval


def run_dev():
    app.logger.log(logging.INFO, 'ADAM: run_dev')
    app.config['DEBUG'] = False

    if debugpy and not debugpy.is_client_connected():
        try:
            debugpy.listen(("0.0.0.0", 5678))
        except:
            pass

    use_debugger = not(app.config.get('DEBUG_EXTERNAL', False))

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=app.debug,
    )
    
if __name__ == '__main__':
    app.logger.log(logging.INFO, 'ADAM: Starting Flask app...')
    debugpy.listen(('0.0.0.0', 5678))
    debugpy.wait_for_client()
    debugpy.breakpoint()
    app.run(debug=True, host='0.0.0.0', port=5000)
else:
    app.logger.log(logging.INFO, 'ADAM: Not running as main')
    run_dev()

