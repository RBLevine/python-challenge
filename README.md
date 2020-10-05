# python-challenge

PyBank Folder:
	Analysis Folder:
		PyBankResults (Text Document): This is the results file that contains the output 
			analysis from the main.py file.			
	Resources Folder:
		budget_data (Microsoft Excel Comma Separated Values File): This is the data file.
			The format contains a header for two columns, the first of which is the
			month-year and the second is the Profit/Loss for that month.
	main (PY File):Takes in a CSV file in formatted with headers, and two columns of code, the 
		first one is the month-year,the second is the Profit Loss associate with that 
		month-year. Reads the file and analyzes the total number of months with data in the 
		file, the total Profit/Loss, the average Profit/Loss, as well as the Greatest 
		Increase in Profits and the Greatest Decrease in Profit and the months associated 
		with those both. This info will be printed to Terminal and a .txt file in the 
		Analysis folder.

PyBoss Folder:
	Analysis Folder:
		updated_employee_data (Microsoft Excel Comma Separated Values File): Result file
			with 6 columns: Emp ID, First Name, Last Name, DOB 
			(formatted as mm/dd/yyyy), SSN (formatted with all but the last four digits 
			starrred out), and State (formatted as the two letter abbreviation).
	Resources Folder:
		employee_data (Microsoft Excel Comma Separated Values File): a CSV file formatted 
			with headers and 5 columns (Emp ID, Name, DOB, SSN, State), where Name 
			contains the first and last name, DOB is in the yyy7-mm-dd format, SSN is 
			fully listed out, separated by dashes, and State is the full state name 
			spelled out.
	main (PY File): Takes in a CSV file formatted with headers and 5 columns (Emp ID, Name, DOB,
		SSN, State), where Name contains the first and last name, DOB is in the yyy7-mm-dd
		format, SSN is fully listed out, separated by dashes, and State is the full state
		name spelled out. This code will then reformat the file so that there are 6 columns:
		Emp ID, First Name, Last Name, DOB (formatted as mm/dd/yyyy), SSN (formatted with
		all but the last four digits starrred out), and State (formatted as the two letter
		abbreviation). This reformatting will be saved to the Analysis Folder.
PyPoll Folder:
	Analysis Folder:
		PyPollResults (Text Document): This is the results file that contains the output 
			analysis from the main.py file.	
	Resources Folder:
		election_data (Microsoft Excel Comma Separated Values File): a CSV file formatted
			with a heard and 3 columns: Voter ID, County, Candidate.
	main (PY File): Reads a CSV file formatted with headers and 3 columns (Voter ID, County, 
		Candidate). Provides a summary of the data, including the total number of votes cast,
		the names of the candidates voted for and the percentage of votes and number of votes
		each received, and the winner of the election based on popular vote. This info will
		be printed to Terminal and a .txt file in the Analysis Folder.
