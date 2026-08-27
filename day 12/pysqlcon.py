import psycopg


conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="dlyticakusummam",
    user="postgres",
    password="manoj"
)


cursor = conn.cursor()


# cursor.execute("SELECT * FROM customer")


# rows = cursor.fetchall()


 
# print(rows)


# cursor.execute(
#     """create table mytable (id int primary key, first_name varchar(50), last_name varchar(50), email text unique, phone text, city text, created_at date default current_date);
#     """)

# cursor.execute("""
#     INSERT INTO mytable
#     VALUES (1,'Manoj', 'Gaihre','manoj@gmail.com','987654321','Kathmandu', '2004-04-22');
# """)


# cursor.execute("SELECT * FROM mytable")
# rows = cursor.fetchall()
# print(rows)


# cursor.execute("""
# UPDATE mytable
 
# SET "f_name" = 'Shyam'
 
# WHERE id = 1;
# """)




# cursor.execute("""CREATE TABLE Customers (
#     CustomerID INT PRIMARY KEY,
#     Name VARCHAR(50),
#     Email VARCHAR(100),
#     Phone VARCHAR(15),
#     City VARCHAR(50),
#     CustomerType VARCHAR(30)
# );""")
 
# cursor.execute("""INSERT INTO Customers (CustomerID, Name, Email, Phone, City, CustomerType) VALUES
# (1, 'Ravi Sharma', 'ravi.sharma@gmail.com', '9812345001', 'Kathmandu', 'Individual'),
# (2, 'Green Leaf Restaurant', 'contact@greenleaf.com', '9812345002', 'Pokhara', 'Business (B2B)'),
# (3, 'HR Department', 'hr@company.com', '9812345003', 'Kathmandu', 'Internal'),
# (4, 'Kathmandu Metro Office', 'info@ktmmetro.gov.np', '9812345004', 'Kathmandu', 'Government'),
# (5, 'Sita Gurung', 'sita.gurung@yahoo.com', '9812345005', 'Lalitpur', 'Loyal/Repeat'),
# (6, 'Anil Thapa', 'anil.thapa@outlook.com', '9812345006', 'Biratnagar', 'New Customer'),
# (7, 'Maya Karki', 'maya.karki@gmail.com', '9812345007', 'Bhaktapur', 'Impulse'),
# (8, 'Suresh Rana', 'suresh.rana@gmail.com', '9812345008', 'Butwal', 'Discount/Bargain'),
# (9, 'Nisha Adhikari', 'nisha.adhikari@gmail.com', '9812345009', 'Dharan', 'Need-Based'),
# (10, 'Bikash Basnet', 'bikash.basnet@gmail.com', '9812345010', 'Chitwan', 'Wandering/Browsing');
# """)

# Update the email of customer with CustomerID = 3 to a new HR email address.
# cursor.execute("""
#     UPDATE Customers
#     SET Email = 'hr.new@company.com'
#     WHERE CustomerID = 3
# """)

# Find all customers (excluding 'Cancelled' orders) who have spent more than 1000 total, and show them sorted from highest to lowest spender.
cursor.execute("""SELECT c.CustomerID,
    c.Name,
    SUM(o.TotalAmount) AS TotalSpent
FROM Customer c
JOIN Orders o
    ON c.CustomerID = o.CustomerID
WHERE o.Status <> 'Cancelled'
GROUP BY c.CustomerID, c.Name
HAVING SUM(o.TotalAmount) > 1000
ORDER BY TotalSpent DESC""")


# Find customers who spent more than 500 in January 2025 (completed orders only), sorted by spend



# Find customers (excluding pending orders) who placed more than 1 order, sorted by number of orders (highest first).
cursor.execute("""SELECT c.CustomerID,
    c.Name,
    SUM(o.TotalAmount) AS TotalSpent
FROM Customer c
JOIN Orders o
    ON c.CustomerID = o.CustomerID
WHERE o.Status != 'Pending'
GROUP BY c.CustomerID, c.Name
HAVING SUM(o.TotalAmount) > 1000
ORDER BY TotalSpent DESC""")

conn.commit()

cursor.close()
conn.close()