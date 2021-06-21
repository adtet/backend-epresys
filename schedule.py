import flask
from flask import Flask, jsonify, request
import json
import datetime
from datetime import date
import calendar
# from waitress import serve
from sqlLib import  get_kelas, get_jadwal, get_nim,get_status,cek_id,get_jadwal_dosen
app = Flask(__name__)


@app.route('/schedule', methods=['POST'])
def schedule():
    json_data = flask.request.json
    if json_data == None:
        result = []
        resp = json.dumps(result)
        return resp, 402
    else:
        if 'id' not in json_data:
            result = []
            resp = json.dumps(result)
            return resp, 409
        else:
            id = json_data['id']
            
            cek = cek_id(id)
            if cek == False:
                result = []
                resp = json.dumps(result)
                return resp, 403
            else:
                status = get_status(id) 
                if status==0:
                    kelas = get_kelas(id)    
                    if kelas == None:
                        result = []
                        resp = json.dumps(result)
                        return resp, 203
                    else:
                        resp = get_jadwal(kelas)
                        return resp, 200
                else:
                    nip = get_nim(id)
                    if nip == None:
                        result = []
                        resp = json.dumps(result)
                        return resp, 203
                    else:
                        resp = get_jadwal_dosen(nip)
                        return resp,200
                        

if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=9001)
    app.run(port=9001, debug=True)