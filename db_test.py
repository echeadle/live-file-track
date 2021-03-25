from filechanges import create_file_tracking_db

def main():
    db_name = 'first.db'
    conn = create_file_tracking_db(db_name)
   

    cursor = conn.cursor()

    cursor.execute("create table people (id integer primary key, name text, count integer)")
    cursor.execute("insert into people (name, count) values ('Bob', 1)")

    conn.commit()

    result = cursor.execute("select * from people")
    print(result.fetchall())

    conn.close()

# --------------------------------------------------
if __name__ == '__main__':
    main()