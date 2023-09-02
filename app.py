from flask import Flask, request
import util
import whatsappservice
import chatgptservice
from pymongo import MongoClient



cluster = MongoClient("mongodb+srv://crance:crance@mybot.2vmns1f.mongodb.net/?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)

db = cluster["Tobaco"]
users = db["users"]




app = Flask(__name__)
@app.route('/welcome',methods= ['GET'])
def index():
    return "welcome crance"

@app.route('/whatsapp',methods= ['GET'])
def VerifyToken():
    try:
        accessToken = "78SAJSNJANS76S8DSHDBSBDS"
        token =request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token != None and challenge != None and token == accessToken:
            return challenge

        else:
            return "", 400

        
    except:
        return "", 400

status = {}
@app.route('/whatsapp',methods= ['POST'])
def RecievedMessage():
    

    try:
        body = request.get_json()
        entry =(body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        message =(value["messages"])[0]
        number =message["from"]
        text = util.GetTextUser(message)
        responseGPT = chatgptservice.GetResponse(text)

        if responseGPT != "error":
            data = util.TextMessage(responseGPT,number)
        else:
            data = util.TextMessage("Error occured try aggain later", number)
        # whatsappservice.SendMessageWhatsapp(data)

        print(text)
        
        ProcessMessage(text,number)

        return "EVENT_RECEIVED"
    except:
        return "EVENT_RECEIVED"
    

def ProcessMessage(text, number):
    user = users.find_one({"number": number})
    print("1.0")
    
    print("1.0.0")
    text =text.lower()
    listData = []
    
    if not bool(user):
        
        buttonMessage = util.ButtonsMessage(number,"Boost your veggie farm success! Register for expert guidance now!","Register","About Us")
        listData.append(buttonMessage)
        users.insert_one({"number": number, "status": "welcome", "messages": []})
        print("1.3") 
        # status[number] = "main"
        
        
    # elif text == "about us" & user["staus"] == "welcome":
    #     url = "https://youtu.be/FSMdzc3GyVY"
    #     dataVideo = util.VideoMessage(url, number )
    #     listData.append(dataVideo)
        
    #     buttonMessage = util.OneButtonsMessage(number,"Boost your veggie farm success! Register for expert guidance now!","Register")
    #     listData.append(buttonMessage)
    #     users.insert_one({"number": number, "status": "welcome", "messages": []})

    elif user["status"] == "welcome":
        # if text == "about us":
            
        #     dataVideo = util.VideoMessage("https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/video_whatsapp.mp4", number )
        #     listData.append(dataVideo)
        #     buttonMessage = util.ButtonsMessage(number,"Boost your veggie farm success! Register for expert guidance now!","Register","About Us")
        #     listData.append(buttonMessage)
        #     users.update_one({"number": number, "status": "welcome"})

        # elif text == "register":
        data = util.TextMessage("Welcome to our vegetable farmer registration! To get started, I'll need some information from you. Please provide your full name", number)
        listData.append(data)
        users.update_one(
            {"number": number}, {"$set": {"status": "user_name"}})




    elif user["status"] == "user_name":
        
        users.update_one(
            {"number": number}, {"$set": {"name": text}})
        
        data = util.TextMessage("Thank you, "+text+". Next, please provide your phone number.", number)
        listData.append(data)
        users.update_one(
            {"number": number}, {"$set": {"status": "user_phone"}})
        
    elif user["status"] == "user_phone":
        phone = text
        users.update_one(
            {"number": number}, {"$set": {"phone": phone}})
        data = util.TextMessage("Great! Lastly, could you please provide your farm's address?", number)
        listData.append(data)
        users.update_one(
            {"number": number}, {"$set": {"status": "user_address"}})
        

    elif user["status"] == "user_address":
        address = text
        users.update_one(
            {"number": number}, {"$set": {"address": address}})
        #name = user["name"]
        # phone = user["phone"]
        # address = user["address"]
        
        data = util.TextMessage("Thank you, "+user['name']+"! I have registered you as a tobacco farmer with the following details:\nName: "+user['name']+"\nPhone number: "+user['phone']+"\nFarm address: "+user['address']+"", number)
        listData.append(data)
        users.update_one(
            {"number": number}, {"$set": {"status": "main"}})
    

    else:
        data = util.TextMessage("I'm not understanding you. talk later!", number)
        listData.append(data)


    for item in listData:
        whatsappservice.SendMessageWhatsapp(item)
    listData.clear()


if(__name__ == "__main__"):
    app.run()