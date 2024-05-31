import firebase_admin  # pip install firebase-admin
from firebase_admin import credentials, db
import pyrebase  # pip install pyrebase4
 
 
class Firebase:
    def __init__(self):
       
        CREDENTIALS_FILE = "smoke.json"
        DATABASE_URL = "https://catb-535cd-default-rtdb.europe-west1.firebasedatabase.app/"
   
        API_KEY = "AIzaSyDRu3t0msAtmaQl8NILK76erH0e1EB5F5A"
        # You can find your project ID in your Firebase project settings.   #
        PROJECT_ID = "catb-535cd"
       
        self.cred = credentials.Certificate(CREDENTIALS_FILE)
        firebase_admin.initialize_app(
            self.cred,
            {
                "databaseURL": DATABASE_URL,
            },
        )
        self.ref = db.reference("/")
        self.config = {
            "apiKey": API_KEY,
            "authDomain": f"{PROJECT_ID}.firebaseapp.com",
            "databaseURL": DATABASE_URL,
            "storageBucket": f"{PROJECT_ID}.appspot.com",
        }
        self.firebase = pyrebase.initialize_app(self.config)
        self.auth = self.firebase.auth()
 
    def login(self, email, password):
        user = self.auth.sign_in_with_email_and_password(email, password)
        return user
 
    def register(self, email, password):
        user = self.auth.create_user_with_email_and_password(email, password)
        return user
 
    def get_current_user(self):
        return self.auth.current_user
 
    def get_user_id(self):
        return self.auth.current_user["localId"]
 
    def get_user_email(self):
        return self.auth.current_user["email"]
 
    def logout(self):
        self.auth.current_user = None
 
 
if __name__ == "__main__":
    f = Firebase()
    print(f.ref.get())
    f.ref.set({"name": "Borssdsdfa Canbula"})
    print(f.ref.get())
    f.ref.set({"n": "Bsadaora"})
    print(f.ref.get())
    try:
        f.login("prof@university.edu", "password")
    except Exception as e:
        f.register("prof@university.edu", "password")
    print(f.get_current_user())