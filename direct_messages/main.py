from direct_messages.dm import InstaDM
import direct_messages.params as params
import re


def get_lines(filename):
    with open(filename, 'r') as file:
        return file.readlines()


def rewrite(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines[20:])


if __name__ == '__main__':
    filepath = 'target.txt'
    post = "https://www.instagram.com/p/CPkix1ArLHj/"
    proxy_list = [False, '185.87.199.103:3128', '91.218.229.103:3128']
    i = 0
    with open('accounts.txt', 'r') as file:
        accounts = file.readlines()
        for account in accounts:
            if i % 5 == 0:
                proxy = proxy_list.pop(0)
            i += 1
            print(proxy)
            account = account.split(":")
            insta = InstaDM(username=account[0], password=account[1].rstrip(), headless=False, proxy=proxy)
            lines = get_lines(filepath)
            if len(lines) != 0:
                insta.redirect(post=post, users=lines[:20])
                rewrite(filepath, lines)
                insta.teardown()
            else:
                print('Mailing was succesfull' + "\n" + "Last account {} : {}".format(account[0], account[1]) + "\n")
                print("Print command:")
                command = input()
                if command == 'e':
                    exit()
