#!/usr/bin/env python
# coding: utf-8

# In[18]:


streamlit_code = """
import os
import subprocess
from IPython.display import display, IFrame
import mysql.connector
import streamlit as st
import pandas as pd


def get_db_connection():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ishant@123",  # Update with your MySQL password
            database="hosho_digital_contract_manager_database"  
        )
        return mydb
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None


def contract_manager_page():
    st.title("Contract Manager Dashboard")
    st.subheader("Manage Templates and Contract Lifecycle")
    menu = ["View Templates", "Add Template", "Track Contract Status"]
    choice = st.selectbox("Choose Action", menu)

    if choice == "View Templates":
        mydb = get_db_connection()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM templates")
            result = mycursor.fetchall()
            mydb.close()
            if result:
                data = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                st.dataframe(data)
            else:
                st.warning("No templates found.")

    elif choice == "Add Template":
        template_name = st.text_input("Template Name")
        description = st.text_area("Template Description")
        created_by = st.number_input("Created By (User ID)", min_value=1, step=1)

        if st.button("Add Template"):
            mydb = get_db_connection()
            if mydb:
                mycursor = mydb.cursor()
                query = "INSERT INTO templates (template_name, description, created_by) VALUES (%s, %s, %s)"
                values = (template_name, description, created_by)
                try:
                    mycursor.execute(query, values)
                    mydb.commit()  # Commit the changes
                    st.success("Template added successfully!")

                    # Re-establish connection and refresh data
                    mydb = get_db_connection()
                    mycursor = mydb.cursor()
                    mycursor.execute("SELECT * FROM templates")
                    result = mycursor.fetchall()
                    mydb.close()
                    if result:
                        data = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                        st.dataframe(data)

                except mysql.connector.Error as err:
                    st.error(f"Error adding template: {err}")
                finally:
                    mydb.close()

    elif choice == "Track Contract Status":
        mydb = get_db_connection()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM contracts")
            result = mycursor.fetchall()
            mydb.close()
            if result:
                data = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                st.dataframe(data)
            else:
                st.warning("No contracts found.")

def sales_rep_page():
    st.title("Sales Representative Dashboard")
    st.subheader("Manage Contracts and Track Revenue")
    menu = ["View Contracts", "Add Contract", "Track Revenue"]
    choice = st.selectbox("Choose Action", menu)

    if choice == "View Contracts":
        mydb = get_db_connection()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM contracts")
            result = mycursor.fetchall()
            mydb.close()
            if result:
                data = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                st.dataframe(data)
            else:
                st.warning("No contracts found.")

    elif choice == "Add Contract":
        template_id = st.number_input("Template ID", min_value=1, step=1)
        created_by = st.number_input("Created By (User ID)", min_value=1, step=1)
        assigned_to = st.number_input("Assigned To (User ID)", min_value=1, step=1)
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")

        if st.button("Add Contract"):
            mydb = get_db_connection()
            if mydb:
                mycursor = mydb.cursor()
                query = "INSERT INTO contracts (template_id, created_by, assigned_to, start_date, end_date) VALUES (%s, %s, %s, %s, %s)"
                values = (template_id, created_by, assigned_to, start_date, end_date)
                try:
                    mycursor.execute(query, values)
                    mydb.commit()  # Commit the changes
                    st.success("Contract added successfully!")

                    # Re-establish connection and refresh data
                    mydb = get_db_connection()
                    mycursor = mydb.cursor()
                    mycursor.execute("SELECT * FROM contracts")
                    result = mycursor.fetchall()
                    mydb.close()
                    if result:
                        data = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                        st.dataframe(data)

                except mysql.connector.Error as err:
                    st.error(f"Error adding contract: {err}")
                finally:
                    mydb.close()

    elif choice == "Track Revenue":
        mydb = get_db_connection()
        if mydb:
            mycursor = mydb.cursor()
            # Implement revenue tracking logic here
            mydb.close()


st.title("HOSHŌ Digital Contract Management System")
st.subheader("Select Your Role to Proceed")

roles = [
    "Contract Manager",
    "Sales Representative",
    "Legal Team",
    "Finance Team",
    "Account Manager",
    "Contract Analyst",
]
role = st.selectbox("Choose Your Role", roles)

if role == "Contract Manager":
    contract_manager_page()
elif role == "Sales Representative":
    sales_rep_page()
elif role == "Legal Team":
    legal_team_page()
else:
    st.warning("This role is under development.")

"""
with open("app.py", "w", encoding="utf-8") as file:
    file.write(streamlit_code)
process = subprocess.Popen(["streamlit", "run", "app.py"])
iframe = IFrame(src="http://localhost:8501", width="100%", height="600px")
display(iframe)


# In[ ]:




