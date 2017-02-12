import csv

def parse(filename):
	f = open('komorki.sql', 'w', encoding='utf-8')
	with open(filename, 'rt', encoding='utf-8') as csvfile:
		reader = csv.reader(csvfile, delimiter='|')
		for nline in reader:
			line = []
			for word in nline:
				word=word.replace("'", '"')
				line.append(word)
			newline = "INSERT INTO `facility_unit` (`id`, `section_id`, `ks_id`, `id_zoz`, `regon`, `section_code`, `unit_code`, `unit_speciality`, `unit_code_viii`, `unit_name`, `teryt`, `teryt_description`, `street`, `building`, `lodging`, `postal_code`, `town`, `all_beds`, `iom_beds`, `ink_beds`, `all_now`, `incubators`, `dialysis`, `beds`, `start_date`, `close_date`, `suspension_start_date`, `suspension_end_date`) VALUES ('"+line[3]+"',"+ "'"+line[2]+"',"+ "'"+line[0]+"',"+ "'"+line[1]+"',"+ "'"+line[4]+"',"+ "'"+line[5]+"',"+ "'"+line[6]+"',"+ "'"+line[7]+"',"+ "'"+line[8]+"',"+ "'"+line[9]+"',"+ "'"+line[10]+"',"+ "'"+line[11]+"',"+ "'"+line[12]+"',"+ "'"+line[13]+"',"+ "'"+line[14]+"',"+ "'"+line[15]+"',"+ "'"+line[16]+"',"+ "'"+line[17]+"',"+ "'"+line[18]+"',"+ "'"+line[19]+"',"+ "'"+line[20]+"',"+ "'"+line[21]+"',"+ "'"+line[22]+"',"+ "'"+line[23]+"',"+ "'"+line[24]+"',"+ "'"+line[25]+"',"+ "'"+line[26]+"',"+ "'"+line[27]+"');"
			print(newline, file=f)
	f.close()
			
def main():
	parse('komorki.txt')
	
if __name__ == '__main__':
	main()