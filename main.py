import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QComboBox, QPushButton
import sqlite3
import pandas as pd
from functions import *

# Import the code to read SQL data into a DataFrame (as mentioned in the previous response)
def read_sql_to_dataframe(file_path, table_name):
    # Create an SQLite connection and read the SQL file
    conn = sqlite3.connect(':memory:')  # In-memory database
    with open(file_path, 'r') as sql_file:
        query = sql_file.read()
    conn.executescript(query)

    # Fetch data from the SQLite database and create a DataFrame
    query = f'SELECT * FROM {table_name}'
    df = pd.read_sql_query(query, conn)

    # Close the connection
    conn.close()

    return df

class SQLDataViewer(QMainWindow):
    def __init__(self, table_names):
        super().__init__()
        self.dataframes = {}

        for table_name in table_names:
            df = read_sql_to_dataframe('Sample-SQL-File-100-Rows.sql', table_name)
            self.dataframes[table_name] = df

        self.table_names = table_names
        self.current_table = None

        # Create a central widget
        central_widget = QTableWidget()
        self.setCentralWidget(central_widget)

        # Create a combo box to select tables
        self.table_selector = QComboBox()
        self.table_selector.addItems(self.table_names)
        self.table_selector.currentIndexChanged.connect(self.display_selected_table)

        # Create a "Show Table" button
        self.show_table_button = QPushButton("Show Table")
        self.show_table_button.clicked.connect(self.display_selected_table)

        self.statusBar().addWidget(self.table_selector)
        self.statusBar().addWidget(self.show_table_button)

        self.setWindowTitle("Data Viewer")
        self.resize(800, 600)

    def display_selected_table(self):
        table_name = self.table_selector.currentText()
        df = self.dataframes.get(table_name)

        if df is not None:
            self.current_table = table_name
            self.centralWidget().setRowCount(df.shape[0])
            self.centralWidget().setColumnCount(df.shape[1])

            for i in range(df.shape[0]):
                for j in range(df.shape[1]):
                    item = QTableWidgetItem(str(df.iat[i, j]))
                    self.centralWidget().setItem(i, j, item)

            self.setWindowTitle(f"Data Viewer - Table: {self.current_table}")
        else:
            self.setWindowTitle(f"Data Viewer - Table: {self.current_table}")

def main():
    app = QApplication(sys.argv)

    table_names = extract_table_names("Sample-SQL-File-100-Rows.sql")
    print(table_names)
    window = SQLDataViewer(table_names)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
