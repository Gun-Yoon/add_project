import joblib
import os

def model_check(unknown_name):
    checking = 0
    path = "F:/Pycharmproject/add_project/HIS_base_UT/model/"
    file_list = os.listdir(path)
    model_list = [file for file in file_list if file.endswith(".pkl")]

    if unknown_name in model_list:
        checking = 1

    return checking

def model_save(model, unknown_name):
    file_name = unknown_name+'.pkl'
    joblib.dump(model,'F:/Pycharmproject/add_project/HIS_base_UT/model/'+file_name)

def model_load(unknown_name):
    file_name = unknown_name+'.pkl'
    model = joblib.load('F:/Pycharmproject/add_project/HIS_base_UT/model/'+file_name)
    print("Model Load")

    return model