import psycopg

# Connect to PostgreSQL
conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="dlyticakusummam",
    user="postgres",
    password="manoj"
)

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(15),
    City VARCHAR(50),
    CustomerType VARCHAR(30)
);
""")

# Insert data
cursor.execute("""
INSERT INTO Customer
(CustomerID, Name, Email, Phone, City, CustomerType)
VALUES
(1, 'Ravi Sharma', 'ravi.sharma@gmail.com', '9812345001', 'Kathmandu', 'Individual'),
(2, 'Green Leaf Restaurant', 'contact@greenleaf.com', '9812345002', 'Pokhara', 'Business (B2B)'),
(3, 'HR Department', 'hr@company.com', '9812345003', 'Kathmandu', 'Internal'),
(4, 'Kathmandu Metro Office', 'info@ktmmetro.gov.np', '9812345004', 'Kathmandu', 'Government'),
(5, 'Sita Gurung', 'sita.gurung@yahoo.com', '9812345005', 'Lalitpur', 'Loyal/Repeat'),
(6, 'Anil Thapa', 'anil.thapa@outlook.com', '9812345006', 'Biratnagar', 'New Customer'),
(7, 'Maya Karki', 'maya.karki@gmail.com', '9812345007', 'Bhaktapur', 'Impulse'),
(8, 'Suresh Rana', 'suresh.rana@gmail.com', '9812345008', 'Butwal', 'Discount/Bargain'),
(9, 'Nisha Adhikari', 'nisha.adhikari@gmail.com', '9812345009', 'Dharan', 'Need-Based'),
(10, 'Bikash Basnet', 'bikash.basnet@gmail.com', '9812345010', 'Chitwan', 'Wandering/Browsing');
""")

# Save changes
conn.commit()

print("Table created and data inserted successfully!")

# Retrieve the data
cursor.execute("SELECT * FROM Customer")

rows = cursor.fetchall()

for row in rows:
    print(row)

# Close
cursor.close()
conn.close()