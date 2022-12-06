def pretty_print(historic, predicted):
   maxlen = list(historic.values())[0].maxlen

   def get_formatted_percentages(h):
      formatted_percentages = " ".join([f"{int(x*100)}%" for x in h])
      return f'{formatted_percentages:<{maxlen*4-1}}'

   for i in historic:
      perc = get_formatted_percentages(historic[i])
      print(f"{i} pred: {int(predicted[i]*100)} - hist {perc}", end="  |  ")
   print()
