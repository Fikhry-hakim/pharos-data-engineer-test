-- View all sales data
    SELECT * FROM sales;

-- Total sales per outlet
SELECT outlet_name,
       SUM(actual_sales) AS total_sales
FROM sales
GROUP BY outlet_name
ORDER BY total_sales DESC;

-- Product sales per outlet
SELECT outlet_name,
       product_name,
       SUM(actual_sales) AS total_sales
FROM sales
GROUP BY outlet_name, product_name
ORDER BY total_sales DESC;

-- Total sales per product
SELECT product_name,
       SUM(actual_sales) AS total_sales
FROM sales
GROUP BY product_name
ORDER BY total_sales DESC;

-- Monthly sales
SELECT DATE_TRUNC('month', sales_period) AS month,
       SUM(actual_sales) AS total_sales
FROM sales
GROUP BY month
ORDER BY month;