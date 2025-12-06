<p align="center">
  <img src="https://github.com/dhruvakashyap73/ExpenseTracker/blob/main/templates/logo.png" alt="Logo" width="250" height="250">
</p>

A simple and elegant expense tracking web application built with Flask, SQLite, HTML, and CSS.

## Features

- ✨ Add expenses with date, category, description, and amount
- 📊 View total expenses and category-wise breakdown
- 🔍 Filter expenses by category and date range
- 🗑️ Delete individual expenses
- 📱 Responsive design for mobile and desktop
- 🎨 Beautiful gradient UI with smooth animations

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Database**: SQLite
- **Frontend**: HTML5, CSS3
- **Styling**: Custom CSS with gradient design

## Installation

1. Make sure you have Python installed (Python 3.7 or higher)

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Usage

### Adding an Expense
1. Fill in the date (defaults to today)
2. Select a category from the dropdown
3. Enter a description
4. Enter the amount
5. Click "Add Expense"

### Filtering Expenses
1. Use the filter section to:
   - Select a specific category
   - Set a date range (from/to)
2. Click "Apply Filter"
3. Click "Clear Filter" to reset

### Deleting an Expense
1. Click the "Delete" button next to any expense
2. Confirm the deletion

## Project Structure

```
newproj/
├── app.py              # Flask application with routes and database logic
├── requirements.txt    # Python dependencies
├── expenses.db         # SQLite database (created automatically)
├── templates/
│   └── index.html     # Main HTML template
└── static/
    └── style.css      # CSS styling
```

## Categories

The app includes the following expense categories:
- Food
- Transportation
- Entertainment
- Shopping
- Bills
- Health
- Education
- Other

## Database Schema

The `expenses` table has the following structure:
- `id`: Primary key (auto-increment)
- `date`: Expense date (TEXT)
- `category`: Expense category (TEXT)
- `description`: Expense description (TEXT)
- `amount`: Expense amount (REAL)

## Features in Detail

### Summary Dashboard
- Displays total expenses
- Shows category-wise breakdown with individual totals
- Color-coded category badges

### Responsive Design
- Mobile-friendly layout
- Adaptive table view for smaller screens
- Touch-friendly buttons and inputs

### User Experience
- Flash messages for success/error feedback
- Auto-hide notifications after 5 seconds
- Confirmation dialog before deleting expenses
- Today's date auto-filled in the form

