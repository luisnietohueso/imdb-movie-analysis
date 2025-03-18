import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load cleaned data
df = pd.read_csv(r"C:\Users\Owner\Documents\imdb-movie-analysis\data\cleaned_imdb.csv")

# Set page title and layout
st.set_page_config(page_title="IMDb Movie Analysis", layout="wide")

# Sidebar filters
st.sidebar.header("🔍 Filter Movies")
selected_genre = st.sidebar.selectbox("Select Genre", ["All"] + sorted(set(df["Genres"].str.replace("[\[\]']", "", regex=True).str.split(", ").explode().dropna())))

min_year, max_year = int(df["Release_Date"].min()[:4]), int(df["Release_Date"].max()[:4])
selected_year = st.sidebar.slider("Select Year", min_value=min_year, max_value=max_year, value=(min_year, max_year))

min_rating, max_rating = float(df["Vote_Average"].min()), float(df["Vote_Average"].max())
selected_rating = st.sidebar.slider("Select Minimum Rating", min_value=min_rating, max_value=max_rating, value=min_rating)

# Filter data
filtered_df = df.copy()

if selected_genre != "All":
    filtered_df = filtered_df[df["Genres"].str.contains(selected_genre, na=False)]
filtered_df = filtered_df[
    (filtered_df["Vote_Average"] >= selected_rating) & 
    (filtered_df["Release_Date"].str[:4].astype(int).between(selected_year[0], selected_year[1]))
]

# Display dataset preview
st.title("🎬 IMDb Movie Analysis Dashboard")
st.write(f"Displaying **{len(filtered_df)}** movies based on selected filters.")

st.dataframe(filtered_df[["Movie_Name", "Genres", "Vote_Average", "Release_Date"]].reset_index(drop=True))

# Top-rated movies
st.subheader("🏆 Top 10 Highest Rated Movies")
top_movies = filtered_df.nlargest(10, "Vote_Average")[["Movie_Name", "Vote_Average"]]

st.table(top_movies)

# Budget vs Revenue (Improved)
# Budget vs Revenue (Improved)
st.subheader("💰 Budget vs Revenue (With Profit Indicator)")

def convert_currency(value):
    """Convert '10.0M' → 10000000, '10.0K' → 10000, and '1.0B' → 1000000000."""
    if isinstance(value, str):
        value = value.replace("$", "").replace(",", "")  # Remove $ and commas
        if "B" in value:
            return float(value.replace("B", "")) * 1e9  # Convert B to billions
        elif "M" in value:
            return float(value.replace("M", "")) * 1e6  # Convert M to millions
        elif "K" in value:
            return float(value.replace("K", "")) * 1e3  # Convert K to thousands
        else:
            return float(value)  # Convert normal numbers
    return value  # Return original value if not a string

# Apply conversion to Budget and Revenue columns
df["Budget_USD"] = df["Budget_USD"].apply(convert_currency)
df["Revenue_$"] = df["Revenue_$"].apply(convert_currency)

# Remove movies with missing values
filtered_df = df.dropna(subset=["Budget_USD", "Revenue_$"])

# Calculate profit margin
filtered_df["Profit"] = filtered_df["Revenue_$"] - filtered_df["Budget_USD"]
filtered_df["Profit Margin (%)"] = (filtered_df["Profit"] / filtered_df["Budget_USD"]) * 100

# Categorize movies based on profit/loss
filtered_df["Success"] = ["Profit" if x > 0 else "Loss" for x in filtered_df["Profit"]]

fig, ax = plt.subplots(figsize=(10, 6))

# Scatter plot with color-coded success
sns.scatterplot(
    data=filtered_df, 
    x="Budget_USD", 
    y="Revenue_$",
    hue="Success", 
    palette={"Profit": "green", "Loss": "red"}, 
    alpha=0.7,
    edgecolor="black"
)

# Apply log scale to fix scale issue
ax.set_xscale("log")
ax.set_yscale("log")

# Labels and title
ax.set_xlabel("Budget (Log Scale, USD)", fontsize=12)
ax.set_ylabel("Revenue (Log Scale, USD)", fontsize=12)
ax.set_title("💰 Budget vs Revenue (Profit in Green, Loss in Red)", fontsize=14)
ax.legend(title="Success", loc="upper left")

st.pyplot(fig)


# WordCloud of Overviews
st.subheader("📝 Movie Overview Word Cloud")
wordcloud_text = " ".join(filtered_df["Overview"].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="black").generate(wordcloud_text)

fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Search Functionality
st.sidebar.subheader("🔎 Search for a Movie")
search_query = st.sidebar.text_input("Enter movie name")

if search_query:
    search_results = df[df["Movie_Name"].str.contains(search_query, case=False, na=False)]
    if not search_results.empty:
        st.subheader(f"🔍 Search Results for '{search_query}'")
        st.write(search_results[["Movie_Name", "Genres", "Vote_Average", "Release_Date"]])
    else:
        st.write("❌ No movies found.")

st.sidebar.markdown("---")
st.sidebar.write("📊 **Built with Streamlit**")
