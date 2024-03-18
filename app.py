"""
        Name Convention Generator
        A Streamlit web application that generates a name convention based on user inputs.

        Usage:
        1. Select environment, location, usage type, server function, and 2-digit ID.
        2. Click "Generate Name Convention" to create a naming convention.
        3. The app checks if the generated name already exists in the audit log.
        4. If the name is unique, it's displayed as a success message.
        5. If the name already exists, an error message is shown.

        Developed by: Haim Cohen (2023)

"""


import streamlit as st
from datetime import datetime
import random

version = '1.2.0.2'

def generate_name_convention(environment, location, usage_type, server_function, id_2_digit):
    # Validate and create the name convention
    valid_environments = ["PRD", "DEV", "QA"]
    if environment not in valid_environments or len(location) < 2 or len(usage_type) < 2 or len(server_function) < 2 or len(id_2_digit) != 2:
        error_message = "❌ Invalid input lengths or values."
        return f"{error_message}"

    if location == "Cloudem-VM":
        location_code = "clm"
    else:
        location_code = location[:3]

    name_convention = f"{environment.lower()}-{location_code}-{usage_type[:5]}-{server_function[:5]}-{id_2_digit}"

    return name_convention

def check_name_existing(generated_name):
    with open("audit.log", "r") as log_file:
        lines = log_file.readlines()
        existing_names = [line.split(" - ")[1].strip() for line in lines if len(line.split(" - ")) >= 2]
        return generated_name in existing_names

    
def generate_unique_2_digit_id(existing_ids):
    while True:
        new_id = str(random.randint(11, 99))
        if new_id not in existing_ids:
            return new_id

def main():
    # Add logo ![Cheat Sheet](~img/cheatcheet.jpg)
    # logo_url = 
    st.image(logo_url, width=150)  # Adjust width as needed

    st.title("Name Convention Generator")

    # Create a sidebar
    menu_selection = st.sidebar.radio("Select Option", ["Help", "About"])

    if menu_selection == "Help":
        st.sidebar.subheader("Help")
        st.sidebar.write("This is the help section. Feel free to provide instructions or assistance here.")
        info_text = """
    The name convention should include:
    - Environment: Production, Developer, QA
    - Location - On-prem, AWS, Azure, GCP etc.
    - Usage type: Production, development, testing, research etc. [5 characters max].
    - Server Function: DB, File-server, DomainController, Application, WebServer etc. [5 characters max].
    - 2-digit ID: Use a unique 2-digit ID as the last two characters.
    
    Examples:
    - prd-proxy-res-aws-20
    - qa-test-vm-01
    - dev-aws-prod-db-20
    """
        st.sidebar.write(f" {info_text}")
    
    elif menu_selection == "About":
        st.sidebar.subheader("About")
        st.sidebar.write(f"Name Convention Generator {version}")
    
    #st.sidebar.image(logo_url, width=150) 
    

    # User inputs
    environment = st.selectbox("Select Environment: )", ["QA", "DEV", "PRD"])
    
    location_options = ["On-prem", "AWS", "Azure", "GCP", "Other"]
    location = st.selectbox("Enter Location:", location_options)
    if location == "Other":
        location = st.text_input("Enter other location:")
    
    usage_type = st.text_input("Enter Usage type (Production, development, testing, research, Infra etc.)").strip().lower()
    server_function = st.text_input("Enter Server Function (DB, File-server, DomainController, Application, WebServer, etc.):").strip().lower()
    id_2_digit = st.text_input("Enter 2-digit ID:")
    
    error_message = None
    if st.button("Generate Name Convention"):
        if not environment or not location or not usage_type or not server_function or not id_2_digit:
            error_message = "All sections are mandatory."

        if not error_message:
            if not id_2_digit.isdigit() or len(id_2_digit) != 2:
                error_message = "ID must be a 2-digit number."

        if not error_message:
            generated_name = generate_name_convention(environment, location, usage_type, server_function, id_2_digit)

            if check_name_existing(generated_name):
                error_message = "System already exists."
            else:
                st.success(f'{generated_name.lower()}')

            # Save output to audit.log
            current_time = datetime.now().strftime("%d-%m-%Y %H:%M")

            with open("audit.log", "a") as log_file:
                log_file.write(f"{current_time} - {generated_name.lower()}\n")



    if st.button("Clear"):
        st.session_state.clear()  # Clear all input fields

    if error_message:
        st.warning(error_message)



    info_text = """
    The name convention should include:
    - Environment: Production, Developer, QA
    - Location - On-prem, AWS, Azure, GCP etc.
    - Usage type: Production, development, testing, research etc. [5 characters max].
    - Server Function: DB, File-server, DomainController, Application, WebServer etc. [5 characters max].
    - 2-digit ID: Use a unique 2-digit ID as the last two characters.
    
    Examples:
    - prd-proxy-res-aws-20
    - qa-qa-test-vm-01
    - dev-aws-prod-db-20
    """

    st.info(info_text)


if __name__ == "__main__":
    main()


st.markdown("***")  # Divider
st.caption(f'Develop by Haim Cohen 2023 :sunglasses: | Version {version}')
