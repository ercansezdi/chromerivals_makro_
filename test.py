from random import randint

users = ["asiye","nihal","emişe","ilknur","leyla","hilal","hatice","sude"]

def get_winner():
    users = ["asiye","nihal","emişe","ilknur","leyla","hilal","hatice","sude"]
    user_count = len(users)
    winner = users[randint(0, user_count-1)]
    return winner

hediye_sabihi_olucak = []
hediye_satin_alicak = []

if __name__ == "__main__":
    user_count = len(users)
    count = 0 
    while count < user_count:
        hediye_sahibi = get_winner()
        hediye_verecek = get_winner()

        while hediye_sahibi == hediye_verecek:
            hediye_sahibi = get_winner()
        while hediye_verecek in hediye_satin_alicak:
            hediye_verecek = get_winner()
        while hediye_sahibi in hediye_sabihi_olucak:
            hediye_sahibi = get_winner()

        hediye_sabihi_olucak.append(hediye_sahibi)
        hediye_satin_alicak.append(hediye_verecek)
        count += 1
    
    for i in range(user_count):
        print(f"{hediye_sabihi_olucak[i]} isimli kullanıcı {hediye_satin_alicak[i]} isimli kullanıcıya hediye alacak.")

    