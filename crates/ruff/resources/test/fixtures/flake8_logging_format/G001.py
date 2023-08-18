import logging
import logging as foo

logging.info('Hello World!')
logging.log(logging.INFO, 'Hello World!')
foo.info('Hello World!')
logging.log(logging.INFO, msg='Hello World!')
logging.log(level=logging.INFO, msg='Hello World!')
logging.log(msg='Hello World!', level=logging.INFO)

# Flask support
import flask
from flask import current_app
from flask import current_app as app

flask.current_app.logger.info('Hello World!')
current_app.logger.info('Hello World!')
app.logger.log(logging.INFO, 'Hello World!')
