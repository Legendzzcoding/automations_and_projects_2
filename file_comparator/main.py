from flask import Flask, render_template,request
import io
import difflib

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    processed_text=""
    diff_lines1 = []
    diff_lines2 = []
    color_line1=[]
    color_line2=[]
    check_if_diff_ans_has_value=''
    if request.method=='POST':
        user_input1=request.form['text_input1']
        user_input2=request.form['text_input2']
        f1=io.StringIO(user_input1).readlines()
        f2=io.StringIO(user_input2).readlines()
        check_if_diff_ans_has_value=''
        differ = difflib.Differ()
        diff_lines1 = []
        diff_lines2 = []
        color_line1=[]
        color_line2=[]
        for line in differ.compare(f1, f2):
            marker=line[0]
            if marker == " ":
                diff_lines1.append(line[2:])
                diff_lines2.append(line[2:])
                color_line1.append("blue")
                color_line2.append("blue")
            elif marker == "-":
                diff_lines1.append(f'{line[2:]}')
                diff_lines2.append("-\n")
                color_line1.append("green")
                color_line2.append("red")
            elif marker == "+":
                diff_lines1.append("-\n")
                diff_lines2.append(f'{line[2:]}')
                color_line1.append("red")
                color_line2.append("green")
            check_if_diff_ans_has_value='a'
        
    return render_template("index.html",check_if_diff_ans_has_value=check_if_diff_ans_has_value,diff_lines2=diff_lines2,diff_lines1=diff_lines1,color_line1=color_line1,color_line2=color_line2)

if __name__ == "__main__":
    app.run(debug=True)