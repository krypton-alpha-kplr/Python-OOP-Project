'''
- Nous allons a présent charger de nouvelles données,
- prenez le temps de lire ATTENTIVEMENT le contenu du nouveau fichier json_data
- En utilisant le code précédemment réalisé, générez un arbre qui en affiche le contenu
- Attention : N'afficher que les Noeuds possédant des sous-classes
- Autrement dit, il ne faut pas inclure les attributs des Produits, mais seulement les catégories de produit.
- Pour ce faire, il ne faut inclure que les noeuds qui ne sont pas terminaux
- Les noeuds sans enfants doivent être skippés.

- voici le Pseudo code pour vous aider à rédiger le code.

'''
# Import des modules nécessaires
import json
from unidecode import unidecode
from treelib import Tree
import os

# Fonction pour charger les données JSON depuis un fichier et les convertir en dictionnaire Python
def json_dict_from_file():
    # Get the directory path of the current Python file
    local_path = os.path.dirname(os.path.abspath(__file__))
    print("Chemin : ",local_p)

    # Chargement des données JSON à partir du fichier dans un dictionnaire python
    json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
    
    # il est nécessaire de reconvertir le dictionnaire en chaine de caractère pour le traiter ensuite
    json_str = json.dumps(json_data)

    # Utilisation de la fonction unidecode pour enlever les accents et autres caractères spéciaux
    json_data = (unidecode(json_str))

    # Conversion de la chaine de caractere JSON à nouveau en dictionnaire Python
    # Le dictionnaire python est plus pratique à manipuler que la chaine de caractère car il est structuré
    json_dict = json.loads(json_data)

    return json_dict

def create_tree_from_dict(tree, parent_node_id, parent_dict):
    for key, value in parent_dict.items():
        if isinstance(value, dict): # test si valeur est de TYPE dictionnaire
            # Créer un nouveau noeud pour la clé courante du dictionnaire

            new_node_id = f"{parent_node_id}.{key}"
#            if value(f"{new_node_id}.{key}")=="subclasses" :
#                new_node_id = f"{new_node_id}.{key}"
            tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)

            # Créer récursivement le sous-arbre pour le dictionnaire courant
            create_tree_from_dict(tree, new_node_id, value)

#            S’il n’existe pas d’enfants, => pas de Nœud parent
#            if (f"{parent_node_id}.{key}"== new_node_id ) & (f"{new_node_id}.{key}" is None ) :
#                continue
#            f"{new_node_id}.{key}" =None

        else:
            # Créer un nouveau noeud pour la feuille courante du dictionnaire
            leaf_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=f"{key}: {value}", identifier=leaf_node_id, parent=parent_node_id)

"""
        Si "subclasses" est dans les attributs de la classe en cours (soit : valeur(class_attrs))
            Appeler récursivement la fonction pour créer les sous-noeuds de ce dictionnaire
"""


def main() :
#    Charger les données JSON depuis un fichier et créer la structure de l'arbre à partir du dictionnaire
    json_dict=json_dict_from_file()
# Créer un nouvel arbre (à partir du dictionnaire Python)
    my_tree = Tree()

# Créer le noeud racine pour l'arbre
    my_tree.create_node(tag="Racine", identifier="racine")

# Créer la structure de l'arbre à partir du dictionnaire Python
    create_tree_from_dict(my_tree, "racine", json_dict)

#    Afficher l'arbre de classes
    my_tree.show()

# imprimons a présent le dictionnaire
    print(json.dumps(json_dict, indent=4))

############# Code principal #########
if __name__ == '__main__':
#    Appeler la fonction principale
    main()
