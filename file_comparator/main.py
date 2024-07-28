from flask import Flask, render_template,request
import io
import difflib

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    processed_text=""
    diff_lines1 = []
    diff_lines2 = []
    check_if_diff_ans_has_value=''
    if request.method=='POST':
        user_input1=request.form['text_input1']
        user_input2=request.form['text_input2']
        f1=io.StringIO(user_input1).readlines()
        f2=io.StringIO(user_input2).readlines()
        if(len(f1)>len(f2)):
            dif=len(f1)-len(f2)
            i=1
            while(i<=1):
                user_input2=user_input2+"\r\n"
                i=i+1
            f2=io.StringIO(user_input2).readlines()
        else:
            dif=len(f2)-len(f1)
            i=1
            while(i<=1):
                user_input1=user_input1+"\r\n"
                i=i+1
            f1=io.StringIO(user_input1).readlines()
        check_if_diff_ans_has_value=''
        differ = difflib.Differ()
        ans=open("ans.txt","w")#
        s1="First file-->"+repr(user_input1)#
        s2="Second file-->"+repr(user_input2)
        ans.write(s1)#
        ans.write(s2)#
        diff_lines1 = []
        diff_lines2 = []
        fa=open("output1.txt","w")#
        fb=open("output2.txt","w")#
        fus1=open("user_input1.txt","w")#
        fus2=open("user_input2.txt","w")#
        for line in differ.compare(f1, f2):
            marker=line[0]
            if marker == " ":
                aa=line[2:]+'\r\n'##
                diff_lines1.append(aa)
                diff_lines2.append(aa)
                fa.write(line[2:]+"\n")#
                fb.write(line[2:]+"\n")#
            elif marker == "-":
                diff_lines1.append(f'{line[2:]}\r\n')##
                diff_lines2.append("-\r\n")##
                fa.write(line[2:]+"\n")#
                fb.write("-\n")#
            elif marker == "+":
                diff_lines1.append("-\r\n")##
                diff_lines2.append(f'{line[2:]}\r\n')##
                fa.write("-\n")#
                fb.write(line[2:]+"\n")#
            check_if_diff_ans_has_value='a'
        
    return render_template("index.html",check_if_diff_ans_has_value=check_if_diff_ans_has_value,diff_lines2=diff_lines2,diff_lines1=diff_lines1)

if __name__ == "__main__":
    app.run(debug=True)
