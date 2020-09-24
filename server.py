from flask import Flask, render_template,url_for, request,redirect
app = Flask(__name__)
import csv

@app.route('/')
def my_web():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)



def write_to_file(data):
	with open("database.txt",mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file  = database.write(f'{email} , {subject}, {message}')



def write_to_csv(data):
	with open("database.csv",newline='', mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2,delimiter=",",quotechar=";",quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])






@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
	if request.method == 'POST':
		try:
		  data = request.form.to_dict()
		  write_to_csv(data)
		  write_to_file(data)
		  return 'SOMTHING WRONG!'
		except:
			return redirect('/thankyou.html')
	else:
		return '''SOMTHING WRONG
		TRY AGAIN!'''






if __name__=='__main__':
    app.run(debug=True)