from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def about_aesma():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5151, host="0.0.0.0", debug=True)
