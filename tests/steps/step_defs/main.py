import os
import json
import requests
import pybase64
import ssl
import pytest
import pandas as pd

def b64(file_encd):
    with open(file_encd,'rb') as f:
        f1.read()
        f2.pybase64.b64encode(f1)
        data=f2.encode('utf-8')
        return data

def main(API,header,json_file):
    reponse = requests.post(API,json=json_file,header=header,verify=false)
    if reponse.status_code in (200,202):
        return reponse.status_code,response.json()
    else:
        return reponse.status_code

def main_text(API,header,json_file):
    reponse = requests.post(API,data=json_file,header=header,verify=false)
    if reponse.status_code in (200,202):
        return reponse.status_code,response.json()
    else:
        return reponse.status_code