from flask import Flask, render_template, redirect, url_for
from flask import request, abort
from DB_Functions import *
from Settings import *

app = Flask(__name__, template_folder='Models')
app.redirect

 
@app.route("/") # redirect to main page
def redir():
    return redirect(url_for('base'))

@app.route("/base") # main page
def base():
    return render_template('htmlsite.html', productList=get_products(Table=TABLE))

@app.route('/base/create', methods = ['GET','POST']) # create form page
def create():
    if request.method == "GET":
        return render_template('index.html')
    
    if request.method == 'POST':
        return redirect(url_for('base'))

@app.route('/base/<int:id>/delete', methods=['GET','POST']) # delete entity
def delete(id):
    product = products.select().where(products.ProdID == id)
    if request.method == 'POST':
        if product:
            delete_product_byID(Table=TABLE, ID=id)
            return redirect('/base')
        abort(404)
    
    return render_template('delete.html')

@app.route("/base/<int:id>/update", methods = ['GET','POST'])
def update():
    if request.method == "GET":
        return render_template('index.html')
    
    if request.method == 'POST':
        return redirect(url_for('base'))
 
if __name__ == "__main__":
    app.run(debug=True)