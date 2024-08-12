from flask import Flask

app = Flask(__name__)

#below is showing dynamic URLs, and the type can be assigned
@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}, ini Zahirul"

#the type allowed is (from GeeksForGeeks)
# string    : It is the default type and it accepts any text without a slash.
# int       : It accepts positive integers.
# float     : It accepts positive floating-point values.
# path      : It is like a string but also accepts slashes.
# uuid      : It accepts UUID strings.
@app.route("/post/<int:id>")
def show_post(id):
    return f"Nilai {id}, tipe data {type(id)}"

@app.route("/")
def index():
    return "Halaman utama Zahirul"

#below is example for using app.add_url_rule()
def show_user(username):
    return f'Hello {username}!'
app.add_url_rule('/user/<username>', 'show_user', show_user)

if __name__=="__main__":
    app.run(debug=True)