

import articles
import post
import share
import time
from flask import Flask, render_template, redirect, url_for, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)
    
class main:
    
    def __init__(self,Form):
        return Form
        
        
    CATEGORIES = TextField('Categories:', validators=[validators.required()])
    AFFLINK = TextField('AffLink:', validators=[validators.required()])
    BANNER = TextField('Banner:', validators=[validators.required()])
    VIDEO = TextField('Video:', validators=[validators.required()])
    
    def startScrape(self):
        cc =  articles(CATEGORIES)   
        cc.findCategories()
        cc.findArticles()
        for aa in cc.articles:
            time.sleep(2)
            #store request and process it number of days
            #post-share 4 articles per day depending on database index
            articlebody = cc.getArticleBody(aa)[1]
            if articlebody.len()>1500:
                articletitle = cc.getArticleBody(aa)[0]    
                pp = post()
                flash(pp.send(articletitle,'<a href='+AFFLINK+' ><img src="'+BANNER+'" /></a><br><br>'+articlebody+
                '<br><br><iframe width="640" height="360" src="'+VIDEO+'" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',CATEGORIES))
                ss = share()
                flash(ss.send(articletitle,articlebody.substring(0,40),aa))
    
    @app.route("/fff")
    def index():
         return "Flask App!"
    
    @app.route("/", methods=['GET', 'POST'])       
    def getForm(self):
        form = main(self.request.form)
        print(form.errors)
        if request.method == 'POST':
          if form.validate():
            CATEGORIES=request.form['categories']
            AFFLINK=request.form['afflink']
            BANNER=request.form['banner']
            VIDEO=request.form['video']
            startScrape()
          else:
            flash('All the form fields are required. ')
        return render_template('index.html', form=form)
         
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
