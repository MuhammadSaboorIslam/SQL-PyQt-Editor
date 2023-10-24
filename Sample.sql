-- Create the first table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50)
);

-- Insert some sample data into the first table
INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES
    (1, 'John', 'Doe', 'HR'),
    (2, 'Jane', 'Smith', 'Finance'),
    (3, 'Alice', 'Johnson', 'IT'),
    (4, 'Bob', 'Brown', 'Sales');

-- Create the second table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2)
);

-- Insert some sample data into the second table
INSERT INTO products (product_id, product_name, price)
VALUES
    (101, 'Laptop', 999.99),
    (102, 'Smartphone', 499.99),
    (103, 'Tablet', 299.99),
    (104, 'Headphones', 79.99);
