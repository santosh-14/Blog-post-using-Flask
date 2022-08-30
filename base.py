
import dbmodule as db
from flask import *
app=Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/authorregister")
def author_log():
    return render_template("authorregister.html")

@app.route("/auth_data",methods=["POST"])
def fetch_auth():
    uname=request.form["uname"]
    pwd=request.form["pwd"]
    email=request.form["email"]
    city=request.form["city"]
    t=(uname,pwd,email,city)
    data=db.insert_data(t)
    return redirect("/")

@app.route("/authorlogin")
def auth_login():
    return render_template("authorlogin.html")

@app.route("/log_data",methods=["POST"])
def fetch_log():
    uname=request.form["uname"]
    pwd=request.form["pwd"]
    t=(uname,pwd)
    data=db.check_data(t)
    return render_template("authortable.html",res=data)

'''@app.route("/authorhome")
def au_home():
    return render_template("authorhome.html")'''

@app.route("/addpost/<int:id>")
def add_post(id):
    t=(id,)
    data=db.check_data2
    return render_template("addpost.html",res=data)

@app.route("/fetch_post",methods=["POST"])
def post_data():
    uname=request.form["uname"]
    title=request.form["title"]
    post=request.form["post"]
    t=(uname,title,post)
    data=db.insert_post(t)
    return redirect("/")

@app.route("/userregister")
def user_reg():
    return render_template("//userregister.html")
    
@app.route("/user_data",methods=["POST"])
def fetch_user():
    uname=request.form["uname"]
    pwd=request.form["pwd"]
    email=request.form["email"]
    city=request.form["city"]
    t=(uname,pwd,email,city)
    data=db.insert_userdata(t)
    return redirect("/")
@app.route("/userlogin")
def user_login():
    return render_template("userlogin.html")

@app.route("/use_data",methods=["POST"])
def fetch_us():
    uname=request.form["uname"]
    pwd=request.form["pwd"]
    t=(uname,pwd)
    data=db.check_userdata(t)
    return render_template("usertable.html",res=data)

@app.route("/viewpost/<string:uname>")
def v_post(uname):
    t=(uname,)
    data=db.display_authorposdata(t)
    return render_template("viewpostauthor.html",res=data)

@app.route("/viewpostuser")
def see_user():
    data=db.display_userdata()
    return render_template("viewpost.html",res=data)


@app.route("/edit_blog/<int:id>")
def sel_blog(id):
    t=(id,)
    data=db.display_editposdata(t)
    return render_template("editpost.html",res=data)

@app.route("/update_blog/<int:id>",methods=["POST"])
def update_blg(id):
    uname=request.form["uname"]
    title=request.form["title"]
    post=request.form["post"]
    t=(uname,title,post,id)
    data=db.update_post(t)
    return redirect("/")

@app.route("/delete_blog/<int:id>")
def del_blog(id):
    t=(id,)
    db.delete_data(t)
    return redirect("/")










    
if __name__=="__main__":
    app.run(debug=True)