from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

app=Flask(__name__)
app.secret_key="flash message"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'esakki123'
app.config['MYSQL_DB'] = 'python_db'

mysql=MySQL(app)


@app.route('/')
def Index():

    cur=mysql.connection.cursor()
    cur.execute("select * from crudapplication")
    data=cur.fetchall()
    cur.close()
    
    
    return render_template('index.html',crudapplication=data)



@app.route('/insert',methods=['POST'])
def insert():
    if request.method == 'POST':
        flash("Data Inserted Sucessfully")
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']

        cur=mysql.connection.cursor()
        cur.execute("insert into crudapplication(name,email,phone) values(%s,%s,%s)", (name,email,phone))
        mysql.connection.commit()
        return redirect(url_for('Index'))
    

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("""
        update crudapplication 
        set name= %s,email=%s,phone=%s
        where id=%s""",
        (name,email,phone,id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id_data>',methods=['POST','GET'])
def delete(id_data):
    
    flash("Data Deleted Sucessfully")
    cur = mysql.connection.cursor()
    cur.execute("delete from crudapplication where id=" + id_data)
    mysql.connection.commit()
    return redirect(url_for('Index'))

    


if __name__=="__main__":
    app.run(debug=True)

