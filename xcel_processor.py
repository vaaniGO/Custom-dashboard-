import streamlit as st
import pandas as pd

def main():
    st.title("Identifier Sum Aggregation Dashboard")

    st.sidebar.header("Configuration")
    identifier_column = st.sidebar.text_input("Enter the name of the identifier column:", "Identifier")
    value_column = st.sidebar.text_input("Enter the name of the values column:", "Values")

    uploaded_file = st.file_uploader("Upload your Excel file:", type=["xlsx"])

    if uploaded_file:
        try:
            # Read the Excel file into a DataFrame
            df = pd.read_excel(uploaded_file)

            # Display the uploaded data
            st.subheader("Uploaded Data")
            st.dataframe(df)

            if identifier_column in df.columns and value_column in df.columns:
                # Perform aggregation: sum of values grouped by the identifier column
                aggregated_df = df.groupby(identifier_column)[value_column].sum().reset_index()

                st.subheader("Aggregated Data")
                st.dataframe(aggregated_df)

                # Provide a download link for the output CSV
                st.download_button(
                    label="Download Aggregated Data as CSV",
                    data=aggregated_df.to_csv(index=False).encode('utf-8'),
                    file_name="aggregated_data.csv",
                    mime="text/csv"
                )
            else:
                st.error(f"Columns '{identifier_column}' or '{value_column}' not found in the uploaded file. Please check the column names.")
        except Exception as e:
            st.error(f"An error occurred while processing the file: {e}")

if __name__ == "__main__":
    main()