import cv2
import time
import requests
import numpy as np
# --- Configuration du Bot Telegram ---
TOKEN = "7876431851:AAEUeICZo-Fqdnd0IVVdiA7zAfzNxL2NIAA"
CHAT_ID = "7299550792"  # L'id du destinataire (l'utilisateur doit avoir démarré la conversation)

def send_telegram_photo(image_path):
    """Envoie une photo via Telegram."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    files = {"photo": open(image_path, "rb")}
    data = {"chat_id": CHAT_ID, "caption": "Mouvement détecté !"}
    try:
        response = requests.post(url, data=data, files=files)
        if response.status_code == 200:
            print("Photo envoyée via Telegram")
        else:
            print("Erreur lors de l'envoi, code :", response.status_code)
    except Exception as e:
        print("Erreur lors de l'envoi :", e)
    finally:
        files["photo"].close()

def main():
    # Initialisation de la capture vidéo
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erreur : impossible d'ouvrir la caméra")
        return

    # Optionnel : réduire la résolution pour alléger le traitement
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 219)

    # Lecture de la première image et conversion en niveaux de gris
    ret, prev_frame = cap.read()
    if not ret:
        print("Erreur lors de la lecture de la première image")
        cap.release()
        return
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    # Paramètres de détection
    motion_cooldown = 30  # secondes entre deux alertes
    last_motion_time = 0
    threshold = 5000  # nombre minimal de pixels modifiés pour déclencher une alerte

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Conversion de l'image courante en niveaux de gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Calcul de la différence absolue avec l'image précédente
        diff = cv2.absdiff(prev_gray, gray)
        # Comptage du nombre de pixels modifiés
        non_zero_count = np.count_nonzero(diff)

        if non_zero_count > threshold:
            current_time = time.time()
            if current_time - last_motion_time > motion_cooldown:
                print("Mouvement détecté ! (Pixels modifiés :", non_zero_count, ")")
                # Sauvegarde de l'image courante
                photo_filename = "detected.jpg"
                cv2.imwrite(photo_filename, frame)
                # Envoi de la photo via Telegram
                send_telegram_photo(photo_filename)
                last_motion_time = current_time

        # Affichage du flux vidéo
        cv2.imshow("Flux de la caméra", frame)
        prev_gray = gray

        # Quitter si on appuie sur 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
