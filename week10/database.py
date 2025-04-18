import psycopg2

def get_user_and_level():
    conn = psycopg2.connect(
        host="localhost",
        dbname="suppliers",
        user="postgres",
        password="Math314#"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            level INTEGER NOT NULL,
            score INTEGER NOT NULL
        )
    """)
    conn.commit()

    username = input("Enter your username: ")

    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cur.fetchone()

    if result:
        user_id = result[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        print(f"Welcome, new player {username}! Starting from level 1.")
        return conn, cur, user_id, 1

    cur.execute("""
        SELECT level FROM user_score 
        WHERE user_id = %s 
        ORDER BY id DESC 
        LIMIT 1
    """, (user_id,))
    level_result = cur.fetchone()

    if level_result:
        level = level_result[0]
        print(f"Welcome back, {username}! Resuming from level {level}.")
    else:
        level = 1
        print(f"Welcome back, {username}! Starting from level 1 (no save found).")

    return conn, cur, user_id, level