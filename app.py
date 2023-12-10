# Python file (app.py)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
<html>
<body>
<center>
<h1>Demo on GitOps with ArgoCD and Github Actions.</h1> <br>
<br>
<img src="https://github.com/kamnigs1993/argo-cd/blob/main/itsworking.jpeg?raw=true">
</center>
</body>
</html>
'''
