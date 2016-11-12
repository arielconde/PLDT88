"""
DISPATCH FUNCTIONS
"""

import actions
import postbacks
import fbutil

# refer to actions.py, plain text from api.ai
action = {
    'showBestProduct': actions.show_best_product,
    'sendRecentBill': actions.send_recent_bill,
    'input.unknown': actions.uknown
}

# on button click
postback = {
    'welcome': postbacks.welcome,
    'welcome_yes': postbacks.welcome_yes,
    'welcome_no': postbacks.welcome_no
}