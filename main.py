import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(layout="wide")
st.title("Netflix Titles Analysis")

# Load the CSV file into a DataFrame
df = pd.read_csv('NETFLIX_TITLES.CSV')

# Remove the 'show_id' column 
df = df.drop(columns=['show_id'])

# Remove rows with any empty column values
df_cleaned = df.dropna()

# Display preview and summary side by side
st.write("## Data Preview and Summary")
col1, col2 = st.columns(2)

with col1:
    st.write("### Original DataFrame Preview:")
    st.write(df.head(10))
    st.write("### Original DataFrame Summary:")
    st.write(df.describe(include='all'))

with col2:
    st.write("### Cleaned DataFrame Preview:")
    st.write(df_cleaned.head(10))
    st.write("### Cleaned DataFrame Summary:")
    st.write(df_cleaned.describe(include='all'))

# Sidebar for filtering and plot selection
st.sidebar.header('Filter Data or Select Plot')
filter_or_plot = st.sidebar.radio("Choose an option:", ["Filter Data", "Select Plot"])

if filter_or_plot == "Filter Data":
    # Filtering section
    selected_country = st.sidebar.selectbox('Select Country', df_cleaned['country'].unique())
    selected_genre = st.sidebar.selectbox('Select Genre', df_cleaned['listed_in'].unique())

    # Filter data based on user selection
    filtered_df = df_cleaned[(df_cleaned['country'] == selected_country) & (df_cleaned['listed_in'] == selected_genre)]

    # Display filtered data
    st.write("## Filtered Data")
    st.dataframe(filtered_df)
else:
    # User selection for graphs
    st.write("## Select Graphs to Plot")
    graph_options = [
        "Number of Titles Added Per Year",
        "Top 10 Countries by Number of Titles",
        "Distribution of Ratings",
        "Top 10 Directors by Number of Titles",
        "Top 10 Genres by Number of Titles",
        "Number of Releases in a Country Year-wise",
        "Custom Plot"
    ]

    selected_graphs = st.multiselect("Choose graphs to display:", graph_options)

    if "Number of Titles Added Per Year" in selected_graphs:
        st.write("### Number of Titles Added Per Year")
        fig2, ax2 = plt.subplots(figsize=(10, 5))
        df_cleaned['release_year'].value_counts().sort_index().plot(kind='bar', color='green', ax=ax2)
        ax2.set_title('Number of Titles Added Per Year')
        ax2.set_xlabel('Release Year')
        ax2.set_ylabel('Count')
        st.pyplot(fig2)

    if "Top 10 Countries by Number of Titles" in selected_graphs:
        st.write("### Top 10 Countries by Number of Titles")
        fig3, ax3 = plt.subplots(figsize=(10, 5))
        df_cleaned['country'].value_counts().head(10).plot(kind='bar', color='purple', ax=ax3)
        ax3.set_title('Top 10 Countries by Number of Titles')
        ax3.set_xlabel('Country')
        ax3.set_ylabel('Count')
        st.pyplot(fig3)

    if "Distribution of Ratings" in selected_graphs:
        st.write("### Distribution of Ratings")
        fig4, ax4 = plt.subplots(figsize=(10, 5))
        df_cleaned['rating'].value_counts().plot(kind='bar', color='red', ax=ax4)
        ax4.set_title('Distribution of Ratings')
        ax4.set_xlabel('Rating')
        ax4.set_ylabel('Count')
        st.pyplot(fig4)

    if "Top 10 Directors by Number of Titles" in selected_graphs:
        st.write("### Top 10 Directors by Number of Titles")
        fig5, ax5 = plt.subplots(figsize=(10, 5))
        df_cleaned['director'].value_counts().head(10).plot(kind='bar', color='cyan', ax=ax5)
        ax5.set_title('Top 10 Directors by Number of Titles')
        ax5.set_xlabel('Director')
        ax5.set_ylabel('Count')
        st.pyplot(fig5)

    if "Top 10 Genres by Number of Titles" in selected_graphs:
        st.write("### Top 10 Genres by Number of Titles")
        fig6, ax6 = plt.subplots(figsize=(10, 5))
        df_cleaned['listed_in'].value_counts().head(10).plot(kind='bar', color='magenta', ax=ax6)
        ax6.set_title('Top 10 Genres by Number of Titles')
        ax6.set_xlabel('Genre')
        ax6.set_ylabel('Count')
        st.pyplot(fig6)

    if "Number of Releases in a Country Year-wise" in selected_graphs:
        st.write("### Number of Releases in a Country Year-wise")
        country = st.selectbox("Choose Country:", df_cleaned['country'].unique())
        
        filtered_df = df_cleaned[df_cleaned['country'] == country]
        releases_per_year = filtered_df['release_year'].value_counts().sort_index()
        
        st.write(f"Number of releases in {country} year-wise:")
        
        fig7, ax7 = plt.subplots(figsize=(10, 5))
        releases_per_year.plot(kind='line', marker='o', color='orange', ax=ax7)
        ax7.set_title(f'Number of Releases in {country} Year-wise')
        ax7.set_xlabel('Year')
        ax7.set_ylabel('Number of Releases')
        st.pyplot(fig7)

    if "Custom Plot" in selected_graphs:
        st.write("### Custom Plot")
        # Add options to select columns for custom plot
        column1 = st.sidebar.selectbox('Select first column for custom plot', df_cleaned.columns)
        column2 = st.sidebar.selectbox('Select second column for custom plot', df_cleaned.columns)

        # Plot the selected columns
        fig_custom, ax_custom = plt.subplots(figsize=(10, 5))
        df_cleaned.plot(kind='scatter', x=column1, y=column2, ax=ax_custom)
        ax_custom.set_title(f'Custom Plot: {column1} vs {column2}')
        ax_custom.set_xlabel(column1)
        ax_custom.set_ylabel(column2)
        st.pyplot(fig_custom)