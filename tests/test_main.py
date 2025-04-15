"""
Unit Test File for main.py

This file is meant to test the core functions implemented in main.py. 

### Expected Tests:
1. **Spark Session Initialization**
   - Ensure that a Spark session is created correctly.

2. **PostgreSQL Data Loading**
   - Validate that data is correctly loaded into a Spark DataFrame from PostgreSQL.
   - Mock the database connection instead of requiring an actual database.

3. **Data Aggregation Tests**
   - Count the number of films per actor.
   - Calculate the average rental duration per film category.
   - Determine which actor has the highest number of rentals.
   - Identify the most popular movie genre based on rentals.

### Recommended Testing Approach:
- Use the `unittest` framework for test structure.
- Use `mock` (via `unittest.mock.patch`) for database-related operations.
- Use `setUp()` and `tearDown()` to initialize and clean up the Spark session.
- Validate expected outputs for each function.
"""