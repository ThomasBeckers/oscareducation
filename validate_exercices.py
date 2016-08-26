# encoding: utf-8

import os
import sys
import yaml

from examinations.utils import validate_exercice_yaml_structure

def main():
    failed = False

    for yaml_file in filter(lambda x: x.endswith(".yaml"), os.listdir("exercices")):
        try:
            exercice = yaml.safe_load(open(os.path.join("exercices", yaml_file)))
        except Exception as e:
            print "Erreur: impossible de charger 'exercice/%s' car la syntaxe yaml n'est pas respectée: %s" % (yaml_file, e)
            failed = True
            continue

        if not validate_exercice_yaml_structure("exercices/" + yaml_file, exercice):
            failed = True

    if not failed:
        print "All checks passed."
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
