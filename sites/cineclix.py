# -*- coding: utf-8 -*-
# Python 3
# Always pay attention to the translations in the menu!
# HTML LangzeitCache hinzugefügt
# showEntries:    6 Stunden
# showSeasons:    6 Stunden
# showEpisodes:   4 Stunden
# Seite vollständig mit JSON erstellt

import json

from resources.lib.handler.ParameterHandler import ParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.tools import logger, cParser
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.config import cConfig
from resources.lib.gui.gui import cGui

SITE_IDENTIFIER = 'cineclix'
SITE_NAME = 'CineClix'
SITE_ICON = 'cineclix.png'

# Global search function is thus deactivated!
if cConfig().getSetting('global_search_' + SITE_IDENTIFIER) == 'false':
    SITE_GLOBAL_SEARCH = False
    logger.info('-> [SitePlugin]: globalSearch for %s is deactivated.' % SITE_NAME)

# Domain Abfrage
DOMAIN = cConfig().getSetting('plugin_' + SITE_IDENTIFIER + '.domain', 'cineclix.de')
URL_MAIN = 'https://' + DOMAIN + '/'
# URL_MAIN = 'https://cineclix.de/'
# Movie / Series / Search Links
URL_MOVIES = URL_MAIN + 'api/v1/channel/movies?channelType=channel&restriction=&paginate=simple'
URL_TOP_MOVIES = URL_MAIN + 'api/v1/channel/top-10-filme-diese-woche?channelType=channel&restriction=&paginate=simple'
URL_NEW_MOVIES = URL_MAIN + 'api/v1/channel/neu-hinzugefuegt?channelType=channel&restriction=&paginate=simple'
URL_SERIES = URL_MAIN + 'api/v1/channel/series?channelType=channel&restriction=&paginate=simple'
URL_TOP_SERIES = URL_MAIN + '/api/v1/channel/top-10-serien-diese-woche?channelType=channel&restriction=&paginate=simple'
URL_NEW_SERIES = URL_MAIN + '/api/v1/channel/neue-serien?channelType=channel&restriction=&paginate=simple'
URL_SEARCH = URL_MAIN + 'api/v1/search/%s?query=%s&limit=8'
# Genre
URL_ACTION = URL_MAIN + 'api/v1/channel/action-filme?channelType=channel&restriction=&paginate=simple'
URL_ANIMATION = URL_MAIN + 'api/v1/channel/animations-filme?channelType=channel&restriction=&paginate=simple'
URL_HORROR = URL_MAIN + 'api/v1/channel/horror-filme?channelType=channel&restriction=&paginate=simple'
URL_KOMOEDIE = URL_MAIN + 'api/v1/channel/komoedien-filme?channelType=channel&restriction=&paginate=simple'
URL_LOVE = URL_MAIN + 'api/v1/channel/gefuehlskino-herzklopfen-inklusive?channelType=channel&restriction=&paginate=simple'
URL_MUSIC = URL_MAIN + 'api/v1/channel/musik?channelType=channel&restriction=&paginate=simple'
URL_SCIFI = URL_MAIN + 'api/v1/channel/kosmische-erzaehlungen?channelType=channel&restriction=&paginate=simple'
URL_KINO = URL_MAIN + 'api/v1/channel/kino-filme-banner?channelType=channel&restriction=&paginate=simple'
URL_ABENTEUER = URL_MAIN + 'api/v1/channel/abenteuer?channelType=channel&restriction=&paginate=simple'
URL_KRIEGSFILM = URL_MAIN + 'api/v1/channel/kriegsfilm?channelType=channel&restriction=&paginate=simple'
URL_KRIMI = URL_MAIN + 'api/v1/channel/krimi?channelType=channel&restriction=&paginate=simple'
URL_THRILLER = URL_MAIN + 'api/v1/channel/thriller?channelType=channel&restriction=&paginate=simple'
URL_WESTERN = URL_MAIN + 'api/v1/channel/western?channelType=channel&restriction=&paginate=simple'
# Hoster
URL_HOSTER = URL_MAIN + 'api/v1/titles/%s?load=images,genres,productionCountries,keywords,videos,primaryVideo,seasons,compactCredits'


def load():
    logger.info("Load %s" % SITE_NAME)
    params = ParameterHandler()
    params.setParam('page', (1))
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30502), SITE_IDENTIFIER, 'showMovieMenu'), params)  # Movies
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30511), SITE_IDENTIFIER, 'showSeriesMenu'), params)  # Series
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30506), SITE_IDENTIFIER, 'showGenre'), params)  # Genre
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30520), SITE_IDENTIFIER, 'showSearch'))  # Search
    cGui().setEndOfDirectory()

def showMovieMenu():    # Menu structure of movie menu
    params = ParameterHandler()
    params.setParam('sUrl', URL_NEW_MOVIES)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30541), SITE_IDENTIFIER, 'showEntries'), params)  # New
    params.setParam('sUrl', URL_MOVIES)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30542), SITE_IDENTIFIER, 'showEntries'), params)  # Movies
    params.setParam('sUrl', URL_TOP_MOVIES)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30539), SITE_IDENTIFIER, 'showEntries'), params)  # Top Movies
    cGui().setEndOfDirectory()

def showSeriesMenu():   # Menu structure of series menu
    params = ParameterHandler()
    params.setParam('sUrl', URL_NEW_SERIES)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30514), SITE_IDENTIFIER, 'showEntries'), params)  # New
    params.setParam('sUrl', URL_SERIES)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30518), SITE_IDENTIFIER, 'showEntries'), params)  # Series
    params.setParam('sUrl', URL_TOP_SERIES)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30540), SITE_IDENTIFIER, 'showEntries'), params)  # Top Series
    cGui().setEndOfDirectory()

def showGenre():
    params = ParameterHandler()
    params.setParam('sUrl', URL_ACTION)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30800), SITE_IDENTIFIER, 'showEntries'), params)  # Action
    params.setParam('sUrl', URL_ANIMATION)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30801), SITE_IDENTIFIER, 'showEntries'), params)  # Animation
    params.setParam('sUrl', URL_HORROR)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30802), SITE_IDENTIFIER, 'showEntries'), params)  # Horror
    params.setParam('sUrl', URL_KOMOEDIE)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30803), SITE_IDENTIFIER, 'showEntries'), params)  # Comedy
    params.setParam('sUrl', URL_LOVE)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30804), SITE_IDENTIFIER, 'showEntries'), params)  # Love
    params.setParam('sUrl', URL_MUSIC)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30805), SITE_IDENTIFIER, 'showEntries'), params)  # Music
    params.setParam('sUrl', URL_SCIFI)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30806), SITE_IDENTIFIER, 'showEntries'), params)  # SciFi
    params.setParam('sUrl', URL_KINO)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30807), SITE_IDENTIFIER, 'showEntries'), params)  # Kino
    params.setParam('sUrl', URL_ABENTEUER)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30808), SITE_IDENTIFIER, 'showEntries'), params)  # Abenteuer
    params.setParam('sUrl', URL_KRIEGSFILM)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30809), SITE_IDENTIFIER, 'showEntries'), params)  # Kriegsfilm
    params.setParam('sUrl', URL_KRIMI)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30810), SITE_IDENTIFIER, 'showEntries'), params)  # Krimi
    params.setParam('sUrl', URL_THRILLER)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30811), SITE_IDENTIFIER, 'showEntries'), params)  # Thriller
    params.setParam('sUrl', URL_WESTERN)
    cGui().addFolder(cGuiElement(cConfig().getLocalizedString(30812), SITE_IDENTIFIER, 'showEntries'), params)  # Western
    cGui().setEndOfDirectory()

def showEntries(entryUrl=False, sGui=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    # Parameter laden
    if not entryUrl:
        entryUrl = params.getValue('sUrl')
    iPage = int(params.getValue('page'))
    oRequest = cRequestHandler(entryUrl + '&page=' + str(iPage) if iPage > 0 else entryUrl, ignoreErrors=(sGui is not False))
    oRequest.addHeaderEntry('Referer', params.getValue('sUrl'))
    if cConfig().getSetting('global_search_' + SITE_IDENTIFIER) == 'true':
        oRequest.cacheTime = 60 * 60 * 6  # 6 Stunden
    jSearch = json.loads(oRequest.request())  # Lade JSON aus dem Request der URL
    if not jSearch: return  # # Wenn Suche erfolglos - Abbruch
    aResults = jSearch['channel']['content']['data']
    total = len(aResults)
    if len(aResults) == 0:
        if not sGui: oGui.showInfo()
        return
    for i in aResults:
        sId = i['id']  # ID des Films / Serie für die weitere URL
        sName = i['name']  # Name des Films / Serie
        if 'is_series' in i: isTvshow = i['is_series']  # Wenn True dann Serie
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showSeasons' if isTvshow else 'showHosters')
        if 'year' in i and len(str(i['year'])) == 4: oGuiElement.setYear(
            i['year'])  # Suche bei year nach 4 stelliger Zahl
        # sDesc = i['description']
        if 'description' in i and i['description'] != '': oGuiElement.setDescription(
            i['description'])  # Suche nach Desc wenn nicht leer dann setze GuiElement
        # sThumbnail = i['poster']
        if 'poster' in i and i['poster'] != '': oGuiElement.setThumbnail(
            i['poster'])  # Suche nach Desc wenn nicht leer dann setze GuiElement
        # sFanart = i['backdrop']
        if 'backdrop' in i and i['backdrop'] != '': oGuiElement.setFanart(
            i['backdrop'])  # Suche nach Desc wenn nicht leer dann setze GuiElement
        oGuiElement.setMediaType('tvshow' if isTvshow else 'movie')
        # Parameter übergeben
        params.setParam('entryUrl', URL_HOSTER % sId)
        params.setParam('sThumbnail', i['poster'])
        params.setParam('sName', sName)
        oGui.addFolder(oGuiElement, params, isTvshow, total)
    if not sGui:
        sPageNr = int(params.getValue('page'))
        if sPageNr == 0:
            sPageNr = 2
        else:
            sPageNr += 1
        params.setParam('page', int(sPageNr))
        oGui.addNextPage(SITE_IDENTIFIER, 'showEntries', params)
        oGui.setView('tvshows' if isTvshow else 'movies')
        oGui.setEndOfDirectory()


def showSeasons(sGui=False):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    # Parameter laden
    entryUrl = params.getValue('entryUrl')
    sThumbnail = params.getValue('sThumbnail')
    oRequest = cRequestHandler(entryUrl)
    oRequest.addHeaderEntry('Referer', entryUrl)
    if cConfig().getSetting('global_search_' + SITE_IDENTIFIER) == 'true':
        oRequest.cacheTime = 60 * 60 * 6  # 6 Stunden
    jSearch = json.loads(oRequest.request()) # Lade JSON aus dem Request der URL
    if not jSearch: return # Wenn Suche erfolglos - Abbruch
    sDesc = jSearch['title']['description'] # Lade Beschreibung aus JSON

    #Nachdem Titel und Beschreibung ausgelesen ist, Wechsel der URL um alle Staffeln darzustellen (max. 50 Staffeln)
    token = oRequest.getCookie('XSRF-TOKEN')
    title_id = jSearch['title']['id']
    entryUrl1 = URL_MAIN + 'api/v1/titles/' + str(title_id) + '/seasons?perPage=50&query=&page=1' # max 50 Staffeln (Page=50)
    oRequest = cRequestHandler(entryUrl1)
    oRequest.addHeaderEntry('Accept', 'application/json')
    oRequest.addHeaderEntry('Content-Type', 'application/json')
    oRequest.addHeaderEntry('Sec-Fetch-Dest', 'empty')
    oRequest.addHeaderEntry('Sec-Fetch-Mode', 'cors')
    oRequest.addHeaderEntry('Sec-Fetch-Site', 'same-origin')
    oRequest.addHeaderEntry('X-XSRF-TOKEN', str(token.value))
    oRequest.addHeaderEntry('Referer', entryUrl)
    jSearch = json.loads(oRequest.request())
    if not jSearch: return
    aResults = jSearch['pagination']['data']

    aResults = sorted(aResults, key=lambda k: k['number'])  # Sortiert die Staffeln nach Nummer aufsteigend
    total = len(aResults)
    if len(aResults) == 0:
        if not sGui: oGui.showInfo()
        return
    for i in aResults:
        sId = i['title_id'] # ID ändert sich !!!
        sSeasonNr = str(i['number']) # Staffel Nummer
        oGuiElement = cGuiElement('Staffel ' + sSeasonNr, SITE_IDENTIFIER, 'showEpisodes')
        oGuiElement.setMediaType('season')
        oGuiElement.setSeason(sSeasonNr)
        oGuiElement.setThumbnail(sThumbnail)
        if sDesc != '': oGuiElement.setDescription(sDesc)
        params.setParam('sSeasonNr', sSeasonNr)
        params.setParam('sId', sId)
        cGui().addFolder(oGuiElement, params, True, total)
    cGui().setView('seasons')
    cGui().setEndOfDirectory()


def showEpisodes(sGui=False):
    oGui = cGui()
    params = ParameterHandler()
    # Parameter laden
    sId = params.getValue('sId')
    sSeasonNr = params.getValue('sSeasonNr')
    #https://cineclix.de/api/v1/titles/2858/seasons/2?load=episodes,primaryVideo
    sUrl = URL_MAIN + 'api/v1/titles/%s/seasons/%s?load=episodes,primaryVideo' % (sId, sSeasonNr)
    oRequest = cRequestHandler(sUrl)
    oRequest.addHeaderEntry('Referer', sUrl)
    if cConfig().getSetting('global_search_' + SITE_IDENTIFIER) == 'true':
        oRequest.cacheTime = 60 * 60 * 4  # 4 Stunden
    jSearch = json.loads(oRequest.request()) # Lade JSON aus dem Request der URL
    if not jSearch: return # Wenn Suche erfolglos - Abbruch
    aResults = jSearch['episodes']['data'] # Ausgabe der Suchresultate von jSearch
    total = len(aResults) # Anzahl aller Ergebnisse
    if len(aResults) == 0:
        if not sGui: oGui.showInfo()
        return
    for i in aResults:
        sName = i['name'] # Episoden Titel
        sEpisodeNr = str(i['episode_number']) # Episoden Nummer
        sThumbnail = i['poster'] # Episoden Poster
        oGuiElement = cGuiElement('Episode ' + sEpisodeNr + ' - ' + sName, SITE_IDENTIFIER, 'showHosters')
        if 'description' in i and i['description'] != '': oGuiElement.setDescription(i['description']) # Suche nach Desc wenn nicht leer dann setze GuiElement
        oGuiElement.setEpisode(sEpisodeNr)
        oGuiElement.setSeason(sSeasonNr)
        oGuiElement.setMediaType('episode')
        oGuiElement.setThumbnail(sThumbnail)
        # Parameter setzen
        #https://cineclix.de/api/v1/titles/2858/seasons/2/episodes/2?load=videos,compactCredits,primaryVideo
        params.setParam('entryUrl', URL_MAIN + 'api/v1/titles/%s/seasons/%s/episodes/%s?load=videos,compactCredits,primaryVideo' % (sId, sSeasonNr, sEpisodeNr))
        oGui.addFolder(oGuiElement, params, False, total)
    oGui.setView('episodes')
    oGui.setEndOfDirectory()


def showSearchEntries(entryUrl=False, sGui=False, sSearchText=''):
    oGui = sGui if sGui else cGui()
    params = ParameterHandler()
    # Parameter laden
    if not entryUrl: entryUrl = params.getValue('sUrl')
    oRequest = cRequestHandler(entryUrl, ignoreErrors=(sGui is not False))
    oRequest.addHeaderEntry('Referer', entryUrl)
    jSearch = json.loads(oRequest.request()) # Lade JSON aus dem Request der URL
    if not jSearch: return  # Wenn Suche erfolglos - Abbruch
    aResults = jSearch['results'] # Ausgabe der Suchresultate von jSearch
    total = len(aResults) # Anzahl aller Ergebnisse
    if len(aResults) == 0: # Wenn Resultate 0 zeige Benachrichtigung
        if not sGui: oGui.showInfo()
        return
    isTvshow = False
    for i in aResults:
        if 'person' in i['model_type']: continue # Personen in der Suche ausblenden
        sId = i['id']   # ID des Films / Serie für die weitere URL
        sName = i['name'] # Name des Films / Serie
        if sSearchText.lower() and not cParser().search(sSearchText, sName.lower()): continue
        if 'is_series' in i: isTvshow = i['is_series'] # Wenn True dann Serie
        oGuiElement = cGuiElement(sName, SITE_IDENTIFIER, 'showSeasons' if isTvshow else 'showHosters')
        if 'year' in i and len(str(i['year'])) == 4: oGuiElement.setYear(i['year']) # Suche bei year nach 4 stelliger Zahl
        #sDesc = i['description']
        if 'description' in i and i['description'] != '': oGuiElement.setDescription(i['description']) # Suche nach Desc wenn nicht leer dann setze GuiElement
        # sThumbnail = i['poster']
        if 'poster' in i and i['poster'] != '': oGuiElement.setThumbnail(i['poster']) # Suche nach Desc wenn nicht leer dann setze GuiElement
        # sFanart = i['backdrop']
        if 'backdrop' in i and i['backdrop'] != '': oGuiElement.setFanart(i['backdrop']) # Suche nach Desc wenn nicht leer dann setze GuiElement
        oGuiElement.setMediaType('tvshow' if isTvshow else 'movie')
        # Parameter setzen
        params.setParam('entryUrl', URL_HOSTER % sId)
        params.setParam('sThumbnail', i['poster'])
        params.setParam('sName', sName)
        oGui.addFolder(oGuiElement, params, isTvshow, total)
    if not sGui:
        oGui.setView('tvshows' if isTvshow else 'movies')
        oGui.setEndOfDirectory()


def showHosters(sGui=False):
    oGui = sGui if sGui else cGui()
    hosters = []
    sUrl = ParameterHandler().getValue('entryUrl')
    oRequest = cRequestHandler(sUrl)
    oRequest.addHeaderEntry('Referer', sUrl)
    jSearch = json.loads(oRequest.request())  # Lade JSON aus dem Request der URL
    if not jSearch: return  # Wenn Suche erfolglos - Abbruch
    if ParameterHandler().getValue('mediaType') == 'movie': #Bei MediaTyp Filme nutze das Result
        aResults = jSearch['title']['videos'] # Ausgabe der Suchresultate von jSearch für Filme
    else:
        aResults = jSearch['episode']['videos'] # Ausgabe der Suchresultate von jSearch für Episoden
    # total = len(aResults)  # Anzahl aller Ergebnisse
    if len(aResults) == 0:
        if not sGui: oGui.showInfo()
        return
    for i in aResults:
        sName = i['name']
        sQuality = str(i['quality'])
        if 'None' in sQuality: sQuality = '720p'
        if 'dvd' in sQuality: sQuality = 'DVD'
        if 'hd' in sQuality: sQuality = 'HD'
        sUrl = i['src']
        if cConfig().isBlockedHoster(sUrl)[0]: continue  # Hoster aus settings.xml oder deaktivierten Resolver ausschließen
        if 'youtube' in sUrl: continue # Trailer ausblenden
        hoster = {'link': sUrl, 'name': sName, 'displayedName': '%s [I][%s][/I]' % (sName, sQuality), 'quality': sQuality, 'resolveable': True}
        hosters.append(hoster)
    if hosters:
        hosters.append('getHosterUrl')
    return hosters


def getHosterUrl(sUrl=False):
    return [{'streamUrl': sUrl, 'resolved': False}]


def showSearch():
    sSearchText = cGui().showKeyBoard()
    if not sSearchText: return
    _search(False, sSearchText)
    cGui().setEndOfDirectory()


def _search(oGui, sSearchText):
    # https://cineclix.de/api/v1/search/Super%20Mario?query=Super+Mario&limit=8
    # Suche mit Quote und QuotePlus beim Suchtext
    sID1 = cParser().quote(sSearchText)
    sID2 = cParser().quotePlus(sSearchText)
    showSearchEntries(URL_SEARCH % (sID1, sID2), oGui, sSearchText)