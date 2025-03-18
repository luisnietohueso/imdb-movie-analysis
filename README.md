# IMDb Movie Analysis Project

## 📌 Project Overview
This project analyzes IMDb movie data, providing insights into movie ratings, genres, budgets, and revenues. It includes an interactive **Streamlit dashboard** for data visualization and uses **Pytest** for automated testing.

## 🚀 Features
- **Data Cleaning**: Converts budget, revenue, and vote count columns into numerical formats.
- **Interactive Dashboard**: Built with Streamlit to visualize movie insights.
- **Filters**: Genre, release year, and IMDb rating filters.
- **Budget vs. Revenue Analysis**: Scatter plot with log scale for better readability.
- **Word Cloud**: Generates a word cloud from movie descriptions.
- **Search Functionality**: Users can search for specific movies.
- **Unit Testing**: Ensures data processing correctness using Pytest.

## 📂 Project Structure
```
📦 imdb-movie-analysis
 ┣ 📂 app                # Streamlit app
 ┃ ┗ 📜 app.py           # Main dashboard script
 ┣ 📂 data               # Data folder
 ┃ ┗ 📜 cleaned_imdb.csv # Processed dataset
 ┣ 📂 notebooks          # Jupyter notebooks (optional analysis)
 ┣ 📂 src                # Data processing scripts
 ┃ ┣ 📜 data_cleaning.py # Cleans and preprocesses dataset
 ┃ ┗ 📜 data_analysis.py # Contains analysis functions
 ┣ 📂 tests              # Unit tests with Pytest
 ┃ ┗ 📜 test_functions.py
 ┣ 📜 .gitignore         # Ignore unnecessary files (venv, __pycache__)
 ┣ 📜 LICENSE            # License file
 ┣ 📜 README.md          # Project documentation
 ┗ 📜 requirements.txt   # Dependencies list
```

## 🛠️ Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/luisnietohueso/imdb-movie-analysis.git
cd imdb-movie-analysis
```

### **2️⃣ Create a Virtual Environment & Install Dependencies**
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### **3️⃣ Run the Streamlit App**
```sh
streamlit run app/app.py
```

## 🔬 Running Tests
To ensure the data processing works correctly, run:
```sh
pytest tests/
```

## 🎯 Future Improvements
- Deploy Streamlit app online.
- Add more advanced visualizations.
- Improve performance for large datasets.

## 📜 License
This project is licensed under the MIT License.

---
🔗 **GitHub Repository**: [IMDb Movie Analysis](https://github.com/luisnietohueso/imdb-movie-analysis)

