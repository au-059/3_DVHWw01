def main():
        t_input = get_string("Type: ")
        output = convert(t_input)
        print(output)

def get_string(prompt):
        return str(input(prompt))

def convert(t_input):
        t_happy = t_input.replace(":)", "🙂")
        t_sad = t_happy.replace(":(", "🙁")
        return t_sad

main()