def get_hidden_card(card_number, num_stars=4):
    hidden_card = '*' * num_stars + card_number[-4:]
    return hidden_card
get_hidden_card('2034399002121100', 1)  # *1100
get_hidden_card('1234567812345678', 2)  # **5678
get_hidden_card('1234567812345678', 3)  # ***5678
get_hidden_card('1234567812345678')     # ****5678

