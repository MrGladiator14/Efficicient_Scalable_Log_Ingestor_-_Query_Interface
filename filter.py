import streamlit as st
from elasticsearch import Elasticsearch
import re

def search_logs(es, query, filters):
    # Build the Elasticsearch query
    es_query = {
        "query": {
            "bool": {
                "must": {"regexp": {"message": query}} if query else {"match_all": {}},
                "filter": [
                    {"term": {field: value}} for field, value in filters.items() if value
                ]
            }
        }
    }

    if filters.get("timestamp_start") and filters.get("timestamp_end"):
        es_query["query"]["bool"]["filter"].append({
            "range": {
                "timestamp": {
                    "gte": filters["timestamp_start"],
                    "lte": filters["timestamp_end"]
                }
            }
        })
    search_results = es.search(index='test-index', body=es_query)
    return search_results.get('hits', {}).get('hits', [])

def main():
    # Elasticsearch connection settings
    ELASTIC_PASSWORD = "Enter Password"
    es = Elasticsearch(hosts="http://localhost:9200/", basic_auth=("elastic", ELASTIC_PASSWORD), verify_certs=False)
    st.set_page_config(page_title="Log Query App", page_icon="🕵🏽‍♀️", layout="wide")
    with st.container():
        left_column, right_column = st.columns(2)
        full_text_query = ""
        filters = {}
        with left_column:
            st.title("🕵🏽‍♀️Log Query App")
            st.subheader("Powered by Elasticsearch")
            full_text_query = st.text_input("Full-text search query:", "")
            try:
                re.compile(full_text_query)
                is_valid_regex = True
            except re.error:
                is_valid_regex = False

            if not is_valid_regex:
                st.warning("Invalid regular expression. Please enter a valid regular expression.")
                return

            filters = {
                "level": st.text_input("Level filter:", ""),
                "message": st.text_input("Message filter:", ""),
                "resourceId": st.text_input("Resource ID filter:", ""),
                "timestamp_start": st.text_input("Start Date (YYYY-MM-DD):", ""),
                "timestamp_end": st.text_input("End Date (YYYY-MM-DD):", ""),
                "traceId": st.text_input("Trace ID filter:", ""),
                "spanId": st.text_input("Span ID filter:", ""),
                "commit": st.text_input("Commit filter:", ""),
                "metadata.parentResourceId": st.text_input("Parent Resource ID filter:", "")
            }    
        with right_column:
            for i in range(0,11):
                st.write("\n")
            if st.button("Search"):
                st.subheader("Search Results:")
                search_results = search_logs(es, full_text_query, filters)
                for hit in search_results:
                    st.json(hit['_source'])

if __name__ == "__main__":
    main()
