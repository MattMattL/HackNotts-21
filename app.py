from flask import Flask
from flask import request, redirect

from backend import Account

def main():

    ADMIN_USER_NAME = "admin1"
    USER_USER_NAME = "user1"

    app = Flask(__name__)
    account = Account()

    # login page
    @app.route("/", methods=['GET', 'POST'])
    def returnLoginPage():
        userName = request.form.get("username")

        print("[debug] user name inputted: {}".format(userName))

        if userName == ADMIN_USER_NAME:
            return redirect("http://127.0.0.1:5000/admin", code=302)
        elif userName == USER_USER_NAME:
            return redirect("http://127.0.0.1:5000/user", code=302)

        return open("./static/home.html").read()

    # admin page
    @app.route("/admin")
    def returnAdminPage():
        return open("./static/admin.html") \
                .read()

    # user page
    @app.route("/user")
    def returnUserPage():
        return open("./static/user.html") \
                .read() \
                .format(monthlyBudget=account.monthlyBudget, \
                        monthlySoFar=account.monthlySoFar)
                        # rentPercent=account.getRentPercent(), \
                        # foodPercent=account.getFoodPercent(), \
                        # billsPercent=account.getBillsPercent(), \
                        # transportPercent=account.getTransportPercent(), \
                        # miscPercent=account.getMiscPercent())

    def isNotString(number):
        return type(number) != str

    # udpate budgets
    @app.route("/update")
    def updateAccountBudget():
        if request.args.get("monthly-budget") != "":
            account.monthlyBudget = float(request.args.get("monthly-budget"))
        
        if request.args.get("balance") != "":
            account.monthlySoFar = float(request.args.get("balance"))

        if request.args.get("rent") != "":
            account.rentBudget = float(request.args.get("rent"))
        
        if request.args.get("food") != "":
            account.foodBudget = float(request.args.get("food"))
        
        if request.args.get("bills") != "":
            account.billsBudget = float(request.args.get("bills"))
        
        if request.args.get("transport") != "":
            account.transportBudget = float(request.args.get("transport"))
        
        account.miscBudget = account.getMiscBudget()

        return redirect("http://127.0.0.1:5000/", code=302)


    # progress bar test
    @app.route("/test")
    def progressBar():
        return open("./static/progress_bar.html") \
                .read() \
                .format(var2=80)
        pass

    app.run()


if __name__ == "__main__":
    main()
