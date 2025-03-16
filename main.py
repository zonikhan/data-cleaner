#  import streamlit as st
#  import pandas as pd
#  from io import BytesIO

#  st.set_page_config(page_title="📁 File Converter & Cleaner", layout="wide")
#  st.title("📁 File Converter & Cleaner")
#  st.write("Upload your CSV and Excel File to clean the data  convert formats effortessly.🩹")

#  files = st.file_uploader("Upload CSV or Excel Files", type=["CSV","xlsx"], accept_multiple_files=True)

#  if files:
#    for file in files:
#        ext = file.name.split(".")[-1]
#      df = pd.read_CSV(file) if ext =="CSV" else pd.read_excel(file)

#    st.subheader(f"🔍 {file.name}I- preview")
#     st.dataframe(df.head())


#  if st.checkbox(f"File Missing Values- {file.name}"):
#      df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
#    st.success("Missing values filled successfully!")
#     st.dataframe(df.head())

#      selected_columns = st.multiselect(f"Select Columns - {file.name}", df.columns, default=df.columns)
#      df = df[selected_columns]
#      st.dataframe(df.head())
#      if st.checkbox(f"📊Show Chart - {file.name}") and not df.select_dtypes(include="number").empty:
         
#          st.bar_chart(df.select_dtypes(include="number").select_dtypes(include="number").iloc[:, :2])
#  format_choice = st.radio(f"Convert {file.name} to:",["CSV", "Excel"], key=file.name)
#  if st.button(f"⬇ Download {file.name} as {format_choice}"):
#     output = BytesIO()
#     if format_choice =="CSV":
#         df.to_csv(output, index=False)mime = "text/csv" new_name = file.name.replace(ext, "csv")
#     else:
#         df.to_excel(output, index=False)
#          mime = "application/vnd.openxmlformate-officedocoment.spreadsheetml.sheet"
#          new_name = file.name.replace(ext, "Xlse")
#  output.seek(0)
# #  st.download_button("⬇ Downlaod File",file_name=new_name, data=output, mime=mime, key=file.name)
# st.download_button("⬇ Download File", file_name=new_name, data=output, mime=mime, key=f"{file.name}_{st.session_state}")
#  st.success("processing Completed!🎉")


# import streamlit as st
# import pandas as pd
# from io import BytesIO
# import uuid

# file = st.file_uploader("Upload a file", type=["csv", "xlsx"])

# if file is not None:
#     df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)

#     if st.checkbox(f"File Missing Values - {file.name}"):
#         st.write("Processing file...")

#     output = BytesIO()
#     df.to_csv(output, index=False)
#     output.seek(0)

#     st.download_button(
#         "⬇ Download File",
#         file_name=f"cleaned_{file.name}",
#         data=output,
#         mime="text/csv",
#         key=str(uuid.uuid4())  # ✅ Unique key
#     )



import streamlit as st
import pandas as pd
from io import BytesIO
import uuid  # Unique keys ke liye

# Set page configuration
st.set_page_config(page_title="📁 File Converter & Cleaner", layout="wide")
st.title("📁 File Converter & Cleaner")
st.write("Upload your CSV or Excel File to clean the data & convert formats effortlessly.🩹")

# File uploader (Multiple files allowed)
files = st.file_uploader("Upload CSV or Excel Files", type=["csv", "xlsx"], accept_multiple_files=True)

if files:
    for file in files:
        ext = file.name.split(".")[-1].lower()  # Ensure lowercase comparison
        df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

        # Display file preview
        st.subheader(f"🔍 {file.name} - Preview")
        st.dataframe(df.head())

        # Handle Missing Values
        if st.checkbox(f"🛠 Fill Missing Values - {file.name}"):
            df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
            st.success("✅ Missing values filled successfully!")
            st.dataframe(df.head())

        # Column Selection
        selected_columns = st.multiselect(f"🎯 Select Columns - {file.name}", df.columns, default=df.columns)
        df = df[selected_columns]
        st.dataframe(df.head())

        # Chart Display
        if st.checkbox(f"📊 Show Chart - {file.name}") and not df.select_dtypes(include="number").empty:
            numeric_df = df.select_dtypes(include="number")
            st.bar_chart(numeric_df.iloc[:, :min(2, numeric_df.shape[1])])  # Show max 2 numeric columns

        # Format Conversion
        format_choice = st.radio(f"🎛 Convert {file.name} to:", ["CSV", "Excel"], key=f"{file.name}_{uuid.uuid4()}")

        if st.button(f"⬇ Download {file.name} as {format_choice}"):
            output = BytesIO()
            if format_choice == "CSV":
                df.to_csv(output, index=False)
                mime = "text/csv"
                new_name = file.name.replace(ext, "csv")
            else:
                df.to_excel(output, index=False, engine="xlsxwriter")
                mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                new_name = file.name.replace(ext, "xlsx")

            output.seek(0)

            # Download button with unique key
            st.download_button(
                "⬇ Download File",
                file_name=new_name,
                data=output,
                mime=mime,
                key=f"{file.name}_{uuid.uuid4()}"  # Unique key to prevent duplication error
            )
            st.success("🎉 Processing Completed!")