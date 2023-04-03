import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import Flask, request

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    # Parse email data from the request body
    recipient = request.form['dxbwansa@gmail.com']
    subject = request.form['Bonjour']
    message = request.form['Oui']

    # Create a SendGrid Mail object
    email = Mail(
        from_email='ybwansa@gmail.com',
        to_emails=dxbwansagmail.com,
        subject=subject,
        html_content=message)

    try:
        # Authenticate with SendGrid using an API key
        sg = SendGridAPIClient(api_key=os.environ.get('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'))
        # Send the email
        response = sg.send(email)
        # Return a success response
        return {'message': 'Email sent successfully.'}, 200
    except Exception as e:
        # Handle any errors that occur
        return {'message': f'Error sending email: {str(e)}'}, 500
