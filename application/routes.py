from flask import Blueprint,jsonify,request
from fiel.util import UtillsMain

main=Blueprint("main",__name__)
obj=UtillsMain()
@main.route("/")
def home():
    return jsonify({"message":"hello welcome to html code downloader!!"})
@main.route("/download",methods =['POST'])
def download():#eg:{"id":2,"url":https://tirupatitirumalainfo.com/gokulashtami/}
    id=request.get_json()
    val=obj.Download_content(id)
    return val
@main.route("/Read",methods=["GET"])
def readData():#example: {"id":2}
    data=request.get_json()
    val=obj.Read_content(id=data)
    return val
