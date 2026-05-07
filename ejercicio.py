import os

# =======================================================
# Lectura del archivo y construcción de interactions
# Entrada: Archivo
# Salida: Lista de interacciones (TF, gene, effect)
# # =====================================================


interactions = []

filename = "data/raw/NetworkRegulatorGene.tsv"

if not os.path.exists(filename):
    print("Error: archivo no encontrado")
    exit(1)
else:
    with open(filename) as f:

        for line in f:

            line = line.strip()

            print(f"Leído: {line[:50]}...")

            # Ignorar líneas vacías
            if not line:
                continue

            # Ignorar comentarios
            if line.startswith("#"):
                continue

            # Ignorar encabezado
            if line.startswith("1)regulatorId"):
                continue

            fields = line.split("\t")

            # Validar número mínimo de columnas
            if len(fields) <= 6:
                continue

            # columnas a utilizar
            TF = fields[1]
            gene = fields[2]
            effect = fields[5]

            # Validar effect
            if effect not in ["+", "-", "-+"]:
                continue

            interactions.append((TF, gene, effect))

print(interactions)

# =====================================================
# Construcción del regulon
# Entrada: Lista de interaccciones (TF, gene, effect)
# Salida: Diccionario regulon con la estructura
# =====================================================

regulon = {}  # diccionario con lista de genes
for tf, gene, effect in interactions:
    if tf not in regulon:
        regulon[tf] = {"genes": [], "activados": 0, "reprimidos": 0}
    regulon[tf]["genes"].append(gene)

    # COntar los activados y reprimidos
    if effect == "+":
        regulon[tf]["activados"] += 1
    elif effect == "-":
        regulon[tf]["reprimidos"] += 1
    elif effect == "-+":
        regulon[tf]["activados"] += 1
        regulon[tf]["reprimidos"] += 1

# AraC{
#    "genes" : ["araC, araA, araB, araD"],
#   "activados" : 3,
#   "reprimidos" : 0
# }

# =====================================================
# Generación de la salida
# imprimimos el resumen de cada TF
# Entrada: Diccionario regulon con la estructura:
# Salida: archivo .tsv
# =====================================================
output_filename = "regulon_summary.tsv"
with open(output_filename, "w") as f:
    f.write(
        "TF\tTotal de genes regulados\tLista de genes\tActivados\tReprimidos\tTipo TF\tLista"
    )
    for tf in sorted(regulon):
        total_genes = len(regulon[tf]["genes"])
        lista_genes = ",".join(regulon[tf]["genes"])
        activados = regulon[tf]["activados"]
        reprimidos = regulon[tf]["reprimidos"]

        # Determinamos si el TF es activador, represor o dual
        if activados > 0 and reprimidos == 0:
            tipo_tf = "Activador"
        elif activados == 0 and reprimidos > 0:
            tipo_tf = "Represor"
        elif activados > 0 and reprimidos > 0:
            tipo_tf = "Dual"

        f.write(
            f"{tf}\t{total_genes}\t{activados}\t{reprimidos}\t{tipo_tf}\t{lista_genes}"
        )
print(f"Archivo de salida generado: {output_filename}")
