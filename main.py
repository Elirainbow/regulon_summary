# Programa regulon_summary que por cada TF obtiene
# TF 	Total de genes regulados 	Lista de genes
# AraC 	2 	araA, araB
# LexA 	1 	recA

# Algoritmo:
# 1. Leer el archivo de texto
# 2. Crear una estructura para almacenar la información de cada TF
# 3. Leer la información de ese TF y almacenar el nombre en

interactions = {
    ("AraC", "araA", "+"),
    ("AraC", "araB", "-"),
    ("LexA", "recA", "-"),
    ("CRP", "lacZ", "+"),
    ("CRP", "lacY", "+"),
}

for tf, gene, effect in interactions:
    print(f"{tf}\t{gene}\t{effect}\n")

# "AraC --> ["araA", "araB"]"
regulon = {}
for tf, gene, effect in interactions:
    if tf not in regulon:
        regulon[tf] = []  # primero se crea la llave con lista vacía
    regulon[tf].append(gene)  # se agrega gene

# Key error: error de llave [primero tiene que crear el key y luego agrega lo que necesita]

# Imprimimos el resumen de cada TF
for tf, genes in regulon.items():
    print(f"{tf}\t{len(genes)}\t{', '.join(genes)}")

for tf in sorted(regulon):
    total_genes = len(regulon[tf])
    lista_genes = ", ".join(regulon[tf])
    print(f"{tf}\t{total_genes}\t{lista_genes}")

# Diccionaro con subdiccionarios para activadores y represores:
# "araC" --> 5

# "araC" --> "genes" --> ["araA", "araB"]
# "araC" --> "activados" --> 1
# "araC" --> "reprimidos" --> 1

regulon = {}
for tf, gene, effect in interactions:
    if tf not in regulon:
        regulon[tf] = {
            "genes": [],
            "activados": 0,
            "reprimidos": 0,
        }  # primero se crea la llave con lista vacía
    regulon[tf]["genes"].append(gene)  # se agrega gene

# Key error: error de llave [primero tiene que crear el key y luego agrega lo que necesita]

# Imprimimos el resumen de cada TF
for tf, genes in regulon.items():
    print(f"{tf}\t{len(genes)}\t{', '.join(genes)}")

for tf in sorted(regulon):
    total_genes = len(regulon[tf]["genes"])
    lista_genes = ", ".join(regulon[tf]["genes"])
    print(f"{tf}\t{total_genes}\t{lista_genes}")
