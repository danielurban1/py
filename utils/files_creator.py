class FilesCreator(object):

    @staticmethod
    def create_txt_file(self, file_name, texts_list):
        with open("copy.txt", "w") as file:
            for text in texts_list:
                file.write(text)



