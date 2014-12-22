#!/usr/bin/env python
"""Automatically generate thank you emails and reports. Run this python
module as a script. Follow the prompts from the shell or interpreter to
navigate the script.
"""

from datetime import date
from safe_input import safe_input    # Reuse from safe_input assignment

donor_dict = {u"Mark Zuckerberg": {u"12-1-2014": 1000., u"12-2-2014":
    2000., u"12-3-2014": 1000.}, u"Michael Bloomberg": {u"12-1-2014":
    2000., u"12-2-2014": 1000., u"12-3-2014": 1000.}, u"Paul Allen":
    {u"12-1-2014": 1000., u"12-2-2014": 1000., u"12-3-2014": 2000.},
    u"George Soros": {u"12-1-2014": 1000.}, u"Bill Gates":
    {u"12-1-2014": 2000.}}

def main_menu():
    """Prompt the user to choose between 'send a Thank You' and 'create
    a report'. Give the user the option to exit the script.
    """
    reply = unicode(safe_input(u"Welcome to the mail room user interface! To exit, " +
        u"type 'quit'. Would you like to send a thank you or create a report?"))
        
    while reply.lower() not in [u"send a thank you", u"create a report", u"quit"]:
        reply = unicode(safe_input(u"Please type either 'Send a thank you' or 'Create a report'. To exit, type 'quit':"))
        
    return reply


def send_a_thank_you_menu():
    """Prompt the user to choose to see a list of donors or to input a
    donation for a thank you by entering a donor's full name. Give the
    user the choice to return to the main menu.
    """
    reply = unicode(safe_input(u"Type 'list' to see a list of donors. Otherwise, provide the full name of the donor. " +
        u"Type 'return' to return to the main menu:"))
    
    return reply


def show_list():
    """Print a list of donor names and re-prompt the choices from the
    send_a_thank_you_menu. Give the user the choice to return to the
    main menu.
    """
    print(donor_dict.keys())
    

def input_a_donation(donor):
    """Prompt the user for a donation amount and record it. Give the
    user the option to exit the script. Compose and print a thank you
    email. Return the user to the main menu.
    """
    reply = unicode(safe_input(u"Please input the donor's donation amount in $. Type 'return' to return to the main menu:"))
    
    if reply != u"return":
        while True:
            try:
                reply = float(reply)    # Check to see if it is a number
                break
            except ValueError:
                reply = unicode(safe_input(u"That is not a number. Please input the donor's donation amount in $. " +
                    u"Type 'return' to return to the main menu:"))
        
        date_today = unicode("-".join([str(date.today().month), str(date.today().day), str(date.today().year)]))
        donor_dict[donor] = donor_dict.setdefault(donor, {})
        donor_dict[donor][date_today] = reply
        
        email = u"Thank you awesome %s for your donation of $%.2f received today, %s. " % (donor, reply, date_today)
        email += u"Cheers, Jesse from your favorite mail room"
        print(email)


def create_report():
    """Create and print a tabular report including donor names, total
    donated, number of donations, and average donation. Return the user
    to the main menu.
    """
    print(u"{:^20} {:^20} {:^20} {:^20}".format(u"Donor Name", u"Total Donated ($)", u"# of Donations", u"Average Donation"))
    for donor in donor_dict.iterkeys():
        print(u"{:20} {:20.2f} {:20d} {:20.2f}".format(donor, sum(donor_dict[donor].values()), len(donor_dict[donor]),
            sum(donor_dict[donor].values())/len(donor_dict[donor])))
    

if __name__ == "__main__":
    
    # Allow the loop to repeat back to the top only breaking with "quit"
    while True:
        main_input = main_menu()
        if main_input.lower() == u"send a thank you":
            donor = send_a_thank_you_menu()
            while donor == u"list":
                show_list()
                donor = send_a_thank_you_menu()
            if donor == u"return":
                continue
            input_a_donation(donor)
        if main_input.lower() == u"create a report":
            create_report()
        if main_input.lower() == u"quit":
            break

