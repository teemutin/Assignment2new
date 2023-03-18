from xmlrpc.server import SimpleXMLRPCServer
import xml.etree.ElementTree as ET


def test(num1, num2):
    return num1 + num2

#def sendtext(topic2, note, text, time):
def sendtext(topic2, note, text, time):
    tree = ET.parse('testi.xml')
    root = tree.getroot()
    check = False
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
        #if match to old topic, append other data to it
        if tname == topic2:
            
            print("Match on topic")
            check = True
            newnote = ET.SubElement(topic, "note")
            newtext = ET.SubElement(newnote, "text")
            newtext.text = text
            newtim = ET.SubElement(newnote, "timestamp")
            newtim.text = time
            #ET.dump(root)
            newtree = ET.ElementTree(root)
            newtree.write("testi.xml")



    #If no previous note topic found, create a new one
    if check == False:
        print("No previous note on this topic")
        #newentry = ET.SubElement(tree, "topic")
        #ET.SubElement(topic, "topic", name=note, text=text)
        #top = ET.SubElement(root, "Topic")
        top = ET.Element("Topic", name=topic2)
        nott = ET.SubElement(top, "note", name=note)
        txt = ET.SubElement(nott, "text")
        txt.text = text
        tim = ET.SubElement(nott, "timestamp")
        tim.text = time
        
        #tree = ET.ElementTree(top)
        #tree = ET.Element(top)
        #tree.write("test.xml")
        root.append(top)
        #tree.write("test.xml")
        #ET.dump(root)
        newtree = ET.ElementTree(root)
        newtree.write("testi.xml")





    return topic2,text,note,time
    #return


#start and serve the server, and functions
def start():
    port = 5001
    print("Server starting at")
    server = SimpleXMLRPCServer(("localhost", port))
    server.register_function(test,"test")
    server.register_function(sendtext,"sendtext")
    server.serve_forever()
    
start()