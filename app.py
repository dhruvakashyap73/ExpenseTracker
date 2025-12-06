from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

DATABASE = 'expenses.db'

def get_db():
    """Create a database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database"""
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """Display all expenses"""
    conn = get_db()
    expenses = conn.execute('''
        SELECT * FROM expenses ORDER BY date DESC, id DESC
    ''').fetchall()
    
    # Calculate total
    total = conn.execute('SELECT SUM(amount) as total FROM expenses').fetchone()['total']
    total = total if total else 0
    
    # Calculate totals by category
    category_totals = conn.execute('''
        SELECT category, SUM(amount) as total 
        FROM expenses 
        GROUP BY category
        ORDER BY total DESC
    ''').fetchall()
    
    conn.close()
    return render_template('index.html', expenses=expenses, total=total, category_totals=category_totals)

@app.route('/add', methods=['POST'])
def add_expense():
    """Add a new expense"""
    date = request.form.get('date')
    category = request.form.get('category')
    description = request.form.get('description')
    amount = request.form.get('amount')
    
    # Validation
    if not all([date, category, description, amount]):
        flash('All fields are required!', 'error')
        return redirect(url_for('index'))
    
    try:
        amount = float(amount)
        if amount <= 0:
            flash('Amount must be greater than 0!', 'error')
            return redirect(url_for('index'))
    except ValueError:
        flash('Invalid amount!', 'error')
        return redirect(url_for('index'))
    
    conn = get_db()
    conn.execute('''
        INSERT INTO expenses (date, category, description, amount)
        VALUES (?, ?, ?, ?)
    ''', (date, category, description, amount))
    conn.commit()
    conn.close()
    
    flash('Expense added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/delete/<int:expense_id>')
def delete_expense(expense_id):
    """Delete an expense"""
    conn = get_db()
    conn.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    conn.commit()
    conn.close()
    
    flash('Expense deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/filter')
def filter_expenses():
    """Filter expenses by category or date range"""
    category = request.args.get('category')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    conn = get_db()
    
    query = 'SELECT * FROM expenses WHERE 1=1'
    params = []
    
    if category and category != 'all':
        query += ' AND category = ?'
        params.append(category)
    
    if start_date:
        query += ' AND date >= ?'
        params.append(start_date)
    
    if end_date:
        query += ' AND date <= ?'
        params.append(end_date)
    
    query += ' ORDER BY date DESC, id DESC'
    
    expenses = conn.execute(query, params).fetchall()
    
    # Calculate filtered total
    total_query = 'SELECT SUM(amount) as total FROM expenses WHERE 1=1'
    if category and category != 'all':
        total_query += ' AND category = ?'
    if start_date:
        total_query += f' AND date >= ?'
    if end_date:
        total_query += f' AND date <= ?'
    
    total = conn.execute(total_query, params).fetchone()['total']
    total = total if total else 0
    
    # Get all category totals
    category_totals = conn.execute('''
        SELECT category, SUM(amount) as total 
        FROM expenses 
        GROUP BY category
        ORDER BY total DESC
    ''').fetchall()
    
    conn.close()
    
    return render_template('index.html', expenses=expenses, total=total, 
                         category_totals=category_totals, 
                         selected_category=category,
                         start_date=start_date, end_date=end_date)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
