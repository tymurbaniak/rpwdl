import csv

def parse(filename):
	f = open('podmioty.sql', 'w', encoding='utf-8')
	with open(filename, 'rt', encoding='UTF-8') as csvfile:
		reader = csv.reader(csvfile, delimiter='|')
		for nline in reader:
			line = []
			for word in nline:
				word=word.replace("'", '"')
				line.append(word)
			print(line)
			newline = "INSERT INTO `facility_division` (`ks_id`, `nip`, `regon`, `register_book_number`, `removal_date`, `removal_decision_date`, `decision_number`, `institution_type`, `institution_code`, `organization_form`, `organization_form_description`, `name`, `facility_name`, `teryt`, `teryt_description`, `street`, `building`, `lodging`, `postal_code`, `town`, `phone`, `email`, `website`, `founder_code`, `founder_name`, `start_date`, `start_date_legal`, `close_date`, `suspension_start_date`, `suspension_end_date`) VALUES ("+"'"+ line[0] +"', "+"'"+ line[1] +"', "+"'"+ line[2] +"', "+"'"+ line[3] +"', "+"'"+ line[4] +"', "+"'"+ line[5] +"', "+"'"+ line[6] +"', "+"'"+ line[7] +"', "+"'"+ line[8] +"', "+"'"+ line[9] +"', "+"'"+ line[10] +"', "+"'"+ line[11] +"', "+"'"+ line[12] +"', "+"'"+ line[13] +"', "+"'"+ line[14] +"', "+"'"+ line[15] +"', "+"'"+ line[16] +"', "+"'"+ line[17] +"', "+"'"+ line[18] +"', "+"'"+ line[19] +"', "+"'"+ line[20] +"', "+"'"+ line[21] +"', "+"'"+ line[22] +"', "+"'"+ line[23] +"', "+"'"+ line[24] +"', "+"'"+ line[25] +"', "+"'"+ line[26] +"', "+"'"+ line[27] +"', "+"'"+ line[28] +"', "+"'"+ line[29]+"'"+");"
			print(newline, file=f)
	f.close()
			
def main():
	parse('podmioty.txt')
	
if __name__ == '__main__':
	main()