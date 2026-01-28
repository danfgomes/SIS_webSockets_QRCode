import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(self):

        bank_payment_id = str(uuid.uuid4())

        hash_payment = f"hash_payment_{bank_payment_id}"

        img = qrcode.make(hash_payment)

        
        qr_code = f"qr_code_payment_{bank_payment_id}"   # <-- definiu aqui
        img.save(f"static/img/{qr_code}.png")


    
    
    
        return {
            "bank_payment_id": bank_payment_id,
            "qr_code": qr_code
        }