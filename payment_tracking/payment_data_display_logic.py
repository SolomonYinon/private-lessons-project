import json

def get_payment_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            # Get all paid students with their payment information
            paid_students = []
            for student in data.get('students', []):
                if student.get('paid', False):
                    paid_students.append({
                        'id': student['id'],
                        'name': student['name'],
                        'amount': student.get('payment_amount', 0),
                        'date': student.get('payment_date', 'N/A')
                    })
            return paid_students
    except FileNotFoundError:
        return []

def get_payment_summary():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            total_paid = sum(student.get('payment_amount', 0) 
                           for student in data.get('students', [])
                           if student.get('paid', False))
            total_students = len([s for s in data.get('students', []) if s.get('paid', False)])
            return {
                'total_amount': total_paid,
                'total_students': total_students
            }
    except FileNotFoundError:
        return {'total_amount': 0, 'total_students': 0}

def display_payment_data():
    # Logic to display payment data
    payments = get_payment_data()
    payment_summary = get_payment_summary()
    # Add logic to display payment data and summary
    return payments, payment_summary
