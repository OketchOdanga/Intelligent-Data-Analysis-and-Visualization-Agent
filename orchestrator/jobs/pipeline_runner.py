from agents.ingest.csv_ingest import ingest_csv
from agents.clean.cleaner import clean_data
from agents.analysis.dummy_analysis import analyze_data
from agents.visualize.plotter import generate_plot

def run_pipeline():
    raw = ingest_csv("dummy.csv")
    cleaned = clean_data(raw)
    analysis = analyze_data(cleaned)
    viz = generate_plot(analysis)
    return viz
