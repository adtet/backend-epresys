from flask import Flask,jsonify,request
from sqlLib import input_data_user, cek_user
import uuid
import hashlib
app = Flask(__name__)

@app.route('/user/regist', methods=['POST'])
def user_regist():
    json_data = request.json
    if json_data == None :
        result = {"message":"process failed"}
        resp = jsonify(result)
        return resp,407
    else:
        if 'nip' not in json_data or 'username' not in json_data or 'jurusan' not in json_data or 'prodi' not in json_data or 'kode_dosen' not in json_data or 'email' not in json_data or 'pass' not in json_data :
            result = {"message":"error request"} 
            resp = jsonify(result)
            return resp, 408
        else:
            id = str(uuid.uuid4().hex)
            nip = json_data ['nip']
            username = json_data ['username']
            jurusan = json_data ['jurusan']
            prodi = json_data ['prodi']
            kode_dosen =json_data ['kode_dosen']
            email = json_data ['email']
            password = json_data ['pass']
            password = hashlib.sha256(password.encode()).hexdigest()
            cek = cek_user(username,password)
            if cek == None:
                input_data_user (id,nip,username,jurusan,prodi,kode_dosen,email,password)
                result = {"message :input berhasil"}
                resp = jsonify(result)
                return resp, 204
            else:
                result = {"message" : "sudah terdaftar"}
                resp = jsonify(result)
                return resp, 205

if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=4001)
    app.run(port=4002, debug=True)