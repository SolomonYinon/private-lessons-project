import json

def integrate_payment_gateway(payment_data):
    # Logic to integrate with payment gateway
    print("Integrating payment gateway...")
    # Simulate payment processing
    if payment_data:
        print(f"Payment of {payment_data['amount']} processed for {payment_data['user']}.")
    else:
        print("No payment data provided.")

def process_payment(payment_data):
    """Process payment and update student payment status"""
    try:
        # Validate payment data
        if not all(key in payment_data for key in ['student_id', 'amount', 'payment_method']):
            return False, "Invalid payment data"

        # Load current data
        with open('data.json', 'r') as f:
            data = json.load(f)

        # Find student and update payment status
        for student in data.get('students', []):
            if student['id'] == payment_data['student_id']:
                # Record payment
                if 'payments' not in data:
                    data['payments'] = []
                
                payment_record = {
                    'student_id': student['id'],
                    'amount': payment_data['amount'],
                    'payment_method': payment_data['payment_method'],
                    'date': payment_data['date'],
                    'status': 'completed'
                }
                
                data['payments'].append(payment_record)
                student['paid'] = True
                
                # Save updated data
                with open('data.json', 'w') as f:
                    json.dump(data, f)
                    
                return True, "Payment processed successfully"
                
        return False, "Student not found"
        
    except Exception as e:
        return False, f"Payment processing error: {str(e)}"

def get_payment_history(student_id=None):
    """Get payment history for a specific student or all payments"""
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            
        payments = data.get('payments', [])
        if student_id:
            payments = [p for p in payments if p['student_id'] == student_id]
            
        return True, payments
        
    except FileNotFoundError:
        return False, "No payment records found"
    except Exception as e:
        return False, f"Error retrieving payment history: {str(e)}"
