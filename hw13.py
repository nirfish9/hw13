def find_err(txtfile,word):
    with open(txtfile) as f1:
        if word in f1.read():
            return True
        else:
            return False



