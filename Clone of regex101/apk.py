from flask import Flask,render_template,request
import re
app = Flask(__name__)

#########################################################
@app.route('/',methods=['GET','POST'])
def fun_1():
    if request.method== 'POST':
        patterns = request.form['var_1']
        strings=request.form['var_2']
        lengths=len(re. findall(patterns, strings))
        words=re.findall(patterns, strings)
        return render_template("result.html",lengths=lengths,words=words)
    return render_template('index.html')


#########################################################
if __name__ == "__main__":
    app.run(debug=False)
