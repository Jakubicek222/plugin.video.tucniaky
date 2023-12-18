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

xbmcplugin.endOfDirectory(addon_handle)
