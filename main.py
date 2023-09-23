import os


def sort_to_dir(extens: str):
    source_directory = 'C:/Users/user/Downloads'
    target_directory = f'C:/Users/user/Desktop/useless/{extens}'

    if extens == 'images':
        image_extensions = ['jpg', 'jpeg', 'png', 'gif', 'jfif', 'webp']
        for item in os.listdir(source_directory):
            if '.' in item:
                ext = item.split('.')[-1]
                if ext in image_extensions:
                    source_path = os.path.join(source_directory, item)
                    target_path = os.path.join(target_directory, item)

                    try:
                        os.replace(source_path, target_path)
                    except Exception as e:
                        print(f"Ошибка при перемещении '{item}': {str(e)}")
    elif extens in ['pptx', 'pdf', 'txt', 'docx', 'torrent']:
        for item in os.listdir(source_directory):
            if '.' in item:
                ext = item.split('.')[-1]
                if ext == extens:
                    source_path = os.path.join(source_directory, item)
                    target_path = os.path.join(target_directory, item)

                    try:
                        os.replace(source_path, target_path)
                    except Exception as e:
                        print(f"Ошибка при перемещении '{item}': {str(e)}")
    else:
        for item in os.listdir(source_directory):

            source_path = os.path.join(source_directory, item)
            target_path = os.path.join(target_directory, item)

            try:
                os.replace(source_path, target_path)
            except Exception as e:
                print(f"Ошибка при перемещении '{item}': {str(e)}")


if __name__ == '__main__':
    sort_to_dir('pdf')
    sort_to_dir('txt')
    sort_to_dir('docx')
    sort_to_dir('pptx')
    sort_to_dir('torrent')
    sort_to_dir('images')
    sort_to_dir('other')
