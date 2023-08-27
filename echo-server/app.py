from flask import Flask, request

app = Flask(__name__)

@app.route("/<path:path>", methods=['GET', 'POST'])
def authen(path):
    # Access other request details
    request_method = request.method
    request_headers = request.headers
    request_query_string = request.query_string
    request_form_data = request.form
    request_args = request.args

    # logging.info the request information
    app.logger.warning("----------------------------------------------------")
    app.logger.warning(f"Request Method: {request_method}")
    app.logger.warning(f"Request Headers: {request_headers}")
    app.logger.warning(f"Request Query String: {request_query_string}")
    app.logger.warning(f"Request Form Data: {request_form_data}")
    app.logger.warning(f"Request Arguments: {request_args}")
    app.logger.warning("----------------------------------------------------")
    
    return "Authentication allowed"

