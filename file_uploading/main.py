from distutils.log import debug 
from fileinput import filename
from utils import everything_function
from flask import *  

app = Flask(__name__)   
  
@app.route('/')   
def main():   
    return render_template("index.html")   
  
@app.route('/success', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save(f.filename)
        print(f.filename)
        everything_function(f.filename)
        return render_template("Acknowledgement.html", name = f.filename)   
  
if __name__ == '__main__':   
    app.run(debug=True)