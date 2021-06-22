import sqlLib
from sqlLib import cek_present_dosen, get_kelas, get_nim, get_matkul, get_matkul_late, insert_main, get_username, cek_id, get_kelas, cek_present
from sqlLib import get_status,get_matkul_dosen,get_matkul_late_dosen,insert_main_dosen
import flask
from flask import Flask, jsonify, request
# from waitress import serve
from datetime import date, datetime
import calendar
app = Flask(__name__)

@app.route('/user/present',methods=['POST'])
def absen():
    json_data = flask.request.json
    if json_data == None:
        result = {"link":"error"}
        resp = jsonify(result)
        return resp, 400
    else:
        if 'id' not in json_data or 'matakuliah' not in json_data:
            result = {"link": "error request"}
            resp = jsonify(result)
            return resp, 401
        else:
            id = json_data['id']
            matakuliah = json_data['matakuliah']
            cek = cek_id(id)
            if cek == False:
                result = {"link" : 'id Not Available'}
                resp = jsonify(result)
                return resp, 403
            else:
                kelas = get_kelas(id)
                nim = get_nim(id)
                username = get_username(id)
                status = get_status(id)
                if status==0:
                    matkul_hadir = get_matkul(kelas)
                    if matkul_hadir==None:
                        matkul_telat = get_matkul_late(kelas)
                        if matkul_telat==None:
                            info = "tidak tersedia"
                            result = {"link":info}
                            resp = jsonify(result)
                            return resp,204
                        else:
                            info = "telat"
                            cek_di_main = cek_present(id,matkul_telat[0])
                            if cek_di_main == True:
                                insert_main(id,nim,username,kelas,matkul_telat[0],matkul_telat[1],matkul_telat[2],matkul_telat[3],info)
                                component_link = matkul_telat[0]+kelas
                                telat = component_link.translate({ord(i): None for i in '-.&'})
                                tlt =  "".join(telat.split())
                                data = "http://g.co/meet/" + tlt.lower()
                                result = {"link": data}
                                resp = jsonify(result)
                                return resp, 200
                            else:
                                component_link = matkul_telat[0]+kelas
                                telat = component_link.translate({ord(i): None for i in '-.&'})
                                tlt =  "".join(telat.split())
                                data = "http://g.co/meet/" + tlt.lower()
                                result = {"link": data}
                                resp = jsonify(result)
                                return resp, 200
                    else:
                        if matakuliah==str(matkul_hadir[0]).rstrip('\r\n'):
                            info = "hadir"
                            cek_di_main = cek_present(id,matkul_hadir[0])
                            if cek_di_main==True:
                                insert_main(id,nim,username,kelas,matkul_hadir[0],matkul_hadir[1],matkul_hadir[2],matkul_hadir[3],info)
                                component_link = matkul_hadir[0]+kelas
                                hadir = component_link.translate({ord(i): None for i in '-.&'})
                                hdr = "".join(hadir.split())
                                data = "http://g.co/meet/" + hdr.lower()
                                result = {"link": data}
                                resp = jsonify(result)
                                return resp, 200
                            else:
                                component_link = matkul_hadir[0]+kelas
                                hadir = component_link.translate({ord(i): None for i in '-.&'})
                                hdr = "".join(hadir.split())
                                data = "http://g.co/meet/" + hdr.lower()
                                result = {"link": data}
                                resp = jsonify(result)
                                return resp, 200
                        else:
                            matkul_telat = get_matkul_late(kelas)
                            if matkul_telat==None:
                                info = "tidak tersedia"
                                result = {"link":info}
                                resp = jsonify(result)
                                return resp,204
                            else:
                                if matakuliah==str(matkul_telat[0]).rstrip('\r\n'):
                                    info = "telat"
                                    cek_di_main = cek_present(id,matkul_telat[0])
                                    if cek_di_main == True:
                                        insert_main(id,nim,username,kelas,matkul_telat[0],matkul_telat[1],matkul_telat[2],matkul_telat[3],info)
                                        component_link = matkul_telat[0]+kelas
                                        telat = component_link.translate({ord(i): None for i in '-.&'})
                                        tlt =  "".join(telat.split())
                                        data = "http://g.co/meet/" + tlt.lower()
                                        result = {"link": data}
                                        resp = jsonify(result)
                                        return resp, 200
                                    else:
                                        component_link = matkul_telat[0]+kelas
                                        telat = component_link.translate({ord(i): None for i in '-.&'})
                                        tlt =  "".join(telat.split())
                                        data = "http://g.co/meet/" + tlt.lower()
                                        result = {"link": data}
                                        resp = jsonify(result)
                                        return resp, 200
                                else:
                                    info = "tidak tersedia"
                                    result = {"link":info}
                                    resp = jsonify(result)
                                    return resp,204
                else:
                    if 'kelas' not in json_data:
                        result = {"link": "error request lecture"}
                        resp = jsonify(result)
                        return resp, 401
                    else:
                        kelas_ngajar = json_data['kelas']
                        matkul_hadir = get_matkul_dosen(nim,kelas_ngajar)
                        if matkul_hadir==None:
                            matkul_telat = get_matkul_late_dosen(nim,kelas_ngajar)
                            if matkul_telat==None:
                                info = "tidak tersedia1"
                                result = {"link":info}
                                resp = jsonify(result)
                                return resp,203
                            else:
                                info = "telat"
                                cek_di_main = cek_present_dosen(id,matkul_telat[1],matkul_telat[0])
                                if cek_di_main == True:
                                    insert_main_dosen(id,nim,username,matkul_telat[1],matkul_telat[0],info)
                                    component_link = matkul_telat[1]+matkul_telat[0]
                                    telat = component_link.translate({ord(i): None for i in '-.&'})
                                    tlt =  "".join(telat.split())
                                    data = "http://g.co/meet/" + tlt.lower()
                                    result = {"link": data}
                                    resp = jsonify(result)
                                    return resp, 200
                                else:
                                    component_link = matkul_telat[1]+matkul_telat[0]
                                    telat = component_link.translate({ord(i): None for i in '-.&'})
                                    tlt =  "".join(telat.split())
                                    data = "http://g.co/meet/" + tlt.lower()
                                    result = {"link": data}
                                    resp = jsonify(result)
                                    return resp, 200
                        else:
                            if matakuliah==str(matkul_hadir[1]).rstrip('\r\n'):
                                info = "hadir"
                                cek_di_main = cek_present_dosen(id,matakuliah,kelas_ngajar)
                                if cek_di_main==True:
                                    insert_main_dosen(id,nim,username,matakuliah,kelas_ngajar,info)
                                    component_link = matkul_hadir[1]+matkul_hadir[0]
                                    hadir = component_link.translate({ord(i): None for i in '-.&'})
                                    hdr = "".join(hadir.split())
                                    data = "http://g.co/meet/" + hdr.lower()
                                    result = {"link": data}
                                    resp = jsonify(result)
                                    return resp, 200
                                else:
                                    component_link = matkul_hadir[1]+matkul_hadir[0]
                                    hadir = component_link.translate({ord(i): None for i in '-.&'})
                                    hdr = "".join(hadir.split())
                                    data = "http://g.co/meet/" + hdr.lower()
                                    result = {"link": data}
                                    resp = jsonify(result)
                                    return resp, 200
                            else:
                                matkul_telat = get_matkul_late(nim,kelas_ngajar)
                                if matkul_telat==None:
                                    info = "tidak tersedia2"
                                    result = {"link":info}
                                    resp = jsonify(result)
                                    return resp,204
                                else:
                                    if matakuliah==str(matkul_telat[1]).rstrip('\r\n'):
                                        info = "telat"
                                        cek_di_main = cek_present_dosen(id,matkul_telat[1],matkul_telat[0])
                                        if cek_di_main == True:
                                            insert_main_dosen(id,nim,username,matkul_telat[1],matkul_telat[0],info)
                                            component_link = matkul_telat[1]+matkul_telat[0]
                                            telat = component_link.translate({ord(i): None for i in '-.&'})
                                            tlt =  "".join(telat.split())
                                            data = "http://g.co/meet/" + tlt.lower()
                                            result = {"link": data}
                                            resp = jsonify(result)
                                            return resp, 200
                                        else:
                                            component_link = matkul_telat[1]+matkul_telat[0]
                                            telat = component_link.translate({ord(i): None for i in '-.&'})
                                            tlt =  "".join(telat.split())
                                            data = "http://g.co/meet/" + tlt.lower()
                                            result = {"link": data}
                                            resp = jsonify(result)
                                            return resp, 200
                                    else:
                                        info = "tidak tersedia3"
                                        result = {"link":info}
                                        resp = jsonify(result)
                                        return resp,203
                                        
if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=9007)
    app.run(port=9007, debug=True)

                                         
                                                    
                                                    
                                                    


                                      
                                            




        



