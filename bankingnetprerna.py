import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime




USERNAME = "Prerna"
PASSWORD = "1234"

balance = 25000.00

transactions = [
    ["Opening Balance", 25000.00, "Credit"]
]

loans = []




def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == USERNAME and password == PASSWORD:
        login_window.destroy()
        open_dashboard()
    else:
        messagebox.showerror(
            "Login Error",
            "Invalid username or password!"
        )



def open_dashboard():

    global balance

    dashboard = tk.Tk()
    dashboard.title("Simple Net Banking System")
    dashboard.geometry("700x600")
    dashboard.resizable(False, False)


    header = tk.Frame(dashboard)
    header.pack(fill="x", pady=15)

    tk.Label(
        header,
        text="🏦 NET BANKING SYSTEM",
        font=("Arial", 22, "bold")
    ).pack()

    tk.Label(
        header,
        text="Welcome, Prerna",
        font=("Arial", 12)
    ).pack(pady=5)


    balance_frame = tk.LabelFrame(
        dashboard,
        text="Account Balance",
        font=("Arial", 12, "bold")
    )

    balance_frame.pack(
        padx=30,
        pady=10,
        fill="x"
    )

    balance_label = tk.Label(
        balance_frame,
        text=f"₹ {balance:.2f}",
        font=("Arial", 20, "bold")
    )

    balance_label.pack(pady=15)

    def update_balance():
        balance_label.config(
            text=f"₹ {balance:.2f}"
        )


    def account_section():

        account_window = tk.Toplevel(dashboard)
        account_window.title("Account Details")
        account_window.geometry("450x400")

        tk.Label(
            account_window,
            text="ACCOUNT DETAILS",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        details = (
            "Customer Name : Prerna Divakar\n\n"
            "Account Number : 1234567890\n\n"
            "Account Type : Savings Account\n\n"
            "Branch : Pune\n\n"
            f"Current Balance : ₹{balance:.2f}"
        )

        tk.Label(
            account_window,
            text=details,
            font=("Arial", 12),
            justify="left"
        ).pack(pady=20)


    def deposit_money():

        global balance

        amount = simpledialog.askfloat(
            "Deposit Money",
            "Enter amount to deposit:"
        )

        if amount is None:
            return

        if amount <= 0:
            messagebox.showerror(
                "Error",
                "Enter a valid amount."
            )
            return

        balance += amount

        transactions.append(
            [
                datetime.now().strftime("%d-%m-%Y %H:%M"),
                amount,
                "Credit"
            ]
        )

        update_balance()

        messagebox.showinfo(
            "Success",
            f"₹{amount:.2f} deposited successfully!"
        )


    def withdraw_money():

        global balance

        amount = simpledialog.askfloat(
            "Withdraw Money",
            "Enter amount to withdraw:"
        )

        if amount is None:
            return

        if amount <= 0:
            messagebox.showerror(
                "Error",
                "Enter a valid amount."
            )
            return

        if amount > balance:
            messagebox.showerror(
                "Error",
                "Insufficient balance!"
            )
            return

        balance -= amount

        transactions.append(
            [
                datetime.now().strftime("%d-%m-%Y %H:%M"),
                amount,
                "Debit"
            ]
        )

        update_balance()

        messagebox.showinfo(
            "Success",
            f"₹{amount:.2f} withdrawn successfully!"
        )


    def transaction_history():

        history_window = tk.Toplevel(dashboard)
        history_window.title("Transaction History")
        history_window.geometry("500x400")

        tk.Label(
            history_window,
            text="TRANSACTION HISTORY",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

        for transaction in transactions:

            text = (
                f"Date: {transaction[0]}\n"
                f"Amount: ₹{transaction[1]:.2f}\n"
                f"Type: {transaction[2]}\n"
                "--------------------------"
            )

            tk.Label(
                history_window,
                text=text,
                font=("Arial", 10),
                justify="left"
            ).pack(anchor="w", padx=30, pady=5)


    def loan_section():

        loan_window = tk.Toplevel(dashboard)
        loan_window.title("Loan Section")
        loan_window.geometry("500x500")

        tk.Label(
            loan_window,
            text="LOAN SECTION",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        tk.Label(
            loan_window,
            text="Select Loan Type"
        ).pack()

        loan_type = tk.StringVar()
        loan_type.set("Personal Loan")

        loan_options = [
            "Personal Loan",
            "Home Loan",
            "Education Loan",
            "Car Loan"
        ]

        tk.OptionMenu(
            loan_window,
            loan_type,
            *loan_options
        ).pack(pady=10)

        tk.Label(
            loan_window,
            text="Enter Loan Amount"
        ).pack()

        loan_amount = tk.Entry(
            loan_window,
            width=30
        )

        loan_amount.pack(pady=10)

        def apply_loan():

            amount = loan_amount.get()

            if amount == "":
                messagebox.showerror(
                    "Error",
                    "Please enter loan amount."
                )
                return

            try:
                amount = float(amount)

                if amount <= 0:
                    raise ValueError

            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Enter a valid amount."
                )
                return

            loans.append(
                [
                    loan_type.get(),
                    amount,
                    "Pending"
                ]
            )

            messagebox.showinfo(
                "Loan Application",
                "Loan application submitted successfully!"
            )

            loan_amount.delete(0, tk.END)

        tk.Button(
            loan_window,
            text="Apply for Loan",
            width=20,
            command=apply_loan
        ).pack(pady=20)

        tk.Label(
            loan_window,
            text="My Loan Applications",
            font=("Arial", 12, "bold")
        ).pack(pady=10)

        def show_loans():

            if not loans:
                messagebox.showinfo(
                    "Loans",
                    "No loan applications found."
                )
                return

            text = ""

            for loan in loans:
                text += (
                    f"Type: {loan[0]}\n"
                    f"Amount: ₹{loan[1]:.2f}\n"
                    f"Status: {loan[2]}\n\n"
                )

            messagebox.showinfo(
                "My Loans",
                text
            )

        tk.Button(
            loan_window,
            text="View My Loans",
            width=20,
            command=show_loans
        ).pack()


    def card_section():

        card_window = tk.Toplevel(dashboard)
        card_window.title("Debit & Credit Cards")
        card_window.geometry("500x400")

        tk.Label(
            card_window,
            text="CARD DETAILS",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        debit_card = (
            "DEBIT CARD\n\n"
            "Card Number : XXXX XXXX XXXX 1234\n"
            "Card Holder : PRERNA DIVAKAR\n"
            "Status : Active"
        )

        tk.Label(
            card_window,
            text=debit_card,
            font=("Arial", 11),
            justify="left"
        ).pack(pady=15)

        tk.Label(
            card_window,
            text="------------------------------"
        ).pack()

        credit_card = (
            "CREDIT CARD\n\n"
            "Card Number : XXXX XXXX XXXX 5678\n"
            "Card Holder : PRERNA DIVAKAR\n"
            "Status : Active"
        )

        tk.Label(
            card_window,
            text=credit_card,
            font=("Arial", 11),
            justify="left"
        ).pack(pady=15)


    def customer_service():

        service_window = tk.Toplevel(dashboard)
        service_window.title("Customer Service")
        service_window.geometry("500x450")

        tk.Label(
            service_window,
            text="CUSTOMER SERVICE",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        tk.Label(
            service_window,
            text="Enter your complaint:"
        ).pack()

        complaint = tk.Text(
            service_window,
            width=45,
            height=8
        )

        complaint.pack(pady=15)

        def submit_complaint():

            message = complaint.get(
                "1.0",
                tk.END
            ).strip()

            if message == "":
                messagebox.showerror(
                    "Error",
                    "Please enter your complaint."
                )
                return

            messagebox.showinfo(
                "Complaint Submitted",
                "Your complaint has been submitted successfully!"
            )

            complaint.delete(
                "1.0",
                tk.END
            )

        tk.Button(
            service_window,
            text="Submit Complaint",
            width=20,
            command=submit_complaint
        ).pack(pady=10)

        tk.Label(
            service_window,
            text="Customer Care: 1800-123-4567\n"
                 "Email: support@bank.com",
            font=("Arial", 11)
        ).pack(pady=15)


    def change_password():

        global PASSWORD

        old_password = simpledialog.askstring(
            "Change Password",
            "Enter old password:",
            show="*"
        )

        if old_password != PASSWORD:
            messagebox.showerror(
                "Error",
                "Incorrect old password!"
            )
            return

        new_password = simpledialog.askstring(
            "Change Password",
            "Enter new password:",
            show="*"
        )

        if not new_password:
            messagebox.showerror(
                "Error",
                "Password cannot be empty."
            )
            return

        PASSWORD = new_password

        messagebox.showinfo(
            "Success",
            "Password changed successfully!"
        )

    def logout():

        dashboard.destroy()

        messagebox.showinfo(
            "Logout",
            "You have been logged out."
        )

   

    button_frame = tk.Frame(dashboard)
    button_frame.pack(pady=15)

    tk.Button(
        button_frame,
        text="Account",
        width=20,
        command=account_section
    ).grid(row=0, column=0, padx=10, pady=8)

    tk.Button(
        button_frame,
        text="Deposit Money",
        width=20,
        command=deposit_money
    ).grid(row=0, column=1, padx=10, pady=8)

    tk.Button(
        button_frame,
        text="Withdraw Money",
        width=20,
        command=withdraw_money
    ).grid(row=1, column=0, padx=10, pady=8)

    tk.Button(
        button_frame,
        text="Transactions",
        width=20,
        command=transaction_history
    ).grid(row=1, column=1, padx=10, pady=8)

    tk.Button(
        button_frame,
        text="Loan",
        width=20,
        command=loan_section
    ).grid(row=2, column=0, padx=10, pady=8)

    tk.Button(
        button_frame,
        text="Debit / Credit Card",
        width=20,
        command=card_section
    ).grid(row=2, column=1, padx=10, pady=8)

    tk.Button(
        button_frame,
        text="Customer Service",
        width=20,
        command=customer_service
    ).grid(row=3, column=0, padx=10, pady=8)

    tk.Button(
        button_frame,
        text="Change Password",
        width=20,
        command=change_password
    ).grid(row=3, column=1, padx=10, pady=8)

    tk.Button(
        dashboard,
        text="Logout",
        width=25,
        command=logout
    ).pack(pady=20)

    dashboard.mainloop()


login_window = tk.Tk()

login_window.title("Net Banking Login")
login_window.geometry("450x400")
login_window.resizable(False, False)

tk.Label(
    login_window,
    text="🏦",
    font=("Arial", 35)
).pack(pady=10)

tk.Label(
    login_window,
    text="NET BANKING SYSTEM",
    font=("Arial", 20, "bold")
).pack(pady=10)

tk.Label(
    login_window,
    text="Username"
).pack(pady=5)

username_entry = tk.Entry(
    login_window,
    width=30
)

username_entry.pack()

tk.Label(
    login_window,
    text="Password"
).pack(pady=5)

password_entry = tk.Entry(
    login_window,
    width=30,
    show="*"
)

password_entry.pack()

tk.Button(
    login_window,
    text="LOGIN",
    width=20,
    command=login
).pack(pady=25)

tk.Label(
    login_window,
    text="Demo Login: Prerna / 1234",
    font=("Arial", 9)
).pack()

login_window.mainloop()
