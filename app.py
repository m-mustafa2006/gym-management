from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Simulate login logic
        username = request.form["username"]
        password = request.form["password"]
        return f"Welcome {username}!"
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Simulate registration logic
        full_name = request.form["full_name"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        return f"Registration complete for {username}!"
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
