import ipaddress

# Liste des sous-réseaux (extraits du tableau)
subnets = [
    "172.16.105.96/29", "172.16.105.0/26", "172.16.104.0/25", "172.16.104.128/25", "172.16.105.64/27",
    "172.16.68.96/28", "172.16.68.64/27", "172.16.64.0/23", "172.16.66.0/23", "172.16.68.0/26",
    "172.16.9.128/28", "172.16.9.0/25", "172.16.4.0/22", "172.16.0.0/22", "172.16.8.0/24",
    "172.16.102.128/27", "172.16.102.64/26", "172.16.100.0/23", "172.16.96.0/22", "172.16.102.0/26"
]

# Création des objets IPv4Network
networks = [ipaddress.ip_network(s) for s in subnets]

# Affichage des réseaux analysés
print("Réseaux analysés :")
for net in networks:
    print(f" - {net}")
print("\nVérification des chevauchements...\n")

# Vérification de chevauchements
overlap_found = False
for i in range(len(networks)):
    for j in range(i + 1, len(networks)):
        if networks[i].overlaps(networks[j]):
            print(f"❌ Chevauchement détecté entre {networks[i]} et {networks[j]}")
            overlap_found = True

if not overlap_found:
    print("✅ Aucun chevauchement détecté entre les réseaux IP.")

