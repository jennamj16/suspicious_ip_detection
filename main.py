from flask import Blueprint, render_template
import pandas as pd
import plotly.express as px
import os

main_bp = Blueprint('main', __name__)

# Define the path to the dataset
DATA_PATH = os.path.join('data', 'network_logs_with_anomalies.csv')

def load_anomalies():
    """Load anomaly data from CSV if it exists."""
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        return df
    else:
        return pd.DataFrame()  # Return empty dataframe if file is missing

@main_bp.route('/')
def dashboard():
    """Render the dashboard with anomaly visualization."""
    df = load_anomalies()
    
    if df.empty:
        return "<h2>No anomaly data available. Please ensure the system is capturing traffic.</h2>"

    # Count anomalies
    anomaly_counts = df['anomaly'].value_counts().sort_index()

    # Create visualization
    fig = px.bar(x=anomaly_counts.index, y=anomaly_counts.values, 
                 labels={'x': 'Anomaly (1: Anomaly, -1: Normal)', 'y': 'Count'},
                 title='Anomaly Detection Overview')

    graph_html = fig.to_html(full_html=False)
    return render_template('index.html', graph=graph_html)
