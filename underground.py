# import streamlit as st
# from pytube import YouTube
# import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader

# Authenticate = yaml



# with open('config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)


# with open('config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)
#     authenticator = Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )

# name, authentication_status, username = authenticator.login('Login', 'main')

# if authentication_status:
#     authenticator.logout('Logout', 'main')
#     if username == 'jsmith':
#         st.write(f'Welcome *{name}*')
#         st.title('Application 1')
#     elif username == 'rbriggs':
#         st.write(f'Welcome *{name}*')
#         st.title('Application 2')
# elif authentication_status == False:
#     st.error('Username/password is incorrect')
# elif authentication_status == None:
#     st.warning('Please enter your username and password')

# hashed_passwords = stauth.Hasher(['abc', 'def']).generate()



# if st.session_state["authentication_status"]:
#     authenticator.logout('Logout', 'main')
#     st.write(f'Welcome *{st.session_state["name"]}*')
#     st.title('Some content')
# elif st.session_state["authentication_status"] == False:
#     st.error('Username/password is incorrect')
# elif st.session_state["authentication_status"] == None:
#     st.warning('Please enter your username and password')
    


# §§§§§§§§§§§§§§§§§§§§§§§    separa login adm de usuario    §§§§§§§§§§§§§§§§§§§§§§
    
# if user_role == "admin":
#     show_admin_UI()
# else:
#     show_regular_UI()

# data = get_country_data(country=user_country)


# §§§§§§§§§§§§§§§§§§§§§§§       §§§§§§§§§§§§§§§§§§§§§§


# YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
# yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()



import sqlite3
import streamlit as st


def create_database():
    
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name='customers'
    """)
    if not c.fetchone():
        c.execute('''CREATE TABLE customers
                     (name text, address text, phone text)''')
        conn.commit()
    conn.close()

def add_customer(name, address, phone):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?, ?, ?)", (name, address, phone))
    conn.commit()
    conn.close()

def delete_customer(name):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE name=?", (name,))
    conn.commit()
    conn.close()

def update_customer(name, address, phone):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("UPDATE customers SET address = ?, phone = ? WHERE name = ?", (address, phone, name))
    conn.commit()
    conn.close()

def view_customers():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    customers = c.fetchall()
    conn.close()
    return customers

def search_customer(name, phone):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE name=? OR phone=?", (name, phone))
    customers = c.fetchall()
    conn.close()
    return customers


def main():
    st.title("Customer Database App")
    
    
    create_database()

    name = st.text_input("Name")
    address = st.text_input("Address")
    phone = st.text_input("Phone Number")
    st.sidebar.header("Click for operations")
    if st.sidebar.button("Add"):
        add_customer(name, address, phone)

    if st.sidebar.button("Delete"):
        delete_customer(name)

    if st.sidebar.button("Update"):
        update_customer(name, address, phone)


    if st.sidebar.button("Search"):
        customers = search_customer(name, phone)
        st.header("Customers File")
        st.table(customers)   

    if st.sidebar.button("View"):
        customers = view_customers()
        st.header("Customers File")
        st.table(customers)

if __name__ == '__main__':
    main()