# It is template for PostgreSql query.

import psycopg2

try:
    # Establish a connection to the database
    conn = psycopg2.connect(
        host="111.111.111.11",
        database="Your_DB",
        user="user_name",
        password="password"
    )

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Execute a sample SQL query to test the connection
    cur.execute("SELECT 1")
    result = cur.fetchone()

    # Check if the query result is 1, indicating a successful connection
    if result[0] == 1:
        print("Connection to the database is successful")

        # Execute the desired SQL query
        cur.execute(" --POSTGRESQL QUERY-- ")  # Insert your SQL query here

        # Print the number of rows affected by the query
        print(f"Inserted {cur.rowcount} rows")

        # Commit the changes to the database
        conn.commit()
    else:
        print("An error occurred")

except Exception as e:
    # If any exception occurs, print the error message
    print(f"An error occurred: {e}")

finally:
    # Close the cursor and connection to the database
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()

# Add this line to stop execution after running in cron
raise SystemExit