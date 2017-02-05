import csv
class ToCSV:
	
	def __init__(self, out_file, data):
		output_file = open(out_file, "wb")
		wrtr = csv.writer(output_file)
		for rec in data:
			
			wrtr.writerow(rec)
		output_file.close()


B=[[1,2,3],[4,5,6]]
A=ToCSV("out.csv",B)