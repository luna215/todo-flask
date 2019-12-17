import sqlite3

DB_PATH = './todo.db'
NOT_STARTED = 'Not Started'
IN_PROGRESS = 'In Progress'
COMPLETED = 'Completed'

def add_to_list(item):
    try:
        conn = sqlite3.connect(DB_PATH)

        # Once a connection has been established, we use the cursor
        # object to execute queries
        c = conn.cursor()

        # Keep the initial status as Not Started
        c.execute('insert into items(item, status) values(?, ?)', (item, NOT_STARTED))

        # We commit to save the change
        conn.commit()
        return { 'item': item, 'status': NOT_STARTED}
    except Exception as e:
        print('Error', e)
        return None

def get_all_items():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('select * from items')
        rows = c.fetchall()
        return {"count": len(rows), "items": rows}
    except Exception as e:
        print('Error', e)
        return None