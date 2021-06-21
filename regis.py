from flask import Flask,jsonify,request
from sqlLib import get_nim, input_data_user, cek_user,cek_nim
import uuid
import hashlib
app = Flask(__name__)

@app.route('/user/regist', methods=['POST'])
def user_regist():
    json_data = request.json
    if json_data == None :
        result = {"message":"process failed"}
        resp = jsonify(result)
        return resp,404
    else:
        if 'nim' not in json_data or 'username' not in json_data or 'jurusan' not in json_data or 'prodi' not in json_data or 'kelas' not in json_data or 'email' not in json_data or 'pass' not in json_data or 'status' not in json_data :
            result = {"message":"error request"} 
            resp = jsonify(result)
            return resp, 405
        else:
            id = str(uuid.uuid4().hex)
            nim = json_data ['nim']
            username = json_data ['username']
            jurusan = json_data ['jurusan']
            prodi = json_data ['prodi']
            kelas =json_data ['kelas']
            email = json_data ['email']
            password = json_data ['pass']
            status = json_data['status']
            password = hashlib.sha256(password.encode()).hexdigest()
            cek = cek_user(username,password)
            nim_cek = cek_nim(nim)
            if cek == None and nim_cek==False:
                input_data_user (id,nim,username,jurusan,prodi,kelas,email,password,status)
                result = {"message :input berhasil"}
                resp = jsonify(result)
                return resp, 203 
            else:
                result = {"message" : "sudah terdaftar"}
                resp = jsonify(result)
                return resp, 202

if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=9002)
    app.run(port=9002, debug=True)