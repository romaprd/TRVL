from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/nova_viagem')
def nova_viagem():
    destino = request.args.get('destino', '')  # Captura o destino passado na URL
    return render_template('nova_viagem.html', destino=destino)

if __name__ == '__main__':
    app.run(debug=True)
