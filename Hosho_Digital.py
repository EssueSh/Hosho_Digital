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
def register_user():
    st.title("Register New User")
    
    # Input fields for new user registration
    username = st.text_input("Username")
    email = st.text_input("Email")
    
    if st.button("Register"):
        # Check if username and email are provided
        if not username or not email:
            st.error("Please provide both username and email.")
            return
        
        # Insert user into the database
        mydb = get_db_connection()
        if mydb:
            mycursor = mydb.cursor()
            
            # Ensure the username does not already exist
            mycursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
            username_exists = mycursor.fetchone()[0] > 0
            if username_exists:
                st.error("Username already exists. Please choose another one.")
                return
            
            # Insert new user into the users table
            query = "INSERT INTO users (username, email) VALUES (%s, %s)"
            values = (username, email)
            try:
                mycursor.execute(query, values)
                mydb.commit()
                st.success(f"User '{username}' registered successfully!")
            except mysql.connector.Error as err:
                st.error(f"Error registering user: {err}")
            finally:
                mydb.close()


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
def legal_team_page():
    st.title("Legal Team Dashboard")
    st.subheader("Review Contracts and Manage Clause Library")
    
    menu = ["Review Contracts", "View Legal Reviews", "Clause Library"]
    choice = st.selectbox("Choose Action", menu)

    if choice == "Review Contracts":
        mydb = get_db_connection()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM contracts WHERE status = 'Draft'")
            result = mycursor.fetchall()
            mydb.close()
            if result:
                data = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                st.dataframe(data)
            else:
                st.warning("No contracts to review.")

        contract_id = st.number_input("Enter Contract ID for Review", min_value=1)
        review_notes = st.text_area("Enter Review Notes")
        compliance_status = st.selectbox("Compliance Status", ["Compliant", "Non-Compliant"])

        if st.button("Submit Review"):
            mydb = get_db_connection()
            if mydb:
                mycursor = mydb.cursor()
                query = """
                    INSERT INTO legal_reviews (contract_id, legal_team_member_id, review_notes, compliance_status)
                    VALUES (%s, %s, %s, %s)
                """
                values = (contract_id, 1, review_notes, compliance_status)  # Assuming '1' is the logged-in legal team member ID
                try:
                    mycursor.execute(query, values)
                    mydb.commit()
                    st.success("Review submitted successfully!")
                except mysql.connector.Error as err:
                    st.error(f"Error submitting review: {err}")
                finally:
                    mydb.close()

    elif choice == "View Legal Reviews":
        mydb = get_db_connection()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM legal_reviews")
            result = mycursor.fetchall()
            mydb.close()
            if result:
                data = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                st.dataframe(data)
            else:
                st.warning("No legal reviews found.")

    elif choice == "Clause Library":
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
                st.warning("No clauses found.")

        clause_text = st.text_area("Add New Clause Text")
        category = st.text_input("Category")

        if st.button("Add Clause"):
            mydb = get_db_connection()
            if mydb:
                mycursor = mydb.cursor()
                query = """
                    INSERT INTO clause_library (clause_text, category, created_by)
                    VALUES (%s, %s, %s)
                """
                values = (clause_text, category, 1)  # Assuming '1' is the logged-in user ID
                try:
                    mycursor.execute(query, values)
                    mydb.commit()
                    st.success("Clause added to library!")
                except mysql.connector.Error as err:
                    st.error(f"Error adding clause: {err}")
                finally:
                    mydb.close()
def finance_team_page():
    st.title("Finance Team Dashboard")
    st.subheader("Track Contract Financials")

    menu = ["Track Contract Payments", "View Financial Reports"]
    choice = st.selectbox("Choose Action", menu)

    if choice == "Track Contract Payments":
        mydb = get_db_connection()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM finance_team_data")
            result = mycursor.fetchall()
            mydb.close()
            if result:
                data = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                st.dataframe(data)
            else:
                st.warning("No financial records found.")

        contract_id = st.number_input("Enter Contract ID", min_value=1)
        total_value = st.number_input("Contract Total Value", min_value=0.0, step=0.01)
        payment_terms = st.text_area("Payment Terms")
        billing_status = st.selectbox("Billing Status", ["Pending", "Paid", "Overdue"])

        if st.button("Submit Payment Information"):
            mydb = get_db_connection()
            if mydb:
                mycursor = mydb.cursor()
                query = """
                    INSERT INTO finance_team_data (contract_id, total_value, payment_terms, billing_status)
                    VALUES (%s, %s, %s, %s)
                """
                values = (contract_id, total_value, payment_terms, billing_status)
                try:
                    mycursor.execute(query, values)
                    mydb.commit()
                    st.success("Payment information submitted successfully!")
                except mysql.connector.Error as err:
                    st.error(f"Error submitting payment info: {err}")
                finally:
                    mydb.close()

    elif choice == "View Financial Reports":
        st.info("Feature under development")
def contract_analyst_page():
    st.title("Contract Analyst Dashboard")
    st.subheader("Analyze Contract Performance")

    menu = ["Track KPIs", "Generate Custom Reports"]
    choice = st.selectbox("Choose Action", menu)

    if choice == "Track KPIs":
        mydb = get_db_connection()
        if mydb:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM contract_analytics")
            result = mycursor.fetchall()
            mydb.close()
            if result:
                data = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                st.dataframe(data)
            else:
                st.warning("No KPI records found.")

        contract_id = st.number_input("Enter Contract ID", min_value=1)
        kpi_name = st.text_input("Enter KPI Name")
        kpi_value = st.number_input("Enter KPI Value", min_value=0.0, step=0.01)
        analysis_notes = st.text_area("Analysis Notes")

        if st.button("Log KPI"):
            mydb = get_db_connection()
            if mydb:
                mycursor = mydb.cursor()
                query = """
                    INSERT INTO contract_analytics (contract_id, analyst_id, kpi_name, kpi_value, analysis_notes)
                    VALUES (%s, %s, %s, %s, %s)
                """
                values = (contract_id, 1, kpi_name, kpi_value, analysis_notes)  # Assuming '1' is the logged-in analyst ID
                try:
                    mycursor.execute(query, values)
                    mydb.commit()
                    st.success("KPI recorded successfully!")
                except mysql.connector.Error as err:
                    st.error(f"Error recording KPI: {err}")
                finally:
                    mydb.close()

    elif choice == "Generate Custom Reports":
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
st.subheader("Select Your Role to Proceed or Register")

menu = [
    "Contract Manager",
    "Sales Representative",
    "Legal Team",
    "Finance Team",
    "Account Manager",
    "Contract Analyst",
    "Register New User"
]
role = st.selectbox("Choose Your Role", menu)

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
elif role == "Register New User":
    register_user()  # Register new user
else:
    st.warning("This role is under development.")
