import os
import json

os.chdir('C:\\Path\\To\\File')

for files in os.listdir("C:\\Path\\To\\File"):
    files.split('.')
    name = files[0]
    metadata = {
        "name": "Collection_Name",
        "symbol": "GLO",
        "image": "{}.gif".format(name),
        "properties": {
            "files": [
                {
                    "uri": "{}.gif".format(name),
                    "type": "image/gif"
                }
            ],
            "category": "image",
            "creators": [
                {
                    "address": "SOLFLR15asd9d21325bsadythp547912501b",
                    "share": 100
                }
            ]
        },
        "description": "Collection_Description",
        "seller_fee_basis_points": 500,
        "collection": {
            "name": "Collection_Name",
            "family": "Collection_Family"
        }
    }




    with open('{}.json'.format(name), 'w') as f:
        # where data is your valid python dictionary
        json.dump(metadata, f)
