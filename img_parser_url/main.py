import requests 

urls = [
    'https://ugol.me/u//upload/material/image/27/555/_10753-2-5_ZUBR_PreView_1.jpg',
    'https://ugol.me/u//upload/material/image/18/348/_NATURE-156G_IMOLA_4NATURE_PreView_1.jpg',
    'https://ugol.me/u//upload/material/image/18/389/_OLMO-1512_LA-FAENZA_LE-ESSENZE_PreView_1.jpg',
    'https://ugol.me/u//upload/material/image/18/428/_BW0TNR07_ALTACERA_OCEAN_PreView_1.jpg',
    'https://ugol.me/u//upload/material/image/18/46/4690379007241__COLISEUMGRES'
    '_%D0%A1%D0%98%D0%A6%D0%98%D0%9B%D0%98%D0%AF_PreView_1.jpg'
]


def get_file(url):
    """ Get file from response """
    r = requests.get(url, stream=True)
    return r


def get_name(url):
    """ Calling name of file """
    name = url.split('/')[-1]
    return name


def save_image(name, file_object):
    """ Save each image """
    with open(name, 'bw') as f:
        for chunk in file_object.iter_content(8192):
            f.write(chunk)


def main():
    
    for url in urls:
        save_image(get_name(url), get_file(url))


if __name__ == '__main__':
    main()