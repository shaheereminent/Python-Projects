def calculate_love_score(name1, name2):
    true = ["t", "r", "u", "e"]
    love = ["l", "o", "v", "e"]

    true_count = 0
    love_count = 0

    combined_name = name1.lower() + name2.lower()

    for i in range(len(true)):
        for letter in combined_name:
            if true[i] == letter:
                true_count += 1
            
    for i in range(len(love)):
        for letter in combined_name:
            if love[i] == letter:
                love_count += 1
    print(f"{true_count}{love_count}")

calculate_love_score("eminent", "Aidah")