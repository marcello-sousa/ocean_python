from flask import Flask, render_template

app = Flask(__name__)

#POST MOCK

posts = [
    {
        "Título": "Post 1",
        "Texto": "Meu primeiro blog"
    },
    {
        "Título": "Post 2",
        "Texto": "Meu segundo texto"
    }
]

@app.route("/")
def exibir_entradas():
    return render_template("exibir_entradas.html", entradas=posts)

@app.route("/pudim")
def pudim():
    return "Eu gosto de pudim"