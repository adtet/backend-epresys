from sqlLib import get_main, cek_id_main, get_status,cek_id,cek_id_main_dosen,get_main_2
import flask
from flask import Flask, jsonify, request
#from waitress import serve
import json
app = Flask(__name__)


@app.route("/user/history", methods=['POST'])
def history():
    json_data = flask.request.json
    if json_data == None:
        result = []
        return json.dumps(result), 504
    else:
        if 'id' not in json_data:
            result = []
            return json.dumps(result), 505
        else:
            id = json_data['id']
            cek = cek_id(id)
            if cek == False:
                result = []
                return json.dumps(result), 403
            else:
                status = get_status(id)
                if status==0: 
                    cek_main = cek_id_main(id)
                    if cek_main == False:
                        result = []
                        return json.dumps(result), 204
                    else:
                        result = get_main(id)
                        return result, 200
                else:
                    cek_main_2 = cek_id_main_dosen(id)
                    if cek_main_2 == False:
                        result = []
                        return json.dumps(result), 204
                    else:
                        result = get_main_2(id)
                        return result, 200

if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=9008)
    app.run(port=9008, debug=True)