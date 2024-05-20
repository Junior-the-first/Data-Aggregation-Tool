# Data Aggregation Tool

This Python script aggregates data from various sources (CSV, JSON, XML, HTML) and stores it in a SQLite database. It also provides functionality for querying the aggregated data using parameterized queries.

## Requirements

Before you begin, ensure you have the following:
- Python 3.x installed on your system.

## Installation

To set up the Data Aggregation Tool, follow these steps:

1. Clone the repository from Github.
2. Navigate to the project directory in your terminal or command prompt.
3. Install the required Python packages using pip:
    ```sh
    pip install pandas
    pip install beautifulsoup4
    pip install requests
    ```

## Configuration

No additional configuration is needed. Ensure your input data files (CSV, JSON, XML) are available in the project directory.

## Running the Script

To run the script, follow these instructions:

1. Open your terminal or command prompt.
2. Navigate to the directory where the `data_aggregation_tool.py` file is located.
3. Execute the script by running:
    ```sh
    python data_aggregation_tool.py
    ```

## Output

The script will create a SQLite database named `aggregated_data.db` in the current directory. This database will contain:
- A table named `data` with the following schema:
    - `id`: INTEGER PRIMARY KEY
    - `source`: TEXT (indicates the source of the data, e.g., CSV, JSON, XML, HTML)
    - `data`: TEXT (the data record stored as a JSON string)

### Example Query

You can query the database to retrieve specific data. For example, to get all data sourced from a CSV file:

```python
query = "SELECT * FROM data WHERE source = 'CSV'"
results = query_data('aggregated_data.db', query)
print("Query Results:", results)
