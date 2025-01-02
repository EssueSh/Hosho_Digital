#!/usr/bin/env python
# coding: utf-8

# In[18]:

import mysql.connector
import streamlit as st
import pandas as pd

def get_db_connection():
    try:
        mydb = mysql.connector.connect(
            host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
            port=4000
            user="2togiDCHrG3RFGf.root",
            password="1nWRCnwmEh6mV0XL",
            database="test"
            CA=""
        )
        return mydb
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None

def contract_manager_page():
    st.title("Contract Manager Dashboard")
    st.subheader("Manage Templates and Contract Lifecycle")
    menu = ["View Templates", "Add Template", "Track Contract Status", "Set Renewal Notifications", "Version Control"]
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
                    mydb.commit()
                    st.success("Template added successfully!")
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

    elif choice == "Set Renewal Notifications":
        st.info("Feature under development")

    elif choice == "Version Control":
        st.info("Feature under development")

def sales_rep_page():
    st.title("Sales Representative Dashboard")
    st.subheader("Manage Contracts and Track Revenue")
    menu = ["View Contracts", "Add Contract", "Track Revenue", "Notifications"]
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
                    mydb.commit()
                    st.success("Contract added successfully!")
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

    elif choice == "Notifications":
        st.info("Feature under development")

# Define additional role-specific pages
def legal_team_page():
    st.title("Legal Team Dashboard")
    st.subheader("Manage Legal Compliance and Risks")
    menu = ["Review Modifications", "Access Clause Library", "Track Negotiations", "Risk Assessment"]
    choice = st.selectbox("Choose Action", menu)

    if choice == "Review Modifications":
        mydb = get_db_connection()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM modifications WHERE status = 'Pending Review'")
            result = mycursor.fetchall()
            mydb.close()
            if result:
                data = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                st.dataframe(data)
            else:
                st.warning("No modifications pending review.")

    elif choice == "Access Clause Library":
        mydb = get_db_connection()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM clause_library")
            result = mycursor.fetchall()
            mydb.close()
            if result:
                data = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                st.dataframe(data)
            else:
                st.warning("Clause library is empty.")

    elif choice == "Track Negotiations":
        st.info("Feature under development")

    elif choice == "Risk Assessment":
        st.info("Feature under development")

def finance_team_page():
    st.title("Finance Team Dashboard")
    st.subheader("Track Financial Obligations and Generate Reports")
    menu = ["Track Payments", "Generate Reports", "Link to Billing"]
    choice = st.selectbox("Choose Action", menu)

    if choice == "Track Payments":
        mydb = get_db_connection()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT contract_id, payment_status FROM payments")
            result = mycursor.fetchall()
            mydb.close()
            if result:
                data = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                st.dataframe(data)
            else:
                st.warning("No payment data available.")

    elif choice == "Generate Reports":
        st.info("Feature under development")

    elif choice == "Link to Billing":
        st.info("Feature under development")

def account_manager_page():
    st.title("Account Manager Dashboard")
    st.subheader("Monitor Performance Metrics and Customer Relationships")
    menu = ["View Contract History", "Track Deliverables", "Identify Upsell Opportunities"]
    choice = st.selectbox("Choose Action", menu)

    if choice == "View Contract History":
        mydb = get_db_connection()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM contract_history")
            result = mycursor.fetchall()
            mydb.close()
            if result:
                data = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                st.dataframe(data)
            else:
                st.warning("No contract history available.")

    elif choice == "Track Deliverables":
        st.info("Feature under development")

    elif choice == "Identify Upsell Opportunities":
        st.info("Feature under development")

def contract_analyst_page():
    st.title("Contract Analyst Dashboard")
    st.subheader("Analyze Contract Performance and Generate Reports")
    menu = ["Generate Performance Reports", "Analyze Pricing", "Track KPIs", "Create Custom Reports"]
    choice = st.selectbox("Choose Action", menu)

    if choice == "Generate Performance Reports":
        mydb = get_db_connection()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM performance_reports")
            result = mycursor.fetchall()
            mydb.close()
            if result:
                data = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                st.dataframe(data)
            else:
                st.warning("No performance reports available.")

    elif choice == "Analyze Pricing":
        st.info("Feature under development")

    elif choice == "Track KPIs":
        st.info("Feature under development")

    elif choice == "Create Custom Reports":
        st.info("Feature under development")

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
elif role == "Finance Team":
    finance_team_page()
elif role == "Account Manager":
    account_manager_page()
elif role == "Contract Analyst":
    contract_analyst_page()
else:
    st.warning("This role is under development.")




