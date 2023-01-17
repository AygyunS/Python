from flask import Flask
# , request, redirect, app
# from flask import render_template
# if __name__ == "__main__":
#     app.run()


# # @app.route("/")
# def index():
#     return render_template("index.html", tasks=tasks)


# tasks = []


# @app.route("/add_task", methods=["POST"])
# def add_task():
#     task = request.form["task"]
#     tasks.append(task)
#     return redirect("/")


# @app.route("/remove_task", methods=["POST"])
# def remove_task():
#     task = request.form["task"]
#     tasks.remove(task)
#     return redirect("/")


# @app.route("/rename_task", methods=["POST"])
# def rename_task():
#     old_task = request.form["old_task"]
#     new_task = request.form["new_task"]
#     tasks.remove(old_task)
#     tasks.append(new_task)
#     return redirect("/")
