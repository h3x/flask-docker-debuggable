from .hello import app

import os.path
import system
import logging

logging.log(logging.INFO, 'ADAM: Starting Flask app...')
try: 
    import debugpy
except:
    debugpy = None

def run_dev():
    app.config['DEBUG'] = False

    if debugpy and not debugpy.is_client_connected():
        try:
            debugpy.listen(("0.0.0.0", 5678))
        except:
            pass

    use_debugger = not(app.config.get('DEBUG_EXTERNAL', False))

    app.run(
        host=app.config['LISTEN_ADDR'],
        port=app.config['LISTEN_PORT'],
        debug=app.debug,
    )

