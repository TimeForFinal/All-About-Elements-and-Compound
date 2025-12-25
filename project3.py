import matplotlib.pyplot as plt

elements = {
    (1, 1): "H", (18, 1): "He",
    (1, 2): "Li", (2, 2): "Be", (13, 2): "B", (14, 2): "C", (15, 2): "N", (16, 2): "O", (17, 2): "F", (18, 2): "Ne",
    (1, 3): "Na", (2, 3): "Mg", (13, 3): "Al", (14, 3): "Si", (15, 3): "P", (16, 3): "S", (17, 3): "Cl", (18, 3): "Ar",
    (1, 4): "K", (2, 4): "Ca", (3, 4): "Sc", (4, 4): "Ti", (5, 4): "V", (6, 4): "Cr", (7, 4): "Mn", (8, 4): "Fe", (9, 4): "Co", (10, 4): "Ni", (11, 4): "Cu", (12, 4): "Zn", (13, 4): "Ga", (14, 4): "Ge", (15, 4): "As", (16, 4): "Se", (17, 4): "Br", (18, 4): "Kr",
    (1, 5): "Rb", (2, 5): "Sr", (3, 5): "Y", (4, 5): "Zr", (5, 5): "Nb", (6, 5): "Mo", (7, 5): "Tc", (8, 5): "Ru", (9, 5): "Rh", (10, 5): "Pd", (11, 5): "Ag", (12, 5): "Cd", (13, 5): "In", (14, 5): "Sn", (15, 5): "Sb", (16, 5): "Te", (17, 5): "I", (18, 5): "Xe",
    (1, 6): "Cs", (2, 6): "Ba", (3, 6): "57-71", (4, 6): "Hf", (5, 6): "Ta", (6, 6): "W", (7, 6): "Re", (8, 6): "Os", (9, 6): "Ir", (10, 6): "Pt", (11, 6): "Au", (12, 6): "Hg", (13, 6): "Tl", (14, 6): "Pb", (15, 6): "Bi", (16, 6): "Po", (17, 6): "At", (18, 6): "Rn",
    (1, 7): "Fr", (2, 7): "Ra", (3, 7): "89-103", (4, 7): "Rf", (5, 7): "Db", (6, 7): "Sg", (7, 7): "Bh", (8, 7): "Hs", (9, 7): "Mt", (10, 7): "Ds", (11, 7): "Rg", (12, 7): "Cn", (13, 7): "Nh", (14, 7): "Fl", (15, 7): "Mc", (16, 7): "Lv", (17, 7): "Ts", (18, 7): "Og",
    (3, 8): "6", (4, 8): "La", (5, 8): "Ce", (6, 8): "Pr", (7, 8): "Nd", (8, 8): "Pm", (9, 8): "Sm", (10, 8): "Eu", (11, 8): "Gd", (12, 8): "Tb", (13, 8): "Dy", (14, 8): "Ho", (15, 8): "Er", (16, 8): "Tm", (17, 8): "Yb", (18, 8): "Lu",
    (3, 9): "7", (4, 9): "Ac", (5, 9): "Th", (6, 9): "Pa", (7, 9): "U", (8, 9): "Np", (9, 9): "Pu", (10, 9): "Am", (11, 9): "Cm", (12, 9): "Bk", (13, 9): "Cf", (14, 9): "Es", (15, 9): "Fm", (16, 9): "Md", (17, 9): "No", (18, 9): "Lr"
}

def plot_periodic_table(elements_diction):
    """Plot a simple periodic table using matplotlib."""
    fig, ax = plt.subplots(figsize=(12, 6))
    for (x, y), symbol in elements_diction.items():
        ax.text(x, y, symbol, ha='center', va='center', fontsize=12,
                bbox=dict(boxstyle="round", facecolor="lightblue"))
    
    ax.set_xlim(0, 19)
    ax.set_ylim(0, 9)
    ax.set_xticks(range(1, 19))
    ax.set_yticks(range(1, 9))
    ax.grid(True)
    plt.gca().invert_yaxis()
    plt.title("Periodic Table")
    plt.show()

from google import genai

GEMINI_KEYS = open("APIkey.txt").read() 
LLM_MODEL = "gemini-2.5-flash"
client = genai.Client(api_key=GEMINI_KEYS)

def chemical_properties(query: str):
    """
    Ask Gemini for chemical properties of an element or compound.
    Returns a structured text answer.
    """
    Query = f"""
    Provide detailed chemical properties of {query}.
    Include:
    - Full name
    - Formula
    - Atomic mass
    - Boiling point
    - Melting point
    - Appearance
    - Density
    - Solubility
    - Properties
    - Dangerousness
    """

    response = client.models.generate_content(
        model=LLM_MODEL,
        contents=Query
    )

    return response.text 

def get_property(element: str, property_name: str) -> str:
    """
    Ask Gemini for a single chemical property of an element or compound.
    
    Parameters:
        element (str): The element or compound name (e.g., "Water", "NaCl").
        property_name (str): The property you want (e.g., "boiling point").
    
    Returns:
        str: The answer from Gemini.
    """
    prompt = f"Provide only the {property_name} of {element}. Do not include other information."
    response = client.models.generate_content(
        model=LLM_MODEL,
        contents=prompt
    )

    return response.text 

def Heat_of_Reaction (mass, specific_heat,temperature1,temperature2):
    """Calculate Heat of Reaction: q = m*c*Δt"""
    return specific_heat * mass * (temperature2-temperature1)

def Gibbs_Free_Energy(Enthalpy, Temperature, Entropy):
    """Calculate Gibbs Free Energy: ΔG = ΔH-TΔS"""
    return Enthalpy - (Temperature * Entropy)

def Electrochemical_Energy (electrons_transferred, cell_potential ,Faraday_constant = 96485.3):
    """Calculate Electrochemical Energy: -nFE"""
    return -electrons_transferred * Faraday_constant * cell_potential

a = input("What function would you like?\n 1. periodic table \n 2. chemical properties\n 3. energy calculation\n type only 1 , 2 , or 3")

if a == "1" :
    plot_periodic_table(elements)

elif a == "2" :
    while True:
        b = input("Do you want specific property? y/n ")
        if b == "y" :
            x = input("Your element :")
            print(" properties include:\n- Full name\n- Formula\n- Atomic mass\n- Boiling point\n- Melting point\n- Appearance\n- Density\n- Solubility \n- Properties\n- Dangerousness")
            y = input("Property :")
            result = get_property(x,y)
            print(result)
        elif b == "n" :
            print("Type your elements/compound or exit to quit")
            Query = input("You: ")
            if Query.lower() in ["exit", "quit", "bye"]:
                print("Goodbye")
                break
            print("GenAI :",chemical_properties(Query))
        else :
            print("Error, please type 'y' or 'n'")
            break
elif a == "3" :
    
    def main():
        print("Energy Calculator")
        print("Choose type of energy:")
        print("a. Heat of Reaction (Calorimetry)")
        print("b. Gibbs Free Energy (ΔG)")
        print("c. Electrochemical Energy")

        choice = input("Enter a, b, or c: ")
        if choice == "a":
            m = float(input("Enter mass: "))
            c = float(input("Enter specific_heat: "))
            t1 = float(input("Enter initial temperature: "))
            t2 = float(input("Enter final temperature: "))
            print("Heat of Reaction =", Heat_of_Reaction (m,c,t1,t2), "Joules")

        elif choice == "b":
            Enthalpy = float(input("Enter enthalpy: "))
            Temperature = float(input("Enter temperature: "))
            Entropy = float(input("Enter entropy: "))
            print("Gibbs Free Energy =", Gibbs_Free_Energy(Enthalpy, Temperature, Entropy), "Joules")

        elif choice == "c" :
            n = float(input("Enter electrons transferred : "))
            E = float(input("Enter cell potential : "))
            print("Electrochemical Energy =",Electrochemical_Energy(n, E), "Joules")

        else:
            print("Invalid choice!")


    if __name__ == "__main__":
        main()

else :
    print("Error, there's no function in this term")