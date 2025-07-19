from confluent_kafka import Consumer
import json
import time
from app.config.settings import KAFKA_CONFIG

def consumir_json(topico, palavras_chave, group_id='web-group', timeout=10):
    conf = {
        'bootstrap.servers': KAFKA_CONFIG['bootstrap.servers'],
        'group.id': group_id,
        'auto.offset.reset': 'earliest',
        'security.protocol': KAFKA_CONFIG['security.protocol'],
        'sasl.mechanism': KAFKA_CONFIG['sasl.mechanism'],
        'sasl.username': KAFKA_CONFIG['sasl.username'],
        'sasl.password': KAFKA_CONFIG['sasl.password']
    }

    consumer = Consumer(conf)
    consumer.subscribe([topico])
    mensagens = []

    inicio = time.time()
    while time.time() - inicio < timeout:
        msg = consumer.poll(1.0)
        if msg and not msg.error():
            try:
                valor = json.loads(msg.value().decode('utf-8'))
                texto = json.dumps(valor).lower()
                if any(p in texto for p in palavras_chave):
                    mensagens.append({
                        'timestamp': msg.timestamp()[1],
                        'mensagem': valor
                    })
            except Exception:
                pass
    consumer.close()
    return sorted(mensagens, key=lambda x: x['timestamp'])



## Exemplo de uso

# if __name__ == "__main__":
#     topico = input("Nome do tópico Kafka: ")
#     palavras = input("Palavras-chave (separadas por vírgula): ").split(',')

#     resultados = consultar_kafka_json_sasl_ssl_env(
#         topico=topico.strip(),
#         palavras_chave=[p.strip() for p in palavras],
#         timeout=15
#     )

#     for r in resultados:
#         ts = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(r['timestamp']/1000))
#         print(f"[{ts}] {json.dumps(r['mensagem'], ensure_ascii=False)}")
