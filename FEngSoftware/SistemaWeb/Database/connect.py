import os
import psycopg2
import psycopg2.extras as ext 

def conn_base(sql,values = None):

    conn = None
    results = []

    try:
        conn = psycopg2.connect(f"host=localhost port=5432 dbname=postgres user=postgres password=kiqdb")
        cursor = conn.cursor(cursor_factory= ext.DictCursor)
        cursor.execute(sql,values)
        conn.commit()
        results = cursor.fetchall()
        cursor.close()
    except (Exception,psycopg2.DatabaseError) as ex:
        print(f"Erro!\n{ex}")
    finally:
        if conn is not None:
            conn.close()
    return results