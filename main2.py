from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
import random

app = FastAPI()

# ⚡️ Model for request
class EmailRequest(BaseModel):
    email: str

@app.post("/send_otp/")
def send_otp(request: EmailRequest):
    receiver_email = request.email
    otp = random.randint(100000, 999999)

    # ✅ Email details
    sender_email = "godofgenjutsu890@gmail.com"
    app_password = "zxhf dhds yvgm vnou"
    subject = "Your Verification OTP - Zebyte App"
    body = f'''Thank you for using Zebyte!
To complete your verification, please use the one-time password (OTP) below:
OTP:{otp}
If you did not request this code, you can safely ignore this email.

Thank you for choosing Zebyte!

Best regards,
The Zebyte Team'''

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        # ✅ Connect to Gmail SMTP
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)

        return {"status": "success", "otp": otp}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error sending email: {str(e)}")


