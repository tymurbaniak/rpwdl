import csv

def parse(filename):
	f = open('jednostki.sql', 'w', encoding='utf-8')
	with open(filename, 'rt', encoding='utf-8') as csvfile:
		reader = csv.reader(csvfile, delimiter='|')
		for nline in reader:
			line = []
			for word in nline:
				word=word.replace("'", '"')
				line.append(word)
			newline = "INSERT INTO `facility_section` (`section_id`, `ks_id`, `id_zoz`, `regon`, `section_code`, `name`, `teryt`, `teryt_description`, `street`, `building`, `lodging`, `postal_code`, `town`, `phone`, `email`, `website`, `start_date`, `close_date`, `suspension_start_date`, `suspension_end_date`) VALUES ('"+line[2]+"',"+ "'"+line[0]+"',"+ "'"+line[1]+"',"+ "'"+line[3]+"',"+ "'"+line[4]+"',"+ "'"+line[5]+"',"+ "'"+line[6]+"',"+ "'"+line[7]+"',"+ "'"+line[8]+"',"+ "'"+line[9]+"',"+ "'"+line[10]+"',"+ "'"+line[11]+"',"+ "'"+line[12]+"',"+ "'"+line[13]+"',"+ "'"+line[14]+"',"+ "'"+line[15]+"',"+ "'"+line[16]+"',"+ "'"+line[17]+"',"+ "'"+line[18]+"','"+line[19]+"');"
			print(newline, file=f)
	f.close()
			
def main():
	parse('jednostki.txt')
	
if __name__ == '__main__':
	main()