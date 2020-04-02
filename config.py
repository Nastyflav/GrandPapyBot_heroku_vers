#! /usr/bin/env python3
# coding: utf-8

#Application informations
APP_NAME = 'GrandPy Bot'
APP_CATCHLINE = 'On lui a installé l\'ADSL, profitez-en ! Trouvez des lieux et leur histoire !'
APP_AUTHOR = 'Flavien Murail'
APP_LINKEDIN_LINK = 'https://www.linkedin.com/in/flavien-murail-7155b7156/'
APP_REPO_LINK = 'https://github.com/Nastyflav/GrandPapyBot_OC'
APP_PARTNER_LINK = 'https://openclassrooms.com/'
APP_GPL_LINK = 'https://fr.wikipedia.org/wiki/Licence_publique_g%C3%A9n%C3%A9rale_limit%C3%A9e_GNU'

#Chatbox presets
TEXT_AREA = 'Coucou GrandPy, tu vas bien ? Dis-moi, tu ne saurais pas où se situe Minneapolis par hasard ?'
EMPTY_QUERY_ANSWER = 'Tu vois le truc devant toi, avec les touches ? Il faut l\'utiliser pour discuter...'
ANSWERS_ADRESS_OK = ['Evidemment, je ne suis pas encore gâteux ! Voici l\'adresse : ', 
                    'Héhé, ça me dit quelque chose : ',
                    'Attends voir...Tiens, j\'ai trouvé : ',
                    'Tu ne connais pas ça ? Faut sortir un peu quand même : ']
ANSWERS_STORY_OK = ['Haha, je me souviens, un bien bel endroit : ',
                    'On y est allé avec ta grand-mère, on a passé du bon temps, héhé... Comment ça tu veux pas savoir ? Bon, voici la version pour les enfants : ',
                    'Alors, attends, oui, je me rappelle maintenant : '
                    'Ouvre bien tes esgourdes, je ne le répéterai pas deux fois : ']
ANSWERS_ADRESS_FAIL = ['Tu as tourné la carte ou quoi ?',
                        'Connais pas. Je bosse pas aux PTT moi !',
                        'Sois plus précis s\'il te plait, GrandPy est fatigué...',
                        'Répète pour voir, j\'ai mal entendu']
ANSWERS_STORY_FAIL = ['Il ne se passe jamais rien là-bas, faut t\'y faire.',
                        'Je ne me suis jamais autant ennuyé que dans ce bled. Rien à dire.',
                        'Bon, je ne vais pas te faire la lecture jusqu\'à ma mort.',
                        'J\'ai pas la science infuse moi ! Regarde dans un livre !']

#Google Maps Api presets
GOOGLE_KEY = 'AIzaSyCH_uGge9XRsTK22BY6zDrR2OgpqOZK204'
GOOGLE_URL = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
GOOGLE_INPUTTYPE = 'textquery'
GOOGLE_FIELDS = 'formatted_address,name,geometry'
GOOGLE_LANGUAGE = 'fr'
GOOGLE_MAP_URL = 'https://maps.googleapis.com/maps/api/staticmap?'
GOOGLE_MAP_SIZE = (500, 400)

#Wikipedia Api presets
WIKI_URL = 'https://en.wikipedia.org/w/api.php'
WIKI_FORMAT = 'json'
WIKI_LIST = 'geosearch'
WIKI_ACTION = 'query'
WIKI_RADIUS = 10000
WIKI_PROP = "extracts|info"
WIKI_INPROP = "url"
WIKI_EXCHARS = 1000
WIKI_EXPLAINTEXT = 1

