import imp
from flask import Flask, render_template
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

    sql = ""
    conn= mysql.connect()
    curso=

    return render_template('empleados/index.html')


if __name__ == '__main__':
    app.run(debug=True)