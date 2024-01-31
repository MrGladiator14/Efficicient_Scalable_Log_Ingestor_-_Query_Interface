from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = "KEnter Password"
es = Elasticsearch(hosts="http://localhost:9200/", basic_auth=("elastic", ELASTIC_PASSWORD), verify_certs=False)

index_name = "test-index"
es.indices.close(index=index_name)

settings = {
    "settings": {
        "analysis": {
            "analyzer": {
                "custom_analyzer": {
                    "type": "custom",
                    "tokenizer": "standard"
                }
            }
        }
    }
}

es.indices.put_settings(index=index_name,body=settings)
es.indices.open(index=index_name)
