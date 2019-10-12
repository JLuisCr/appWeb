from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def entrar():
    return render_template('entrar.html')

@app.route('/raiz')
def raiz():
    return render_template('raiz.html')

@app.route('/menu')
def about():
    return render_template('menu.html') 

@app.route('/registro')
def registro():
    return render_template('registro.html') 

if __name__ == '__main__':
    app.run(debug=True)