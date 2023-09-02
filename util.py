def GetTextUser(message):
    text= ""
    typeMessage =message["type"]


    if typeMessage == "text":
        text =(message["text"])["body"]


    elif typeMessage =="interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]

        if typeInteractive == "button_reply":
            text = (interactiveObject["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObject["list_reply"])["title"]
        else:
            print("no message")        
    else:
        print("no massage")

    return text


def TextMessage(text, number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "text": {
                "body": text
            },
            "type": "text"
           }
    return data

def ImageMessage(image_url ,number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "image",
            "image": {
                "link": image_url
            }
        }
    return data

def AudioMessage(audio_url, number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "audio",
            "audio": {
                "link": audio_url
            }
        }
    return data

def VideoMessage(video_url, number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "video",
            "video": {
                "link": video_url
            }
        }
    return data

def DocumentMessage(document_url, number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "document",
            "document": {
                "link": document_url
            }
        }
    return data

def LocationMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "location",
            "location": {
                "latitude": "-12.067158831865067",
                "longitude": "-77.03377940839486",
                "name": "Estadio Nacional del Perú",
                "address": "C. José Díaz s/n, Cercado de Lima 15046"
            }
        }
    return data

def ButtonsMessage(number,bodyText,buttonTitle1,buttonTitle2):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": bodyText
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "001",
                            "title": buttonTitle1
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "002",
                            "title": buttonTitle2
                        }
                    }
                ]
            }
        }
    }
    return data


def ListMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": "51943662964",
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "✅ I have these options"
            },
            "footer": {
                "text": "Select an option"
            },
            "action": {
                "button": "See options",
                "sections": [
                    {
                        "title": "Buy and sell products",
                        "rows": [
                            {
                                "id": "main-buy",
                                "title": "Buy",
                                "description": "Buy the best product your home"
                            },
                            {
                                "id": "main-sell",
                                "title": "Sell",
                                "description": "Sell your products"
                            }
                        ]
                    },
                    {
                        "title": "📍center of attention",
                        "rows": [
                            {
                                "id": "main-agency",
                                "title": "Agency",
                                "description": "Your can visit our agency"
                            },
                            {
                                "id": "main-contact",
                                "title": "Contact center",
                                "description": "One of our agents will assist you"
                            }
                        ]
                    }
                ]
            }
        }
    }
    return data

        
def button(buttonTitle):
    button = {
                        "type": "reply",
                        "reply": {
                            "id": "001",
                            "title": buttonTitle
                        }
    },
    return button


def OneButtonsMessage(number,bodyText,buttonTitle1):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": bodyText
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "001",
                            "title": buttonTitle1
                        }
                    },"",
                ]
            }
        }
    }
    return data