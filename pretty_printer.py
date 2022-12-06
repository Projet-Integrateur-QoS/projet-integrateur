def pretty_print(historic):
   maxlen = historic["A"]["CPU"].maxlen

   def get_formatted_percentages(historic, node, ressource):
      formatted_percentages = ", ".join([f"{int(x*100)}%" for x in historic[node][ressource]])
      return f'{formatted_percentages:<{maxlen*5}}'

   cpu_a = get_formatted_percentages(historic, "A", "CPU")
   cpu_b = get_formatted_percentages(historic, "B", "CPU")
   cpu_c = get_formatted_percentages(historic, "C", "CPU")
   ram_a = get_formatted_percentages(historic, "A", "RAM")
   ram_b = get_formatted_percentages(historic, "B", "RAM")
   ram_c = get_formatted_percentages(historic, "C", "RAM")
   print(f"A - CPU: {cpu_a}\tB - CPU: {cpu_b}\tC - CPU: {cpu_c}")
   print(f"    RAM: {ram_a}\tB - RAM: {ram_b}\tC   RAM: {ram_c}")
   print(f"-"*200)
