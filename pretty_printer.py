def pretty_print(history, predicted):
   maxlen = list(history.values())[0].maxlen

   def get_formatted_percentages(h):
      formatted_percentages = " ".join([f"({int(x[0]*100):2d},{int(x[1]*100):2d})" for x in h])
      return f'{formatted_percentages:<{maxlen*8-1}}'

   for i in history:
      perc = get_formatted_percentages(history[i])
      print(f"{i} pred: ({int(predicted[i][0]*100):2d},{int(predicted[i][1]*100):2d}) - hist {perc}", end="  |  ")
   print()
