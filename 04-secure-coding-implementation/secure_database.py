import mysql.connector
import logging
import re

# --- Logging Setup (Extra Credit: logs suspicious input) ---
logging.basicConfig(
    filename="security.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --- Database Connection ---
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # Replace with your DB user
        password="",         # Replace with your DB password
        database="dvwa"      # Replace with your database name
    )

# --- Input Validation Layer (Extra Credit) ---
def is_valid_user_id(user_id):
    """Only allow pure numeric input for user ID."""
    return re.fullmatch(r'\d+', str(user_id)) is not None

# --- Secure User Lookup Function ---
def get_user_by_id(user_id):
    """
    Safely queries the database for a user by ID.
    Uses a parameterized query to prevent SQL injection completely.
    """

    # Input validation check
    if not is_valid_user_id(user_id):
        logging.warning(f"Suspicious input detected and blocked: '{user_id}'")
        return {"error": "Invalid input. Only numeric user IDs are accepted."}

    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        # Parameterized query -- user input is NEVER part of the SQL string
        query = "SELECT user_id, first_name, last_name FROM users WHERE user_id = %s"
        cursor.execute(query, (user_id,))  # Input passed separately as a parameter

        result = cursor.fetchone()
        cursor.close()
        connection.close()

        if result:
            return result
        else:
            # Generic message -- avoids leaking whether user exists (Extra Credit)
            return {"message": "No user found."}

    except mysql.connector.Error:
        # Never expose raw database errors to the user (Extra Credit)
        logging.error("Database error occurred during user lookup.")
        return {"error": "An internal error occurred. Please try again later."}


# --- Example Usage ---
if __name__ == "__main__":
    test_inputs = [
        "1",                    # Valid input
        "1 OR 1=1",            # Classic SQLi attempt
        "1 UNION SELECT user, password FROM users#",  # UNION attack
        "' OR '1'='1",         # Quote-based SQLi
        "2"                     # Another valid input
    ]

    for test in test_inputs:
        print(f"\nInput: {test}")
        print(f"Result: {get_user_by_id(test)}")
