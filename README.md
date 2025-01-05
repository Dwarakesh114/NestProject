# Clinical Trial Similarity Analysis

This project provides a framework for identifying and ranking similar clinical trials based on their textual descriptions, such as study title, conditions, interventions, and eligibility criteria. The model uses TF-IDF vectorization and cosine similarity to compute relevance between trials and offers an interactive dashboard to visualize the results.

---

## Features

- Extract and preprocess data from JSON and text files.
- Compute text-based similarity using TF-IDF and cosine similarity.
- Visualize insights with bar charts, pie charts, and treemaps.
- Interactive dashboard built with Dash for trial exploration.

---

## Requirements

The project requires the following dependencies:

- Python 3.8+
- pandas
- scikit-learn
- Dash
- dash-bootstrap-components
- Plotly

Install all required libraries using the following command:

```bash
pip install -r requirements.txt
```

---

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-repo/clinical-trial-similarity.git
   cd clinical-trial-similarity
   ```

2. **Install Dependencies:**

   Ensure you have Python installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Input Data:**

   - Place the clinical trial JSON file in the root directory (e.g., `response.json`).
   - Ensure the eligibility criteria file (e.g., `eligibilities.txt` which will be found in the brief case of nest) is formatted as pipe-separated values (|). Note that the eligibilities are provided in brief case format.
