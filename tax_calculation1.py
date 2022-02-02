import csv
import json

with open('data2.csv', 'w', newline="") as f:
    writer = csv.writer(f)

    product_name = ["Soap","detergent","cream"]
    cost_price = [100,200,300]
    tax = [10,30]
    country_name = ["India:","US:"]

    country = []
    for country in range(len(country_name)):
        writer.writerow([country_name[country]])
        writer.writerow(["ProductName","CostPrice", "Tax_Amt", "Tax_Per", "Final_Pice"])
        for pd,cp in zip(product_name,cost_price):
            product_dict = {}
            tax_per = tax[country]
            tax_amt = (cp*tax_per)/100
            final_price = cp + tax_amt
            writer.writerow([pd,cp, tax_amt, tax_per, final_price])
            product_dict['product_name'] = pd
            product_dict['cost_price'] = cp
            product_dict['tax_amt'] = tax_amt
            product_dict['tax_per'] = tax_per
            product_dict['final_price'] = final_price
           
f.close()

