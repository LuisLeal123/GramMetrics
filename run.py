# runs the website

# import the creator function and run it
from app import create_app
app = create_app()

# check for module
if __name__ == '__main__':
    app.run(debug=True)
