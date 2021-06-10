from flask import Flask,jsonify,request
from sqlLib import input_data_user, cek_user
import hashlib

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
            password = hashlib.sha256(password.encode()).hexdigest()
            cek = cek_user(username,password)
            if cek==None:
                result = {"message":"Forbidden"}
                resp = jsonify(result)
                return resp,403
            else:
                result = {"message":cek}
                resp = jsonify(result)
                return resp,200





if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=9005)
    app.run(port=9005, debug=True)




   