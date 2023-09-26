def main():

    budget_data = []
    columns = ["Date","Profit/Losses"]
    csv_file_path = "Resources/budget_data.csv"
    text_file_path = "analysis/financial_analysis.txt"

    #Open file, extract data, sort data
    with open(csv_file_path, "r") as data:
        for row in data:
            row = row.replace("\n","")
            split_row = row.split(",")
            if split_row[0] != columns[0] and split_row[1] != columns[1]:

                data_dictionary = {
                    "month":split_row[0],
                    "net_amount":int(split_row[1])
                }
                budget_data.append(data_dictionary)


    #Get total months
    total_months = get_total_months(budget_data)

    #Get net total amount
    net_total_amount = get_net_total_amount(budget_data)

    #Get average change
    avg_change = get_average_change(get_profit_losses_changes(budget_data))

    #Get greatest profit increase
    greatest_profit_increase = get_greatest_profit_increase(get_profit_losses_changes(budget_data))

    #Get greatest profit increase
    greatest_profit_decrease = get_greatest_profit_decrease(get_profit_losses_changes(budget_data))

    #Create text file and write to it
    write_to_txt_file(total_months,net_total_amount,avg_change,greatest_profit_increase,greatest_profit_increase,greatest_profit_decrease,greatest_profit_decrease,text_file_path)

    #Print results
    print("Financial Analysis")
    print()
    print("----------------------------------------------")
    print()
    print(F"Total Months: {total_months}")
    print(F"Total: ${net_total_amount}")
    print(F"Average Change: ${avg_change}")
    print(F"Greatest Increase in Profits: {greatest_profit_increase['month']} (${greatest_profit_increase['increase_amount']})")
    print(F"Greatest Decrease in Profits: {greatest_profit_decrease['month']} (${greatest_profit_decrease['decrease_amount']})")


def write_to_txt_file(arg1,arg2,arg3,arg4,arg5,arg6,arg7, file_path):
    write_data = [
        "Financial Analysis",
        "----------------------------------------",
        F"Total Months: {arg1}",
        F"Total: ${arg2}",
        F"Average Change: ${arg3}",
        F"Greatest Increase in Profits: {arg4['month']} (${arg5['increase_amount']})",
        F"Greatest Decrease in Profits: {arg6['month']} (${arg7['decrease_amount']})"
    ]

    with open(file_path, "w") as financial_analysis_file:
        for data in write_data:
            financial_analysis_file.write(data + "\n")


def get_total_months(arg):
    output = len(arg)
    return output

def get_net_total_amount(arg):

    output = None

    for i in range(0, len(arg)):
        if output == None:
            output = arg[i]["net_amount"]
        else:
            output += arg[i]["net_amount"]

    return output


def get_profit_losses_changes(arg):
    output = []

    for i in range(0, len(arg) - 1):

        index1 = (i + 1)
        index2 = i

        profit_loss_change = {
            "month": arg[index1]["month"],
            "net_amount": arg[index1]["net_amount"],
            "profit_loss_change": (arg[index1]["net_amount"] - arg[index2]["net_amount"])
        }

        output.append(profit_loss_change)


    return output


def get_average_change(arg):

    total = None

    for i in range(0, len(arg)):
        if total == None:
            total = arg[i]["profit_loss_change"]
        else:
            total += arg[i]["profit_loss_change"]


    output = total / len(arg)
    output = round(output, 2)
    return output

def get_greatest_profit_increase(arg):

    greatest_profit_increase = {
        "month": None,
        "increase_amount": None
    }

    for i in range(0, len(arg)):
        if greatest_profit_increase["increase_amount"] == None:
            greatest_profit_increase["month"] = arg[i]["month"]
            greatest_profit_increase["increase_amount"] = arg[i]["profit_loss_change"]

        elif arg[i]["profit_loss_change"] > greatest_profit_increase["increase_amount"]:
            greatest_profit_increase["month"] = arg[i]["month"]
            greatest_profit_increase["increase_amount"] = arg[i]["profit_loss_change"]

    return greatest_profit_increase


def get_greatest_profit_decrease(arg):

    greatest_profit_decrease = {
        "month":None,
        "decrease_amount": None
    }

    for i in range(0, len(arg)):
        if greatest_profit_decrease["decrease_amount"] == None:
            greatest_profit_decrease["month"] = arg[i]["month"]
            greatest_profit_decrease["decrease_amount"] = arg[i]["profit_loss_change"]

        elif arg[i]["profit_loss_change"] < greatest_profit_decrease["decrease_amount"]:
            greatest_profit_decrease["month"] = arg[i]["month"]
            greatest_profit_decrease["decrease_amount"] = arg[i]["profit_loss_change"]

    return greatest_profit_decrease



if __name__ == "__main__":
    main()
