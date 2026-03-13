import psycopg2

def load_data(df):

    conn = psycopg2.connect(
        host="localhost",
        database="pharos_sales",
        user="postgres",
        password="Hakim-2004"
    )

    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE sales")
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO sales(
                sales_period,
                outlet_code,
                outlet_name,
                product_code,
                product_name,
                qty,
                product_price,
                actual_sales
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            row["sales_period (DD/MM/YYYY)"],
            row["outlet_code"],
            row["outlet_name"],
            row["product_code"],
            row["product_name"],
            row["qty"],
            row["product_price"],
            row["actual_sales"]
        ))

    conn.commit()
    cur.close()
    conn.close()