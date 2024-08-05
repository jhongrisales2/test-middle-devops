import datetime
import random

vecNombres = ["Santiago","Monica","Mariana","Jaime","Gabriel","Miguel","Juan","Elkin","Juanita","Silvia","Leonor","Miguel","Manuela","Hans","Jose",
            "Mauricio","Guillermo","Diana","Melissa","Camila","Juliana","Valentina","Laura","Sebastian","Maria","Isabela","Daniela","Lorena",
            "Lorenzo","Camilo","Eliana","Elizabeth","Martin","Jairon","Amparo","Jorge","Adriana","Oscar","Kim","Tatiana","Kelly","Doris","Ana"]

vecApellidos = ["Mercedee","Sosa","Garcia","Arango","Ortega","Molina","Smith","Saldarriaga","Gutierrez","Palacio","Medina","Gomez","Arango","Diaz",
            "Hill","Donadio","Copello","Rendon","Ruiz","Guerra","Perico","Hernandez","Lopez","Giraldo","Echeverry","Dominguez","Murillo","Sol",
            "Upegui","Bustamante","Ramirez","Castanno","Posada","Alvarez","Madrir","Restrepo","Areiza","Blandon","Perez","Correa","Mendez",
            "Isaza","Renteria","Rodas","Barrreneche","Berrio","Castro","Castellano","Ceballos","Toretto","Toricelli","Idarra","Zapata","Yepes",
            "Villamil","Contreras","Arauco","Beltran","Rios","Velazques","Llano","Escobar","Cardenas","Bonaparte","Wolf","Padilla","Mendoza"]

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    DateFlask_VAR = datetime.datetime.now().strftime( "%d %B %Y (%I:%M%p) " )
    AmountNames_VAR = random.randint(5,15)
    VecNames_VAR = []
    for _ in range(AmountNames_VAR):
        VecNames_VAR.append( random.choice(vecNombres) + " " + random.choice(vecApellidos) + " " 
                          + random.choice(vecApellidos) + "." )

    return( render_template("index_names.html", DATE_FLASK_VAR=DateFlask_VAR, AMOUNT_NAMES_VAR=AmountNames_VAR, VEC_NAMES_VAR=VecNames_VAR) )

if(__name__) == '__main__':
    app.run(host="0.0.0.0",port=5500,debug=True)
