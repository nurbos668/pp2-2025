from database import get_user_and_level
from snake import start_game

def main():
    conn, cur, user_id, level = get_user_and_level()
    start_game(user_id, level, conn, cur)
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()