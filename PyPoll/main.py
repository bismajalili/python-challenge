


def main():
    voting_data = []
    candidate_data = []
    csv_file_path = "Resources/election_data.csv"
    excel_columns = ["Ballot ID", "County", "Candidate"]
    text_file_path = "analysis/vote_analysis.txt"

    # Open file, extract data, sort data
    with open(csv_file_path, "r") as data:
        for row in data:
            row = row.replace("\n", "")
            split_row = row.split(",")
            if split_row[0] != excel_columns[0] and split_row[1] != excel_columns[1] and split_row[1] != excel_columns[2]:
                candidate_info = {
                    "ballot_id": split_row[0],
                    "county": split_row[1],
                    "candidate": split_row[2]
                }
                voting_data.append(candidate_info)


    final_results = get_candidate_vote_data(voting_data, len(voting_data))
    election_winner = []
    print_candidate_info_txt_file = []


    #print final results
    print("Election Results")
    print("-----------------------------------")
    print(F"Total Votes: {len(voting_data)}")
    print("-----------------------------------")

    for i in range(0, len(final_results)):
        data_string = F"{final_results[i]['candidate']}: {final_results[i]['percentage_of_votes']}% ({final_results[i]['total_vote_count']})"
        print(data_string)
        print_candidate_info_txt_file.append(data_string)

        if len(election_winner) == 0:
            election_winner.append(final_results[i]["candidate"])
            election_winner.append(final_results[i]["total_vote_count"])
        elif final_results[i]["total_vote_count"] > election_winner[1]:
            election_winner = []
            election_winner.append(final_results[i]["candidate"])
            election_winner.append(final_results[i]["total_vote_count"])

    print("-----------------------------------")
    print(F"Winner: {election_winner[0]}")
    print("-----------------------------------")

    #Write to text file
    write_to_txt_file(len(voting_data),print_candidate_info_txt_file,election_winner[0],text_file_path)



def write_to_txt_file(arg1,arg2,arg3,file_path):
    write_data = []

    write_data.append("Election Results")
    write_data.append("----------------------------------------")
    write_data.append(F"Total Votes: {arg1}")
    write_data.append("----------------------------------------")
    for i in range(0, len(arg2)):
        write_data.append(arg2[i])
    write_data.append("----------------------------------------")
    write_data.append(F"Winner: {arg3}")
    write_data.append("----------------------------------------")

    with open(file_path, "w") as financial_analysis_file:
        for data in write_data:
            financial_analysis_file.write(data + "\n")

def get_candidate_vote_data(arg1, arg2):
    output = []
    candidate_frequency_count = {}

    for i in range(0, len(arg1)):
        if arg1[i]["candidate"] in candidate_frequency_count.keys():
            candidate_frequency_count[arg1[i]["candidate"]] += 1
        else:
            candidate_frequency_count[arg1[i]["candidate"]] = 1

    for [key,value] in candidate_frequency_count.items():
        percentage_of_votes = (value / arg2) * 100
        percentage_of_votes = round(percentage_of_votes, 3)

        candidate_data = {
            "candidate": key,
            "total_vote_count": value,
            "percentage_of_votes": percentage_of_votes
        }

        output.append(candidate_data)


    return output



if __name__ == '__main__':
    main()


