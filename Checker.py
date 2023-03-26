import re
import os


class CheckerTagi18n():
    """
    Класс CheckerTagi18n используется для проверки html файлов на отсутствие метки "i18n"
    В качестве параметра для инициализации принимает список тегов для проверки
    Defaul tags: 'p', 'button', 'h2', 'h'
    """

    __tags = ['p', 'button', 'h2', 'h']
    re_string = "<(h2|h|p|button)(\s.*?(>)|(>))"

    __errors = []


    def __init__(self, tags: list = __tags) -> None:
        self.__tags = tags
        self.re_string = f"<({'|'.join(tags)})(\s.*?(>)|(>))"

    def check_tags(self, string):
        """
        В данном методе реализлвана проверка
        тега на наличие метки i18n
        В случае отсутствия метки i18n хотя бы в 1 html-теге возращает False и тег с ошибкой
        """

        results = re.finditer(self.re_string,  string, flags=re.M)

        for res in list(results):
            if 'i18n' not in res.group(0):
                return False, res.group(0)
        return True, None

    def check_file(self, file_path) -> list():
        """
        Метод для проверки всего файла на наличие ошибок
        Добавляет ошибки в self.__errors
        Возвращает список кортежей с ошибками:
        [(Путь к файлу, номер_строки_с_ошибкой, тег_с_ошибкой)...]
        """
        file_errors = []
        with open(file_path, 'r') as file:
            file_lines = file.readlines()

        for line_number, line in enumerate(file_lines):
            status, tag = self.check_tags(line)
            if not status:
                file_errors.append((file_path, line_number+1, tag))
                self.__errors.append((file_path, line_number+1, tag))

        return file_errors



    def read_folder(self, folder_path) -> list:
        """
        В данном методе мы получаем путь ко всем файлам с расширением .html в папке и подпапкаx
        """
        files_list = []

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.html'):
                    files_list.append(os.path.join(root, file))

        return files_list
    

    def check_project(self, project_folder):
        """
        Метод проверки всех html файлов в указанной папке
        """
        files = self.read_folder(project_folder)
        for file in files:
            self.check_file(file)



    def write_errors_file(self) -> None:
        """Метод записи найденых ошибок в файл"""
        if self.__errors:
            with open('errors_report.txt', 'w') as file:
                file.write(f"file_path\terror_line\ttag_with_error\n")
                for error in self.__errors:
                    tabulation = '\t'
                    file.writelines(
                        f"{tabulation.join([str(x) for x in error])}\n"
                    )


    def reset_errors(self) -> None:
        """
        Метод очистки списка ошибок
        """
        self.__errors = []