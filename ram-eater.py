import secrets

data = []
count = 0
while True:
    byte = secrets.token_bytes(10000)
    data.append(byte)
    data.append(byte)
    data.append(byte)
    count += 3
    print(f"Ram Eaten: {count}")
