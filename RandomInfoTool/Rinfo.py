import random

COLLEGES = ['IIT, Delhi (Delhi)', 'IIT, Bombay (Mumbai)', 'IIT, Kharagpur (Kharagpur)', 'IIT, Kanpur (Kanpur)', 'Birla Institute Of Technology & Science (Pilani)', 'NIT, Karnataka (Mangalore)', 'College Of Engineering, Guindy (Chennai)', 'Netaji Subhas Institute Of Technology* (New Delhi)', 'VIT University (Vellore)', 'College Of Engineering, Pune (Pune)', 'IIIT, Hyderabad (Hyderabad)', 'IIIT, Allahabad (Allahabad)', 'Indian Institute Of Technology (Indian School Of Mines), Dhanbad (Dhanbad)', 'Delhi Technological University (New-Delhi)', 'Manipal Institue Of Technology (Manipal)', 'University Institute Of Engineering, Chandigarh University (Chandigarh)', 'PSG College of Technology (Coimbatore)', 'Visvesvaraya National Institute Of Technology (Nagpur)', 'Thapar University (Patiala)', 'M.S. Ramaiah Institute Of Technology (Bangalore)', 'Birla Institute Of Technology (Ranchi)', 'The National Institute Of Engineering (Mysore)', 'University College Of Engineering (Hyderabad)', 'Sri Sivasubramaniya Nadar College of Engineering (Kalavakkam)', 'B.I.T. Sindri (Dhanbad)', 'Institute Of Technology (Ahmedabad)', 'SRM Engineering College (Chennai)', 'Government College Of Engineering (Amravati)', "SVKM's NMIMS-Mukesh Patel School Of Technology Management & Engineering (Mumbai)", 'Mepco Schlenk Engineering College (Sivakasi)', 'Thiagarajar College Of Engineering (Madurai)', 'Chaitanya Bharathi Institute Of Technology (Hyderabad)', 'Dwarkadas J. Sanghvi College Of Engineering (Mumbai)', 'Rungta College Of Engineering And Technology (Bhilai)', 'Guru Nanak Dev Engineering College (Ludhiana)', 'Zakir Husain College Of Engineering & Technology, Aligarh (Aligarh)', 'Govt. Model Engineering College (Cochin)', 'MIT College Of Engineering (Pune)', 'PES University (Bangalore)', 'KLE Dr M.S Sheshgiri College Of Engineering And Technology (Belgaum)', 'Bannari Amman Institute Of Technology (Erode)', 'Symbiosis Institute Of Technology (Pune)', 'BMS Institute Of Technology & Management (Bangalore)', 'BMS College Of Engineering (Bangalore)', 'Bharati Vidyapeeth University College Of Engineering (Pune)', 'Jawaharlal Nehru National College Of Engineering (Shimoga)', 'K L University (Guntur)', 'Galgotias College Of Engineering And Technology (Noida)', 'Shri Ramdeobaba College Of Engineering And Management (Nagpur)', 'Sri Sairam Engineering College (Chennai)', 'Cummins College of Engineering for Women (Pune)', 'Faculty Of Engineering, DIT University (Dehradun)', "Sanjivani Rural Education Society's College Of Engineering (Ahmednagar)", 'SDM College Of Engineering & Technology (Dharwad)', 'Pimpri Chinchwad College Of Engineering (Pune)', 'M V J College Of Engineering (Bangalore)', 'Sir M Visvesvaraya Institute Of Technology (Bangalore)', 'The Northcap University (Gurgaon)', 'Rajagiri School Of Engineering & Technology (Ernakulam)', 'Indraprastha Institute Of Information Technology Delhi (New Delhi)', 'National Institute Of Science & Technology (Berhampur)', 'Muffakham Jah College Of Engineering And Technology (Hyderabad)', 'JSS Academy Of Technical Education (Bangalore)', 'Army Institute Of Technology (Pune)', 'Amity School Of Engineering & Technology (Noida)', 'Lovely Professional University (Phagwara)', 'JIS College Of Engineering (Kalyani, West Bengal)', 'IMS Engineering College (Ghaziabad)', 'P.E.S. College Of Engineering (Mandya)', 'Lakshmi Narain College Of Technology (Bhopal)', 'Sikkim Manipal Institute Of Technology (Sikkim)', 'Ganeshi Lal Bajaj Institute Of Technology & Management (Noida)', 'SCMS School Of Engineering & Technology (Ernakulam)', 'Kongu Engineering College (Erode)', 'K.S.R. College Of Enginnering (Thiruchengode)', 'Maharashtra Institute Of Technology (Aurangabad)', 'Sri Sairam College of Engineering (Bangalore)', 'J.B. Institute Of Technology (Dehradun)', 'Jaipur Engineering College And Research Center (Jaipur)', 'R.M.K. Engineering College (Kavaripettai)', 'S.A. Engineering College (Chennai)', 'University Institute Of Engineering & Technology, Panjab University (Chandigarh)', 'Kuppam Engineering College (Kuppam)', 'Asia Pacific Institute of Information Technology (APIIT SD) (Panipat)', 'Malla Reddy College of Engineering & Technology (Secunderabd)', 'CVR College Of Engineering (Hyderabad)', 'Veltech High Tech Dr .Rangarajan Dr. Sakunthala Engineering College (Chennai)', 'Vishwakarma Institute of Technology (Pune)', 'M.S. Engineering College (Bangalore)', 'R.M.D. Engineering College (Thiruvallur)', 'Rajarambapu Institute Of Technology (Sangli)', 'Shri Vishnu Engineering College For Women (Bhimavaram)', 'Government College Of Engineering (Karad)', 'Institute Of Engineering & Technology, J.K.Lakshmipat University (Jaipur)', 'Shri Shankaracharya Technical Campus Bhilai (Bhilai)', 'IES College Of Technology (Bhopal)', 'Madhav Institute of Technology & Science (Gwalior)', 'KIET Group Of Institutions (Ghaziabad)', "BRACT'S Vishwakarma Institute of Information Technology (Pune)", 'KLS Gogte Institute Of Technology (Belagavi)']

GIRL_NAMES = ['Saanvi', 'Anya', 'Aadhya', 'Aaradhya', 'Ananya', 'Pari', 'Anika', 'Navya', 'Angel', 'Diya', 'Myra', 'Sara', 'Iraa', 'Ahana', 'Anvi', 'Prisha', 'Riya', 'Aarohi', 'Anaya', 'Akshara', 'Eva', 'Shanaya', 'Kyra', 'Siya']

AGENTS = """Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36

Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36

Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko

Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0

Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9

Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4

Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36

Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36

Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240

Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0

Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko

Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36

Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko

Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0

Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12

Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36

Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0

Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/7.1.8 Safari/537.85.17

Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4""".split("\n")

def Rcollege():

  return random.choice(COLLEGES)

def Rgirl():

  return random.choice(GIRL_NAMES)

def Ragent():

  return random.choice(AGENTS)
