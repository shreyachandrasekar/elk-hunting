import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")
    
conn.execute('create table if not exists pwVault(id TEXT, pw TEXT, test TEXT)')
print("Table created successfully")
conn.close()