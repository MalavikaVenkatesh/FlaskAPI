from flask import Flask 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Malu :) !"

@app.route("/sai")
def malu():
    return "Hello Sai Idiot :) !"



if __name__ == "__main__":
    app.run(debug= True)


# REAL REST API todo : 

# 1. CRUD 
# 2. SQLite as DB 
# 3. JSON based Request & Response
# 4. postman based testing for our API
# 
# 
# Step 1 - 
# 
# Install these libs- 
# 
# 1. pip install flask_sqlalchemy
# 2. pip install flask_marshmallow
# 3. pip install marshmallow-sqlalchemy
# 
# 
#  