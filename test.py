import json

with open("test.json") as jsonFile:
    data = json.load(jsonFile)

    jkeys = data.keys()

    for k  in jkeys:
        # print('type = ' ,type(data[k]))
        if type(data[k]) is list:
            for x in data[k]:
                if type(x) is dict:
                    keys = x.keys()
                    print(f'{k}.{list(keys)}')
                else:
                   print(k) 
        else:
            print(k)
