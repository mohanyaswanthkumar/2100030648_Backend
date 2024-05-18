import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bitra7981",
    database="backend"
)

cursor = conn.cursor()

create_tables_queries = [
    """
    CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INT PRIMARY KEY,
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        Email VARCHAR(100),
        DateOfBirth DATE
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Products (
        ProductID INT PRIMARY KEY,
        ProductName VARCHAR(100),
        Price DECIMAL(10, 2)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Orders (
        OrderID INT PRIMARY KEY,
        CustomerID INT,
        OrderDate DATE,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS OrderItems (
        OrderItemID INT PRIMARY KEY,
        OrderID INT,
        ProductID INT,
        Quantity INT,
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
        FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
    )
    """
]

for query in create_tables_queries:
    cursor.execute(query)

insert_data_queries = [
    """
    INSERT INTO Customers (CustomerID, FirstName, LastName, Email, DateOfBirth) VALUES
    (1, 'John', 'Doe', 'john.doe@example.com', '1985-01-15'),
    (2, 'Jane', 'Smith', 'jane.smith@example.com', '1990-06-20')
    """,
    """
    INSERT INTO Products (ProductID, ProductName, Price) VALUES
    (1, 'Laptop', 1000),
    (2, 'Smartphone', 600),
    (3, 'Headphones', 100)
    """,
    """
    INSERT INTO Orders (OrderID, CustomerID, OrderDate) VALUES
    (1, 1, '2023-01-10'),
    (2, 2, '2023-01-12')
    """,
    """
    INSERT INTO OrderItems (OrderItemID, OrderID, ProductID, Quantity) VALUES
    (1, 1, 1, 1),
    (2, 1, 3, 2),
    (3, 2, 2, 1),
    (4, 2, 3, 1)
    """
]

for query in insert_data_queries:
    cursor.execute(query)

conn.commit()
cursor.close()
conn.close()
