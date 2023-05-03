import os
import requests
import json
import unicodedata
import ast

from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api
from json import dumps

# Disable HTTP Request warnings
import urllib3
urllib3.disable_warnings()

app = Flask(__name__)
api = Api(app)

applicationVersion = '1.0'
applicationTitle = 'Response Simulator %s' % (applicationVersion)
responseDataText = '%s is FuNnY :)' % (applicationTitle)
responseDataHtml = '<html><head><title>%s</title></head><body><h1>%s</h1><p>%s</p></body></html>' % (applicationTitle, applicationTitle, responseDataText)
responseDataJson = '{"responseSimulator": "%s"}' % (responseDataText)
responseDataXml = '<soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope"><soapenv:Body><soapenv:Fault><soapenv:Code><soapenv:Value>soapenv:Receiver</soapenv:Value></soapenv:Code><soapenv:Reason><soapenv:Text xml:lang="pt">%s</soapenv:Text></soapenv:Reason><soapenv:Detail>%s</soapenv:Detail></soapenv:Fault></soapenv:Body></soapenv:Envelope>' % (applicationTitle, responseDataText)
responseDataNotDefined = 'Oooooops... Response Type NOT Defined.'

def getResponseData(responseType):
    if responseType == 'text':
        return responseDataText
    elif responseType == 'html':
        return responseDataHtml
    elif responseType == 'json':
        return responseDataJson
    elif responseType == 'xml':
        return responseDataXml
    else:
        return responseDataNotDefined

contentTypeBase = 'Content-Type: %s; charset=utf-8'

def getContentType(responseType):
    if responseType == 'text':
        return contentTypeBase % ('text/plain')
    elif responseType == 'html':
        return contentTypeBase % ('text/html')
    elif responseType == 'json':
        return contentTypeBase % ('application/json')
    elif responseType == 'xml':
        return contentTypeBase % ('application/soap+xml')
    else:
        return contentTypeBase % ('text/plain')

class ResponseSimulator(Resource):
    def get(self, statusCode, responseType):
        responseType = responseType.lower()
        try:
            return Response(response=getResponseData(responseType),mimetype=getContentType(responseType),status=statusCode)
        except Exception as ex:
            print(ex)
            return Response(response='{"message": "%s"}' % ex,status=500)

api.add_resource(ResponseSimulator, '/<statusCode>/<responseType>')

# Main
if __name__ == '__main__':
    app.run(host='0.0.0.0',ssl_context='adhoc',port='5002',debug=True)
