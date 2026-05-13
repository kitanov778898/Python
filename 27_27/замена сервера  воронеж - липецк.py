import os
import shutil

def create_backup(file_path):
    """
    Функция для создания резервной копии файла.
    """
    backup_path = file_path + ".bak"
    try:
        # Копируем файл в резервную копию
        shutil.copyfile(file_path, backup_path)
        print(f"Резервная копия создана: {backup_path}")
    except Exception as e:
        print(f"Ошибка при создании резервной копии: {e}")
    return backup_path


def replace_text_in_file(file_path, old_text, new_text):
    """
    Функция для поиска и замены текста в файле.
    """
    try:
        # Открываем файл для чтения
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Проверяем, содержится ли старый текст в файле
        if old_text in content:
            # Заменяем старый текст на новый
            updated_content = content.replace(old_text, new_text)

            # Сохраняем изменения в тот же файл
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)

            print(f"Замена выполнена успешно в файле: {file_path}")
        else:
            print(f"Текст для замены не найден в файле: {file_path}")

    except Exception as e:
        print(f"Произошла ошибка при обработке файла {file_path}: {e}")


# Определяем старый и новый текст
old_text = '''<databaseName Type="QString">lims_server</databaseName>
          <userName Type="QString">report</userName>
          <password Type="QString" Value="NqWi6z+oAbjELx7IIkX89Q=="/>
          <host Type="QString">10.36.0.61</host>'''

new_text = '''<databaseName Type="QString">lims_server</databaseName>
          <userName Type="QString">report</userName>
          <password Value="7y3B01LjQ3Q=" Type="QString"/>
          <host Type="QString">10.148.10.110</host>'''

# Указываем путь к файлу (или каталогу с файлами .lrxml)
file_path = "example.lrxml"  # Укажите путь к вашему файлу

# Проверяем, существует ли файл
if os.path.exists(file_path):
    # Создаем резервную копию
    create_backup(file_path)
    
    # Выполняем замену текста
    replace_text_in_file(file_path, old_text, new_text)
else:
    print(f"Файл не найден: {file_path}")
