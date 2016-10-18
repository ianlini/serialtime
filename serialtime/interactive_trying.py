import traceback


def try_load_yaml(yaml_path):
    try:
        import yaml
    except ImportError:
        raise ImportError("This function requires yaml module. "
                          "You can install it via "
                          "\"pip install PyYAML\".")

    while True:
        try:
            with open(yaml_path) as fp:
                data = yaml.load(fp)
            break
        except:  # pylint: disable=W0702
            traceback.print_exc()
            # reload or go into ipdb if there's error
            while True:
                is_try_again = input("Error while loading schedule.yml, "
                                     "try again ([y]/n)? ")
                if is_try_again == "n":
                    raise
                elif is_try_again == "y" or is_try_again == "":
                    break
    return data
