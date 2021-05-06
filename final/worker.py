import pandas as pd
from jobs import q, rd_jobs, update_job_status, get_locations, _generate_job_key, get_menus, get_price
import time
import redis

def formula(id, address, categories, menus_amountmax, menus_amountmin):

    new_table = {'id':id, 'address': address, 'categories': categories, 'max menus': menus_amountmax, 'min menus': menus_amountmin, 'minimum price': pricerangemin, '\
maximum price': pricerangemax)}

    menus_num_min = int(menus_amountmin)
    menus_num_max = int(munes_amountmax)
    menus_num = menus_num_min + menus_num_max

    avg_min_price = sum(pricerangemin)/len(pricerangemin)
    avg_max_price = sum(pricerangemax)/len(pricerangemax)

    start_menu = [0]*(menus_num)
    end_menu = [0]*(menus_num)

    start_menu[0] = menus_num_min

    new_table.update({"menus_min" : start_menu[0]})


def subset(status, start_id, end_id):

    subset_1 = pd.DataFrome()

    subset_1 = subset_.append(get_locations.loc[(get_locations['address'] == status) & (start_id <= get_locations['id']) & (end_id >= get_locations['id']), ['id', 'a\
ddress', 'category']])

    return subset_1



@q.worker
def do_work(jid):
    update_job_status(jid, 'in progress')

    locations = get_locations()
    menus = get_menus()
    pricing = get_price()


    rd_jobs.hset(_generate_job_key(jid), 'location number', len(locations))

    max_price = max(pricing)

    columns1 = ['id', 'address', 'categories', 'menus', 'pricing']

    output = pd.DataFrame(columns = columns1)
    index = 0
    counter = 0

    subset1 = subset_.append(get_locations.loc[(get_locations['address'] == st\
atus) & (start_id <= get_locations['id']) & (end_id >= get_locations['id']), ['                                                                                       
id', 'address', 'category']])

    for index in range(len(subset1)):
        location = subset1.iloc[index]['address']
        menu = subset1.iloc[index]['menu']
        pricing = subset1.iloc[index]['pricing']

        if (index ==0):
            counter = 0
        elif(pricing != subset1.iloc[index-1]['pricing']):
            counter = 0)

       new_table =  formula(id, address, categories, menus_amountmax, menus_amountmin)

       update_job_status(jid, 'complete')

do_work()


