def form():
    if request.method == "POST":
        sum = request.form["TEXT_1"]
        return redirect(url_for("user", usr = sum))
    else:
        return render_template("form.html")