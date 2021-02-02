import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

# lists to store data
Date = []
monthly_profit_loss = []
total_months = []
monthly_profit_loss2 = []
max_monthly_increase = 0
max_monthly_decrease = 0


# reset variables
total_profit = 0
#monthly_change = 0

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # get rid of header in csv
    csv_header = next(csv_file)
    # print(f"Header: {csv_header}")

    # read through each row in the csv
    for row in csv_reader:
       
        # puts every month in a list
        total_months.append(row[0])
   
        # add together all the values in row 2
        monthly_profit_loss = float(row[1])
        total_profit += monthly_profit_loss
       
        monthly_profit_loss2.append(int(row[1]))
       
        #monthly_change = [int(x) - int(monthly_profit_loss2[i - 1]) for i, x in enumerate(monthly_profit_loss2) if i > 0]
        # monthly_change = monthly_change + monthly_profit_loss2
        monthly_change = []
        for i, x in enumerate(monthly_profit_loss2):
            if i > 0:
                monthly_change.append(int(x) - int(monthly_profit_loss2[i - 1]))

        if i == 85:
            max_monthly_increase = max(monthly_change)
            max_monthly_decrease = min(monthly_change)

            max_index = (monthly_change.index(max_monthly_increase) + 1)
            #print(max_index)
            max_month = total_months[max_index]
            #print(max_month)

            min_index = (monthly_change.index(max_monthly_decrease) + 1)
            #print(min_index)
            min_month = total_months[min_index]
            #print(min_month)

        # set total_profit to string to format in USD
        dollar_total_profit = "${:,.2f}".format(total_profit)

# assigning the total rows in the total_months list as a variable
real_total_months = len(total_months)

#calculating average monthly change. 1 less than total rows since there's no change in 1st month.
average_monthly_change = (sum(monthly_change)) / (real_total_months - 1)

# set average_monthly_change to string to format in USD
dollar_average_monthly_change = "${:,.2f}".format(average_monthly_change)

# print(max_index)
dollar_max_monthly_increase = "${:,.2f}".format(max_monthly_increase)
dollar_max_monthly_decrease = "${:,.2f}".format(max_monthly_decrease)

#consider converting the report to a multiline f string)

print(f'''
Financial Analysis
--------------------------------------------------------------------------
Total Months:                  {real_total_months}
Total Profit:                  {dollar_total_profit}
Average Change:                {dollar_average_monthly_change}
Greatest Increase in Profits:  {max_month}  {dollar_max_monthly_increase}
Greatest Decrease in Profits:  {min_month}  {dollar_max_monthly_decrease}
''')