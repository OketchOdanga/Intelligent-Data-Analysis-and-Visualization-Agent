def parse_natural_language(query: str) -> dict:
    print("[GeminiMock] Parsing natural language query")
    return {"pipeline": ["ingest_csv", "clean_data", "analyze_data", "generate_plot"]}
