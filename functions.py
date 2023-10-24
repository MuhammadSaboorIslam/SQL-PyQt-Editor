import re


def extract_table_names(path):
    # Read the SQL file
    with open(path, 'r') as file:
        sql_content = file.read()

    # Define a regular expression pattern to match CREATE TABLE statements
    table_pattern = r'CREATE TABLE (\w+)'

    # Find all matches in the SQL content
    table_names = re.findall(table_pattern, sql_content)

    # Print the table names
    if table_names:
        return table_names
    else:
        return None
