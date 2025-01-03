import mysql.connector
import streamlit as st
import pandas as pd

def get_db_connection():
    try:
        mydb = mysql.connector.connect(
            host="sql12.freesqldatabase.com",
            port=3306,  # Port number for MySQL
            user="sql12755432",
            password="qUtIGrBs3L",
            database="sql12755432"
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
        renewal_date = st.date_input("Renewal Date")

        if st.button("Add Contract"):
            mydb = get_db_connection()
            if mydb:
                mycursor = mydb.cursor()
                query = "INSERT INTO contracts (template_id, created_by, assigned_to, start_date, end_date, renewal_date) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (template_id, created_by, assigned_to, start_date, end_date, renewal_date)
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

def contract_manager_actions_page():
    st.title("Contract Manager Actions")
    st.subheader("Track Actions Taken on Contracts")
    menu = ["View Actions", "Log New Action"]
    choice = st.selectbox("Choose Action", menu)

    if choice == "View Actions":
        mydb = get_db_connection()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM contract_manager_actions")
            result = mycursor.fetchall()
            mydb.close()
            if result:
                data = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                st.dataframe(data)
            else:
                st.warning("No actions found.")

    elif choice == "Log New Action":
        contract_id = st.number_input("Contract ID", min_value=1, step=1)
        action_type = st.selectbox("Action Type", ["Status Update", "Renewal", "Versioning"])
        details = st.text_area("Action Details")
        performed_by = st.number_input("Performed By (User ID)", min_value=1, step=1)

        if st.button("Log Action"):
            mydb = get_db_connection()
            if mydb:
                mycursor = mydb.cursor()
                query = "INSERT INTO contract_manager_actions (contract_id, action_type, details, performed_by) VALUES (%s, %s, %s, %s)"
                values = (contract_id, action_type, details, performed_by)
                try:
                    mycursor.execute(query, values)
                    mydb.commit()
                    st.success("Action logged successfully!")
                except mysql.connector.Error as err:
                    st.error(f"Error logging action: {err}")
                finally:
                    mydb.close()

# Define other pages (Sales Representative, Legal Team, Finance Team, etc.) similarly

st.title("HOSHŌ Digital Contract Management System")
st.subheader("Select Your Role to Proceed")

roles = [
    "Contract Manager",
    "Sales Representative",
    "Account Manager",
    "Contract Manager Actions",
]
role = st.selectbox("Choose Your Role", roles)

if role == "Contract Manager":
    contract_manager_page()
elif role == "Sales Representative":
    sales_rep_page()
elif role == "Account Manager":
    account_manager_page()
elif role == "Contract Manager Actions":
    contract_manager_actions_page()
else:
    st.warning("This role is under development.")
