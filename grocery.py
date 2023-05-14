def main():
        print("(press ctrl+d to end the list)")
        gr_list = {}

        while True:
                    try:
                        item = input().upper()
                        if item in gr_list:
                               gr_list[item] += 1
                        else:
                               gr_list[item] = 1
                    except EOFError:
                        for item in sorted(gr_list):
                               print(gr_list[item], item)

                        break
main()