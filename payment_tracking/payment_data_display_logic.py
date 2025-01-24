import json

def display_payment_data():
    # Logic to display payment data
    try:
        with open('payments.json', 'r') as f:
            payments = json.load(f)
            return payments  # Return the list of payments
    except FileNotFoundError:
        print("No payments found.")
        return []
