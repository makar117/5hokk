def get_vat(payment, persent=20):
	try:	
		payment = float(payment)
		vat = payment / 100 * persent
		vat = round(vat, 2)
		return "sum VAT: {}".format(vat)
	except TypeError:
		return "Ты дэлбик? Цифры пиши"	
result = get_vat(1488, 69)
print(result)