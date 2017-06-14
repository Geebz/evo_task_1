from pprint import pprint
import re


def update(data, service, count):
    while count:
        min_number_of_instances_service = min(data, key=lambda x: sum(data[x].values()))
        if service in data[min_number_of_instances_service]:
            data[min_number_of_instances_service][service] += 1
        else:
            data[min_number_of_instances_service][service] = 1
        count -= 1
    return data


def main():
    example_data = {
        'ginger': {
            'django': 2,
            'flask': 3,
        },
        'cucumber': {
            'flask': 1,
        },
    }

    # Interactive mode start
    print("Hello Evo! Welcome to program.")
    print("Configuration before:")
    pprint(example_data)

    while True:
        while True:
            service = input("What service do you want to add?: ").lower()
            if re.fullmatch('^[a-z]+$', service) is None:
                print("Service must be written only letters")
                continue
            else:
                break

        while True:
            try:
                number = int(input("How many instances do you want to run?: "))
                break
            except ValueError:
                print("Number must be integer. Let`s try again")
                continue

        update(example_data, service, number)

        decision = input("Do you want to add another one? Yes or No: ")
        if decision.lower() == 'yes':
            continue
        else:
            break

    print("Configuration after:")
    pprint(example_data)
    print("That`s it. Let`s go to another task ;)")
    # Interactive mode end

if __name__ == '__main__':
    main()
