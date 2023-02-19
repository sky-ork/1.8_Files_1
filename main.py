def read_cook_book(recipes: str):
    cook_book = {}
    with open(recipes, encoding='UTF-8') as f:
        while True:
            try:
                dish_name = f.readline().strip()
                count_ingr = int(f.readline())
                ingr_list = []
                for _ in range(count_ingr):
                    ingr_dict = {'ingredient_name': '', 'quantity': '', 'measure': ''}
                    ingr = f.readline().strip()
                    splited = ingr.split(' | ')
                    i = 0
                    for key in ingr_dict.keys():
                        ingr_dict[key] = splited[i]
                        i += 1
                    ingr_list.append(ingr_dict)
                cook_book[dish_name] = ingr_list
                f.readline()
            except Exception:
                break
    return cook_book


def main(recipes: str):
    print(read_cook_book(recipes))


if __name__ == "__main__":
    main('recipes.txt')
