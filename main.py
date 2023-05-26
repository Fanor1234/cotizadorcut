from flask import Flask, render_template, request
from prompt import get_completion
import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')


app = Flask(__name__)
### open ai api key and function to chatgpt promt 
openai.api_key = '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'

tabla = """
los precios unitarios para los diferentes materiales y espesores son:
para acero inox de 0.8 mm de espesor el precio unitario es 40.00 Bs/m,\
para acero inox de 1.0 mm de espesor el precio unitario es 47.00 Bs/m,\
para acero inox de 1.5 mm de espesor el precio unitario es 54.00 Bs/m,\
para acero inox de 2.0 mm de espesor el precio unitario es 61.00 Bs/m,\
para acero inox de 2.5 mm de espesor el precio unitario es 68.00 Bs/m,\
para acero inox de 3.0 mm de espesor el precio unitario es 80.00 Bs/m,\
para acero inox de 5.0 mm de espesor el precio unitario es 100.00 Bs/m,\
para acero inox de 6.0 mm de espesor el precio unitario es 160.00 Bs/m,\
para acero dulce de 0.8 mm de espesor el precio unitario es 20.00 Bs/m,\
para acero dulce de 1.0 mm de espesor el precio unitario es 26.00 Bs/m,\
para acero dulce de 1.5 mm de espesor el precio unitario es 30.00 Bs/m,\
para acero dulce de 2.0 mm de espesor el precio unitario es 36.00 Bs/m,\
para acero dulce de 2.5 mm de espesor el precio unitario es 37.00 Bs/m,\
para acero dulce de 3.0 mm de espesor el precio unitario es 41.00 Bs/m,\
para acero dulce de 5.0 mm de espesor el precio unitario es 52.00 Bs/m,\
para acero dulce de 6.0 mm de espesor el precio unitario es 80.00 Bs/m,\
para acero dulce de 8.0 mm de espesor el precio unitario es 120.00 Bs/m,\
para acero dulce de 10.0 mm de espesor el precio unitario es 135.00 Bs/m,\
"""
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.form['material']:
        material = request.form['material']
        espesor = request.form['espesor']
        longitud = request.form['longitud']
        
        prompt = f"""
                determina el precio unitario de la tabla,\
                {material},\
                para un espesor de {espesor},\
                ese precio unitario multiplicalo por {longitud} y muestra el valor,\
                solo necesito el resultado del valor,\
                la cual esta delimitada por triple backticks.\
                si el valor no existe en la tabla, escribe que no existe el valor.\
                muestra de texto: '''{tabla}'''
                """
        response = get_completion(prompt)

        return render_template('index.html', response = response)
    
    else:
        return render_template('index.html')

@app.route('/prueba', methods = ['GET','POST'])
def prueba():
    pepo = "mani manito es mi amigo pero lo que ha hecho esta mal"
    marcus = "no hay nada brother"
    get = "get ok"

    if request.method == 'GET':
        return render_template('indexp.html', get = get)
    
    if request.form['question']:
        return render_template('indexp.html', pepo = pepo)
    
    else:
        return render_template('indexp.html', marcus = marcus)


if __name__ == '__main__':
    app.run(debug=True, port=4000)

