import flask
from flask import Flask, jsonify,request
from sqlLib import get_code_command_get_room,query_cek_ruangan_bengkel,query_cek_ruangan_gedung_a,query_cek_ruangan_lab_atas,query_cek_ruangan_lab_bawah,query_cek_ruangan_p2t
from sqlLib import cek_id
app = Flask(__name__)


@app.route('/lokasi', methods=['POST'])
def lokasi():
    json_data = request.json
    if json_data==None:
        result = {"message":"process failed"}
        resp = jsonify(result)
        return resp,400
    else:
        if 'id' not in json_data or 'lat' not in json_data or 'lng' not in json_data or 'ruangan' not in json_data:
            result = {"message": "error request"}
            resp = jsonify(result)
            return resp, 401
        else:
            id = json_data['id']
            ruangan = json_data['ruangan']
            lat = json_data['lat']
            lng = json_data['lng']
            cek = cek_id(id)
            if cek==False:
                result = {"message":"Forbidden"}
                resp = jsonify(result)
                return resp,403
            else:
                command = get_code_command_get_room(ruangan)
                if command==0:
                    query_cek = query_cek_ruangan_bengkel(ruangan,lat,lng)
                    if query_cek==False:
                        result = {"message":"Forbidden User at this room"}
                        resp = jsonify(result)
                        return resp,203
                    else:
                        result = {"message":"You are allow at "+ruangan}
                        resp = jsonify(result)
                        return resp,200
                elif command==1:
                    query_cek = query_cek_ruangan_gedung_a(ruangan,lat,lng)
                    if query_cek==False:
                        result = {"message":"Forbidden User at this room"}
                        resp = jsonify(result)
                        return resp,203
                    else:
                        result = {"message":"You are allow at "+ruangan}
                        resp = jsonify(result)
                        return resp,200
                elif command==2:
                    query_cek = query_cek_ruangan_p2t(ruangan,lat,lng)
                    if query_cek==False:
                        result = {"message":"Forbidden User at this room"}
                        resp = jsonify(result)
                        return resp,203
                    else:
                        result = {"message":"You are allow at "+ruangan}
                        resp = jsonify(result)
                        return resp,200
                elif command==3:
                    query_cek = query_cek_ruangan_lab_atas(ruangan,lat,lng)
                    if query_cek==False:
                        result = {"message":"Forbidden User at this room"}
                        resp = jsonify(result)
                        return resp,203
                    else:
                        result = {"message":"You are allow at "+ruangan}
                        resp = jsonify(result)
                        return resp,200
                elif command==4:
                    query_cek = query_cek_ruangan_lab_bawah(ruangan,lat,lng)
                    if query_cek==False:
                        result = {"message":"Forbidden User at this room"}
                        resp = jsonify(result)
                        return resp,203
                    else:
                        result = {"message":"You are allow at "+ruangan}
                        resp = jsonify(result)
                        return resp,200
                else:
                    result = {"message":"No room for you"}
                    resp = jsonify(result)
                    return resp,204


if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=9004)
    app.run(port=9004, debug=True)