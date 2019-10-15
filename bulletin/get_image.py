import parser_lib, os

def download_image(image_link, avito_item_number):
    image_name_index = 0
    image_lib = image_link
    image_name = avito_item_number

    path = avito_item_number
    try:
        os.mkdir(path)
    except OSError:
        print ("Создать директорию %s не удалось" % path)
    else:
        print ("Успешно создана директория %s " % path)

    for link in image_lib:
        image_name = image_name + str(image_name_index)
        parser_lib.load_image(link, image_name, path)
        image_name_index += 1