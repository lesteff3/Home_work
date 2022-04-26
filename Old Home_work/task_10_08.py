import csv_utils




title = ['Product name', 'Price', 'Amount', 'Comment']
products_info = [
    ["Iphone", "2000", "100", "Phone"],
    ["MackBook", "1000", "50", "laptop"],
    ["Samsung", "1500", "300", "Phone"],
    ["Intel", "400", "1000", "CPU"],
    ["Ipad", "750", "200", "Audio player"]

]
new_products = ['Bloody', '50', '100000', 'Mouse']

csv_utils.write_file(file_to_write='file_with_price.csv', fields=title, rows=products_info)
fields, rows = csv_utils.read_file(file_to_read='file_with_price.csv')
rows_add = csv_utils.add_by_position(rows=rows, new_row=new_products)
csv_utils.write_file(file_to_write='file_with_price.csv', fields=fields, rows=rows_add)
rows_del = csv_utils.delete_by_position(rows=rows_add, position=1)
csv_utils.write_file(file_to_write='file_with_price.csv', fields=fields, rows=rows_del)
csv_utils.count_sum(file_to_read='file_with_price.csv')
csv_utils.decrease_amount(file_to_read='file_with_price.csv')
csv_utils.decrease_amount(file_to_read='file_with_price.csv')
