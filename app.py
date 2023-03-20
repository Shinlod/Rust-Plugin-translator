from flask import Flask, render_template, request, send_file
from json_translator import JSONTranslatorPlugin
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        source_file = request.files['source_file']
        source_file_path = os.path.join(os.getcwd(), 'uploaded_file.json')
        source_file.save(source_file_path)
        
        target_language = request.form['language']
        
        json_translator = JSONTranslatorPlugin(source_file_path)
        translated_data = json_translator.translate_plugin(target_language)
        output_file_path = os.path.join(os.getcwd(), 'translated_file.json')
        json_translator.save_translated_plugin(output_file_path, translated_data)
        
        os.remove(source_file_path)
        
        return send_file(output_file_path, as_attachment=True, download_name='translated_file.json', mimetype='application/json')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
