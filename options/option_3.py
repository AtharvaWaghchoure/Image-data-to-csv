"""
This file gets the 3rd option.
"""
from datetime import date

FILE_NAMES = []
PHOTO = "{}.jpg|{}_{}_Proof.jpg"
VIDEO =  '{}_{}_'
sku_list = []

def _date():    # to get today's date
    today = date.today()
    d1 = today.strftime("%d%m20%y")
    return d1

def get_f_for_2nd_csv(FILE_NAMES):
    ret_list = []
    if len(FILE_NAMES)%2 == 0:
        half = int(len(FILE_NAMES)/2)
        for _ in range(1,(half+1)):
            ret_list.append(24)
        ret_list.append(8)
        while len(ret_list) != len(FILE_NAMES):
            ret_list.append('')
        return ret_list
    else:
        half = int((len(FILE_NAMES)+1)/2)
        for _ in range(1,(half+1)):
            ret_list.append(24)
        ret_list.append(8)
        while len(ret_list) != len(FILE_NAMES):
            ret_list.append('')
        return ret_list

def option_3(FILE_NAMES):
    product_list  = []
    price = []
    Sale_price = []
    photo_list = []
    video_list = []
    name_list = []
    name_link = []

    product_name = "{} {} signed model 8×10 Photo -PROOF- -CERTIFICATE-  (A{})"
    date1 = _date()

    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the last element
        Last_4 = file_ele[-1]

        # product list
        product_list.append(product_name.format(First_name,Last_name,Last_4))
        
        #sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "r"
        sku_list.append(sku)

         # price
        price.append(29.95)

        # sale price
        Sale_price.append(22.95)

        # photo list
        photo_list.append(PHOTO.format(i, First_name, Last_name))
        
        # video list
        video_list.append('[video width="360" height="640" mp4="https://stalicali.com/wp-content/uploads/wpallimport/files/' + VIDEO.format(First_name, Last_name) + 'Signing_Autographs_Video.mp4"][/video]')

        # name list
        name_list.append((First_name+" "+Last_name))

        # namelink list
        name_link.append((First_name+"-"+Last_name))

    return [product_list, sku_list, price, Sale_price, photo_list, video_list, name_list, name_link]

def option_3_2nd_csv(FILE_NAMES):
    '''
    This option creates returns data for 2nd csv.
    '''
    product_list = []
    sku_list = []
    price =[]
    column_d = []
    column_e = []
    column_f = get_f_for_2nd_csv(FILE_NAMES)
    column_g = []
    last_sku =[]

    product_name = "{} {} signed model 8×10 Photo -PROOF- -CERTIFICATE-  (A{})"    
    date1 = _date()
    
    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the second element
        Last_4 = file_ele[-1]

        # name
        product_list.append(product_name.format(First_name,Last_name, Last_4))

        # sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "r"
        sku_list.append(sku)
         
        # price
        price.append(29.95)

        # column d
        column_d.append(1)

        # column e - skip all
        column_e.append("")

        # column g - yet to be done.
        column_g.append('')

        # sku last part
        last_sku.append("r")

    return [product_list, sku_list, price, column_d, column_e, column_f, column_g, last_sku]

def option_3_3rd_csv(FILE_NAMES):
    column_a = []

    for _ in FILE_NAMES:
        # column a
        column_a.append(1)

    return ([column_a, sku_list])