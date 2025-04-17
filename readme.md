'''
# Détecteur de Mouvement avec Notification Telegram

## Description du projet

Ce projet utilise une caméra pour surveiller une zone et détecter tout mouvement qui se produit. Lorsqu'un mouvement est détecté, une photo est capturée et envoyée automatiquement via un bot Telegram, avec un message d'alerte. Ce script est particulièrement utile pour des applications de surveillance, de sécurité ou simplement pour toute personne souhaitant surveiller un espace en temps réel à l'aide de leur ordinateur et d'une caméra.

### Fonctionnalités

- **Détection de mouvement** : Le programme capture en continu des images depuis la caméra et les compare pour détecter des changements significatifs (mouvement).
- **Envoi de notifications Telegram** : Lorsque le mouvement est détecté, une photo de l'événement est envoyée via Telegram avec un message d'alerte.
- **Configuration flexible** : Le projet permet de personnaliser le seuil de détection de mouvement, la fréquence des alertes et le chat Telegram qui recevra les notifications.
- **Visualisation en temps réel** : Affichage en direct du flux vidéo de la caméra tout en surveillant la détection de mouvement.

---

## Prérequis

Avant de commencer, vous devez installer certaines bibliothèques Python nécessaires pour le bon fonctionnement de ce projet. Ces bibliothèques sont :

- **OpenCV** : Pour la capture vidéo et la détection des mouvements.  
- **Requests** : Pour envoyer des photos via l'API Telegram.  
- **Numpy** : Pour le traitement d'image.  
- **Aiogram** : Pour créer et gérer le bot Telegram.  

### Installation des dépendances

Installez les bibliothèques nécessaires avec la commande suivante :

```bash
pip install opencv-python requests numpy aiogram
```

Si vous utilisez un environnement virtuel (fortement recommandé), vous pouvez créer un environnement virtuel avec :

```bash
python -m venv env
source env/bin/activate   # Sur Linux/Mac
env\Scripts\activate      # Sur Windows
```

Puis, installez les dépendances via `pip`.

---

## Configuration du Bot Telegram

### Étapes pour créer un bot Telegram

1. Ouvrez [Telegram](https://telegram.org/) et recherchez le bot **BotFather**.  
2. Lancez une conversation avec **BotFather** et utilisez la commande `/newbot` pour créer un nouveau bot.  
3. Choisissez un nom pour votre bot et un nom d’utilisateur se terminant par `bot`.  
4. **BotFather** vous fournira un `TOKEN`. Conservez-le précieusement.  

### Obtenir votre `chat_id`

1. Lancez une conversation avec votre bot.  
2. Envoyez-lui `/start`.  
3. Appelez l’API pour récupérer les updates :

   ```
   https://api.telegram.org/bot<TOKEN>/getUpdates
   ```

4. Dans le JSON renvoyé, repérez la valeur `chat.id` de votre message : c’est votre `chat_id`.

---

## Structure des fichiers

- **`motion-detector.py`** : Script principal de détection de mouvement et envoi de photos.  
- **`chat_id.py`** : Script pour obtenir votre `chat_id`.

---

## Variables de configuration

### Dans `motion-detector.py`

```python
TOKEN = "VOTRE_TOKEN"
CHAT_ID = "VOTRE_CHAT_ID"
```

### Dans `chat_id.py`

```python
TOKEN = "VOTRE_TOKEN"
```

---

## Utilisation

1. **Obtenir votre `chat_id`**  
   ```bash
   python chat_id.py
   ```
2. **Lancer la détection**  
   ```bash
   python motion-detector.py
   ```
3. Pour arrêter, appuyez sur `q` dans la fenêtre vidéo.

---

## Explication du code

- **Capture vidéo** : Ouverture et lecture continue de la caméra.  
- **Détection** : Comparaison image courante/précédente en niveaux de gris.  
- **Seuil** : Alerte si nombre de pixels modifiés > `threshold`.  
- **Cooldown** : Temps minimal entre deux alertes (`motion_cooldown`).  
- **Envoi** : Sauvegarde de l’image (`detected.jpg`) et envoi via l’API Telegram.

---

## Personnalisation

- `threshold = 5000` (pixels modifiés)  
- `motion_cooldown = 30` (secondes)  
- Résolution caméra (`cap.set(...)`)

---

## Dépannage

- **Caméra** : Vérifiez la connexion et les permissions.  
- **Telegram** : Vérifiez `TOKEN` et `CHAT_ID`, et que le bot est démarré.

---

## Sécurité

- Conservez le `TOKEN` privé.  
- Respectez la vie privée et la législation locale.

---

## Licence

Please just don't steal my code..
