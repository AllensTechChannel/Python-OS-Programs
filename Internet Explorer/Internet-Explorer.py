import webview
user_input = input("Enter a URL: ")
# Open a website in the default browse


# Create a window to display the website
webview.create_window("Internet Explorer-"+user_input, user_input )
webview.start()
