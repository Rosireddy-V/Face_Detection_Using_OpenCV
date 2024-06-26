from flask import Flask,redirect,url_for, render_template, request

app=Flask(__name__)

@app.route('/')
def welcome():
   return render_template('index.html')

@app.route('/hobby/<activity>')
def hobby(activity):
   return "Hi my name is angel and my hobby is "+activity

@app.route('/study/<education>')
def study(education):
   return "Hi my name is angel and I am studying "+education

@app.route('/fail/<int:marks>')
def fail(marks):
   res=""
   if marks:
      res="FAIL"
   return render_template('results.html',result=res)

@app.route('/success/<int:marks>')
def success(marks):
   res=""
   if marks:
      res="PASS"
   return render_template('results.html',result=res)


@app.route('/result/<int:marks>')
def result(marks):
   results=''
   if marks<=50:
      results='fail'
   else:
      results='success'
      

   return redirect(url_for(results,marks=marks))

@app.route('/submit',methods=['POST','GET'])
def submit():
   total_score=0 
   if request.method=='POST':
      science=float(request.form['science'])
      maths=float(request.form['maths'])
      c=float(request.form['c'])
      data_science=float(request.form['datascience'])
      total_score=(science+maths+c+data_science)/4
    
   res=""
   if total_score>=50:
      res="success"
   else:
      res='fail'
    
   return redirect(url_for(res,marks=total_score))
   

if __name__=='__main__':
   app.run(debug=True) 