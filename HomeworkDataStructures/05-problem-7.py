st_accounts = {"Ivan": ["BG04DS154566", "BG07IA735845"],
               "Smilyana": ["BG15DS985632"],
               "Georgi": ["BG80UC326598", "BG25RF123252", "BG96UB589878"]}

print("Students Bank Account: ")
for student, accounts in st_accounts.items():
    print(f'{student}, {accounts}')