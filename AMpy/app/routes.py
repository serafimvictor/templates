from flask import Blueprint, render_template, request
from app.services.postgres import executar_query
from app.services.kafka import consumir_json

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    if request.method == "POST":
        tipo = request.form.get("tipo")
        if tipo == "PostgreSQL":
            query = request.form.get("query")
            df = executar_query(query)
            resultado = df.to_html()
        elif tipo == "Kafka":
            topico = request.form.get("topico")
            palavras = request.form.get("palavras").split(',')
            mensagens = consumir_json(topico, [p.strip().lower() for p in palavras])
            resultado = "<br>".join(f"[{m['timestamp']}] {m['mensagem']}" for m in mensagens)
    return render_template("index.html", resultado=resultado)
