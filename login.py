from flask import Flask,jsonify,request
from sqlLib import input_data_user, cek_user

app = Flask(__name__)

@app.route('/user/login',methods=['POST'])
def user_login():
    json_data = request.json
    if json_data==None:
        result = {"message":"process failed"}
        resp = jsonify(result)
        return resp,400
    else:
        if 'username' not in json_data or 'password' not in json_data:
            result = {"message":"error request"}
            resp = jsonify(result)
            return resp,401
        else:
            username = json_data['username']
            password = json_data['password']
            cek = cek_user(username,password)
            if cek==None:
                result = {"message":"Forbidden"}
                resp = jsonify(result)
                return resp,403
            else:
                result = {"message":cek}
                resp = jsonify(result)
                return resp,200

@app.route('/user/regist', methods=['POST'])
def user_regist():
    json_data = request.json
    if json_data == None :
        result = {"message":"process failed"}
        resp = jsonify(result)
        return resp,404
    else:
        if 'id' not in json_data or 'nim' not in json_data or 'username' not in json_data or 'jurusan' not in json_data or 'prodi' not in json_data or 'kelas' not in json_data or 'email' not in json_data or 'pass' not in json_data :
            result = {"message":"error request"} 
            resp = jsonify(result)
            return resp, 405
        else:
            id = json_data ['id']
            nim = json_data ['nim']
            username = json_data ['username']
            jurusan = json_data ['jurusan']
            prodi = json_data ['prodi']
            kelas = json_data ['kelas']
            email = json_data ['email']
            password = json_data ['pass']
            cek = cek_user(username,password)
            if cek == None:
                input_data_user (id,nim,username,jurusan,prodi,kelas,email,password)
                result = {"message" : "input berhasil"}
                resp = jsonify(result)
                return resp, 203 
            else:
                result = {"message" : "sudah terdaftar"}
                resp = jsonify(result)
                return resp, 202



if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=4001)
    app.run(port=4001, debug=True)




   