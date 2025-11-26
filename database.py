import sqlite3
import pandas as pd
import os

#creates new class to manage all database opeartions
class DatabaseManager:
    def __init__(self, db_path="intelligence_platform.db"):
        self.db_path = db_path #stores the database name
        self.connection = None
      #creates connection to SQlite  
    def connect(self):
        """Connect to SQLite database"""
        self.connection = sqlite3.connect(self.db_path)
        return self.connection.cursor()
    #closes databsse when we are done
    def disconnect(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
    #creates table for our users
    def create_tables(self):
        """Create tables for Cyber + IT domains only"""
        cursor = self.connect()
        
        #creates table for users (Week 7)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        #table for cybersecurity
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cyber_incidents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                incident_id TEXT UNIQUE NOT NULL,
                title TEXT NOT NULL,
                severity TEXT NOT NULL,
                category TEXT NOT NULL,
                status TEXT NOT NULL,
                created_date TEXT NOT NULL,
                resolved_date TEXT,
                resolution_time_hours REAL,
                description TEXT
            )
        ''')
        
        #table for IT users
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS it_tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticket_id TEXT UNIQUE NOT NULL,
                title TEXT NOT NULL,
                status TEXT NOT NULL,
                assignee TEXT NOT NULL,
                priority TEXT NOT NULL,
                created_date TEXT NOT NULL,
                resolved_date TEXT,
                current_stage TEXT NOT NULL,
                description TEXT
            )
        ''')
        
        self.connection.commit()
        print("Tables created for Cyber + IT domains!")
        self.disconnect()

    #cybersecurity CRUD operations
    def create_cyber_incident(self, incident_id, title, severity, category, status, created_date, description=""): #the parameters
        cursor = self.connect()
        cursor.execute('''
            INSERT INTO cyber_incidents 
            (incident_id, title, severity, category, status, created_date, description)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (incident_id, title, severity, category, status, created_date, description))
        self.connection.commit()
        self.disconnect()
        print(f"Created cyber incident: {incident_id}")
    
    #this function helps read everyhting in the databse
    def read_cyber_incidents(self):
        cursor = self.connect()
        cursor.execute('SELECT * FROM cyber_incidents') #this is the database we want to read from
        results = cursor.fetchall()
        self.disconnect()
        return results
    
    #this function is used to update/change information in the database
    def update_cyber_incident(self, incident_id, status, resolved_date=None, resolution_time_hours=None):
        cursor = self.connect()
        cursor.execute('''
            UPDATE cyber_incidents 
            SET status = ?, resolved_date = ?, resolution_time_hours = ?
            WHERE incident_id = ?
        ''', (status, resolved_date, resolution_time_hours, incident_id)) #new values
        self.connection.commit() #save changes
        self.disconnect()
        print(f"Updated cyber incident: {incident_id}")
    
    #this function is used to delete rows
    def delete_cyber_incident(self, incident_id):
        cursor = self.connect()
        cursor.execute('DELETE FROM cyber_incidents WHERE incident_id = ?', (incident_id,))
        self.connection.commit()
        self.disconnect()
        print(f"Deleted cyber incident: {incident_id}")

    #CRUD operations for IT
    def create_it_ticket(self, ticket_id, title, status, assignee, priority, created_date, current_stage, description=""): #the parameters
        cursor = self.connect()
        cursor.execute('''
            INSERT INTO it_tickets 
            (ticket_id, title, status, assignee, priority, created_date, current_stage, description)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (ticket_id, title, status, assignee, priority, created_date, current_stage, description))
        self.connection.commit()
        self.disconnect()
        print(f"Created IT ticket: {ticket_id}")
    #function for reading table
    def read_it_tickets(self):
        cursor = self.connect()
        cursor.execute('SELECT * FROM it_tickets')
        results = cursor.fetchall()
        self.disconnect()
        return results
    
    #function to update table
    def update_it_ticket(self, ticket_id, status, current_stage, resolved_date=None):
        cursor = self.connect()
        cursor.execute('''
            UPDATE it_tickets 
            SET status = ?, current_stage = ?, resolved_date = ?
            WHERE ticket_id = ?
        ''', (status, current_stage, resolved_date, ticket_id))
        self.connection.commit()
        self.disconnect()
        print(f"Updated IT ticket: {ticket_id}")
    
    #function to delete
    def delete_it_ticket(self, ticket_id):
        cursor = self.connect()
        cursor.execute('DELETE FROM it_tickets WHERE ticket_id = ?', (ticket_id,))
        self.connection.commit()
        self.disconnect()
        print(f"Deleted IT ticket: {ticket_id}")

        