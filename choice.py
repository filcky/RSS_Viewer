
def make_a_dict():
    with open (r'F:\py\RSS\rss_list.txt','r',encoding="utf-8") as fp:
        data = fp.read()
        all_lists_list=data.split('\n')
        print(all_lists_list)
    list_length = len(all_lists_list)
    all_clear_dict = {}
    for i in range (1,list_length+1,2):
        try:
            all_clear_dict[all_lists_list[i]] = all_lists_list[i+1]
        except:
            pass
        print(all_clear_dict)

    for key in all_clear_dict:
        print(key)

if __name__ == "__main__":
    make_a_dict()



     

    