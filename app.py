from flask import Flask, render_template, request, redirect

app=Flask(__name__)
tasks=[]

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title=request.form.get("title","").strip()
    priority=request.form.get("priority","Medium")
    if title:
        tasks.append({"title":title,"priority":priority,"done":False})
    return redirect("/")

@app.route("/toggle/<int:i>")
def toggle(i):
    if 0<=i<len(tasks):
        tasks[i]["done"]=not tasks[i]["done"]
    return redirect("/")

@app.route("/delete/<int:i>")
def delete(i):
    if 0<=i<len(tasks):
        tasks.pop(i)
    return redirect("/")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)