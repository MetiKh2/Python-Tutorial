import json

# #json
# # x='{"name":"john","age":20,"city":"New York"}'
# x={
#    "name":"john",
#    "age":20,
#    "city":"New York"
# }

# #parse json
# # y=json.loads(x)

# #convert into json
# y=json.dumps(x)

# #the result is a python dictionary

# #the result is a json string
# print(y)




# print(json.dumps({"name":"john" ,"age":20}))
# print(json.dumps(["banana",'apple']))
# print(json.dumps(("banana",'apple')))
# print(json.dumps('hello'))
# print(json.dumps(4))
# print(json.dumps(4.5))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))


x={
    "name": "John",
    "age": 20,
    "married":True,
    "children":("Ann",'Billy'),
    "pets":None,
    "cars":[
        {"model":"BMW 230","mpg":27.5},
        {"model":"Ford Edge","mpg":24.1},
    ]
}

print(json.dumps(x,indent=4,separators=('. ',' = '),sort_keys=True))




