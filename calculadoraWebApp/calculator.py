from flask import Flask, render_template

app = Flask('Calculadora')

@app.route('/')
def hola() -> 'html':
    return render_template ('entry.html', the_title="Bienvenido a la calculadora web con python")

app.run()