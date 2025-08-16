# 🔐 Creating Login Program using Decorators in Python

# ✅ Decorator to check login credentials
def greet(fx):
    def mfx(user_username, user_password):
        if user_username == "omkale" and user_password == "1006":
            print("✅ Correct username and password!")
            return fx()
        else:
            print("❌ Wrong username or password!")
            print("🚫 Access Denied.")
    return mfx

# 🎉 Function to display after successful login
@greet
def welcome():
    print("🎉 Login Successful! Welcome, Om Kale!")

# 🖥️ Login Interface
print("🔐 Welcome to the Login Portal")
print("📥 Please enter your username and password to continue:\n")

user_username = input("👤 Enter your username: ")
user_password = input("🔑 Enter your password: ")

welcome(user_username, user_password)
