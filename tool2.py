import requests
from fpdf import FPDF
import warnings #used for ignore deprecation warnings
warnings.simplefilter("ignore", DeprecationWarning)
warnings.simplefilter("ignore", UserWarning)
pdf = FPDF()

# created two function first domain_scanner and pdf_file
# 1st is used scan domain and 2nd used for pdf_file
def domain_scanner(domain_name,sub_domnames):
	print('----URL after scanning subdomains----')
	
	for subdomain in sub_domnames:
		url = f"https://{subdomain}.{domain_name}"
		try:
			requests.get(url) # here get the GET req
			# print(url)
			with open('subd.txt','a') as f:
				f.write(f'[+] {url}\n')
		except:
			pass

#function which creates pdf file for ease to use
def pdf_file():
	pdf.add_page()

	# add page for title
	pdf.set_font('Arial', 'B', 12)

	# Add title name
	pdf.cell(0, 10, 'SUBDOMAIN LIST : ', 0, 1, 'C') # used for title into center of the page

	# max width for adjust the length of the text
	max_width = 200

	# back to the normal text
	pdf.set_font('Arial', '', 12)
	
	with open('subd.txt','r') as f:
		data = f.readlines()
	
	for line in data:
		pdf.multi_cell(max_width, 4, line.strip())
		#pdf.cell(0, 10, line.strip())
		pdf.ln()
		
	pdf.output('sub_domain_list.pdf', 'F')
	print('--FINISHED--')
	
# inputting the domain name
domain_name = input("Enter the Domain Name:")

# opening the subdomain text file
with open('wordlist.txt','r') as file:
	# reading the file
	name = file.read()
	# of splitted strings
	sub_domain = name.splitlines()
	 
# calling the function for scanning the subdomains
# and getting the url
domain_scanner(domain_name,sub_domain)
pdf_file()