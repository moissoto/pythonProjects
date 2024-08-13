from flask import Flask, render_template

app = Flask('prueba')

@app.route('/entry')
def prueba () -> 'html':
    return render_template('entry.html')


app.run(debug=True)
    