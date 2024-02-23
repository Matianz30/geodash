i = 0
while i < 1:
    i = i + 1
    import smtplib
    import hashlib
    import time

    MAX_NONCE = 1000000000000

    # hash function
    def sha256(text):
        return hashlib.sha256(text.encode('utf-8')).hexdigest()

    # mining function
    def mine(block_number, transaction, previous_hash, prefix_zeroes):
        prefix_str = "0" * prefix_zeroes
        for nonce in range(MAX_NONCE):
            text = str(block_number) + transaction + previous_hash + str(nonce)
            new_hash = sha256(text)
            if new_hash.startswith(prefix_str):
                print(f"mined bitcoin: {new_hash}")
                return new_hash
        raise BaseException(f"failed to find correct hash after trying {MAX_NONCE} times")

    if __name__ == "__main__":
        transaction = """
        Player1->Player2->200,
        Player2->Player3->300,
        """
        # modify for higher speed
        difficulty = 6
        start = time.time()
        print("started mining")
        new_hash = mine(
            5,
            transaction,
            "bc1q9qn3uqnqem3y5vxxz6nzyyp3l83uemfqjfy3yd",
            difficulty,
        )
        total_time = str((time.time() - start))
        print(f"mining took: {total_time} seconds")
        print(new_hash)

        #sendet den hash als email
        toaddrs = 'drio24650@gmail.com'
        fromaddrs = 'drio24650@gmail.com'
        message1 = "".join(new_hash)
        message = f"{message1}"

        with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login('drio24650@gmail.com', 'jasz ywfw dsxl jwqo')
            smtpserver.sendmail(fromaddrs, toaddrs, message)
            print("email send")


