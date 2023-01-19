
# This is a sample Python script.
import multiprocessing


from Cert import gen_ca_cert_key

import App
print("00")

# print("00")

def run_script():
    print("11")
    gen_ca_cert_key()
    print("22")
    app = App()
    print("33")
    app.mainloop()
    print("44")

if __name__ == '__main__':
    run_script()
    ## TODO : remove #
    print("55")
    # gen_ca_cert_key()
    print("66")
    # app = App()
    # print("77")
    # app.mainloop()
    # print("88")
    # p1 = multiprocessing.Process(target=run_script)
    # p2 = multiprocessing.Process(target=run_script)
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()



