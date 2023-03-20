import json
from googletrans import Translator

class JSONTranslatorPlugin:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def translate_plugin(self, target_language):
        translated_data = {}

        with open(self.input_file_path, 'r', encoding='utf-8') as input_file:
            data = json.load(input_file)

        translator = Translator()
        for key, value in data.items():
            try:
                response = translator.translate(value, dest=target_language)
                if response is not None:
                    translated_value = response.text
                    translated_data[key] = translated_value
                else:
                    print(f"Erro ao traduzir {key}: resposta inesperada da API")
                    translated_data[key] = value
            except Exception as e:
                print(f"Erro ao traduzir {key}: {e}")
                translated_data[key] = value

        return translated_data

    def save_translated_plugin(self, output_file_path, translated_data):
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            json.dump(translated_data, output_file, ensure_ascii=False, indent=4)
