import os
import json
import pytest
from pytest_bdd import scenarios,parsers,given,when,then
from main import *
from configparser import ConfigParser

CONVERTERS={
    'files':str,
    'S_files':str,
    'code':int,
    'TF':str
}

path_file=os.path.dirname(__file__)
file=path_file+'/config.ini'

config=ConfigParser()
config.read(file)

API1_API=config['BULK-OCR']['API']

API1_hdr_json=json.loads(config['BULK-OCR']['headers'])
API1_hdr_multipart=json.loads(config['BULK-OCR']['headers1'])

scenarios('features/test_API1.feature',example_converters=CONVERTERS)

def test_API1():
    pass

@pytest.fixture
@when('Execute the API with given <pdf_files> json where having 2 pdf file only')
def step_API1_pdf(pdf_files):
    with open(pdf_files,encoding='utf-8') as API1:
        API1_input=json.load(API1)
    API1_output=main(API1_API,API1_hdr_json,API1_input)
    return API1_output

@then('response should be <code> for pdf')
def step_reponse_API1_pdf(step_API1_pdf,code):
    assert step_API1_pdf[0]==code
    assert len(step_API1_pdf[1][0].get('content'))!=0
    assert len(step_API1_pdf[1][1].get('content'))!=0

@pytest.fixture
@when('Execute the API1 with given <files> json with multipart content-type')
def step_API1_multipart(files):
    with open(files,encoding='utf-8') as API1:
        API1_input=json.load(API1)
    API1_output=main(API1_API,API1_hdr_multipart,API1_input)
    return API1_output

@then('response should be <code> for multipart')
def step_reponse_API1_doc(step_API1_multipart,code):
    assert step_API1_multipart[0]==code
    assert len(step_API1_multipart[1][0].get('content'))!=0
    assert len(step_API1_multipart[1][1].get('content'))!=0

@pytest.fixture
@when('Execute the given <callback_files> in bulk-OCR')
def step_API1_202(callback_files):
    with open(callback_files,encoding='utf-8') as API1:
        API1_input=json.load(API1)
    API1_output_202=main(API1_API,API1_hdr_json,API1_input)
    return API1_output_202

@then('response should be <call_res> with parent and task id')
def step_API1_202_res(step_API1_202,call_res):
    assert str(step_API1_202[0])==call_res
    assert step_API1_202[1].get('parent_id')!=0
    assert step_API1_202[1].get('task_id')!=0

@pytest.fixture
@when('Execute the given <Sch_files> in bulk-OCR to check schema')
def step_API1_schema(Sch_files):
    with open(Sch_files,encoding='utf-8') as API1:
        API1_input=json.load(API1)
    API1_output=main(API1_API,API1_hdr_json,API1_input)
    return API1_output

@then('response should be <boolean> for the given <schema>')
def step_check_schema(step_API1_schema,schema,boolean):
    API1_schema=[]
    for sch_item in step_API1_schema[1][0]:
        API1_schema.append(sch_item.lower())
    schema=schema.lower()
    schema=list(schema.split(", "))
    assert str(set(schema).issubset(set(API1_schema)))==boolean

@pytest.fixture
@when('Execute bulk-OCR with blank file')
def API1_empty_json():
    json={}
    API1_output=main(API1_API,API1_hdr_json,json)
    return API1_output

@then('response should be <blank_res>')
def API1_empty_json_res(API1_empty_json,blank_res):
    assert API1_empty_json==400