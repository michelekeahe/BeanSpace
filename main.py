# @author: Michele Kauahi -> Guide by: TechWithTim
# Languages: HTML, CSS, JS, Flask, Jinja, SQLAlchemy, Bootstrap
# File to run and start BeanSpace website

# Import website package (Folder) to run files wtihin
from website import create_app

app = create_app()

# Run Flask app/server only if file is run, not imported
if __name__ == '__main__':
   app.run(debug=True) # debug=false in production