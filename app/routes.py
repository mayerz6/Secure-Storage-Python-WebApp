from app import app

@app.route("/")
@app.route("/index")
def index():
    return "<h2>Initial Flask MVC Web Application</h2>"