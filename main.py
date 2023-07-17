import streamlit as st

class TicketType:
    CLASSIC = "Contravention classique"
    POST_PARKING = "Forfait post stationnement"

def validate_ticket_number(ticket_number, type_of_ticket):
    if type_of_ticket == TicketType.CLASSIC:
        if len(ticket_number) != 10 or ticket_number[0] not in ['1', '3', '4', '6', '8']:
            return False
    elif type_of_ticket == TicketType.POST_PARKING:
        if len(ticket_number) != 26:
            return False
    return True

def calculate_payment_number_and_key(ticket_number, type_of_ticket):
    if not validate_ticket_number(ticket_number, type_of_ticket):
        st.error("Le numéro de contravention est invalide.")
        return None, None

    if type_of_ticket == TicketType.CLASSIC:
        payment_number = "333" + ticket_number + "1"
        key = str(int(payment_number) % 97)
        if len(key) == 1:
            key = '0' + key
        return payment_number, key

    elif type_of_ticket == TicketType.POST_PARKING:
        # Ici, ajouter le calcul pour le Forfait post stationnement
        pass

    else:
        st.error("Type de contravention non reconnu.")
        return None, None

st.title("Calculateur de numéro de télépaiement et clé de e-paiement pour les contraventions 🇫🇷")
st.markdown("Vous avez perdu la deuxième partie de votre contravention OU vous ne possédez que le numéro de l'avis de contravention ET vous souhaitez payer en ligne ? <br> " \
            "Ce site est fait pour vous !", unsafe_allow_html=True)

type_of_ticket = st.selectbox("Type de contravention", [TicketType.CLASSIC, TicketType.POST_PARKING])
ticket_number = st.text_input("Numéro de contravention", "", help="Le numéro de contravention est composé de 10 chiffres pour les contraventions classiques et de 26 caractères pour les forfaits post stationnement.")

if st.button("Calculer le numéro de e-paiement la clé de télépaiement"):
    payment_number, key = calculate_payment_number_and_key(ticket_number, type_of_ticket)
    if payment_number and key:
        st.success("Calcul réussi !")
        st.markdown(f"### Numéro de télépaiement")
        st.markdown(f"<h2 style='text-align: center;'>{payment_number}</h2>", unsafe_allow_html=True)
        st.markdown(f"### Clé de e-paiement")
        st.markdown(f"<h2 style='text-align: center;'>{key}</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><a href='https://www.amendes.gouv.fr/tai' target='_blank'>Payer l'amende - https://www.amendes.gouv.fr/tai</a></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Attention : www.amendes.gouv.fr est le seul site gouvernemental pour payer votre amende en ligne. Faites attention aux arnaques.</p>", unsafe_allow_html=True)

        


# add a footer with a link to the github repo
st.markdown("<br> <br> <br> <br> <br> <br> <br> <br>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><a href='https://github.com/tcaruchet/CleAmende'>Github</a></p>", unsafe_allow_html=True)
keywords = ["contravention", "amende", "télépaiement", "e-paiement", "CléAmende", "paiement en ligne", "contravention française", "forfait post stationnement", "FPS", 
            "paiement en ligne contravention", "paiement en ligne amende", "paiement en ligne contravention française", "paiement en ligne amende française", "paiement en ligne FPS",
            "paiement en ligne forfait post stationnement", "paiement en ligne contravention classique", "paiement en ligne amende classique", "paiement en ligne contravention classique française",
            "notice de paiement perdue", "avis de paiement perdu", "notice de paiement perdu", "avis de paiement perdu", "paiement en ligne avis de paiement perdu", "paiement en ligne notice de paiement perdue",
            "generer numero de paiement", "generer numero de telepaiement", "generer numero de télépaiement", "generer numero de e-paiement", "generer numero de e paiement", "generer numero de paiement en ligne",
            "generer clé telepaiement", "generer clé de telepaiement", "generer clé de e-paiement", "generer clé de e paiement", "generer clé de paiement en ligne", "generer clé de paiement en ligne", "antai", 
            "agence nationale de traitement automatisé des infractions", "antai.gouv.fr", "stationnement.gouv.fr",
            "générateur de numéro de paiement", "outil de paiement d'amende", "service de paiement d'amende en ligne", "solution de paiement de contravention",
            "calculateur de clé de télépaiement", "calculateur de clé de e-paiement", "outil de calcul de clé de paiement", "solution de calcul de clé de paiement",
            "paiement d'amende française en ligne", "paiement de contravention française en ligne", "paiement de FPS en ligne", "paiement de forfait post stationnement en ligne",
            "outil de paiement d'amende classique", "solution de paiement d'amende classique", "outil de paiement de contravention classique", "solution de paiement de contravention classique",
            "outil de paiement d'amende perdue", "solution de paiement d'amende perdue", "outil de paiement de contravention perdue", "solution de paiement de contravention perdue",
            "générateur de numéro de paiement pour amende perdue", "générateur de numéro de paiement pour contravention perdue", "générateur de clé de paiement pour amende perdue", "générateur de clé de paiement pour contravention perdue",
            "ANTAI", "Agence Nationale de Traitement Automatisé des Infractions", "ANTAI.gouv.fr", "Stationnement.gouv.fr", "paiement d'amende ANTAI", "paiement de contravention ANTAI",
            "paiement de FPS ANTAI", "paiement de forfait post stationnement ANTAI", "générateur de numéro de paiement ANTAI", "générateur de clé de paiement ANTAI"]
st.markdown("<p style='text-align: center; color: lightgray; font-size: 10px;'>{}</p>".format(", ".join(keywords)), unsafe_allow_html=True)
