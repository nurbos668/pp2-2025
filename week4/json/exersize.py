import json

with open("sample-data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")

for imdata in data["imdata"]:
    for i in imdata:
        for j in imdata[i]:
            print(imdata[i][j]["dn"] + " " * 31 + imdata[i][j]["speed"] + "  " + imdata[i][j]["mtu"])