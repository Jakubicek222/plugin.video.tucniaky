import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Strateny.v.zablesku.Sk.dub.avi'
li = xbmcgui.ListItem('1x1 - Stratený v záblesku')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Vylet.na.Mesiac.Sk.dub.avi'
li = xbmcgui.ListItem('1x2 - Výlet na Mesiac')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Strasidelne.miesto.Sk.dub.avi'
li = xbmcgui.ListItem('1x3 - Strašidelné miesto')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Strasidelne.miesto.Sk.dub.avi'
li = xbmcgui.ListItem('1x3 - Strašidelné miesto')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Operacia.Plysiaci.Sk.dub.avi'
li = xbmcgui.ListItem('1x4 - Operácia: Plyšiaci')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Stastny.den.krala.Juliena.Sk.dub.avi'
li = xbmcgui.ListItem('1x5 - Šťastný deň kráľa Juliena')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Rodicovsky.instinkt.Sk.dub.avi'
li = xbmcgui.ListItem('1x6 - Rodičovský inštinkt')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Utok.a.baterky.Sk.dub.avi'
li = xbmcgui.ListItem('1x7 - Útok a baterky')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Tucniaky.beru.vsetko.Sk.dub.avi'
li = xbmcgui.ListItem('1x8 - Tučniaky berú všetko')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Zakon.o.zakaze.dotykania.sa.noh.Sk.dub.avi'
li = xbmcgui.ListItem('1x9 - Zákon o zákaze dotýkania sa nôh')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Nastrahy.netu.Sk.dub.avi'
li = xbmcgui.ListItem('1x10 - Nástrahy netu')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Korunovani.hlupaci.Sk.dub.avi'
li = xbmcgui.ListItem('1x11 - Korunovaní hlupáci')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.V.utajeni.Sk.dub.avi'
li = xbmcgui.ListItem('1x12 - V utajení')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Nove.kralovstvo.Sk.dub.avi'
li = xbmcgui.ListItem('1x13 - Nové kráľovstvo')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Male.zoologicke.kupe.Sk.dub.avi'
li = xbmcgui.ListItem('1x14 - Malé zoologické kupé')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Vsetko.je.prehltnute.Sk.dub.avi'
li = xbmcgui.ListItem('1x15 - Všetko je prehltnuté')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Pukancova.panika.Sk.dub.avi'
li = xbmcgui.ListItem('1x16 - Pukancová panika')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Rybacka.Sk.dub.avi'
li = xbmcgui.ListItem('1x17 - Rybačka')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Zazrak.na.lade.Sk.dub.avi'
li = xbmcgui.ListItem('1x18 - Zázrak na ľade')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Strasidelna.ihla.Sk.dub.avi'
li = xbmcgui.ListItem('1x19 - Strašidelná ihla')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://jd.wz.cz/Tucniaky.z.Madagaskaru.Zatmenie.Sk.dub.avi'
li = xbmcgui.ListItem('1x20 - Zatmenie')
li.setProperty("IsPlayable", "true")
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
