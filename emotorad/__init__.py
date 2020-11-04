from firebase_admin import credentials, initialize_app

cred = credentials.Certificate("firebaseauth.json")
firebase_client = initialize_app(cred)
