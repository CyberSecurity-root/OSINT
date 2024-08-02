import webbrowser



title = r"""

         _______                   _____                    _____                    _____                _____          
        /::\    \                 /\    \                  /\    \                  /\    \              /\    \         
       /::::\    \               /::\    \                /::\    \                /::\____\            /::\    \        
      /::::::\    \             /::::\    \               \:::\    \              /::::|   |            \:::\    \       
     /::::::::\    \           /::::::\    \               \:::\    \            /:::::|   |             \:::\    \      
    /:::/~~\:::\    \         /:::/\:::\    \               \:::\    \          /::::::|   |              \:::\    \     
   /:::/    \:::\    \       /:::/__\:::\    \               \:::\    \        /:::/|::|   |               \:::\    \    
  /:::/    / \:::\    \      \:::\   \:::\    \              /::::\    \      /:::/ |::|   |               /::::\    \   
 /:::/____/   \:::\____\   ___\:::\   \:::\    \    ____    /::::::\    \    /:::/  |::|   | _____        /::::::\    \  
|:::|    |     |:::|    | /\   \:::\   \:::\    \  /\   \  /:::/\:::\    \  /:::/   |::|   |/\    \      /:::/\:::\    \ 
|:::|____|     |:::|    |/::\   \:::\   \:::\____\/::\   \/:::/  \:::\____\/:: /    |::|   /::\____\    /:::/  \:::\____\
 \:::\    \   /:::/    / \:::\   \:::\   \::/    /\:::\  /:::/    \::/    /\::/    /|::|  /:::/    /   /:::/    \::/    /
  \:::\    \ /:::/    /   \:::\   \:::\   \/____/  \:::\/:::/    / \/____/  \/____/ |::| /:::/    /   /:::/    / \/____/ 
   \:::\    /:::/    /     \:::\   \:::\    \       \::::::/    /                   |::|/:::/    /   /:::/    /          
    \:::\__/:::/    /       \:::\   \:::\____\       \::::/____/                    |::::::/    /   /:::/    /           
     \::::::::/    /         \:::\  /:::/    /        \:::\    \                    |:::::/    /    \::/    /            
      \::::::/    /           \:::\/:::/    /          \:::\    \                   |::::/    /      \/____/             
       \::::/    /             \::::::/    /            \:::\    \                  /:::/    /                           
        \::/____/               \::::/    /              \:::\____\                /:::/    /                            
         ~~                      \::/    /                \::/    /                \::/    /                             
                                  \/____/                  \/____/                  \/____/                              
                                                                                                                         
                                          
"""
print(title)
print("=" * 100)
print("get 100+ osint tools using this script")
print("=" * 100)
print("1.- all tools")
print("2.- whitepages")
print("3.- mails")
print("4.- phone numbers")
print("5.- domains")
print("6.- fake profile generator")
print("7.- IP Adresses")
print("8.- google dorking")
print("9.- anonymity")
print("10.- images")
print("11.- locations")
print("12.- usernames")
print("00.- leave")
print("=" * 100)
print("\n")
print("|")
selection = input("--------(-🕵️‍♂️-)[Select an option] : ")

if selection == '1':
    webbrowser.open("github.com/CyberSecurity-root/OSINT")
    quit()
elif selection == '2':
    webbrowser.open("github.com/CyberSecurity-root/whitepages")
    quit()
elif selection == '3':
    print("-" * 20 + "select a web page" + "-" * 20)
    print("1.- intelx.io")
    print("2.- epieos.com")
    print("3.- exposed.lol")
    print("4.- sherlockeye.io")
    print("5.- thatsthem.com")
    print("6.- voilanorbert.com")
    print("7.- osint.industries")
    print("8.- skymem.info")
    print("9.- mailscrap.com")
    print("10.- emailrep.io")
    print("11.- haveibeenpwned.com")
    print("12.- ashley.cynic.al")
    print("13.- mxtoolbox.com")
    print("14.- hudsonrock.com")
    print("15.- mailpro.com")
    print("-" * 20 + "github repos" + "-" * 20)
    print("16.- check if mail exists")
    print("17.- infoga")
    print("18.- Ghunt")
    mail_osint_selection = input("--------(-📧-)[Mail-OSINT]/[Select a Webpage] : ")
    if mail_osint_selection == '1':
        webbrowser.open("intelx.io")
        quit()
    elif mail_osint_selection == '2':
        webbrowser.open("epieos.com")
        quit()
    elif mail_osint_selection == '3':
        webbrowser.open("exposed.lol")
        quit()
    elif mail_osint_selection == '4':
        webbrowser.open("sherlockeye.io")
        quit()
    elif mail_osint_selection == '5':
        webbrowser.open("thatsthem.com")
        quit()
    elif mail_osint_selection == '6':
        webbrowser.open("voilanorbert.com")
        quit()
    elif mail_osint_selection == '7':
        webbrowser.open("osint.industries")
        quit()
    elif mail_osint_selection == '8':
        webbrowser.open("skymem.info")
        quit()
    elif mail_osint_selection == '9':
        webbrowser.open("mailscrap.com")
        quit()
    elif mail_osint_selection == '10':
        webbrowser.open("emailrep.io")
        quit()
    elif mail_osint_selection == '11':
        webbrowser.open("haveibeenpwned.com")
        quit()
    elif mail_osint_selection == '12':
        webbrowser.open("ashley.cynic.al")
        quit()
    elif mail_osint_selection == '13':
        webbrowser.open("mxtoolbox.com")
        quit()
    elif mail_osint_selection == '14':
        webbrowser.open("hudsonrock.com")
        quit()
    elif mail_osint_selection == '15':
        webbrowser.open("mailpro.com")
        quit()
    elif mail_osint_selection == '16':
        webbrowser.open("github.com/reacherhq/check-if-email-exists")
        quit()
    elif mail_osint_selection == '17':
        webbrowser.open("github.com/m4ll0k/infoga")
        quit()
    elif mail_osint_selection == '18':
        webbrowser.open("github.com/mxrch/GHunt")
        quit()
    else:
        print("Invalid option, QUITTING!")
        quit()


elif selection == '4':
    print("-" * 20 + "select a web page" + "-" * 20)
    print("1.- epieos.com")
    print("2.- app.osint.industries")
    print("3.- spydialer.com")
    print("4.- slydial.com")
    print("5.- whocalld.com")
    print("6.- phonevalidator.com")
    print("7.- calleridservice.com")
    print("8.- freecarrierlookup.com")
    print("-" * 20 + "github repos" + "-" * 20)
    print("9.- phoneinfoga")
    print("10.- numspy")
    phone_number_osint_page = input("--------(-📞-)[Phone-number-OSINT]/[Select an option] : ")
    if phone_number_osint_page == '1':
        webbrowser.open("epieos.com")
        quit()
    elif phone_number_osint_page == '2':
        webbrowser.open("app.osint.industries")
        quit()
    elif phone_number_osint_page == '3':
        webbrowser.open("spydialer.com")
        quit()
    elif phone_number_osint_page == '4':
        webbrowser.open("slydial.com")
        quit()
    elif phone_number_osint_page == '5':
        webbrowser.open("whocalld.com")
        quit()
    elif phone_number_osint_page == '6':
        webbrowser.open("phonevalidator.com")
        quit()
    elif phone_number_osint_page == '7':
        webbrowser.open("calleridservice.com")
        quit()
    elif phone_number_osint_page == '8':
        webbrowser.open("freecarrierlookup.com")
        quit()
    elif phone_number_osint_page == '9':
        webbrowser.open("github.com/sundowndev/phoneinfoga")
        quit()
    elif phone_number_osint_page == '10':
        webbrowser.open("bhattsameer.github.io/numspy/")
        quit()
    else:
        print("Invalid option, QUITTING!")
        quit()
elif selection == '5':
    print("-" * 20 + "select a web page" + "-" * 20)
    print("1.- intelx.io")
    print("2.- app.osint.industries")
    print("3.- phonebook.cz")
    print("4.- urlscan.io")
    print("5.- tools.hixec.com whois")
    print("6.- urlvoid.com")
    print("7.- hackcontrol.org")
    print("8.- nikto.online")
    print("9.- crt.sh")
    print("10.- avg.com")
    print("11.- virustotal.com")
    print("12.- wheregoes.com")
    print("13.- visualping.io")
    print("14.- BurpSuite")
    domain_osint_selection = input("--------(-🗃️-)[Domain-OSINT]/[Select an option] : ")
    if domain_osint_selection == '1':
        webbrowser.open("intelx.io")
        quit()
    elif domain_osint_selection == '2':
        webbrowser.open("app.osint.industries")
        quit()
    elif domain_osint_selection == '3':
        webbrowser.open("phonebook.cz")
        quit()
    elif domain_osint_selection == '4':
        webbrowser.open("urlscan.io")
        quit()
    elif domain_osint_selection == '5':
        webbrowser.open("tools.hixec.com/tool/domain-whois")
        quit()
    elif domain_osint_selection == '6':
        webbrowser.open("urlvoid.com")
        quit()
    elif domain_osint_selection == '7':
        webbrowser.open("hackcontrol.org/OSINT/Domain_name.html")
        quit()
    elif domain_osint_selection == '8':
        webbrowser.open("nikto.online")
        quit()
    elif domain_osint_selection == '9':
        webbrowser.open("crt.sh")
        quit()
    elif domain_osint_selection == '10':
        webbrowser.open("avg.com")
        quit()
    elif domain_osint_selection == '11':
        webbrowser.open("virustotal.com")
        quit()
    elif domain_osint_selection == '12':
        webbrowser.open("wheregoes.com")
        quit()
    elif domain_osint_selection == '13':
        webbrowser.open("visualping.io")
        quit()
    elif domain_osint_selection == '14':
        webbrowser.open("portswigger.net/burp")
        quit()
    else:
        print("Invalid option, QUITTING!")
        quit()


elif selection == '6':
    print("-" * 20 + "create a fake profile" + "-" * 20)
    print("1.- generate random identity")
    print("2.- this person does not exist")
    print("3.- test card numbers")
    print("4.- temp mail")
    print("5.- temp number")
    fakeid = input("--------(-👽-)[Fake-profiles]/[Select an option] : ")
    if fakeid == '1':
        webbrowser.open("fakenamegenerator.com")
        quit()
    elif fakeid == '2':
        webbrowser.open("thispersondoesnotexist.com")
        quit()
    elif fakeid == '3':
        webbrowser.open("developers.bluesnap.com/reference/test-credit-cards")
        quit()
    elif fakeid == '4':
        webbrowser.open("temp-mail.org")
        quit()
    elif fakeid == '5':
        webbrowser.open("temp-number.org")
        quit()
    else: 
        print("invalid option, QUITTING!")
        quit()

elif selection == '7':
    print("-" * 20 + "select a webpage" + "-" * 20)
    print("1.- grabify.link")
    print("2.- whatismyipaddress.com")
    print("3.- intelx.io")
    print("4.- nmap.org")
    print("5.- iplocation.net")
    print("6.- iptrackeronline.com")
    print("7.- criminalip.io")
    print("8.- shodan.io")
    print("9.- ipvoid.com")
    print("10.- ipfingerprints.com")
    print("11.- abuseipdb.com")
    ip_osint_selection = input("--------(-🌐-)[IP-OSINT]/[Select an option] : ")
    if ip_osint_selection == '1':
        webbrowser.open("grabify.link")
        quit()
    elif ip_osint_selection == '2':
        webbrowser.open("whatismyipaddress.com")
        quit()
    elif ip_osint_selection == '3':
        webbrowser.open("intelx.io")
        quit()
    elif ip_osint_selection == '4':
        webbrowser.open("nmap.org")
        quit()
    elif ip_osint_selection == '5':
        webbrowser.open("iplocation.net")
        quit()
    elif ip_osint_selection == '6':
        webbrowser.open("iptrackeronline.com")
        quit()
    elif ip_osint_selection == '7':
        webbrowser.open("criminalip.io")
        quit()
    elif ip_osint_selection == '8':
        webbrowser.open("shodan.io")
        quit()
    elif ip_osint_selection == '9':
        webbrowser.open("ipvoid.com")
        quit()
    elif ip_osint_selection == '10':
        webbrowser.open("ipfingerprints.com")
        quit()
    elif ip_osint_selection == '11':
        webbrowser.open("abuseipdb.com")
        quit()
    else:
        print("Invalid option, QUITTING!")
        quit()
elif selection == '8':
    webbrowser.open("exploit-db.com/google-hacking-database")
    quit()


elif selection == '9':
    print("-" * 20 + "select an option" + "-" * 20)
    print("1.- VPN/Proxies")
    print("2.- virtual machines")
    print("3.- antimalware")
    print('4.- AD block')
    print("5.- user agent")
    print("6.- browsers")
    print("7.- Mail services")
    print("8.- Browser Extensions")
    print("9.- cookie editors")

    anonymous_option_selection = input("--------(-💀-)[Be-Anonymous]/[Select an option] : ")
    if anonymous_option_selection == '1':
        print("-" * 20 + "(VPN)" + "-" * 20)
        print("1.- NordVPN")
        print("2.- ProtonVPN")
        print("3.- SurfShark")
        print("-" * 20 + "(Web Extensions)" + "-" * 20)
        print("4.- windscribe VPN")
        print("5.- uno VPN")
        print("6.- proton VPN")
        print("7.- touch VPN")
        proxie_selection = input("--------(-💀-)[Proxies]/[Select an option] : ")
        if proxie_selection == '1':
            webbrowser.open("nordvpn.com")
            quit()
        elif proxie_selection == '2':
            webbrowser.open("protonvpn.com")
            quit()
        elif proxie_selection == '3':
            webbrowser.open("surfshark.com")
            quit()
        elif proxie_selection == '4':
            webbrowser.open("chromewebstore.google.com/detail/windscribe-free-proxy-and/hnmpcagpplmpfojmgmnngilcnanddlhb")
            quit()
        elif proxie_selection == '5':
            webbrowser.open("chromewebstore.google.com/detail/vpn-gratuito-adblock-1vpn/akcocjjpkmlniicdeemdceeajlmoabhg")
            quit()
        elif proxie_selection == '6':
            webbrowser.open("chromewebstore.google.com/detail/proton-vpn-a-swiss-vpn-yo/jplgfhpmjnbigmhklmmbgecoobifkmpa")
            quit()
        elif proxie_selection == '7':
            webbrowser.open("chromewebstore.google.com/detail/touch-vpn-proxy-y-vpn-gra/bihmplhobchoageeokmgbdihknkjbknd")
            quit()
        else:
            print("Invalid option, QUITTING!")
            quit()
    elif anonymous_option_selection == '2':
        webbrowser.open("virtualbox.org")
        quit()
    elif anonymous_option_selection == '3':
        print("-" * 20 + "select an option" + "-" * 20)
        print("1.- Kaspersky")
        print("2.- AVG")
        print("3.- Norton")
        print("4.- MCafee")
        print("5.- eset")
        print("6.- MalwareBytes")
        antivirus_selection = input("--------(-🚨-)[AntiMalware]/[Select an option] : ")
        if antivirus_selection == '1':
            webbrowser.open("kaspersky.com")
            quit()
        elif antivirus_selection == '2':
            webbrowser.open("avg.com")
            quit()
        elif antivirus_selection == '3':
            webbrowser.open("norton.com")
            quit()
        elif antivirus_selection == '4':
            webbrowser.open("mcafee.com")
            quit()
        elif antivirus_selection == '5':
            webbrowser.open("eset.com")
            quit()
        elif antivirus_selection == '6':
            webbrowser.open("malwarebytes.com")
            quit()
        else:
            print("Invalid option, QUITTING!")
            quit()
    elif anonymous_option_selection == '4':
        print("-" * 20 + "select an option" + "-" * 20)
        print("1.- Ublock")
        print("2.- Brave")
        adblock_selection = input("--------(-🔭-)[ADBLOCKERS]/[Select an option] : ")
        if adblock_selection == '1':
            webbrowser.open("ublockorigin.com")
            quit()
        elif adblock_selection == '2':
            webbrowser.open("brave.com")
            quit()
        else:
            print("Invalid option, QUITTING!")
            quit()


    elif anonymous_option_selection == '5':
        print("-" * 20 + "select an option" + "-" * 20)
        print("1.- user agent switcher")
        print("2.- user agent manager ")
        useragent_select = input("--------(-🕵️‍♂️-)[User agent Switcher]/[Select an option] : ")
        if useragent_select == '1':
            webbrowser.open("chromewebstore.google.com/detail/user-agent-switcher-for-c/djflhoibgkdhkhhcedjiklpkjnoahfmg")
            quit()
        elif useragent_select == '2':
            webbrowser.open("chromewebstore.google.com/detail/user-agent-switcher-and-m/bhchdcejhohfmigjafbampogmaanbfkg")
            quit()
        else:
            print("Invalid option, QUITTING!")
            quit()
    elif anonymous_option_selection == '6':
        print("-" * 20 + "select an option" + "-" * 20)
        print("1.- brave")
        print("2.- tor")
        print("3.- epic privacy browser")
        browser_selection = input("--------(-🌐-)[Browsers]/[Select an option] : ")
        if browser_selection == '1':
            webbrowser.open("brave.com")
            quit()
        elif browser_selection == '2':
            webbrowser.open("torproject.org")
            quit()
        elif browser_selection == '3':
            webbrowser.open("epicbrowser.com")
            quit()
        else: 
            print("Invalid option, QUITTING!")
            quit()
    elif anonymous_option_selection == '7':
        print("-" * 20 + "select an option" + "-" * 20)
        print("1.- ProtonMail")
        print("2.- DuckDuckGo Mail")
        mail_selection = input("--------(-📧-)[Mail]/[Select an option] : ")
        if mail_selection == '1':
            webbrowser.open("proton.me")
            quit()
        elif mail_selection == '2':
            webbrowser.open("duckduckgo.com/email/")
            quit()
        else:
            print("Invalid option, QUITTING!")
            quit()
    elif anonymous_option_selection == '8':
        print("-" * 20 + "select an option" + "-" * 20)
        print("1.- Captcha solver")
        print("2.- Decentral Eyes")
        print("3.- disconnect")
        print("4.- Security Tools")
        print("5.- MalwareBytes")
        print("6.- SquareX")
        print("7.- VT4browsers (virustotal)")
        extensions_select = input("--------(-🕸️-)[Extensions]/[Select an option] : ")
        if extensions_select == '1':
            webbrowser.open("chromewebstore.google.com/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl")
            quit()
        elif extensions_select == '2':
            webbrowser.open("chromewebstore.google.com/detail/decentraleyes/ldpochfccmkkmhdbclfhpagapcfdljkj")
            quit()
        elif extensions_select == '3':
            webbrowser.open("chromewebstore.google.com/detail/disconnect/jeoacafpbcihiomhlakheieifhpjdfeo")
            quit()
        elif extensions_select == '4':
            webbrowser.open("chromewebstore.google.com/detail/ip-dns-security-tools-hac/phjkepckmcnjohilmbjlcoblenhgpjmo")
            quit()
        elif extensions_select == '5':
            webbrowser.open("chromewebstore.google.com/detail/malwarebytes-browser-guar/ihcjicgdanjaechkgeegckofjjedodee")
            quit()
        elif extensions_select == '6':
            webbrowser.open("chromewebstore.google.com/detail/squarex-be-secure-anonymo/kapjaoifikajdcdehfdlmojlepfpkpoe")
            quit()
        elif extensions_select == '7':
            webbrowser.open("chromewebstore.google.com/detail/vt4browsers/efbjojhplkelaegfbieplglfidafgoka")
            quit()
        else:
            print("Invalid option, QUITTING!")
            quit()
    elif anonymous_option_selection == '9':
        print("-" * 20 + "select an option" + "-" * 20)
        print("1.- cookie editor")
        print("2.- cookie auto delete")
        cookie_manager_select = input("--------(-🍪-)[Cookies]/[Select an option] : ")
        if cookie_manager_select == '1':
            webbrowser.open("chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm")
            quit()
        elif cookie_manager_select == '2':
            webbrowser.open("chromewebstore.google.com/detail/cookie-autodelete/fhcgjolkccmbidfldomjliifgaodjagh")
            quit()
        else:
            print("Invalid option, QUITTING!")
            quit()
    else:
        print("Invalid option, QUITTING!")
        quit()


elif selection == '10':
    print("-" * 20 + "select a webpage" + "-" * 20)
    print("1.- geospy")
    print("2.- jimpl")
    print("3.- exiftool")
    print("4.- geocreepy")
    print("5.- ocr online")
    print("6.- foto forensics")
    print("7.- img ops")
    print("12.- pimeyes.com")
    print("8.- flickr.com")
    print("9.- yandex.com images")
    print("-" * 20 + "github repos" + "-" * 20)
    print("10.- ghiro")
    print("11.- xeuledoc")
    imgosintselection = input("--------(-🖼️-)[Images]/[Select an option] : ")
    if imgosintselection == '1':
        webbrowser.open("geospy.web.app")
        quit()
    elif imgosintselection == '2':
        webbrowser.open("jimpl.com")
        quit()
    elif imgosintselection == '3':
        webbrowser.open('exiftool.org')
        quit()
    elif imgosintselection == '4':
        webbrowser.open("geocreepy.com")
        quit()
    elif imgosintselection == '5':
        webbrowser.open("onlineocr.net")
        quit()
    elif imgosintselection == '6':
        webbrowser.open("fotoforensics.com")
        quit()
    elif imgosintselection == '7':
        webbrowser.open("imgops.com")
        quit()
    elif imgosintselection == '8':
        webbrowser.open("flickr.com")
        quit()
    elif imgosintselection == '9':
        webbrowser.open("yandex.com/images")
        quit()
    elif imgosintselection == '10':
        webbrowser.open("github.com/ghirensics/ghiro")
        quit()
    elif imgosintselection == '11':
        webbrowser.open('github.com/Malfrats/xeuledoc')
        quit()
    elif imgosintselection == '12':
        webbrowser.open("pimeyes.com")
    else:
        print("Invalid option, QUITTING!")
        quit()

    
elif selection == '11':
    print("-" * 20 + "select a webpage" + "-" * 20)
    print("1.- geospy")
    print("2.- metadata")
    print("3.- google maps")
    print("4.- yandex maps")
    print("5.- earth")
    print("6.- gps coordinates")
    print("7.- mapviewer")
    

    location_OSINT_selection = input("--------(-🌎-)[Locations]/[Select an option] : ")

    if location_OSINT_selection == '1':
        webbrowser.open("geospy.ai")
        quit()
    elif location_OSINT_selection == '2':
        webbrowser.open("jimpl.com")
        quit()
    elif location_OSINT_selection == '3':
        webbrowser.open("google.de/maps")
        quit()
    elif location_OSINT_selection == '4':
        webbrowser.open("yandex.com/maps")
        quit()
    elif location_OSINT_selection == '5':
        webbrowser.open("earth.google.com/web/")
        quit()
    elif location_OSINT_selection == '6':
        webbrowser.open("gps-coordinates.net")
        quit()
    elif location_OSINT_selection == '7':
        webbrowser.open("mapviewer.org")
        quit()
    else:
        print("Invalid option, QUITTING!")
        quit()


elif selection == '12':
    print("-" * 20 + "select a webpage" + "-" * 20)
    print("1.- whatsmyname")
    print("2.- namesdir.com")
    print("3.- namechk.com")
    print("4.- namecheckr.com")
    print("5.- usersearch.org")
    print("6.- checkusernames.com")
    print("7.- namecheckup.com")
    print("8.- instantusername.com")
    
    
    username_search = input("--------(-🙂-)[Username-Search]/[Select an option] : ")
    if username_search == '1':
        webbrowser.open("whatsmyname.app")
        quit()
    elif username_search == '2':
        webbrowser.open("namesdir.com")
        quit()
    elif username_search == '3':
        webbrowser.open("namechk.com")
        quit()
    elif username_search == '4':
        webbrowser.open("namecheckr.com")
        quit()
    elif username_search == '5':
        webbrowser.open("usersearch.org")
        quit()
    elif username_search == '6':
        webbrowser.open("checkusernames.com")
        quit()
    elif username_search == '7':
        webbrowser.open("namecheckup.com")
        quit()
    elif username_search == '8':
        webbrowser.open("instantusername.com")
        quit()
    else:
        print("Invalid option, QUITTING!")
        quit()
elif selection == '00':
    print('Leaving...')
    quit()
else:
    print("Invalid Option, QUITTING!")
    quit()

