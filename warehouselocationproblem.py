import random

warehouse = [1,2,3]
warehouse_limit = [100,100,500]
customer = [1,2,3,4]
customer_request = [50,50,75,75]
warehouse_build_cost = [100.123,100.456,100.789]
warehouse_customer_cost = [[100.1,200.2,2000.3],[100.4,200.5,2000.6],[200.7,100.8,2000.9],[200.10,200.11,100.12]]


list_cost = 2
customer_cost = 3
cost = 0
total_cost = 0
total_cost_list= []

for p in range(2):
    for i in range(4):
        k=random.randint(0,list_cost)
        q=k
        l=customer_request[i]
        m=warehouse_limit[k]
        #print(i+1,"numarali musteri")
        #print(k+1,"numarali depo")
        #print(warehouse_limit)
        if(m>=l):
            m -= l
            warehouse_limit[k]=m
            #print("kalan depo limiti",warehouse_limit)
            customer.remove(customer[0])
            #print("kalan musteriler",customer)
            cost = warehouse_build_cost[k] + warehouse_customer_cost[i][k]
            if(m<=0):
                warehouse_limit.remove(warehouse_limit[k])
                warehouse_build_cost.remove(warehouse_build_cost[k])
                list_cost = list_cost-1
            customer_cost = customer_cost-1
        elif(m<l):
            k=random.randint(0,list_cost)
            while(m<l):
                k=random.randint(0,list_cost)
                if(m>=l):
                    break
            m -= l
            warehouse_limit[k]=m
            #print("kalan depo limiti",warehouse_limit)
            customer.remove(customer[0])
            #print("kalan musteriler",customer)
            cost = warehouse_build_cost[k] + warehouse_customer_cost[i][k]
            if(m<=0):
                warehouse_limit.remove(warehouse_limit[k])
                warehouse_build_cost.remove(warehouse_build_cost[k])
                list_cost = list_cost-1
            customer_cost = customer_cost-1
        total_cost = total_cost + cost
        warehouse.clear
        warehouse_limit.clear
        customer.clear
        customer_request.clear
        warehouse_build_cost.clear
        warehouse_customer_cost.clear
        warehouse = [1,2,3]
        warehouse_limit = [100,100,500]
        customer = [1,2,3,4]
        customer_request = [50,50,75,75]
        warehouse_build_cost = [100.123,100.456,100.789]
        warehouse_customer_cost = [[100.1,200.2,2000.3],[100.4,200.5,2000.6],[200.7,100.8,2000.9],[200.10,200.11,100.12]]
    #print("\n")
    total_cost_list.append(total_cost)
print(total_cost_list)
print("toplam maliyet",min(total_cost_list))

    
    
    
            



