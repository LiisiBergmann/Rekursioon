def arva(m):


    võlusõna_arvamine = input("Miks see programmerimine nii raske on? ")
    if võlusõna_arvamine == m:
        print("Ära arvasid")

    else:

        print("Aga miks?")
        arva(m)

arva("sestniion")