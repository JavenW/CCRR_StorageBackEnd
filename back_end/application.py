from flask import Flask, Response, request
from datetime import datetime
import json
from storageService import StorageService
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__)

CORS(app)


@app.route("/getitems/<email>", methods=["GET"])
def get_all_items(email):
    
    result = StorageService.get_items(email)

    if result or result == {}:
        result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/additem", methods=["POST"])
def add_item():
    email = request.args.get('email', None)
    item = request.args.get('item', None)
    expired_date = request.args.get('expdate', None)
    StorageService.insert_item(email, item, expired_date)

    return Response(json.dumps({}), status=200, content_type="application.json")


@app.route("/deleteitem", methods=["POST"])
def delete_item():
    email = request.args.get('email', None)
    item = request.args.get('item', None)
    StorageService.remove_item(email, item)

    return Response(json.dumps({}), status=200, content_type="application.json")


@app.route("/edititem", methods=["POST"])
def edit_item():
    email = request.args.get('email', None)
    item = request.args.get('item', None)
    expired_date = request.args.get('expdate', None)
    StorageService.insert_item(email, item, expired_date)

    return Response(json.dumps({}), status=200, content_type="application.json")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)
