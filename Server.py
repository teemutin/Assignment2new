from xmlrpc.server import SimpleXMLRPCServer
import xml.etree.ElementTree as ET


def test(num1, num2):
    return num1 + num2

#def sendtext(topic2, note, text, time):
def sendtext(topic2, note, text, time):
    tree = ET.parse('notes.xml')
    root = tree.getroot()
    #for child in root:
        #nimi = child.get("")
        #print(child.tag, child.attrib)
        #print(child.attrib)
        #if child.attrib == topic:
            #print("Topic found")
        #else:
            #print("No topic found")
    for topic in root.findall("topic"):
        tname = topic.get("name")
        print("name is ",tname)


    return topic2,text,note,time
    #return



def start():
    port = 5001
    print("Server starting at")
    server = SimpleXMLRPCServer(("localhost", port))
    server.register_function(test,"test")
    server.register_function(sendtext,"sendtext")
    server.serve_forever()
    
start()