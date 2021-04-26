from datetime import datetime

def sample_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ("merhaba", "hey"):
        return "Merhaba dostum hoşgeldin!"

    if user_message in ("selam", "sa", "selamun aleykum", "selamün aleyküm", "selamünaleyküm"):
        return "Ve aleyna aleyküm selam verahmetullahi veberekatuhu"

    if user_message in ("nasılsın", "nasılsın?"):
        return "İyiyim, teşekkür ederim. Sen nasılsın?"

    if user_message in ("kimsin sen", "kimsin", "sen kimsin" "sen nesin"):
        return "Ben BT yardım botuyum. Size nasıl yardımcı olabilirim?"

    if user_message in ("zaman", "saat kaç", "saat"):
        now = datetime.now()
        date_time = now.strftime("Tarih: %d/%m/%y - Saat: %H:%M:%S")
        return str(date_time)

    return "Seni anlamadım ne demek istedin?"

