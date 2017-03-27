import choices


def start():
    category_choice = choices.get_category()
    go_scenario(category_choice)

def go_scenario(category_choice):
    scenario_choice = choices.get_scenario(category_choice)
    go_word(scenario_choice, category_choice)

def go_word(scenario_choice, category_choice):
    word_choice = choices.get_words(scenario_choice)
    option_choice = choices.get_sentence(word_choice,category_choice,scenario_choice)
    if option_choice == 1:
    	start()
    elif option_choice == 2:
        go_scenario(category_choice)
    elif option_choice == 3:
        go_word(scenario_choice,category_choice)
    else:
        exit()

if __name__ == "__main__":
    start()