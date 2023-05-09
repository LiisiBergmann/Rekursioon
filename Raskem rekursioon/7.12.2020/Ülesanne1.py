

def kõikvõimalikud_naturaalarvude_liidetavate_summad(n, kombinatsioon : list):

    if n == 0:
        print(kombinatsioon)
        return 1

    if n < 0:
        return 0

    else:
        return kõikvõimalikud_naturaalarvude_liidetavate_summad(n - 3, kombinatsioon + [3]) + kõikvõimalikud_naturaalarvude_liidetavate_summad(n - 4, kombinatsioon + [4]) + kõikvõimalikud_naturaalarvude_liidetavate_summad(n - 5, kombinatsioon + [5])


kõikvõimalikud_naturaalarvude_liidetavate_summad(10, [])