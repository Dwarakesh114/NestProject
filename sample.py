import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import re

# Load Data
file_path = "response.json"
eligibilities_path = "eligibilities.txt"

with open(file_path, "r") as file:
    data = json.load(file)

eligibilities = pd.read_csv(eligibilities_path, delimiter="|")

# Extract relevant fields and merge
trials = []
for study in data.get("studies", []):
    protocol = study.get("protocolSection", {})
    outcomes = protocol.get("outcomesModule", {})
    eligibility = protocol.get("eligibilityModule", {})
    
    nct_id = protocol.get("identificationModule", {}).get("nctId", "")
    study_title = protocol.get("identificationModule", {}).get("briefTitle", "")
    primary_outcomes = " ".join(outcome.get("measure", "") for outcome in outcomes.get("primaryOutcomes", []))
    secondary_outcomes = " ".join(outcome.get("measure", "") for outcome in outcomes.get("secondaryOutcomes", []))
    conditions = ", ".join(protocol.get("conditionsModule", {}).get("conditions", []))
    interventions = ", ".join(i.get("name", "") for i in protocol.get("armsInterventionsModule", {}).get("interventions", []))
    phases = ", ".join(protocol.get("designModule", {}).get("phases", []))
    criteria = eligibility.get("eligibilityCriteria", "")
    amendments = protocol.get("amendments", [])

    trials.append({
        "NCT ID": nct_id,
        "Study Title": study_title,
        "Primary Outcome Measures": primary_outcomes,
        "Secondary Outcome Measures": secondary_outcomes,
        "Conditions": conditions,
        "Interventions": interventions,
        "Phases": phases,
        "Criteria": criteria,
        "Amendments": len(amendments),
    })

df = pd.DataFrame(trials)
df = df.merge(eligibilities, how="left", left_on="NCT ID", right_on="nct_id")

# Clean and preprocess the data
def clean_text(text):
    if pd.isnull(text):
        return ""
    text = re.sub(r"[^a-zA-Z0-9\s,]", "", text)
    return text.lower().strip()

columns_to_clean = [
    "Study Title", "Primary Outcome Measures", "Secondary Outcome Measures",
    "Conditions", "Interventions", "Phases", "Criteria"
]
for col in columns_to_clean:
    df[col] = df[col].apply(clean_text)

# Combine fields with weights
weights = {
    "Study Title": 1,
    "Primary Outcome Measures": 1.5,
    "Secondary Outcome Measures": 1,
    "Conditions": 2,
    "Interventions": 1.5,
    "Phases": 2,
    "Criteria": 2.5
}

df["combined"] = (
    df["Study Title"] + " " +
    df["Primary Outcome Measures"] + " " +
    df["Secondary Outcome Measures"] + " " +
    df["Conditions"] + " " +
    df["Interventions"] + " " +
    df["Phases"] + " " +
    df["Criteria"]
)

# Compute similarity
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["combined"])
similarity_matrix = cosine_similarity(tfidf_matrix)

# Function to get similar trials
def get_similar_trials(nct_id, top_n=10):
    if nct_id not in df["NCT ID"].values:
        return []
    index = df[df["NCT ID"] == nct_id].index[0]
    scores = list(enumerate(similarity_matrix[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    similar_trials = [{"NCT ID": df.iloc[i]["NCT ID"], "Similarity": score} for i, score in scores[1:top_n+1]]
    return similar_trials

# Dash App
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

# Navbar
navbar = dbc.Navbar(
    dbc.Container([dbc.NavbarBrand("Clinical Trials Dashboard", className="ms-2 text-primary", style={"fontSize": "1.5rem"})]),
    color="light", dark=False, className="mb-4"
)

# Dashboard Layout
import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import re

# Load Data
file_path = "response.json"
eligibilities_path = "eligibilities.txt"

with open(file_path, "r") as file:
    data = json.load(file)

eligibilities = pd.read_csv(eligibilities_path, delimiter="|")

# Extract relevant fields and merge
trials = []
for study in data.get("studies", []):
    protocol = study.get("protocolSection", {})
    outcomes = protocol.get("outcomesModule", {})
    eligibility = protocol.get("eligibilityModule", {})

    nct_id = protocol.get("identificationModule", {}).get("nctId", "")
    study_title = protocol.get("identificationModule", {}).get("briefTitle", "")
    primary_outcomes = " ".join(outcome.get("measure", "") for outcome in outcomes.get("primaryOutcomes", []))
    secondary_outcomes = " ".join(outcome.get("measure", "") for outcome in outcomes.get("secondaryOutcomes", []))
    conditions = ", ".join(protocol.get("conditionsModule", {}).get("conditions", []))
    interventions = ", ".join(i.get("name", "") for i in protocol.get("armsInterventionsModule", {}).get("interventions", []))
    phases = ", ".join(protocol.get("designModule", {}).get("phases", []))
    criteria = eligibility.get("eligibilityCriteria", "")
    amendments = protocol.get("amendments", [])

    trials.append({
        "NCT ID": nct_id,
        "Study Title": study_title,
        "Primary Outcome Measures": primary_outcomes,
        "Secondary Outcome Measures": secondary_outcomes,
        "Conditions": conditions,
        "Interventions": interventions,
        "Phases": phases,
        "Criteria": criteria,
        "Amendments": len(amendments),
    })

df = pd.DataFrame(trials)
df = df.merge(eligibilities, how="left", left_on="NCT ID", right_on="nct_id")

# Clean and preprocess the data
def clean_text(text):
    if pd.isnull(text):
        return ""
    text = re.sub(r"[^a-zA-Z0-9\s,]", "", text)
    return text.lower().strip()

columns_to_clean = [
    "Study Title", "Primary Outcome Measures", "Secondary Outcome Measures",
    "Conditions", "Interventions", "Phases", "Criteria"
]
for col in columns_to_clean:
    df[col] = df[col].apply(clean_text)

# Combine fields with weights
weights = {
    "Study Title": 1,
    "Primary Outcome Measures": 1.5,
    "Secondary Outcome Measures": 1,
    "Conditions": 2,
    "Interventions": 1.5,
    "Phases": 2,
    "Criteria": 2.5
}

df["combined"] = (
    df["Study Title"] + " " +
    df["Primary Outcome Measures"] + " " +
    df["Secondary Outcome Measures"] + " " +
    df["Conditions"] + " " +
    df["Interventions"] + " " +
    df["Phases"] + " " +
    df["Criteria"]
)

# Compute similarity
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["combined"])
similarity_matrix = cosine_similarity(tfidf_matrix)

# Function to get similar trials
def get_similar_trials(nct_id, top_n=10):
    if nct_id not in df["NCT ID"].values:
        return []
    index = df[df["NCT ID"] == nct_id].index[0]
    scores = list(enumerate(similarity_matrix[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    similar_trials = [{"NCT ID": df.iloc[i]["NCT ID"], "Similarity": score} for i, score in scores[1:top_n+1]]
    return similar_trials

# Dash App
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

# Navbar
navbar = dbc.Navbar(
    dbc.Container([dbc.NavbarBrand("Clinical Trials Dashboard", className="ms-2 text-primary", style={"fontSize": "1.5rem"})]),
    color="light", dark=False, className="mb-4"
)

# Dashboard Layout
app.layout = html.Div([
    navbar,
    dbc.Container([
        html.H3("Top Similar Trials and Detailed Information", className="text-center text-primary mb-4"),
        dcc.Input(
            id="search-nct-id",
            type="text",
            placeholder="Search by NCT ID",
            debounce=True,
            className="mb-3",
            style={"width": "100%"}
        ),
        dcc.Dropdown(
            id="nct-ids-dropdown",
            options=[{"label": nct, "value": nct} for nct in df["NCT ID"].unique()],
            multi=True,
            placeholder="Select Clinical Trial NCT IDs",
            className="mb-4"
        ),
        dcc.Graph(id="multiple-similar-trials-chart", style={"height": "500px"}),
        html.Hr(),
        html.Div(id="trial-detail-section", style={"marginTop": "20px"}),
    ])
])

# Callbacks
@app.callback(
    [Output("nct-ids-dropdown", "value"), Output("nct-ids-dropdown", "options")],
    Input("search-nct-id", "value")
)
def update_search_bar(search_value):
    if not search_value:
        return [], [{"label": nct, "value": nct} for nct in df["NCT ID"].unique()]

    matching_ids = df[df["NCT ID"].str.contains(search_value, case=False, na=False)]["NCT ID"].unique()
    options = [{"label": nct, "value": nct} for nct in matching_ids]
    return matching_ids.tolist(), options

@app.callback(
    Output("multiple-similar-trials-chart", "figure"),
    Input("nct-ids-dropdown", "value")
)
def update_multiple_similar_trials(selected_nct_ids):
    if not selected_nct_ids:
        return px.bar(title="No Trials Selected", labels={"x": "NCT ID", "y": "Similarity"})

    data = []
    for nct_id in selected_nct_ids:
        similar_trials = get_similar_trials(nct_id, top_n=10)
        for trial in similar_trials:
            data.append({
                "Source NCT ID": nct_id,
                "Similar NCT ID": trial["NCT ID"],
                "Similarity": trial["Similarity"]
            })
    
    df_results = pd.DataFrame(data)
    if not df_results.empty:
        fig = px.bar(
            df_results,
            x="Similar NCT ID",
            y="Similarity",
            color="Source NCT ID",
            barmode="group",
            title="Similar Trials for Selected NCT IDs",
            labels={"Similarity": "Similarity Score", "Similar NCT ID": "Trial ID"}
        )
        fig.update_layout(title_x=0.5, xaxis_tickangle=45)
    else:
        fig = px.bar(title="No Similar Trials Found")
    return fig

@app.callback(
    Output("trial-detail-section", "children"),
    Input("nct-ids-dropdown", "value")
)
def update_trial_details(selected_nct_ids):
    if not selected_nct_ids:
        return html.Div("No trials selected.", className="text-center text-secondary")
    
    details_sections = []
    for nct_id in selected_nct_ids:
        trial_data = df[df["NCT ID"] == nct_id].iloc[0]
        
        # Detailed Information Section
        details_sections.append(html.Div([
            html.H4(f"Details for NCT ID: {nct_id}", className="text-primary"),
            html.P(f"Study Title: {trial_data['Study Title']}"),
            html.P(f"Conditions: {trial_data['Conditions']}"),
            html.P(f"Interventions: {trial_data['Interventions']}"),
            html.P(f"Phases: {trial_data['Phases']}"),
            html.P(f"Criteria: {trial_data['Criteria']}"),
            
            # Pie Chart for Conditions
            dcc.Graph(figure=px.pie(
                names=trial_data['Conditions'].split(", "),
                title=f"Condition Distribution for NCT ID {nct_id}"
            )),
            
            # Bar Chart for Interventions
            dcc.Graph(figure=px.bar(
                x=trial_data['Interventions'].split(", "),
                y=[1] * len(trial_data['Interventions'].split(", ")),
                labels={"x": "Interventions", "y": "Count"},
                title=f"Interventions for NCT ID {nct_id}"
            )),
            
            # Word Cloud for Criteria
            dcc.Graph(figure=px.treemap(
                names=trial_data["Criteria"].split(),
                parents=[""] * len(trial_data["Criteria"].split()),
                title=f"Eligibility Criteria Word Cloud for NCT ID {nct_id}"
            ))
        ], className="mb-5"))

    return details_sections

if __name__ == "__main__":
    app.run_server(debug=True)
