import requests

# Список URL
urls = [
    'https://entermedia.io/city/chernoe-zoloto-tatnefti-15-glupyh-voprosov-o-dobyche-nefti/',
    'https://entermedia.io/city/direktsiya-parkov-i-skverov-nude-story-i-drugie/',
    'https://entermedia.io/city/prodaem-tochku-sbora-za-rubl-kak-v-kazani-razvivayut-zelenyj-biznes/',
    'https://entermedia.io/city/rostelekom-sem-tehnologij-kotorye-menyayut-zhizn-pryamo-sejchas/',
    'https://entermedia.io/city/kruzhechnyj-vedernyj-i-nadolbinskij-gid-po-pitejnym-domam-staroj-kazani/',
    'https://entermedia.io/city/v-novom-kokshane-rekonstruiruyut-zavodskuyu-shkolu-pochemu-eto-vazhno/',
    'https://entermedia.io/city/s-chistogo-lista-nachinaem-zhizn-zanovo-na-obnovlennoj-portovoj-ulitse-v-kazani/',
    'https://entermedia.io/city/10-luchshih-vsesezonnyh-glempingov-tatarstana-rejting-enter/',
    'https://entermedia.io/city/eto-shans-open-call-na-festival-mediaiskusstva-intervals-konkurs-sotsialnyh-arhitektorov-i-drugoe/',
    'https://entermedia.io/city/gid-po-inklyuzivnym-proektam-i-mestam-kazani/',
    'https://entermedia.io/city/novyj-teatr-kamala-ofitsialno-otkryt-rasskazyvaem-10-faktov-o-sovremennom-meste-prityazheniya/',
    'https://entermedia.io/city/kak-s-ulits-kazani-ubirayut-sneg-i-kto-za-eto-otvechaet/',
    'https://entermedia.io/city/15-glupyh-voprosov-o-registratsii-sobak-v-tatarstane/',
    'https://entermedia.io/city/kam-on-izuchaem-ulichnoe-iskusstvo-s-hudozhnikami-muralov-v-nizhnekamske/',
    'https://entermedia.io/city/pedagogika-infrastruktura-ravenstvo-kak-roditelskij-kruzhok-v-staroj-kazani-izmenil-podhod-k-vospitaniyu-detej-vsego-goroda/',
    'https://entermedia.io/city/v-kazani-formiruetsya-gastroklaster-na-telmana-chto-v-nem-budet-rasskazyvaet-kamastrojinvest/',
    'https://entermedia.io/city/shest-otlichij-sovetskogo-i-sovremennogo-doma-razbiraemsya-na-primere-zhk-origana/',
    'https://entermedia.io/city/kakim-stal-park-na-kvartalah-ryadom-s-bolshim-chajkovym-ozerom/',
    'https://entermedia.io/city/kak-zhili-kazanskie-velosipedisty-v-xix-veke-kolonka-kraeveda-marka-shishkina/',
    'https://entermedia.io/city/briks-v-kazani-dlya-chego-nuzhen-sammit-chto-poyavilos-v-gorode-i-kakie-ogranicheniya-vvodyat-dlya-zhitelej/',
    'https://entermedia.io/city/ot-varlamovskoj-do-ishaki-kak-po-ulitse-v-tri-kvartala-uznat-istoriyu-goroda-i-chto-sdelaet-s-rajonom-novyj-dom-na-ishaki/',
    'https://entermedia.io/city/ostrovskogo-novaya-stolbova-kak-i-zachem-zastraivat-istoricheskij-tsentr/',
    'https://entermedia.io/city/lyudi-proekty-i-proizvodstvo-kto-i-kak-menyaet-kulturnuyu-i-biznes-sredu-v-gorodah-tatarstana/',
    'https://entermedia.io/city/na-ulitse-serova-v-kazani-otkryvaetsya-bulvar-kakim-on-stal/',
    'https://entermedia.io/food/gde-otmetit-8-marta-v-kazani-restorany-spa-otel-i-vecherinki/',
    'https://entermedia.io/food/avtorskie-napitki-kontsept-stor-i-skejt-rampa-v-novom-filtre-na-shalyapina/',
    'https://entermedia.io/food/vmesto-valentinki-13-mest-gde-otmetit-14-fevralya-v-kazani/',
    'https://entermedia.io/food/bezuprechnyj-interer-i-comfort-food-v-kafe-zelenaya-grechka-na-podluzhnoj/',
    'https://entermedia.io/food/s-lyubovyu-k-traditsiyam-v-istoricheskom-tsentre-otkrylsya-restoran-tatarskoj-kuhni-umaj/',
    'https://entermedia.io/food/enter-zapustil-spetsialnye-sety-k-premii-itogi-goda-2024-v-zavedeniyah-kazani/',
    'https://entermedia.io/food/retsepty-nashih-mam-v-art-tsentre-otkrylsya-restoran-tatarskoj-kuhni-eniem/',
    'https://entermedia.io/food/gde-otmetit-novyj-god-2025-v-kazani-zagorodnye-oteli-restorany-i-vecherinki/',
    'https://entermedia.io/food/budet-vkusno-gid-po-fudhollu-novogo-art-tsentra/',
    'https://entermedia.io/food/gastronomicheskij-slovar-chast-2-razbiraemsya-v-populyarnyh-kuhnyah-desertah-hlebe-myase-i-metodah-prigotovleniya-pishhi/',
    'https://entermedia.io/food/5-legendarnyh-tatarstanskih-deserta-ot-traditsionnyh-sladostej-k-novoj-legende/',
    'https://entermedia.io/food/prostranstvo-the-revel-tihij-gedonizm-i-prostye-blyuda-iz-slozhnyh-komponentov/',
    'https://entermedia.io/food/rossijskij-restorannyj-festival-2024-kto-uchastvuet-i-chto-v-menyu/',
    'https://entermedia.io/food/kak-razvivaetsya-gastroindustriya-kazani-i-kak-na-nee-povliyaet-obnovlennyj-moskovskij-rynok/',
    'https://entermedia.io/food/gastronom-redaktsiya-enter-zapustila-set-menyu-s-blyudami-iz-detstva-v-zavedeniyah-kazani/',
    'https://entermedia.io/food/novoe-etnobistro-skazki-o-solntse-v-kazani-multikulturnaya-kuhnya-i-vnevremennaya-atmosfera/',
    'https://entermedia.io/food/fermerskie-produkty-dostavka-i-sistema-loyalnosti-kak-rabotaet-zhiznmart-v-kazani/',
    'https://entermedia.io/food/gastronom-redaktsiya-enter-obyavlyaet-mesyats-zavtrakov-s-utra-do-nochi-v-zavedeniyah-kazani/',
    'https://entermedia.io/food/gastronom-redaktsiya-enter-zapuskaet-tematicheskie-set-menyu-v-zavedeniyah-kazani/',
    'https://entermedia.io/food/sovetskie-raritety-i-eda-so-vkusom-nostalgii-v-kafe-steklyashka/',
    'https://entermedia.io/people/uchastniki-pryg-skoka-ot-enter-i-federatsii-nastolnogo-tennisa-rossii-o-lyubvi-k-kazani-sportu-i-nastupivshej-vesne/',
    'https://entermedia.io/people/vnutri-komandy-kto-formiruet-hr-brend-kazani-i-kak-meriya-kazani-privlekaet-v-gorod-luchshih-sotrudnikov/',
    'https://entermedia.io/people/osnovatelnitsa-brenda-qayna-ob-intellektualnoj-mode-mirovom-glyantse-i-sile-zhenshhin/',
    'https://entermedia.io/people/chto-ty-iz-sebya-stroish-15-glupyh-voprosov-arhitektoru/',
    'https://entermedia.io/people/vnutri-komandy-kto-i-kak-razvivaet-tsifrovizatsiyu-v-kazani/',
    'https://entermedia.io/people/baryshniki-s-tolchka-kak-zhili-kazanskie-predprinimateli-s-samoj-plohoj-reputatsiej/',
    'https://entermedia.io/people/kazanskie-inflyuensery-o-tom-kak-byt-na-svyazi-24-7-lyubimyh-mestah-dlya-udalenki-i-poiske-sebya-vne-najma/',
    'https://entermedia.io/people/kak-v-rossii-perezagruzili-hor-osnovatel-posthora-attaque-de-panique-ob-eksperimentah-v-zvuchanii-i-na-stsene/',
    'https://entermedia.io/people/gosti-brancha-finn-flare-ob-intellektualnoj-mode-rossijskih-brendah-i-metamoderne-v-novogodnih-kampejnah/',
    'https://entermedia.io/people/kto-prishel-na-premeru-podslushano-v-rybinske-gosti-ob-ozhidaniyah-ot-seriala-i-kino-v-rossii/',
    'https://entermedia.io/people/hronika-nauchnyh-otkrytij-chem-zanimayutsya-uchenye-v-laboratoriyah-kfu/',
    'https://entermedia.io/people/net-dyma-bez-ognya-15-glupyh-voprosov-pozharnomu/',
    'https://entermedia.io/people/vnutri-komandy-kto-i-kak-razvivaet-shkolu-21-v-kazani/',
    'https://entermedia.io/people/yurij-subbotin-o-vyzovah-festivalnoj-industrii-trende-na-nishevost-i-glavnyh-sobytiyah-v-2025-godu/',
    'https://entermedia.io/people/entsiklopediya-tatarstanskogo-interneta-v-memah-litsah-i-sobytiyah/',
    'https://entermedia.io/people/uzory-na-nogah-15-glupyh-voprosov-o-varikoze/',
    'https://entermedia.io/people/15-glupyh-voprosov-o-virusah/',
    'https://entermedia.io/people/rozovyj-oktyabr-15-glupyh-voprosov-o-rake-grudi/',
    'https://entermedia.io/people/zri-v-koren-kak-vidit-glaz-prichem-zdes-mozg-i-pochemu-nash-mire-ne-perevernutyj/',
    'https://entermedia.io/people/vidit-ne-vidit-15-glupyh-voprosov-o-bioekvajringe/',
    'https://entermedia.io/people/krugom-odni-polimery-kak-proshla-ekskursiya-po-nochnomu-kazanorgsintezu/',
    'https://entermedia.io/people/hudozhnitsa-zulfiya-ilkaeva-o-gorodskih-issledovaniyah-i-natsionalnyh-temah-v-iskusstve/',
    'https://entermedia.io/people/himiya-sna-mozhno-li-nauchitsya-vysypatsya/',
    'https://entermedia.io/people/kak-sozdavat-iskusstvo-kuratory-i-hudozhniki-reactor-fest-ob-itogah-rezidentsii/',
    'https://entermedia.io/people/vmeste-prosto-v-gorode-kak-proshlo-otkrytie-dvora-v-privolzhskom-rajone/',
    'https://entermedia.io/people/15-glupyh-voprosov-o-plasticheskoj-hirurgii/',
    'https://entermedia.io/people/gosti-vechera-dzhaza-i-shahmat-v-lyadskom-sadu-o-shahmatnoj-strasti-i-lyubimoj-kazani/',
    'https://entermedia.io/people/arhitektor-i-inzhener-chem-otlichayutsya-gde-uchitsya-v-kazani-i-kto-glavnee/',
    'https://entermedia.io/people/novye-kuratory-napravleniya-i-festival-kak-izmenilsya-re-actor-i-chto-predstavit-programma-v-etom-godu/',
    'https://entermedia.io/people/aleksej-suharev-o-rebrendinge-kollaboratsiyah-i-izmeneniyah-na-rossijskom-feshn-rynke/',
    'https://entermedia.io/people/vnutri-komandy-kto-i-kakie-proekty-sozdaet-v-innopolise/',
    'https://entermedia.io/people/anastasiya-slabinyak-o-tsifrovom-iskusstve-vizualnyh-metaforah-i-nure/',
    'https://entermedia.io/people/hudozhnitsa-nadya-rigova-o-yagnyatah-zhertvennosti-i-pugayushhej-realnosti/',
    'https://entermedia.io/people/glavnye-arhitektory-kazani-bugulmy-i-nizhnekamska-o-proshlom-i-budushhem-gorodov-tatarstana/',
    'https://entermedia.io/people/10-glupyh-voprosov-agronomu-hk-chistopole/',
    'https://entermedia.io/people/poznakomtes-s-lyudmi-kotorye-delayut-turnir-combonation/',
    'https://entermedia.io/people/himiya-chuvstv-kak-molekuly-rukovodyat-nashimi-emotsiyami-i-zhiznyu-v-tselom/',
    'https://entermedia.io/fashion/kak-v-modu-voshli-nesovershennye-veshhi-sviter-s-zatsepkami-nerovnye-shvy-i-asimmetriya/',
    'https://entermedia.io/fashion/balneum-spa-salon-v-kotorom-obedinili-russkuyu-banyu-i-massazh/',
    'https://entermedia.io/fashion/kult-pokloneniya-pochemu-nedelya-mody-vse-eshhe-imeet-znachenie/',
    'https://entermedia.io/fashion/o-zdorove-estetike-i-lokalnom-turizme-kak-luciano-povliyal-na-sferu-otdyha-i-uslug-kazani-za-20-let/',
    'https://entermedia.io/weekend/stendap-kontsert-maksa-evdokimova-knizhnyj-market-i-mnogoe-drugoe/',
    'https://entermedia.io/weekend/hr-brend-netvorking-i-strategiya-kto-i-zachem-primet-uchastie-v-kiberturnire-ot-k9-i-mintsifry-rt/',
    'https://entermedia.io/weekend/maslenitsa-boulevard-depo-i-mnogoe-drugoe/',
    'https://entermedia.io/weekend/gid-po-festivalyu-ulichnoj-kultury-hip-hop-kazan/',
    'https://entermedia.io/weekend/pryg-skok-v-art-tsentre-kto-igraet-chto-delat-bolelshhikam-i-gde-projdet-final/',
    'https://entermedia.io/weekend/den-vseh-vlyublennyh-hip-hop-kazan-i-mnogoe-drugoe/',
    'https://entermedia.io/weekend/enter-premier-i-reactor-vypustili-detektivnye-skretch-postery-podslushano-v-kazani/',
    'https://entermedia.io/weekend/redaktsiya-enter-i-lejbl-play-music-organizuyut-proslushivaniya-muzykantov-iz-tatarstana/',
    'https://entermedia.io/weekend/vecherinka-gde-moj-2007-vinil-market-i-mnogoe-drugoe/',
    'https://entermedia.io/weekend/den-rozhdeniya-kommunalka-lektsiya-ot-alekseya-korsi-i-mnogoe-drugoe/',
    'https://entermedia.io/city/festival-nur-developer-avtory-i-drugie/',
    'https://entermedia.io/city/kakoj-budet-territoriya-vokrug-novogo-zdaniya-teatra-kamala/',
    'https://entermedia.io/city/pyat-bulvarov-i-sadov-kazani-kotorye-my-poteryali-kolonka-kraeveda-marka-shishkina/',
    'https://entermedia.io/people/rustam-vildanov-o-mobilnom-marketinge-tendentsiyah-v-reklame-i-blagotvoritelnosti/',
    'https://entermedia.io/people/avtory-komiksa-tatarskie-zhenshhiny-o-sotsialnoj-bombe-filme-na-bumage-i-geroinyah-za-shirmoj/',
    'https://entermedia.io/people/kazanskie-dizajnery-i-illyustratory-o-profilnom-obrazovanii-zakazchikah-i-generativnyh-nejrosetyah/',
    'https://entermedia.io/people/poznakomtes-s-lyudmi-kotorye-rabotayut-na-teatralnoj-ploshhadke-mon/',
]

# User-Agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Скачивание и сохранение страницы
def download_page(url, index):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        filename = f"page_{index}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)
        return filename, url
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при скачивании {url}: {e}")
        return None, None
    except Exception as e:
        print(f"Непредвиденная ошибка при обработке {url}: {e}")
        return None, None

# Создание индексного файла
index_data = []

downloaded_count = 0
for i, url in enumerate(urls):
    filename, downloaded_url = download_page(url, i)
    if filename:
        index_data.append(f"{i}: {downloaded_url}")
        downloaded_count += 1

# Запись в индексный файл
with open("index.txt", "w", encoding="utf-8") as f:
    for line in index_data:
        f.write(line + "\n")

print(f"Скачано {downloaded_count} страниц. Создан файл index.txt")
