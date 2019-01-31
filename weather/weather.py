import json
import xmltodict

file = open("weather.xml", "r") 
xml = file.read()

print("XML : ")
print(xml)
     
jsonString = json.dumps(xmltodict.parse(xmlString,attr_prefix='',cdata_key=''),indent = 2)

print("json : ")
print(jsonString)
outputFile = "weather.json" 
file = open(outputFile, "w") 
file.write(jsonString)
