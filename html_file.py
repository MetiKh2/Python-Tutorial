f=open('hello.html','w')

message="""
<html>
<head><title>Hello World</title></head>
<body><h1>Hello World</h1></body>
</html>
"""

f.write(message)
f.close()   
