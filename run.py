from app import create_app

app = create_app() # Imported from 'app/__init__.py'

if __name__ == "__main__":
    app.run(debug=True) # To reload the page