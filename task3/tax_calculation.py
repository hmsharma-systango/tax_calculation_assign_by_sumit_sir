import csv
import json
import string

with open('data2.csv', 'w', newline="") as f:
    writer = csv.writer(f)

    product_name = ["soap","detergent","cream","toys"]
    cost_price = [100,200,300,500]
    tax = [10,30,40]
    country_name = ["India:","US:","china"]
    country = []
    try:
        for country in range(len(country_name)):
            writer.writerow([country_name[country]])
            writer.writerow(["ProductName", "CostPrice","Tax_Amt", "Tax_Per", "Final_Pice"])
            for pd, cp in zip(product_name, cost_price):
                # validation check for input...

                    if(type(pd) == str and type(cp) == int and cp >= 0.0):
                        product_dict = {}
                        tax_per = tax[country]

                        if(type(tax_per) == int and tax_per >= 0.0):
                            tax_amt = (cp*tax_per)/100
                            final_price = cp + tax_amt
                            writer.writerow(
                                [pd, cp, tax_amt, tax_per, final_price])
                            product_dict['product_name'] = pd
                            product_dict['cost_price'] = cp
                            product_dict['tax_amt'] = tax_amt
                            product_dict['tax_per'] = tax_per
                            product_dict['final_price'] = final_price
                        else:
                            print("tax price is invalid")
                            break

                    else:
                        print("either product name or cost price is invalid")
    except:
        print("Index matching error with tax or country")       
            
f.close()

"""creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())

	lst.append(ele) # adding the element
	
print(lst)
"""
