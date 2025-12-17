import requests,os
# import jsonify
import shutil
class NotWritable(Exception):
    pass
class UtillsMain:
    def __init__(self):
        # self.__names=os.listdir("inp")
        self.__ids={}#{"id":"filename"} to keep track on existance of data
        if os.path.exists("inp"):#to delete the existing data when server refresh
            for dirpath, dirnames, filenames in os.walk("inp"):
                for filename in filenames:
                    os.remove(os.path.join(dirpath, filename))
    def Download_content(self,id):
        # print(self.__ids)
        content=requests.get(id["url"])#id={"id":2,"url":"https://tirupatitirumalainfo.com/gokulashtami/"}
        n=id["url"].split("/")
        if id["id"] not in self.__ids:
            # print(n[-1])
            self.__ids[id["id"]]=f"{n[-2]}"#updating the hashtable
            try:
                with open(f"inp/{n[-2]}.txt",'w') as f:
                    if f.writable():
                        f.write(content.text)
                    else:
                        raise NotWritable("content is not writable !!")
            except Exception as e:
                return {"message":f"{e}!"}   
            return {"message":f"successfully added {n[-2]}"}
        else:
            return {"message":"Id already exists"}
    
    
    def Read_content(self,id):
        if id["id"] not in self.__ids.keys():
            return {"message":f"Item is not exist!!{self.__ids}"}
        else:
            try:
                with open(f"inp/{self.__ids[id["id"]]}.txt",'r') as f:
                    if f.readable():
                        sentance=f.readlines()
            except Exception as e:
                return {"message":f" {self.__ids["id"]}"}
            sentance=" ".join(i for i in sentance)
            return {"data":sentance}