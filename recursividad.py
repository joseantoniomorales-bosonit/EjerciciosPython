def recursiva1(old_list, new_list, last_id = None, last_parent = None):
    if len(old_list) <= 0:
        return new_list

    element = old_list.pop(0)

    if last_parent is not element["parent"]:
        if last_id == element["parent"]:
            print(f"Primer hijo: {element}")
            if "children" not in new_list[-1]:
                new_list[-1]["childrens"] = []

            new_list[-1]["childrens"].append(element)
        else:
            print(f"Nuevo parent: {element}")
            new_list.append(element)
    else:
        if len(new_list)>0:
            new_list[-1]["childrens"].append(element)
        else:
            print(f"Mismo nivel de parent: {element}")
            new_list.append(element)

    return recursiva1(old_list, new_list, element["id"], element["parent"])

def recursiva2(old_list, new_list, last_id = None, last_parent = None):
    if len(old_list) <= 0:
        return new_list

    element = old_list.pop(0)

    if last_parent is not element["parent"]:
        if last_id == element["parent"]:
            # print(f"Primer hijo: {element}")
            if "children" not in new_list[-1]:
                new_list[-1]["childrens"] = []

            if last_parent is not None:
                print("Tiene otro nodo como padre")
                new_list[-1]["childrens"].extend(recursiva2(old_list, [], element["id"], element["parent"]))
            else:
                new_list[-1]["childrens"].append(element)
                print(f"Nueva lista: {new_list}")
        else:
            print(f"Nuevo parent: {element}")
            new_list.append(element)
    else:
        new_list.append(element)

    return recursiva2(old_list, new_list, element["id"], element["parent"])


def recursiva3(old_list, new_list, last_id = None, last_parent = None):
    if len(old_list) <= 0:
        return new_list

    element = old_list.pop(0)

    if last_parent is not element["parent"]:
        if last_id == element["parent"]:
            # print(f"Primer hijo: {element}")
            if "children" not in new_list[-1]:
                new_list[-1]["childrens"] = []

            if last_parent is not None:
                print("Tiene otro nodo como padre")
                new_list[-1]["childrens"] = recursiva3(old_list, new_list[-1], element["id"], element["parent"])
            else:
                new_list[-1]["childrens"].append(element)
                print(f"Nueva lista: {new_list}")
        else:
            print(f"Nuevo parent: {element}")
            # print(new_list[-1])
            new_list.append(element)
    else:
        # print(new_list)
        # if len(new_list)>0:
        #     # print(f"Mismo nivel de parent: {element}")
        #     new_list[-1]["childrens"].append(element)
        # else:
        #     # print(f"Mismo nivel de parent: {element}")
        new_list.append(element)

    return recursiva3(old_list, new_list, element["id"], element["parent"])

def recursiva4(old_list, new_list,  last_id = None, last_parent = None):
    if len(old_list) <= 0:
        return new_list

    element = old_list.pop(0)

    # Hay un cambio de padre
    if not last_parent == element["parent"]:
        print(f"El padre anterior es distinto al actual [ID: {element.get('id')}]")
        if last_id == element["parent"]:
            if "children" not in new_list[-1]:
                new_list[-1]["childrens"] = []

            print("\tEl elemento anterior es padre del actual")
            new_list[-1]["childrens"].extend(recursiva4(old_list, [], element["id"], element["parent"]))
            # return recursiva4(old_list, new_list, element["id"], element["parent"])
        else:
            print("\tEl elemento anterior es hermano del actual")
            # return recursiva4(old_list, new_list, element["id"], element["parent"])
    else:
        print(f"Tiene el mismo padre [ID: {element.get('id')}]")
        # print(new_list)
        # new_list[-1]["childrens"] = recursiva4(old_list, new_list[-1], element["id"], element["parent"])

    new_list.append(element)
    return recursiva4(old_list, new_list, element["id"], element["parent"])


lista_nodos = [
    {"id": 1, "name": "nodo1", "path": "nodo1", "parent": None},
    {"id": 2, "name": "subnodo1", "path": "nodo1/subnodo1", "parent": 1},
    {"id": 3, "name": "subnodo2", "path": "nodo1/subnodo2","parent": 1},
    {"id": 4, "name": "nodo2", "path": "/nodo2", "parent": None},
    {"id": 5, "name": "subnodo3", "path": "/nodo2/subnodo3", "parent": 4},
    {"id": 6, "name": "subnodo4", "path": "/nodo2/subnodo4", "parent": 4},
    {"id": 7, "name": "subnodo5", "path": "/nodo2/subnodo5", "parent": 4},
    {"id": 8, "name": "subnodo6", "path": "/nodo2/subnodo6", "parent": 4},
    {"id": 9, "name": "nodo3", "path": "nodo3/", "parent": None},
    {"id": 10, "name": "subnodo7", "path": "nodo3/subnodo7", "parent": 9},
    {"id": 11, "name": "subnodo7", "path": "nodo3/subnodo7", "parent": 9},
    {"id": 12, "name": "subnodo8", "path": "nodo3/subnodo8", "parent": 9},
    {"id": 13, "name": "subnodo9", "path": "nodo3/subnodo9", "parent": 9},
    {"id": 14, "name": "subnodo10", "path": "nodo3/subnodo10", "parent": 9},
    {"id": 15, "name": "subnodo11", "path": "nodo3/subnodo11", "parent": 9},
    {"id": 16, "name": "subnodo12", "path": "nodo3/subnodo12", "parent": 9},
    {"id": 17, "name": "subsubnodo1", "path": "nodo3/subnodo12/subsubnodo1", "parent": 16},
    {"id": 18, "name": "subsubnodo2", "path": "nodo3/subnodo12/subsubnodo2", "parent": 16},
    {"id": 19, "name": "subsubnodo3", "path": "nodo3/subnodo12/subsubnodo3", "parent": 16},
    {"id": 20, "name": "subsubnodo4", "path": "nodo3/subnodo12/subsubnodo4", "parent": 16},
    {"id": 21, "name": "subsubnodo5", "path": "nodo3/subnodo12/subsubnodo5", "parent": 16},
    {"id": 22, "name": "subsubnodo6", "path": "nodo3/subnodo12/subsubnodo6", "parent": 16}
]
lista = recursiva4(lista_nodos, [])
print("-------------------------------")
print("lista final")
for l in lista:
    print(l)