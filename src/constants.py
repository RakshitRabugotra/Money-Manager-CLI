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
    "Savings"
)

GUIstyle = {
    'button': {
        'relief': 'groove',
        'width': 30
    },
    'label': {
        'relief': 'groove',
        'borderwidth': 2,
        'font': 'Verdana 12',
        'width': 30
    }
}
GUIstyle['label-width-small'] = GUIstyle['label']
GUIstyle['label-width-small']['width'] = 20