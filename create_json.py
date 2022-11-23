import json

# Data to be written
dictionary = {
  "name": "SamurAi Collection",
  "symbol": "SAMU",
  "description": "DiscoSea.com SamurAi Collection",
  "image": "collection.png",
  "attributes": [],
  "properties": {
    "files": [
      {
        "uri": "collection.png",
        "type": "image/png"
      }
    ]
  }
}
 
# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("assets/collection.json", "w") as outfile:
    outfile.write(json_object)



for x in range(20000):

    print(x)
    dictionary = {
      "name": str(x),
      "symbol": "SAMU",
      "description": "DiscoSea.com SamurAi Collection",
      "image": str(x)+".png",
      "attributes": [
        {
          "trait_type":"lvl",
          "value": "0"
        }
      ],
      "properties": {
        "files": [
          {
            "uri": str(x)+".png",
            "type": "image/png"
          }
        ],
        "category":"image"
      }
    }
     
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    fileName = "assets/"+str(x)+".json"
     
    # Writing to sample.json
    with open(fileName, "w") as outfile:
        outfile.write(json_object)

