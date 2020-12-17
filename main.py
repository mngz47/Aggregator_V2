

import articles
import post
import share
import time
from flask import Flask, render_template, redirect, url_for, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)
#app.config.from_object(__name__)
#app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
    
class main(Form):
    
    def startScrape(self):
        cc =  articles(CATEGORIES)   
        cc.findCategories()
        cc.findArticles()
        for aa in cc.articles:
            time.sleep(10)
            #store request and process it number of days
            #post-share 4 articles per day depending on database index
            pp = post()
            flash(pp.send(cc.getArticleBody(aa)[0],'<a href='+AFFLINK+' ><img src="'+BANNER+'" /></a><br><br>'+cc.getArticleBody(aa)[1]+
            '<br><br><iframe width="640" height="360" src="'+VIDEO+'" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',CATEGORIES))
            ss = share()
            flash(ss.send(cc.getArticleBody(aa)[0],cc.getArticleBody(aa)[1].substring(0,40),aa))
    
    
    @app.route("/getForm", methods=['GET', 'POST'])       
    def getForm(self):
        form = main(request.form)
        print form.errors
        if request.method == 'POST':
        if form.validate():
            
            CATEGORIES=request.form['categories']
            AFFLINK=request.form['afflink']
            BANNER=request.form['banner']
            VIDEO=request.form['video']
            startScrape()
        else:
            flash('All the form fields are required. ')
    
    CATEGORIES = TextField('Categories:', validators=[validators.required()])
    AFFLINK = TextField('AffLink:', validators=[validators.required()])
    BANNER = TextField('Banner:', validators=[validators.required()])
    VIDEO = TextField('Video:', validators=[validators.required()])
    
    return render_template('index.html', form=form)
        
if __name__ == "__main__":
    app.run()
