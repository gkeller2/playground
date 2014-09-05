from selenium import webdriver

browser = webdriver.Firefox()

# Load homepage.
browser.get('http://localhost:8000')

# Ensure homepage title says 'To-Do'.
assert 'To-Do' in browser.title

# Invite user to enter to-do item right away.


# Enter sample to-do item.


# Press enter. Page should update, and show new to-do item.


# There should appear a text box to add a new to-do item.


# Add a second item.


# After pressing enter, page should be reloaded, and then show both items.


# Unique URL generated for user?


# Visit URL.


# Exit.

browser.quit()
