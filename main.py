from Checker import CheckerTagi18n


if __name__ == '__main__':

    checker = CheckerTagi18n()

    checker.check_project('project_path')
    checker.write_errors_file()


    