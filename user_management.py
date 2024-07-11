import pandas as pd
import requests

# In a real application, you'd use a secure database instead of a CSV file
USER_DB = 'users.csv'
WEBHOOK_URL = 'https://f9global.app.n8n.cloud/webhook/user-registration'

def load_users():
    try:
        return pd.read_csv(USER_DB)
    except FileNotFoundError:
        return pd.DataFrame(columns=['email', 'password', 'first_name', 'last_name', 'phone'])

def save_users(df):
    df.to_csv(USER_DB, index=False)

def check_credentials(email, password):
    users = load_users()
    return ((users['email'] == email) & (users['password'] == password)).any()

def register_user(password, first_name, last_name, phone, email):
    users = load_users()
    if (users['email'] == email).any():
        return False
    
    new_user = {
        'email': email,
        'password': password,
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone
    }
    
    # Send data to webhook
    try:
        response = requests.post(WEBHOOK_URL, json=new_user)
        if response.status_code == 200:
            users = pd.concat([users, pd.DataFrame([new_user])], ignore_index=True)
            save_users(users)
            return True
        else:
            return False
    except requests.RequestException:
        return False