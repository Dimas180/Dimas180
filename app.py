from flask import Flask, render_template, request,flash,redirect,url_for
import sqlite3

app = Flask(__name__)

def get_bd_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection



@app.route('/')
def draw_main_page():
    conn = get_bd_connection()
    posts = conn.execute('select * from posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/create', methods = ("GET", "POST"))

def create():


    if request.method == "POST":
        title = request.form("title")
        content = request.form("content")

        if not title:
            flash("Title is required")
        else:

            conn = get_bd_connection()
            conn.execute('insert into posts (title, content) VALUES  (?, ?)',
                        (title,content))
            conn.commit()
            conn.close()
            return redirect(url_for('draw_main_page'))
    return render_template("create.html")






@app.route('/about')
def about():
    return render_template("about.html")

if __name__== "__main__":
    app.run()
