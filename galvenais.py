from spele import VarduSpelesKlase
from datu_apstrade import ieladet_pareizos_vardus, ieladet_burtus

def izvadit_info(burti):
    print("Laipni lūdzam spēlē 'Uzmini Vārdu'!")
    print("Tev doti burti: " + ", ".join(burti))
    print("Ievadi vārdus, ko iespējams izveidot no šiem burtiem.")
    print("Ieraksti 'iziet', lai beigtu spēli.\n")

def spelet():
    pareizie_vardi = ieladet_pareizos_vardus()
    burti = ieladet_burtus()
    spele = VarduSpelesKlase(pareizie_vardi, burti)

    izvadit_info(burti)

    while True:
        vards = input("Ievadi vārdu: ").lower()

        if vards == "iziet":
            print("Spēle pārtraukta.")
            break

        if spele.minet_vardu(vards):
            print("Pareizi!")
        else:
            print("Nepareizi vai jau minēts.")

        mineti, kopa = spele.iegut_statistiku()
        print(f"Minētie vārdi: {mineti}/{kopa}\n")

        if spele.ir_visi_atmineti():
            print("Tu atminēji visus iespējamos vārdus!")
            break

if _name_ == "_main_":
    spelet()
