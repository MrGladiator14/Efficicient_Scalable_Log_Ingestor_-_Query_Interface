from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)

# Elasticsearch connection settings
ELASTIC_PASSWORD = "Enter Password"
es = Elasticsearch(hosts="http://localhost:9200/", basic_auth=("elastic", ELASTIC_PASSWORD), verify_certs=False)


# Elasticsearch index name
es_index_name = 'test-index'

@app.route('/submit_log', methods=['POST'])
def submit_log():
    try:
        json_data = request.get_json()
        es.index(index=es_index_name, body=json_data)

        return jsonify({"message": "Log successfully indexed in Elasticsearch"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)
