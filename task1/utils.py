import psycopg2

def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def save_fibonacci_number(n: int, number: int):
    conn = psycopg2.connect(host="sirojserver",database="work", user="sirojs", password="siroj2020")
    cur = conn.cursor()
    cur.execute("INSERT INTO fibonacci (id, number) VALUES (%s, %s)", (n, number))
    conn.commit()
    cur.close()
    conn.close()
