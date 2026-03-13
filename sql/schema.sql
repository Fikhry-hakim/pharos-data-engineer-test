-- Buat tabel sales
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    sales_period DATE,
    outlet_code VARCHAR(50),
    outlet_name TEXT,
    product_code VARCHAR(50),
    product_name TEXT,
    qty INTEGER,
    product_price INTEGER,
    actual_sales INTEGER
);
