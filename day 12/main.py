import psycopg


conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="dlyticakusummam",
    user="postgres",
    password="manoj"
)


cursor = conn.cursor()


cursor.execute("SELECT * FROM customer")


rows = cursor.fetchall()


 
print(rows)
cursor.execute("""create table mytable (id int primary key, name varchar(50))""");


cursor.close()
conn.close()





import psycopg2
 
def connect_to_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="test_db",
            user="",
            password="",
            port="5432"
        )
        print("Successfully connected to the PostgreSQL database!")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None
 
# Establish connection
conn = connect_to_db()
 
if conn:
    try:
        cursor = conn.cursor()
        # Execute a SELECT query on the customers table
        cursor.execute("SELECT * FROM bank_customers;")
        records = cursor.fetchall()
 
        if records:
            print("Records in 'customers' table:")
            for row in records:
                print(row)
        else:
            print("No records found in 'customers' table.")
 
    except psycopg2.Error as e:
        print(f"Error executing query: {e}")
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        conn.close()
        print("Connection closed after query.")







#  look this also 
# ============================================================
# DAY 13: BANKING DATABASE - COMPLETE RUNNABLE SQLITE SHEET
# JUPYTER / LET'S NOTEBOOK VERSION
# Database: kusuma_class.db
# ============================================================
 
import sqlite3
import pandas as pd
 
# ============================================================
# 1. CONNECT TO SQLITE DATABASE
# ============================================================
 
DB_NAME = "kusuma_class.db"
 
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()
 
# Enable foreign keys
cursor.execute("PRAGMA foreign_keys = ON;")
 
print("=" * 70)
print("CONNECTED TO DATABASE:", DB_NAME)
print("=" * 70)
 
 
# ============================================================
# 2. CREATE CUSTOMERS TABLE
# ============================================================
 
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers_new (
 
    customer_id INTEGER PRIMARY KEY,
 
    first_name TEXT NOT NULL,
 
    last_name TEXT NOT NULL,
 
    email TEXT UNIQUE,
 
    phone TEXT,
 
    city TEXT,
 
    created_at DATE DEFAULT CURRENT_DATE
);
""")
 
 
# ============================================================
# 3. CREATE ACCOUNTS TABLE
# ============================================================
 
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts_new (
 
    account_id INTEGER PRIMARY KEY,
 
    customer_id INTEGER NOT NULL,
 
    account_number TEXT UNIQUE NOT NULL,
 
    account_type TEXT,
 
    balance NUMERIC DEFAULT 0,
 
    account_status TEXT,
 
    opened_date DATE,
 
    FOREIGN KEY (customer_id)
    REFERENCES customers_new(customer_id)
);
""")
 
 
# ============================================================
# 4. CREATE TRANSACTIONS TABLE
# ============================================================
 
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions_new (
 
    transaction_id INTEGER PRIMARY KEY,
 
    account_id INTEGER NOT NULL,
 
    transaction_type TEXT,
 
    amount NUMERIC,
 
    txn_date DATE,
 
    description TEXT,
 
    FOREIGN KEY (account_id)
    REFERENCES accounts_new(account_id)
);
""")
 
conn.commit()
 
print("\nTables created successfully.")
 
 
# ============================================================
# 5. INSERT CUSTOMER DATA
# ============================================================
 
customers_data = [
 
    (1, "Kusum", "Khatri",
     "kusum@example.com",
     "9800000000",
     "Kathmandu"),
 
    (2, "Ram", "Sharma",
     "ram@example.com",
     "9811111111",
     "Kathmandu"),
 
    (3, "Sita", "Thapa",
     "sita@example.com",
     "9822222222",
     "Pokhara"),
 
    (4, "Hari", "Karki",
     "hari@example.com",
     "9833333333",
     "Chitwan")
]
 
cursor.executemany("""
INSERT OR IGNORE INTO customers_new
(
    customer_id,
    first_name,
    last_name,
    email,
    phone,
    city
)
VALUES (?, ?, ?, ?, ?, ?);
""", customers_data)
 
conn.commit()
 
print("Customer data inserted.")
 
 
# ============================================================
# 6. INSERT ACCOUNT DATA
# ============================================================
 
accounts_data = [
 
    (1, 1, "ACC001", "Savings",
     50000, "Active", "2026-01-01"),
 
    (2, 2, "ACC002", "Current",
     75000, "Active", "2026-02-01"),
 
    (3, 3, "ACC003", "Savings",
     30000, "Inactive", "2026-03-01"),
 
    (4, 4, "ACC004", "Savings",
     45000, "Active", "2026-04-01")
]
 
cursor.executemany("""
INSERT OR IGNORE INTO accounts_new
(
    account_id,
    customer_id,
    account_number,
    account_type,
    balance,
    account_status,
    opened_date
)
VALUES (?, ?, ?, ?, ?, ?, ?);
""", accounts_data)
 
conn.commit()
 
print("Account data inserted.")
 
 
# ============================================================
# 7. INSERT TRANSACTION DATA
# ============================================================
 
transactions_data = [
 
    (1, 1, "Deposit",
     10000, "2026-01-10",
     "Salary Deposit"),
 
    (2, 1, "Withdrawal",
     5000, "2026-01-15",
     "ATM Withdrawal"),
 
    (3, 2, "Deposit",
     20000, "2026-02-10",
     "Business Income"),
 
    (4, 3, "Withdrawal",
     3000, "2026-03-05",
     "Online Payment"),
 
    (5, 4, "Deposit",
     15000, "2026-04-10",
     "Cash Deposit")
]
 
cursor.executemany("""
INSERT OR IGNORE INTO transactions_new
(
    transaction_id,
    account_id,
    transaction_type,
    amount,
    txn_date,
    description
)
VALUES (?, ?, ?, ?, ?, ?);
""", transactions_data)
 
conn.commit()
 
print("Transaction data inserted.")
 
 
# ============================================================
# HELPER FUNCTION
# ============================================================
 
def run_query(title, query):
 
    print("\n")
    print("=" * 70)
    print(title)
    print("=" * 70)
 
    df = pd.read_sql_query(query, conn)
 
    display(df)
 
    return df
 
 
# ============================================================
# 8. CHECK ALL TABLES
# ============================================================
 
run_query(
    "1. CHECK ALL TABLES",
    """
    SELECT name
    FROM sqlite_master
    WHERE type = 'table';
    """
)
 
 
# ============================================================
# 9. VIEW CUSTOMERS
# ============================================================
 
run_query(
    "2. VIEW CUSTOMERS",
    """
    SELECT *
    FROM customers_new;
    """
)
 
 
# ============================================================
# 10. VIEW ACCOUNTS
# ============================================================
 
run_query(
    "3. VIEW ACCOUNTS",
    """
    SELECT *
    FROM accounts_new;
    """
)
 
 
# ============================================================
# 11. VIEW TRANSACTIONS
# ============================================================
 
run_query(
    "4. VIEW TRANSACTIONS",
    """
    SELECT *
    FROM transactions_new;
    """
)
 
 
# ============================================================
# 12. READ ALL CUSTOMERS
# ============================================================
 
run_query(
    "12. READ ALL CUSTOMERS",
    """
    SELECT *
    FROM customers_new;
    """
)
 
 
# ============================================================
# 13. FILTER ACTIVE ACCOUNTS
# ============================================================
 
run_query(
    "13. FILTER ACTIVE ACCOUNTS",
    """
    SELECT *
    FROM accounts_new
    WHERE account_status = 'Active';
    """
)
 
 
# ============================================================
# 14. FILTER SAVINGS ACCOUNTS
# ============================================================
 
run_query(
    "14. FILTER SAVINGS ACCOUNTS",
    """
    SELECT *
    FROM accounts_new
    WHERE account_type = 'Savings';
    """
)
 
 
# ============================================================
# 15. FILTER HIGH BALANCE ACCOUNTS
# ============================================================
 
run_query(
    "15. FILTER HIGH BALANCE ACCOUNTS",
    """
    SELECT *
    FROM accounts_new
    WHERE balance > 50000;
    """
)
 
 
# ============================================================
# 16. FETCH ONE CUSTOMER
# ============================================================
 
run_query(
    "16. FETCH ONE CUSTOMER",
    """
    SELECT *
    FROM customers_new
    LIMIT 1;
    """
)
 
 
# ============================================================
# 17. FETCH FIRST 3 CUSTOMERS
# ============================================================
 
run_query(
    "17. FETCH FIRST 3 CUSTOMERS",
    """
    SELECT *
    FROM customers_new
    LIMIT 3;
    """
)
 
 
# ============================================================
# 18. SORT ACCOUNTS BY BALANCE
# ============================================================
 
run_query(
    "18. SORT ACCOUNTS BY BALANCE",
    """
    SELECT *
    FROM accounts_new
    ORDER BY balance DESC;
    """
)
 
 
# ============================================================
# 19. JOIN CUSTOMERS + ACCOUNTS
# ============================================================
 
run_query(
    "19. JOIN CUSTOMERS + ACCOUNTS",
    """
    SELECT
 
        c.customer_id,
 
        c.first_name,
 
        c.last_name,
 
        c.email,
 
        a.account_number,
 
        a.account_type,
 
        a.balance,
 
        a.account_status
 
    FROM customers_new AS c
 
    JOIN accounts_new AS a
 
        ON c.customer_id = a.customer_id;
    """
)
 
 
# ============================================================
# 20. JOIN ALL THREE TABLES
# ============================================================
 
run_query(
    "20. JOIN ALL THREE TABLES",
    """
    SELECT
 
        c.first_name,
 
        c.last_name,
 
        a.account_number,
 
        a.account_type,
 
        t.transaction_type,
 
        t.amount,
 
        t.txn_date,
 
        t.description
 
    FROM customers_new AS c
 
    JOIN accounts_new AS a
        ON c.customer_id = a.customer_id
 
    JOIN transactions_new AS t
        ON a.account_id = t.account_id
 
    ORDER BY t.txn_date;
    """
)
 
 
# ============================================================
# 21. COUNT CUSTOMERS
# ============================================================
 
run_query(
    "21. COUNT CUSTOMERS",
    """
    SELECT
        COUNT(*) AS total_customers
    FROM customers_new;
    """
)
 
 
# ============================================================
# 22. COUNT ACTIVE ACCOUNTS
# ============================================================
 
run_query(
    "22. COUNT ACTIVE ACCOUNTS",
    """
    SELECT
        COUNT(*) AS active_accounts
    FROM accounts_new
    WHERE account_status = 'Active';
    """
)
 
 
# ============================================================
# 23. TOTAL BANK BALANCE
# ============================================================
 
run_query(
    "23. TOTAL BANK BALANCE",
    """
    SELECT
        SUM(balance) AS total_balance
    FROM accounts_new;
    """
)
 
 
# ============================================================
# 24. AVERAGE ACCOUNT BALANCE
# ============================================================
 
run_query(
    "24. AVERAGE ACCOUNT BALANCE",
    """
    SELECT
        AVG(balance) AS average_balance
    FROM accounts_new;
    """
)
 
 
# ============================================================
# 25. MINIMUM AND MAXIMUM BALANCE
# ============================================================
 
run_query(
    "25. MINIMUM AND MAXIMUM BALANCE",
    """
    SELECT
 
        MIN(balance) AS minimum_balance,
 
        MAX(balance) AS maximum_balance
 
    FROM accounts_new;
    """
)
 
 
# ============================================================
# 26. TOTAL TRANSACTION AMOUNT
# ============================================================
 
run_query(
    "26. TOTAL TRANSACTION AMOUNT",
    """
    SELECT
 
        transaction_type,
 
        SUM(amount) AS total_amount
 
    FROM transactions_new
 
    GROUP BY transaction_type;
    """
)
 
 
# ============================================================
# 27. TRANSACTION COUNT BY TYPE
# ============================================================
 
run_query(
    "27. TRANSACTION COUNT BY TYPE",
    """
    SELECT
 
        transaction_type,
 
        COUNT(*) AS total_transactions
 
    FROM transactions_new
 
    GROUP BY transaction_type;
    """
)
 
 
# ============================================================
# 28. ACCOUNT COUNT BY TYPE
# ============================================================
 
run_query(
    "28. ACCOUNT COUNT BY TYPE",
    """
    SELECT
 
        account_type,
 
        COUNT(*) AS total_accounts
 
    FROM accounts_new
 
    GROUP BY account_type;
    """
)
 
 
# ============================================================
# 29. UPDATE CUSTOMER
# ============================================================
 
cursor.execute("""
UPDATE customers_new
 
SET city = 'Lalitpur'
 
WHERE customer_id = 1;
""")
 
conn.commit()
 
print("\n29. UPDATE CUSTOMER")
print("Customer 1 city updated to Lalitpur.")
 
 
# ============================================================
# 30. UPDATE ACCOUNT BALANCE
# ============================================================
 
# IMPORTANT:
# Set to 60000 rather than balance + 10000
# so the notebook can be safely executed multiple times.
 
cursor.execute("""
UPDATE accounts_new
 
SET balance = 60000
 
WHERE account_id = 1;
""")
 
conn.commit()
 
print("\n30. UPDATE ACCOUNT BALANCE")
print("Account ACC001 balance updated to 60000.")
 
 
# ============================================================
# 31. UPDATE ACCOUNT STATUS
# ============================================================
 
cursor.execute("""
UPDATE accounts_new
 
SET account_status = 'Inactive'
 
WHERE account_id = 4;
""")
 
conn.commit()
 
print("\n31. UPDATE ACCOUNT STATUS")
print("Account ACC004 updated to Inactive.")
 
 
# ============================================================
# 32. DELETE TRANSACTION
# ============================================================
 
cursor.execute("""
DELETE FROM transactions_new
 
WHERE transaction_id = 5;
""")
 
conn.commit()
 
print("\n32. DELETE TRANSACTION")
print("Transaction 5 deleted.")
 
 
# ============================================================
# 33. DELETE CUSTOMER
# ============================================================
 
# Not executed intentionally because customer 4
# still has an account linked to it.
 
print("\n33. DELETE CUSTOMER")
print("Delete operation skipped to preserve foreign-key integrity.")
 
 
# ============================================================
# 34. CUSTOMER ACCOUNT SUMMARY
# ============================================================
 
run_query(
    "34. CUSTOMER ACCOUNT SUMMARY",
    """
    SELECT
 
        c.customer_id,
 
        c.first_name,
 
        c.last_name,
 
        COUNT(a.account_id) AS total_accounts,
 
        COALESCE(SUM(a.balance), 0) AS total_balance,
 
        COALESCE(AVG(a.balance), 0) AS average_balance
 
    FROM customers_new AS c
 
    LEFT JOIN accounts_new AS a
 
        ON c.customer_id = a.customer_id
 
    GROUP BY
 
        c.customer_id,
 
        c.first_name,
 
        c.last_name;
    """
)
 
 
# ============================================================
# 35. TRANSACTION SUMMARY BY ACCOUNT
# ============================================================
 
run_query(
    "35. TRANSACTION SUMMARY BY ACCOUNT",
    """
    SELECT
 
        a.account_number,
 
        COUNT(t.transaction_id) AS total_transactions,
 
        COALESCE(SUM(t.amount), 0) AS total_transaction_amount
 
    FROM accounts_new AS a
 
    LEFT JOIN transactions_new AS t
 
        ON a.account_id = t.account_id
 
    GROUP BY a.account_number;
    """
)
 
 
# ============================================================
# 36. CUSTOMERS WITH ACTIVE ACCOUNTS
# ============================================================
 
run_query(
    "36. CUSTOMERS WITH ACTIVE ACCOUNTS",
    """
    SELECT
 
        c.first_name,
 
        c.last_name,
 
        a.account_number,
 
        a.balance
 
    FROM customers_new c
 
    JOIN accounts_new a
 
        ON c.customer_id = a.customer_id
 
    WHERE a.account_status = 'Active';
    """
)
 
 
# ============================================================
# 37. HIGHEST BALANCE ACCOUNT
# ============================================================
 
run_query(
    "37. HIGHEST BALANCE ACCOUNT",
    """
    SELECT *
 
    FROM accounts_new
 
    ORDER BY balance DESC
 
    LIMIT 1;
    """
)
 
 
# ============================================================
# 38. TRANSACTIONS ABOVE 5000
# ============================================================
 
run_query(
    "38. TRANSACTIONS ABOVE 5000",
    """
    SELECT *
 
    FROM transactions_new
 
    WHERE amount > 5000;
    """
)
 
 
# ============================================================
# 39. CUSTOMER SEARCH
# ============================================================
 
run_query(
    "39. CUSTOMER SEARCH",
    """
    SELECT *
 
    FROM customers_new
 
    WHERE first_name LIKE '%Kusum%';
    """
)
 
 
# ============================================================
# 40. FINAL COMPLETE BANKING REPORT
# ============================================================
 
run_query(
    "40. FINAL COMPLETE BANKING REPORT",
    """
    SELECT
 
        c.customer_id,
 
        c.first_name || ' ' || c.last_name
        AS customer_name,
 
        c.city,
 
        a.account_number,
 
        a.account_type,
 
        a.balance,
 
        a.account_status,
 
        t.transaction_type,
 
        t.amount,
 
        t.txn_date,
 
        t.description
 
    FROM customers_new c
 
    LEFT JOIN accounts_new a
 
        ON c.customer_id = a.customer_id
 
    LEFT JOIN transactions_new t
 
        ON a.account_id = t.account_id
 
    ORDER BY
 
        c.customer_id,
 
        t.txn_date;
    """
)
 
 
# ============================================================
# FINAL DATABASE CHECK
# ============================================================
 
print("\n")
print("=" * 70)
print("DAY 13 COMPLETED SUCCESSFULLY")
print("=" * 70)
 
print("\nDatabase:", DB_NAME)
 
print("\nCustomers:",
      cursor.execute("SELECT COUNT(*) FROM customers_new").fetchone()[0])
 
print("Accounts:",
      cursor.execute("SELECT COUNT(*) FROM accounts_new").fetchone()[0])
 
print("Transactions:",
      cursor.execute("SELECT COUNT(*) FROM transactions_new").fetchone()[0])
 
print("\nSQLite database is ready for use.")
 
 
# ============================================================
# CLOSE DATABASE
# ============================================================
 
conn.close()
 
print("\nDatabase connection closed.")










# do this 
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    Amount DECIMAL(10,2),
    Status VARCHAR(20),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);
 
INSERT INTO Orders (OrderID, CustomerID, OrderDate, Amount, Status) VALUES
(101, 1, '2025-01-10', 1500.00, 'Completed'),
(102, 1, '2025-02-15', 2500.00, 'Completed'),
(103, 2, '2025-01-20', 12000.00, 'Completed'),
(104, 3, '2025-03-01', 500.00, 'Cancelled'),
(105, 5, '2025-01-05', 800.00, 'Completed'),
(106, 5, '2025-02-10', 950.00, 'Completed'),
(107, 5, '2025-03-15', 1100.00, 'Completed'),
(108, 6, '2025-01-25', 300.00, 'Pending'),
(109, 8, '2025-02-05', 200.00, 'Completed'),
(110, 9, '2025-03-10', 4500.00, 'Completed');