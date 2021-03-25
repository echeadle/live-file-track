import sqlite3
import sys


# Write a function that can create an SQLite instance.

def create_file_tracking_db(full_path_to_name):
    """Create File Tracking Database"""
    return sqlite3.connect(full_path_to_name)



# Write a function that can query the master database 
# for the SQLite instance created.

def main():
    pass

# --------------------------------------------------
if __name__ == '__main__':
    main()