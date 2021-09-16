from installator import check_keys

if __name__ == '__main__':
    if not check_keys("license.key"):
        print("You don't have a license!")
        mb.showerror("error", "You don't have a license!")
        sys.exit()
    else:
        print('YUHUUU')