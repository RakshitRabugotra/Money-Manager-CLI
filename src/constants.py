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
    "Other"
)

GUIstyle = {
    'button': {
        'width': 25
    },
    'label': {
        # 'font': "Helvetica",
        'width': 25
    }
}
GUIstyle['label-width-small'] = GUIstyle['label']
GUIstyle['label-width-small']['width'] = 20