import web
from web import form
from lineCount import *

render = web.template.render('templates/')
urls = ('/(.*)', 'Index')
app = web.application(urls,globals())
web.config.debug = True

class Index:
	sylCount = [0,0,0]
	status =  "Haiku"
	haiku = ["","",""]
	def __init__(self):
		self.haikuForm = form.Form(
			form.Textbox("firstLine", description="5:", value="This is a haiku", class_="entry-line eleven columns"),
			form.Textbox("secondLine", description="7:", value="Enter your haiku right here", class_="entry-line eleven columns"),
			form.Textbox("thirdLine", description="5:", value="This one kind of sucks", class_="entry-line eleven columns"),
			form.Button("Submit", type="submit", description="btnSubmit", class_="button-primary eleven columns")
		)
		self.twitterSubmit = form.Form(
			form.Button("Tweet", type="submit", description="btnSubmit", class_="button-primary eleven columns")
		)
	def GET(self,urls):
		self.sylCount = [0,0,0]
		form = self.haikuForm()
		return render.index(form, self.sylCount, self.status, self.haiku)

	def POST(self,urls):
		form = self.haikuForm()
		
		if not form.validates(): 
			self.status = "Confusion"
			return render.index(form, self.sylCount, self.status, self.haiku)
		else:
			self.sylCount = lineSubmission(form.d.firstLine,form.d.secondLine,form.d.thirdLine)
			if self.sylCount != [5,7,5]:
				self.status = "Confusion"
				return render.index(form, self.sylCount, self.status, self.haiku)
			else:
				self.status = "Zen"
				self.haiku = [form.d.firstLine,form.d.secondLine,form.d.thirdLine]
				form = self.twitterSubmit
				return render.index(form, self.sylCount, self.status, self.haiku)

if __name__=='__main__':
	app.run()

