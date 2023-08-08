import enum
import cx_Oracle
import config.config_db as cf
from datetime import datetime as dt
from datetime import timedelta
import datetime
import uuid
import os
import json
import shutil 
import connect_minio
import sys
sys.path.append('/home/dang/Downloads/kse/facenet/jetson_nano_demo/face_recognition/')

dsn_tns = cx_Oracle.makedsn(cf.host,cf.port,service_name=cf.serviceName)
con = cx_Oracle.connect(cf.username,cf.password,dsn=dsn_tns)
con_01 = cx_Oracle.connect(cf.username_01,cf.password,dsn=dsn_tns)
cur = con.cursor()
cur_01 = con_01.cursor()
print(con.version)

def getEmployee(id):
    name=''
    fullName = ''
    # info = cur.execute(f'''SELECT * FROM "EMPLOYEES" WHERE ID={id}''')
    # info = cur.execute(f'''SELECT "userName","fullName" FROM "QT_EMPLOYEES" WHERE "id"='{id}' ''')
    info = cur.execute(f'''SELECT "QT_EMPLOYEES"."userName","QT_EMPLOYEES"."fullName","QT_POSITION"."name" FROM "QT_EMPLOYEES" INNER JOIN "QT_POSITION" ON "QT_EMPLOYEES"."positionId" = "QT_POSITION"."id" WHERE "QT_EMPLOYEES"."id"='{id}' ''')

    for i in info:
        # name = i[1]
        name = i[0]
        fullName = i[1]
        position = i[2]
    return name,fullName,position
# name,fullName,position=getEmployee('c7c8acf3-e066-4a63-84f4-3750e1408aa7')
# print(name,fullName,position)
# def getTimeInYearID(id_emp):
#     id =''
#     timeYearID = cur.execute(f''' SELECT "id" FROM "TIME_IN_YEAR" WHERE "employeeId"='{id_emp}' ''')
#     for i in timeYearID:
#         # name = i[1]
#         id = i[0]
#     return id

def getAllEmployee():
    
    infos = cur.execute(f'''SELECT "QT_EMPLOYEES"."id","QT_EMPLOYEES"."fullName","QT_POSITION"."name","QT_COMPANY_UNITS"."name" FROM "QT_EMPLOYEES" INNER JOIN "QT_COMPANY_UNITS" ON "QT_EMPLOYEES"."fromUnitId" = "QT_COMPANY_UNITS"."id" INNER JOIN "QT_POSITION" ON "QT_EMPLOYEES"."positionId"="QT_POSITION"."id" ''')
    infos_arr =[]
    for info in infos:
        infos_arr.append(info)
    return infos_arr
    # return(infos)
# infos_arr = getAllEmployee()
# print(infos_arr)
# def getChucVu(allEmps):
#     for info in allEmps:
#         pbs = cur.execute(f'''SELECT "name" FROM QT_COMPANY_UNITS WHERE "id"="{info[16]}"  ''')
#         for pb in pbs:
#             info.append(pb[0])

def getTimeCheck():
    # checkIn_time = cur.execute(f'''SELECT EXTRACT(HOUR FROM CHECKIN)|| ':' ||EXTRACT(MINUTE FROM CHECKIN) FROM TIMECHECK''')
    # cur_2 = con.cursor()
    # checkOut_time = cur_2.execute(f'''SELECT EXTRACT(HOUR FROM CHECKOUT)|| ':' ||EXTRACT(MINUTE FROM CHECKOUT) FROM TIMECHECK''')
    checkIn_time = cur.execute(f'''SELECT "morningShiftStartCheckIn" FROM "SET_UP_TIMEKEEPING" ''')
    cur_2 = con.cursor()
    checkOut_time = cur_2.execute(f'''SELECT "afternoonShiftEndCheckOut" FROM "SET_UP_TIMEKEEPING" ''')
    cur_3 = con.cursor()
    others_time = cur_3.execute(f'''SELECT "morningShiftEndCheckIn","morningShiftStartCheckOut","morningShiftEndCheckOut","afternoonShiftStartCheckIn","afternoonShiftEndCheckIn","afternoonShiftStartCheckOut" FROM "SET_UP_TIMEKEEPING" ''')
    mn_end_in = ''
    mn_start_out=''
    mn_end_out = ''
    atn_start_in = ''
    atn_end_in = ''
    atn_start_out = ''
    for i in others_time:
        mn_end_in = i[0]
        mn_start_out=i[1]
        mn_end_out = i[2]
        atn_start_in = i[3]
        atn_end_in = i[4]
        atn_start_out = i[5]
    h_in = ''
    m_in = ''
    h_out = ''
    m_out = ''
    for i in checkIn_time:
        h_in = i[0].split(':')[0]
        m_in = i[0].split(':')[1]
    for t in checkOut_time:
        h_out = t[0].split(':')[0]
        m_out = t[0].split(':')[1]
    return [h_in,m_in,h_out,m_out,mn_end_in,mn_start_out,mn_end_out,atn_start_in,atn_end_in,atn_start_out]
# print(getTimeCheck())
def getEmpHopLe(idEmp):
    now = dt.now()
    day = now.date().day
    month = now.date().month
    year = now.date().year
    id = cur.execute(f''' SELECT "id" FROM "TIME_IN_DAY" WHERE "employeeId"='{idEmp}' AND "day"={day} AND "month"={month} AND "year"={year}  ''')
    if id.fetchone() == None:
        return False
    else:
        return True
# print(getEmpHopLe('75c581b5-c888-41ac-93e0-034ead59c854'))

def diemDanh(employee,h_in,m_in,h_out,m_out,device):
    # id_rent = uuid.uuid4()
    id_emp = employee['id']
    # name = employee['name']
    # timeYearID = getTimeInYearID(id_emp)
    # print(timeYearID)

    time = employee['time']
    date = datetime.date.today()
    h_in = int(h_in)
    m_in = int(m_in)
    h_out = int(h_out)
    m_out = int(m_out)
    threshold_In = dt.combine(date,datetime.time(h_in,m_in))
    threshold_Out = dt.combine(date,datetime.time(h_out,m_out))
    day = time.date().day
    month = time.date().month
    year = time.date().year
    print(id_emp)
    print(day)
    print(month)
    print(year)
    time_in = cur.execute(f''' SELECT "timeCheckIn" FROM "TIME_IN_DAY" WHERE "employeeId"='{id_emp}' AND "day"={day} AND "month"={month} AND "year"={year}  ''')
    status = ''
    # print(time_in.fetchall())
    l = time_in.fetchone()
    l = list(l)
    # print(l)
    # print(l[0])
    if l[0] == None:
        # print('haha')
        if time >= threshold_In:
            #push to DB
            # time = time.strftime('%y-%m-%d %H:%M:%S')
            time = time.strftime('%H:%M')
            # print(time)
            # cur.execute(f'''INSERT INTO "DIEMDANH" (ID,ID_EMP,NAME,CHECK_IN,DATE_IN) VALUES ('{id_rent}','{id_emp}','{name}',TO_TIMESTAMP('{time}','YYYY-MM-DD HH24:MI:SS'), TO_DATE('{date}','YYYY-MM-DD') )''')
            cur_2 = con.cursor()
            cur_2.execute(f'''UPDATE "TIME_IN_DAY" SET "timeCheckIn" = '{time}',"device"='{device}' WHERE "employeeId"='{id_emp}' AND "day"={day} AND "month"={month} AND "year"={year} ''')
            con.commit()

            status = 'CHECK-IN'
            print(f'{status} thanh cong')
        else:
            pass
    else:
        if time <= threshold_Out:
            #push to DB
            # time = time.strftime('%d-%m-%y %I:%M:%S %p')
            time = time.strftime('%H:%M')
            # print(time)
            # cur.execute(f'''INSERT INTO "DIEMDANH" (ID,NAME,CHECK_OUT) VALUES ('{id}','{name}',TO_TIMESTAMP('{time}','YYYY-MM-DD HH24:MI:SS') )''')
            # cur.execute(f''' UPDATE "DIEMDANH" SET CHECK_OUT = TO_TIMESTAMP('{time}','YYYY-MM-DD HH24:MI:SS') WHERE ID_EMP={id_emp} AND DATE_IN=TO_DATE('{date}','YYYY-MM-DD') ''')
            cur_2 = con.cursor()
            cur_2.execute(f'''UPDATE "TIME_IN_DAY" SET "timeCheckOut" = '{time}',"device"='{device}' WHERE "employeeId"='{id_emp}' AND "day"={day} AND "month"={month} AND "year"={year}  ''')
            con.commit()
            status = 'CHECK-OUT'
            print(f'{status} thanh cong')
    return status
# def test():
#     id = '7c581b5-c888-41ac-93e0-034ead59c854'
#     time_in = cur.execute(f''' SELECT "timeCheckIn" FROM "TIME_IN_DAY" WHERE "employeeId"='{id}' AND "day"={16} AND "month"={9} AND "year"={2022}  ''')
#     status = ''
#     # print(time_in.fetchall())
#     l = time_in.fetchone()
#     if l == None:
#         print('khong ton tai id')
#     else:
#         l = list(l)
#         print(l)
# test()
def autoUpdateDB():
    ids = cur.execute('''SELECT "id" FROM "QT_EMPLOYEES" ''')
    ids_arr = []
    ids_folder = []
    for id in ids:
        ids_arr.append(id[0])
        # print(id[0])
        checkFolder = os.path.exists(f'/home/dang/Downloads/kse/facenet/jetson_nano_demo/face_recognition/face_db_online/{id[0]}')
        if checkFolder == False:
            print(f'them folder {id[0]} ')
            os.mkdir(f'/home/dang/Downloads/kse/facenet/jetson_nano_demo/face_recognition/face_db_online/{id[0]}') 
        else:
            pass
    for e,i in enumerate(os.listdir('/home/dang/Downloads/kse/facenet/jetson_nano_demo/face_recognition/face_db_online')):
        ids_folder.append(i)
    # print(len(ids_arr))
    # print(ids_arr)
    # print(len(ids_folder))
    # print(ids_folder)

    if len(ids_arr) < len(ids_folder):
        diff = set(ids_folder).difference(set(ids_arr))
        print('nhung folder thay doi khac giua local va db')
        # print(diff)
        # for i in diff:
        #    os.mkdir(f'/home/dang/Downloads/kse/facenet/jetson_nano_demo/face_recognition/face_db_online/{i}')  
        #    print(f'them folder {i}')
        for i in diff:
            print(f'xoa folder {i}')
            shutil.rmtree(os.path.join('/home/dang/Downloads/kse/facenet/jetson_nano_demo/face_recognition/face_db_online', i), ignore_errors=True)
# autoUpdateDB()

def pushPhotoTimeKP(id,img,folderPath):
    # id = 'f1a8fa81-44ac-4a9c-93ef-3dd6bfc9c50e'
    # img = 'hehe'
    arr = cur_01.execute(f'''SELECT "id","photoTimeKeeping" FROM "QT_EMPLOYEES" WHERE "id"='{id}' ''')
    rows = arr.fetchall()
    for row in rows:
        if row[1] == None:
            print('them anh moi vao')
            connect_minio.push_data(img,folderPath)
            cur_01.execute(f'''UPDATE "QT_EMPLOYEES" SET "photoTimeKeeping" ='["{img}"]' WHERE "id"='{id}'  ''')
            con_01.commit()
        else:
            
            data =row[1].read()
            json_data = json.loads(data)
            print('da co anh')
            print(type(json_data))
            if len(json_data)==4:
                connect_minio.push_data(img,folderPath)
                json_data[-1]=f"{img}"
            elif len(json_data)<4:
                connect_minio.push_data(img,folderPath)
                json_data.append(f"{img}")
            else:
                print('da du 4 anh')
                pass
            # print(json_data)
            # json_data = str(json_data)
            text = '['
            for i in range (0,len(json_data)):
                if i != len(json_data)-1:
                    text += f'"{json_data[i]}",'
                else:
                    text += f'"{json_data[i]}"'
            text+=']'
            print(text)
            cur_01.execute(f'''UPDATE "QT_EMPLOYEES" SET "photoTimeKeeping" ='{text}' WHERE "id"='{id}'  ''')
            con_01.commit()
            print('them anh thanh cong')
            # # print('done')
            # print(json_data)
            # print(type(json_data))
    

#AUTO
def checkUpdateImg(status):

    empData_dict = {}
    time_now = dt.now()
    if status == 'now':

        day = time_now .date().day
        month = time_now .date().month
        year = time_now.date().year

    else:
        pre_date = time_now - timedelta(hours=24)

        day = pre_date .date().day
        month = pre_date .date().month
        year = pre_date.date().year

    arr = cur_01.execute(f'''SELECT "id","photoTimeKeeping" FROM "QT_EMPLOYEES" WHERE EXTRACT(DAY FROM "updatedAt")='{str(day)}' AND EXTRACT(MONTH FROM "updatedAt")='{str(month)}' AND EXTRACT(YEAR FROM "updatedAt")='{str(year)}' ''')
    # arr = cur.execute(f'''SELECT "id","photoTimeKeeping" FROM "QT_EMPLOYEES" WHERE EXTRACT(DAY FROM "updatedAt")='24' AND EXTRACT(MONTH FROM "updatedAt")='8' AND EXTRACT(YEAR FROM "updatedAt")='2022' ''')
    rows = arr.fetchall()
    for row in rows:
        if row[1] == None:
            empData_dict[row[0]] = []
        else:
            # print( row[1].read())
            # print(row[0])
            data =row[1].read()
            json_data = json.loads(data)
            empData_dict[row[0]] = json_data
    
    #check image in db local
    for e,i in enumerate(os.listdir('/home/dang/Downloads/kse/facenet/jetson_nano_demo/face_recognition/face_db_online')):
        for k,v in empData_dict.items():
            if k==i:
                folder_path = os.path.join('/home/dang/Downloads/kse/facenet/jetson_nano_demo/face_recognition/face_db_online', i)
                #xoa anh trong folder i
                for f in os.listdir(folder_path):
                    os.remove(os.path.join(folder_path, f))
                    print('xoa thanh cong: '+ f)
                #update lai anh tu server ve
                if v ==[]:
                    pass
                else:
                    for l in v:
                        name_img = l.split('/')[-1]
                        print(f'tai them anh {name_img}')
                        connect_minio.get_data(name_img,folder_path)
                        name = name_img.split('.')[0]
                        name_wt = name.split('_')[0]
                        duoi = name_img.split('.')[1]
                        if name_wt != i:
                            id_set =[]
                            for e,t in enumerate(os.listdir(folder_path)):
                                filename = t.split('.')[0]
                                if '_' in filename:
                                    id = filename.split('_')[0]
                                    if id == i:
                                        number = filename.split('_')[1]
                                        id_set.append(int(number))
                                else:
                                    if(filename == i):
                                        id_set.append(0)
                            # print(id_set)
                            if id_set:
                                id_set = sorted(id_set)
                                old_f = os.path.join(folder_path,name_img)
                                # print(i)
                                # print(duoi)
                                new_f = os.path.join(folder_path,f'{i}_{str(id_set[-1]+1)}.{duoi}')
                                os.rename(old_f,new_f)
                                print(f'da doi ten file {old_f} thanh {new_f}')
                            else:
                                old_f = os.path.join(folder_path,name_img)
                                new_f = os.path.join(folder_path,f'{i}.{duoi}')
                                # print(i)
                                # print(duoi)
                                os.rename(old_f,new_f)
                                print(f'da doi ten file {old_f} thanh {new_f}')
  
            else:
                pass

# checkUpdateImg('now')
# test()