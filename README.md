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
   - Ensure the eligibility criteria file (e.g., `eligibilities.txt`) is formatted as pipe-separated values (|). Note that the eligibilities are provided in brief case format.

4. **Run the Application:**

   Execute the following command to start the Dash application:

   ```bash
   python app.py
   ```

5. **Access the Dashboard:**

   Open your browser and navigate to:

   ```
   http://127.0.0.1:8050
   ```

---

## Project Structure

```
clinical-trial-similarity/
├── app.py                 # Main Dash application
├── response.json          # Example JSON file containing trial data
├── eligibilities.txt      # Eligibility criteria data
├── requirements.txt       # Project dependencies
├── utils.py               # Helper functions (optional)
└── README.md              # Project setup instructions
```

---

## Usage

- Enter an NCT ID in the search bar to find similar trials.
- Explore visual insights, such as condition distributions and eligibility criteria treemaps.
- Use the dropdown to select multiple trials and compare similarity scores.

---

## Future Improvements

- Integrate advanced NLP models (e.g., BERT) for semantic similarity.
- Enhance the dashboard with additional visualizations.
- Expand functionality to include metadata-based filtering.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

For questions or contributions, contact [Your Name] at [your_email@example.com].

