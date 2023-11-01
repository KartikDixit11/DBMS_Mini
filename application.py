from flask import render_template,Flask,jsonify,request
from flask_mysqldb import MySQL

app=Flask(__name__)
import datetime as dt

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Kartik@11'
app.config['MYSQL_DB']='DBMS_APP'
sql=MySQL(app)


def data_extract(tbname):
    conn=sql.connection
    cur=conn.cursor()
    cura=conn.cursor()
    cur.execute(f"SELECT Sr_no,question,option1,option2,option3,option4 from {tbname}")
    cura.execute(f"SELECT answer from {tbname}")
    data=cur.fetchall()
    ans=cura.fetchall()
    return data,ans

def score(exam):
     conn=sql.connection
     cur=conn.cursor()
     cur.execute(f"SELECT * FROM {exam} order by score desc")
     data=cur.fetchall()
     return data    

##Login and Landing
@app.route("/")
def landing():
    return render_template("index.html")

@app.route('/login/')
def render():
    return "Hello world"

@app.route('/signup/',methods=["GET","POST"])
def signup():
    if(request.method=='POST'):
            pass

##Leaderboards
@app.route('/score/')
def leader():
    return render_template("exam_ID.html")

@app.route('/score/ML/',methods=["POST","GET"])
def ml_score():
      if request.method=='POST':
        sc=score("leader_board_ml")
        n=len(sc)
        return render_template("leaderboard.html",Exam=sc,n=n,db="Machine Learning")

@app.route('/score/Web/',methods=["POST","GET"])
def web_score():
      if request.method=='POST':
        sc=score("leader_board_web")
        n=len(sc)
        return render_template("leaderboard.html",Exam=sc,n=n,db="Web Development")

@app.route('/score/Android/',methods=["POST","GET"])
def android_score():
      if request.method=='POST':
        sc=score("leader_board_android")
        n=len(sc)
        return render_template("leaderboard.html",Exam=sc,n=n,db="Android Development")

@app.route('/score/Cloud/',methods=["POST","GET"])
def cloud_score():
      if request.method=='POST':
        sc=score("leader_board_cloud")
        n=len(sc)
        return render_template("leaderboard.html",Exam=sc,n=n,db="Cloud Computing")
      
##Exams
@app.route('/examWb/' ,methods=["GET","POST"])
def Web():
     if request.method=="POST":
                try:
                    global data
                    global ans
                    data,ans=data_extract("web")

                    return render_template("questions.html",questions=data)
                except:
                      return "Unknow Error Occured"


@app.route('/examCloud/' ,methods=["GET","POST"])
def cloud():
    if request.method=="POST":
                try:
                    global data
                    global ans
                    data,ans=data_extract("cloud")
                    return render_template("questions.html",questions=data)
                except:
                      return "Unknow Error Occured"


@app.route('/examML/' ,methods=["GET","POST"])
def ML():
    if request.method=="POST":
                try:
                    global data
                    global ans
                    data,ans=data_extract("ML")

                    return render_template("questions.html",questions=data)
                except:
                      return "Unknow Error Occured"


@app.route('/examAndroid/' ,methods=["GET","POST"])
def Android():
     if request.method=="POST":
                try:
                    global data
                    global ans
                    data,ans=data_extract("android")

                    return render_template("questions.html",questions=data)
                except Exception as e:
                      print(e)
                      
                return "hello"
                      

@app.route('/result/',methods=["GET","POST"] )
def result():
      attempted=0
      correct=0
      if(request.method=='POST'):
            for i in range(20):
                  try:
                     index=int(request.form[str(i+1)])-1
                     attempted+=1
                     if(data[i][2+index]==list(ans[i])[0]):
                           correct+=1
                  except:
                        continue
      lb=sql.connection
      cur=lb.cursor()

      return render_template("result.html",att=attempted,cor=correct,marks=correct*2,outof=40)


if (__name__=="__main__"):
    app.run(host="0.0.0.0",debug=True)