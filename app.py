from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app= Flask(__name__)

mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema'
mysql.init_app(app)


@app.route('/')
def index():
    return render_template('empleados/index.html')


@app.route('/create')
def create():
    return render_template('empleados/create.html')

@app.route('/store', methods=['POST'])
def storage():
    _name=request.form['txt_name']
    _last_name=request.form['txt_last_name']
    _email=request.form['txt_email']
    _photo=request.files['txt_photo']

    sql = "INSERT INTO `empleados` (`id`, `name`, `last_name`, `email`, `photo`) VALUES (NULL, %s, %s, %s, %s);"
    
    datos=(_name,_last_name,_email,_photo.filename)

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()

    return render_template('empleados/index.html')


if __name__ == '__main__':
    app.run(debug=True)