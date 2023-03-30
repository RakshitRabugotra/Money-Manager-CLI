"""
File for the constants in our app
"""
APP_TITLE = "Money-Manager"

RESIZABLE = (False, False)

EXPENSE_CATEGORIES = (
    "Transportation",
    "Snacks, eating out, and food in general",
    "School Supplies",
    "Movies, music and entertainment",
    "Hobby",
    "Cell phone or internet",
    "Savings",
    "Flat expense",
    "Other"
)

GUIstyle = {
    'button': {
        'width': 25
    },
    'bordered-frame': {
        # 'border_width': 3,
        # 'border_color': "#260703"
    },
    'label': {
        # 'font': "Helvetica",
        'width': 25
    }
}
GUIstyle['label-width-small'] = GUIstyle['label']
GUIstyle['label-width-small']['width'] = 20


MESSAGES = {
    'expense-unsaved': "You have unsaved expense modifications, please save changes first...",
    'expense-notfound': "No prior records found...",
    'no-new-expenses': "Nothing to modify, no new expenses...",
    'all-expenses-recorded': "All expenses recorded successfully!",
}