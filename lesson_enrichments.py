import copy


def apply_enrichments(lesson: dict, book: str, num: int) -> dict:
    enriched = copy.deepcopy(lesson)
    lesson_enrichment = ENRICHMENTS.get(book, {}).get(str(num))
    if not lesson_enrichment:
        return enriched

    grammar = enriched.setdefault("grammar", {})
    bullets = grammar.setdefault("bullets", [])
    for bullet in lesson_enrichment.get("bullets", []):
        if bullet not in bullets:
            bullets.append(bullet)

    phrases = enriched.setdefault("phrases", [])
    existing_phrase_ge = {item.get("ge") for item in phrases if isinstance(item, dict)}
    for phrase in lesson_enrichment.get("phrases", []):
        ge = phrase.get("ge")
        if ge and ge not in existing_phrase_ge:
            phrases.append(phrase)
            existing_phrase_ge.add(ge)

    vocab = enriched.setdefault("vocab", [])
    existing_vocab_ge = {item.get("ge") for item in vocab if isinstance(item, dict)}
    for item in lesson_enrichment.get("extra_vocab", []):
        ge = item.get("ge")
        if ge and ge not in existing_vocab_ge:
            vocab.append(item)
            existing_vocab_ge.add(ge)

    return enriched


ENRICHMENTS = {
    "a2": {
        "1": {
            "bullets": [
                "Genitive of names: vowel endings usually take -ს, consonant endings take -ის.",
                "Compound kinship words are common: და-ძმა, დედ-მამა, ბებია-ბაბუა.",
                "Time span uses -იდან ... -ამდე to show from and to.",
                "Possession phrases stay compact: noun+noun often replaces long relative clauses.",
            ],
            "phrases": [
                {"ge": "გიორგის და უნივერსიტეტში სწავლობს.", "en": "Giorgi's sister studies at university.", "ru": "Сестра Георгия учится в университете."},
                {"ge": "ორშაბათიდან პარასკევამდე სამსახურში ვარ.", "en": "From Monday to Friday I am at work.", "ru": "С понедельника до пятницы я на работе."},
                {"ge": "ეს ანას ბიძაშვილია.", "en": "This is Ana's cousin.", "ru": "Это двоюродный брат/сестра Аны."},
                {"ge": "ჩვენი ოჯახი ძალიან მეგობრულია.", "en": "Our family is very friendly.", "ru": "Наша семья очень дружная."},
                {"ge": "შაბათს სტუმრები გვყავს.", "en": "On Saturday we have guests.", "ru": "В субботу у нас гости."},
                {"ge": "მარტო არ ვცხოვრობ, ძმასთან ერთად ვარ.", "en": "I do not live alone, I live with my brother.", "ru": "Я не живу один, я живу с братом."},
            ],
            "extra_vocab": [
                {"ge": "ნათლია", "en": "godparent", "ru": "крестный/крестная", "group": "Family"},
                {"ge": "ნათესაობა", "en": "kinship", "ru": "родство", "group": "Family"},
                {"ge": "საოჯახო", "en": "family-related", "ru": "семейный", "group": "Family"},
                {"ge": "ურთიერთობა", "en": "relationship", "ru": "отношения", "group": "Social life"},
                {"ge": "დროის მონაკვეთი", "en": "time period", "ru": "период времени", "group": "Time"},
                {"ge": "დღის რეჟიმი", "en": "daily routine", "ru": "режим дня", "group": "Life"},
            ],
        },
        "2": {
            "bullets": [
                "Instrumental -ით answers how/with what/by what means.",
                "Adjectives with -იანი often describe weather, quality, or surface traits.",
                "Geographic description often stacks adjectives before the noun.",
                "Cardinal direction nouns behave like regular nouns in phrases.",
            ],
            "phrases": [
                {"ge": "საქართველო მთიანი და ტყიანი ქვეყანაა.", "en": "Georgia is a mountainous and forested country.", "ru": "Грузия — горная и лесистая страна."},
                {"ge": "ზაფხულში ზღვისპირა ქალაქები ძალიან ცხელია.", "en": "In summer seaside cities are very hot.", "ru": "Летом приморские города очень жаркие."},
                {"ge": "ზამთარში თოვლიანი ამინდია კავკასიაში.", "en": "In winter the weather is snowy in the Caucasus.", "ru": "Зимой на Кавказе снежная погода."},
                {"ge": "ავტობუსით წავედით დასავლეთ საქართველოში.", "en": "We went to western Georgia by bus.", "ru": "Мы поехали на автобусе в западную Грузию."},
                {"ge": "ეს მხარე ძალიან მწვანეა.", "en": "This region is very green.", "ru": "Этот край очень зеленый."},
                {"ge": "ჩრდილოეთით მაღალი მთებია.", "en": "There are high mountains in the north.", "ru": "На севере высокие горы."},
            ],
            "extra_vocab": [
                {"ge": "ველი", "en": "plain/field", "ru": "равнина/поле", "group": "Geography"},
                {"ge": "ხეობა", "en": "valley", "ru": "долина", "group": "Geography"},
                {"ge": "კლიმატი", "en": "climate", "ru": "климат", "group": "Weather"},
                {"ge": "ნოტიო", "en": "humid", "ru": "влажный", "group": "Weather"},
                {"ge": "მშრალი ჰავა", "en": "dry climate", "ru": "сухой климат", "group": "Weather"},
                {"ge": "სიმაღლე", "en": "altitude/height", "ru": "высота", "group": "Geography"},
            ],
        },
        "3": {
            "bullets": [
                "Adjective comes before noun in neutral word order.",
                "Time adverbs like დილით/საღამოს often stand first for emphasis.",
                "Frequency with -ჯერ gives clear count expressions.",
                "Household and lifestyle descriptions often use parallel adjective pairs.",
            ],
            "phrases": [
                {"ge": "დილით ადრე ვდგები და ყავას ვსვამ.", "en": "I get up early in the morning and drink coffee.", "ru": "Утром я рано встаю и пью кофе."},
                {"ge": "საღამოს ოჯახთან ერთად ვვახშმობ.", "en": "In the evening I have dinner with my family.", "ru": "Вечером я ужинаю с семьей."},
                {"ge": "კვირაში ორჯერ სპორტდარბაზში დავდივარ.", "en": "I go to the gym twice a week.", "ru": "Два раза в неделю я хожу в спортзал."},
                {"ge": "ჩვენს სახლში ნათელი მისაღები ოთახია.", "en": "Our house has a bright living room.", "ru": "В нашем доме светлая гостиная."},
                {"ge": "ღამით მალე ვიძინებ.", "en": "At night I go to sleep quickly.", "ru": "Ночью я быстро засыпаю."},
                {"ge": "მეზობლები ძალიან წყნარები არიან.", "en": "The neighbors are very calm.", "ru": "Соседи очень спокойные."},
            ],
            "extra_vocab": [
                {"ge": "მისაღები ოთახი", "en": "living room", "ru": "гостиная", "group": "Home"},
                {"ge": "ყოველკვირა", "en": "every week", "ru": "каждую неделю", "group": "Time"},
                {"ge": "ჩვეულება", "en": "habit/custom", "ru": "привычка", "group": "Lifestyle"},
                {"ge": "დაძინება", "en": "to fall asleep", "ru": "засыпать", "group": "Daily routine"},
                {"ge": "გაღვიძება", "en": "to wake up", "ru": "просыпаться", "group": "Daily routine"},
                {"ge": "მოწესრიგებული", "en": "organized/tidy", "ru": "организованный", "group": "Descriptions"},
            ],
        },
        "4": {
            "bullets": [
                "Ordinals after პირველი are mostly predictable in form.",
                "იყო/ჰქონდა/ჰყავდა are core past narration verbs.",
                "Reported speech marker -ო appears in storytelling and hearsay.",
                "Character descriptions combine profession + adjective naturally.",
            ],
            "phrases": [
                {"ge": "ჩემი მეორე მეზობელი ექიმი იყო.", "en": "My second neighbor was a doctor.", "ru": "Мой второй сосед был врачом."},
                {"ge": "მას დიდი გამოცდილება ჰქონდა.", "en": "He/she had great experience.", "ru": "У него/неё был большой опыт."},
                {"ge": "მეგობარს ძაღლი ჰყავდა.", "en": "My friend had a dog.", "ru": "У друга была собака."},
                {"ge": "ყველა ამბობდა, ძალიან კეთილიაო.", "en": "Everyone said that he/she is very kind.", "ru": "Все говорили, что он/она очень добрый(ая)."},
                {"ge": "მესამე სართულზე ახალი ოჯახი გადმოვიდა.", "en": "A new family moved to the third floor.", "ru": "На третий этаж переехала новая семья."},
                {"ge": "ის ძალიან მხიარული ადამიანი იყო.", "en": "He/she was a very cheerful person.", "ru": "Это был очень веселый человек."},
            ],
            "extra_vocab": [
                {"ge": "ხასიათის აღწერა", "en": "character description", "ru": "описание характера", "group": "People"},
                {"ge": "ნიჭიერი", "en": "talented", "ru": "талантливый", "group": "Descriptions"},
                {"ge": "თავმდაბალი", "en": "modest", "ru": "скромный", "group": "Descriptions"},
                {"ge": "გულწრფელი", "en": "sincere", "ru": "искренний", "group": "Descriptions"},
                {"ge": "შრომისმოყვარე", "en": "hardworking", "ru": "трудолюбивый", "group": "Descriptions"},
                {"ge": "ბავშვობიდან", "en": "since childhood", "ru": "с детства", "group": "Time"},
            ],
        },
        "5": {
            "bullets": [
                "Comparative pattern: უფრო + adjective + ვიდრე.",
                "Superlative pattern: ყველაზე + adjective.",
                "Indefinite pronouns help keep speech flexible and polite.",
                "City-tour speech often chains location words with comparisons.",
            ],
            "phrases": [
                {"ge": "ეს მუზეუმი უფრო საინტერესოა, ვიდრე ის.", "en": "This museum is more interesting than that one.", "ru": "Этот музей интереснее, чем тот."},
                {"ge": "თბილისში ვინმე კარგი გიდი ხომ არ იცი?", "en": "Do you know any good guide in Tbilisi?", "ru": "Ты не знаешь хорошего гида в Тбилиси?"},
                {"ge": "სადმე ძველ უბანში წავიდეთ.", "en": "Let's go somewhere in the old district.", "ru": "Пойдем куда-нибудь в старый район."},
                {"ge": "არაფერი განსაკუთრებული არ გვინახავს.", "en": "We did not see anything special.", "ru": "Мы ничего особенного не увидели."},
                {"ge": "ეს ხიდი ყველაზე ლამაზია საღამოს.", "en": "This bridge is the most beautiful in the evening.", "ru": "Этот мост самый красивый вечером."},
                {"ge": "რამდენიმე საათი ქალაქში ვიარეთ.", "en": "We walked around the city for several hours.", "ru": "Мы гуляли по городу несколько часов."},
            ],
            "extra_vocab": [
                {"ge": "საექსკურსიო", "en": "for excursions", "ru": "экскурсионный", "group": "Travel"},
                {"ge": "მონუმენტი", "en": "monument", "ru": "монумент", "group": "Sightseeing"},
                {"ge": "ღირსშესანიშნაობა", "en": "landmark", "ru": "достопримечательность", "group": "Sightseeing"},
                {"ge": "ძეგლი", "en": "statue/memorial", "ru": "памятник", "group": "Sightseeing"},
                {"ge": "პანორამა", "en": "panorama", "ru": "панорама", "group": "Sightseeing"},
                {"ge": "გასეირნება", "en": "walk/stroll", "ru": "прогулка", "group": "Travel"},
            ],
        },
        "6": {
            "bullets": [
                "Comparative and equality patterns can appear in one sentence.",
                "Routine adverbs often stand before the main verb.",
                "Daily-sequence narration benefits from clear time anchors.",
                "Kitchen/home routines naturally combine action + object chunks.",
            ],
            "phrases": [
                {"ge": "ჩვეულებრივ შვიდ საათზე ვიღვიძებ.", "en": "I usually wake up at seven o'clock.", "ru": "Обычно я просыпаюсь в семь часов."},
                {"ge": "ხანდახან სახლში ვსაუზმობ.", "en": "Sometimes I have breakfast at home.", "ru": "Иногда я завтракаю дома."},
                {"ge": "ჩემი დღე უფრო დატვირთულია, ვიდრე ადრე.", "en": "My day is busier than before.", "ru": "Мой день более загружен, чем раньше."},
                {"ge": "ჩემი საღამო ისეთივე მშვიდია, როგორც შაბათი.", "en": "My evening is as calm as Saturday.", "ru": "Мой вечер такой же спокойный, как суббота."},
                {"ge": "თითქმის ყოველდღე თვითონ ვამზადებ სადილს.", "en": "Almost every day I cook lunch myself.", "ru": "Почти каждый день я сам(а) готовлю обед."},
                {"ge": "საღამოს სამზარეულოს ვალაგებ.", "en": "In the evening I tidy the kitchen.", "ru": "Вечером я прибираю кухню."},
            ],
            "extra_vocab": [
                {"ge": "საუზმე", "en": "breakfast", "ru": "завтрак", "group": "Meals"},
                {"ge": "სადილი", "en": "lunch", "ru": "обед", "group": "Meals"},
                {"ge": "ვახშამი", "en": "dinner", "ru": "ужин", "group": "Meals"},
                {"ge": "სამუშაო დღე", "en": "workday", "ru": "рабочий день", "group": "Routine"},
                {"ge": "დასვენების დღე", "en": "day off", "ru": "выходной", "group": "Routine"},
                {"ge": "გეგმა", "en": "plan", "ru": "план", "group": "Time"},
            ],
        },
        "7": {
            "bullets": [
                "Conjunctions build longer natural speech: და, მაგრამ, თუმცა, იმიტომ რომ.",
                "Reported meaning with -ო is common in stories and retellings.",
                "Word-building suffixes add nuance without changing core meaning.",
                "Weekend narration often alternates plans vs actual outcomes.",
            ],
            "phrases": [
                {"ge": "შაბათს ბაზარში წავედი, მაგრამ ყველაფერი ვერ ვიყიდე.", "en": "On Saturday I went to the market, but I could not buy everything.", "ru": "В субботу я пошел(шла) на рынок, но не все купил(а)."},
                {"ge": "კვირას სახლში დავრჩით, იმიტომ რომ წვიმდა.", "en": "On Sunday we stayed home because it was raining.", "ru": "В воскресенье мы остались дома, потому что шел дождь."},
                {"ge": "თუ დრო გვექნება, პარკში გავისეირნებთ.", "en": "If we have time, we will walk in the park.", "ru": "Если у нас будет время, погуляем в парке."},
                {"ge": "მეგობარმა თქვა, იაფი ხილიო.", "en": "My friend said the fruit was cheap.", "ru": "Друг сказал, что фрукты дешевые."},
                {"ge": "ბაზარში დიდი არჩევანია და ფასიც კარგია.", "en": "There is a big choice at the market and the price is good too.", "ru": "На рынке большой выбор и цена тоже хорошая."},
                {"ge": "ხილი ვიყიდე, თუმცა ბოსტნეული აღარ იყო.", "en": "I bought fruit, although there were no vegetables left.", "ru": "Я купил(а) фрукты, хотя овощей уже не было."},
            ],
            "extra_vocab": [
                {"ge": "შესყიდვა", "en": "purchase", "ru": "покупка", "group": "Shopping"},
                {"ge": "სათადარიგო", "en": "spare/additional", "ru": "запасной", "group": "Shopping"},
                {"ge": "სასურსათო", "en": "grocery", "ru": "продуктовый", "group": "Shopping"},
                {"ge": "მთლიანი", "en": "whole/entire", "ru": "целый", "group": "Quantities"},
                {"ge": "კილო ნახევარი", "en": "half a kilo", "ru": "полкило", "group": "Quantities"},
                {"ge": "გამყიდველი", "en": "seller", "ru": "продавец", "group": "People"},
            ],
        },
        "8": {
            "bullets": [
                "Purpose/place nouns with სა- often denote functional spaces.",
                "Postpositions usually require genitive before them in formal language.",
                "Bank communication favors polite imperatives and service formulas.",
                "Financial topics rely on fixed collocations (interest rate, term, form).",
            ],
            "phrases": [
                {"ge": "კრედიტის პირობების შესახებ ინფორმაცია მინდა.", "en": "I want information about loan conditions.", "ru": "Мне нужна информация об условиях кредита."},
                {"ge": "გთხოვთ, ანკეტა სრულად შეავსეთ.", "en": "Please fill in the form completely.", "ru": "Пожалуйста, заполните анкету полностью."},
                {"ge": "საპროცენტო განაკვეთი რამდენია?", "en": "What is the interest rate?", "ru": "Какая процентная ставка?"},
                {"ge": "ანგარიშზე თანხა უკვე ჩაირიცხა.", "en": "The money has already been deposited to the account.", "ru": "Деньги уже зачислены на счет."},
                {"ge": "დაელოდეთ, კონსულტანტს ახლავე მოგიხმობთ.", "en": "Please wait, I will call the consultant right away.", "ru": "Подождите, сейчас позову консультанта."},
                {"ge": "მობრძანდით სალაროსთან.", "en": "Please come to the cash desk.", "ru": "Подойдите, пожалуйста, к кассе."},
            ],
            "extra_vocab": [
                {"ge": "ბალანსი", "en": "balance", "ru": "баланс", "group": "Banking"},
                {"ge": "ვალდებულება", "en": "obligation", "ru": "обязательство", "group": "Banking"},
                {"ge": "სესხი", "en": "loan", "ru": "заем", "group": "Banking"},
                {"ge": "განაცხადის ნომერი", "en": "application number", "ru": "номер заявки", "group": "Documents"},
                {"ge": "დოკუმენტაცია", "en": "documentation", "ru": "документация", "group": "Documents"},
                {"ge": "შეთანხმება", "en": "agreement", "ru": "соглашение", "group": "Legal"},
            ],
        },
        "9": {
            "bullets": [
                "Modal markers (უნდა, შეიძლება, შემიძლია) shape advice and rules.",
                "Health complaints often use მაქვს / მტკივა constructions.",
                "Doctor-patient speech uses polite imperative and reassurance.",
                "Modal chains help explain what is possible vs necessary.",
            ],
            "phrases": [
                {"ge": "ორი დღეა თავი მტკივა.", "en": "I have had a headache for two days.", "ru": "У меня два дня болит голова."},
                {"ge": "ექიმმა მითხრა, მეტი წყალი უნდა დალიო.", "en": "The doctor told me you should drink more water.", "ru": "Врач сказал, что нужно пить больше воды."},
                {"ge": "შეიძლება ეს წამალი დღეში ორჯერ მივიღო?", "en": "May I take this medicine twice a day?", "ru": "Можно принимать это лекарство два раза в день?"},
                {"ge": "არ შეიძლება სიცხით გარეთ გასვლა.", "en": "You must not go outside with a fever.", "ru": "Нельзя выходить на улицу с температурой."},
                {"ge": "შემიძლია ხვალ ანალიზის ჩაბარება?", "en": "Can I do the test tomorrow?", "ru": "Могу я сдать анализ завтра?"},
                {"ge": "გთხოვთ, პაციენტი ჯერ გასინჯეთ.", "en": "Please examine the patient first.", "ru": "Пожалуйста, сначала осмотрите пациента."},
            ],
            "extra_vocab": [
                {"ge": "დიაგნოზი", "en": "diagnosis", "ru": "диагноз", "group": "Medical care"},
                {"ge": "რეცეპტი", "en": "prescription", "ru": "рецепт", "group": "Medical care"},
                {"ge": "დოზა", "en": "dose", "ru": "доза", "group": "Medical care"},
                {"ge": "გვერდითი ეფექტი", "en": "side effect", "ru": "побочный эффект", "group": "Medical care"},
                {"ge": "აღდგენა", "en": "recovery", "ru": "восстановление", "group": "Health"},
                {"ge": "პრევენცია", "en": "prevention", "ru": "профилактика", "group": "Health"},
            ],
        },
        "10": {
            "bullets": [
                "Formal imperative often takes -ეთ endings.",
                "Stem contraction appears in oblique forms of many nouns.",
                "Service interactions combine command + politeness markers.",
                "Home-shopping talk mixes color, size, and function adjectives.",
            ],
            "phrases": [
                {"ge": "გთხოვთ, მისამართი სწორად დაწერეთ.", "en": "Please write the address correctly.", "ru": "Пожалуйста, правильно напишите адрес."},
                {"ge": "ინებეთ, ეს ახალი კატალოგია.", "en": "Here you are, this is the new catalog.", "ru": "Вот, пожалуйста, это новый каталог."},
                {"ge": "მობრძანდით და ავეჯი ადგილზე ნახეთ.", "en": "Please come and see the furniture on site.", "ru": "Приходите и посмотрите мебель на месте."},
                {"ge": "ეს თარო უფრო პრაქტიკულია პატარა ბინისთვის.", "en": "This shelf is more practical for a small apartment.", "ru": "Эта полка практичнее для маленькой квартиры."},
                {"ge": "ფარდა ღია ფერის ავარჩიოთ.", "en": "Let's choose light-colored curtains.", "ru": "Давайте выберем шторы светлого цвета."},
                {"ge": "სარეცხი მანქანა ხვალ მოიტანეთ.", "en": "Please bring the washing machine tomorrow.", "ru": "Привезите стиральную машину завтра."},
            ],
            "extra_vocab": [
                {"ge": "ავეჯი", "en": "furniture", "ru": "мебель", "group": "Home"},
                {"ge": "ინტერიერი", "en": "interior", "ru": "интерьер", "group": "Home"},
                {"ge": "რემონტი", "en": "renovation", "ru": "ремонт", "group": "Home"},
                {"ge": "ზომა", "en": "size/measurement", "ru": "размер", "group": "Shopping"},
                {"ge": "განლაგება", "en": "layout/placement", "ru": "расположение", "group": "Home"},
                {"ge": "შეკვეთის მიწოდება", "en": "order delivery", "ru": "доставка заказа", "group": "Shopping"},
            ],
        },
        "11": {
            "bullets": [
                "Prefix მო- can soften taste adjectives: slightly sweet/sour.",
                "Wine descriptions often combine taste + aroma + finish.",
                "Location markers help navigate festival spaces precisely.",
                "Cultural vocabulary around wine is often metaphorical and fixed.",
            ],
            "phrases": [
                {"ge": "ეს ღვინო ოდნავ მომჟავოა, მაგრამ სასიამოვნოა.", "en": "This wine is slightly sour, but pleasant.", "ru": "Это вино слегка кислое, но приятное."},
                {"ge": "რომელი კუთხის ღვინოა ეს?", "en": "From which region is this wine?", "ru": "Из какого региона это вино?"},
                {"ge": "დეგუსტაციის ზონა შესასვლელთანაა.", "en": "The tasting area is near the entrance.", "ru": "Зона дегустации находится у входа."},
                {"ge": "გვერდით დგას ადგილობრივი მწარმოებელი.", "en": "A local producer is standing nearby.", "ru": "Рядом стоит местный производитель."},
                {"ge": "სუნი ძალიან ხილისებრია.", "en": "The aroma is very fruity.", "ru": "Аромат очень фруктовый."},
                {"ge": "ყანწით დალევა ტრადიციად ითვლება.", "en": "Drinking from a horn is considered a tradition.", "ru": "Пить из рога считается традицией."},
            ],
            "extra_vocab": [
                {"ge": "დეგუსტაცია", "en": "tasting", "ru": "дегустация", "group": "Wine culture"},
                {"ge": "არომატი", "en": "aroma", "ru": "аромат", "group": "Wine culture"},
                {"ge": "დაყენება", "en": "fermentation/aging setup", "ru": "выдержка/настаивание", "group": "Wine production"},
                {"ge": "რთველი", "en": "grape harvest", "ru": "ртвели/сбор винограда", "group": "Wine production"},
                {"ge": "ვენახი", "en": "vineyard", "ru": "виноградник", "group": "Wine production"},
                {"ge": "ქვევრი", "en": "qvevri clay vessel", "ru": "квеври", "group": "Wine production"},
            ],
        },
        "12": {
            "bullets": [
                "Similarity can be expressed with -ის მსგავსი and -ივით.",
                "Host-guest formulas are culturally fixed and widely reused.",
                "Comparison structures help discuss traditions and manners.",
                "Hospitality speech often blends respect and warmth markers.",
            ],
            "phrases": [
                {"ge": "მასპინძელი სტუმარს სიხარულით ხვდება.", "en": "The host welcomes the guest with joy.", "ru": "Хозяин встречает гостя с радостью."},
                {"ge": "ეს კერძი ქართლურის მსგავსია.", "en": "This dish is similar to a Kartlian one.", "ru": "Это блюдо похоже на картлийское."},
                {"ge": "ბავშვივით გახარებული იყო სტუმარი.", "en": "The guest was happy like a child.", "ru": "Гость был рад как ребенок."},
                {"ge": "ისეთი სუფრა იყო, როგორც დღესასწაულზე.", "en": "The table was such as at a holiday feast.", "ru": "Стол был как на празднике."},
                {"ge": "თამადამ საინტერესო სადღეგრძელო თქვა.", "en": "The toastmaster made an interesting toast.", "ru": "Тамада сказал интересный тост."},
                {"ge": "ქართულ ოჯახში სტუმარს დიდ პატივს სცემენ.", "en": "In a Georgian family guests are greatly respected.", "ru": "В грузинской семье гостя очень уважают."},
            ],
            "extra_vocab": [
                {"ge": "სტუმართმოყვარეობა", "en": "hospitality", "ru": "гостеприимство", "group": "Culture"},
                {"ge": "პატივისცემა", "en": "respect", "ru": "уважение", "group": "Culture"},
                {"ge": "წესი", "en": "custom/rule", "ru": "обычай/правило", "group": "Culture"},
                {"ge": "მოსაწვევი", "en": "invitation", "ru": "приглашение", "group": "Social life"},
                {"ge": "მისალმება", "en": "greeting", "ru": "приветствие", "group": "Social life"},
                {"ge": "გამასპინძლება", "en": "to host/treat guests", "ru": "угощать/принимать гостей", "group": "Social life"},
            ],
        },
    },
    "a2plus": {
        "1": {
            "bullets": [
                "Passive-style economic reporting keeps focus on process, not person.",
                "Trend verbs like იზრდება/ძლიერდება are key for statistics language.",
                "Trade contexts often pair export and import as contrast.",
                "Economic discussion uses fixed noun collocations (market demand, revenue growth).",
            ],
            "phrases": [
                {"ge": "ქართული ღვინის ექსპორტი წლიდან წლამდე იზრდება.", "en": "The export of Georgian wine grows year by year.", "ru": "Экспорт грузинского вина растет из года в год."},
                {"ge": "ადგილობრივი წარმოება საერთაშორისო ბაზარზე ძლიერდება.", "en": "Local production is strengthening in the international market.", "ru": "Местное производство укрепляется на международном рынке."},
                {"ge": "იმპორტის შემცირება ბიუჯეტს ეხმარება.", "en": "Reducing imports helps the budget.", "ru": "Сокращение импорта помогает бюджету."},
                {"ge": "მაღალი მოთხოვნის გამო საწარმო ფართოვდება.", "en": "Because of high demand, the enterprise is expanding.", "ru": "Из-за высокого спроса предприятие расширяется."},
                {"ge": "საგარეო ბაზარზე ახალი კონტრაქტები დაიდო.", "en": "New contracts were made on the foreign market.", "ru": "На внешнем рынке заключены новые контракты."},
                {"ge": "ექსპორტით ქვეყანაში მეტი შემოსავალი შემოდის.", "en": "More revenue enters the country through exports.", "ru": "Через экспорт в страну поступает больше дохода."},
            ],
            "extra_vocab": [
                {"ge": "სავაჭრო ბალანსი", "en": "trade balance", "ru": "торговый баланс", "group": "Trade"},
                {"ge": "გაყიდვების ზრდა", "en": "sales growth", "ru": "рост продаж", "group": "Market"},
                {"ge": "ბაზრის წილი", "en": "market share", "ru": "доля рынка", "group": "Market"},
                {"ge": "კონტრაქტი", "en": "contract", "ru": "контракт", "group": "Trade"},
                {"ge": "მიმწოდებელი", "en": "supplier", "ru": "поставщик", "group": "Trade"},
                {"ge": "მოგების მარჟა", "en": "profit margin", "ru": "маржа прибыли", "group": "Finance"},
            ],
        },
        "2": {
            "bullets": [
                "Product labels rely on short noun chains for key data.",
                "Genitive + postposition gives formal packaging information.",
                "Quality adjectives (-იანი, -ური) help classify goods quickly.",
                "Comparing natural vs artificial is central in label reading.",
            ],
            "phrases": [
                {"ge": "ეტიკეტზე პროდუქტის შემადგენლობა დეტალურად წერია.", "en": "The product composition is written in detail on the label.", "ru": "Состав продукта подробно указан на этикетке."},
                {"ge": "ვადის გასვლის თარიღი აუცილებლად შეამოწმეთ.", "en": "Always check the expiration date.", "ru": "Обязательно проверяйте срок годности."},
                {"ge": "ეს პროდუქტი ორგანულია და სერტიფიკატი აქვს.", "en": "This product is organic and has a certificate.", "ru": "Этот продукт органический и имеет сертификат."},
                {"ge": "ხელნაკეთი ყველი უფრო ძვირია, მაგრამ ხარისხიანია.", "en": "Handmade cheese is more expensive, but high-quality.", "ru": "Ручной сыр дороже, но качественнее."},
                {"ge": "შეფუთვაზე წონა და მოცულობა მითითებულია.", "en": "Weight and volume are indicated on the packaging.", "ru": "На упаковке указаны вес и объем."},
                {"ge": "ფასდაკლება მხოლოდ ამ კვირაში მოქმედებს.", "en": "The discount is valid only this week.", "ru": "Скидка действует только на этой неделе."},
            ],
            "extra_vocab": [
                {"ge": "კვებითი ღირებულება", "en": "nutritional value", "ru": "пищевая ценность", "group": "Nutrition"},
                {"ge": "ენერგეტიკული ღირებულება", "en": "energy value", "ru": "энергетическая ценность", "group": "Nutrition"},
                {"ge": "ალერგენი", "en": "allergen", "ru": "аллерген", "group": "Health"},
                {"ge": "შენახვის პირობები", "en": "storage conditions", "ru": "условия хранения", "group": "Labeling"},
                {"ge": "გახსნის შემდეგ", "en": "after opening", "ru": "после открытия", "group": "Labeling"},
                {"ge": "საკვები დანამატი", "en": "food additive", "ru": "пищевая добавка", "group": "Labeling"},
            ],
        },
        "3": {
            "bullets": [
                "Emergency instructions prioritize necessity and sequence.",
                "Formal imperative is preferred in urgent public communication.",
                "Accurate location and symptom details are essential.",
                "Short direct sentences improve response speed in emergencies.",
            ],
            "phrases": [
                {"ge": "სასწრაფოდ დარეკეთ 112-ზე.", "en": "Call 112 immediately.", "ru": "Срочно позвоните на 112."},
                {"ge": "დაშავებული უგონოდაა და სუნთქვა უჭირს.", "en": "The injured person is unconscious and has difficulty breathing.", "ru": "Пострадавший без сознания и ему трудно дышать."},
                {"ge": "მისამართი ზუსტად გვითხარით.", "en": "Tell us the address precisely.", "ru": "Точно скажите адрес."},
                {"ge": "ოპერატორის ინსტრუქციას აუცილებლად მიჰყევით.", "en": "Follow the operator's instructions without fail.", "ru": "Обязательно следуйте инструкциям оператора."},
                {"ge": "ხანძარია, შენობაში ხალხი დარჩა.", "en": "There is a fire, people remained in the building.", "ru": "Пожар, в здании остались люди."},
                {"ge": "დაელოდეთ ადგილზე მაშველებს.", "en": "Wait for rescuers at the location.", "ru": "Дождитесь спасателей на месте."},
            ],
            "extra_vocab": [
                {"ge": "მაშველი", "en": "rescuer", "ru": "спасатель", "group": "Emergency"},
                {"ge": "ევაკუაცია", "en": "evacuation", "ru": "эвакуация", "group": "Emergency"},
                {"ge": "პირველი დახმარება", "en": "first aid", "ru": "первая помощь", "group": "Medical"},
                {"ge": "სუნთქვის გაძნელება", "en": "breathing difficulty", "ru": "затрудненное дыхание", "group": "Medical"},
                {"ge": "გონების დაკარგვა", "en": "loss of consciousness", "ru": "потеря сознания", "group": "Medical"},
                {"ge": "შემთხვევის ადგილი", "en": "incident scene", "ru": "место происшествия", "group": "Reporting"},
            ],
        },
        "4": {
            "bullets": [
                "Lost-item reports need clear object description + time + place.",
                "Formulas like დამეკარგა express accidental loss naturally.",
                "Police interaction requires polite question structures.",
                "Identity and ownership terms are central to reports.",
            ],
            "phrases": [
                {"ge": "გუშინ მეტროში საფულე დამეკარგა.", "en": "Yesterday I lost my wallet in the metro.", "ru": "Вчера в метро я потерял(а) кошелек."},
                {"ge": "ნივთის ფერი და ზომა ზუსტად აღვწერე.", "en": "I described the item's color and size precisely.", "ru": "Я точно описал(а) цвет и размер вещи."},
                {"ge": "შეიძლება გკითხოთ, სად უნდა დავწერო განცხადება?", "en": "May I ask where I should write the statement?", "ru": "Можно спросить, где мне написать заявление?"},
                {"ge": "პოლიციელმა ოქმი შეადგინა.", "en": "The police officer drafted a report.", "ru": "Полицейский составил протокол."},
                {"ge": "ნაპოვნი დოკუმენტები განყოფილებაშია.", "en": "The found documents are in the department.", "ru": "Найденные документы в отделении."},
                {"ge": "მფლობელის პოვნის შემდეგ ნივთი დავაბრუნეთ.", "en": "After finding the owner, we returned the item.", "ru": "После нахождения владельца мы вернули вещь."},
            ],
            "extra_vocab": [
                {"ge": "ძებნა", "en": "search", "ru": "поиск", "group": "Recovery"},
                {"ge": "მფლობელობა", "en": "ownership", "ru": "владение", "group": "Legal"},
                {"ge": "აღმოჩენა", "en": "discovery/finding", "ru": "обнаружение", "group": "Recovery"},
                {"ge": "დაკარგვის ადგილი", "en": "place of loss", "ru": "место утери", "group": "Reporting"},
                {"ge": "დროითი მონაკვეთი", "en": "time interval", "ru": "временной промежуток", "group": "Reporting"},
                {"ge": "საგამოძიებო", "en": "investigative", "ru": "следственный", "group": "Police"},
            ],
        },
        "5": {
            "bullets": [
                "Tour offers rely on duration and inclusion structures.",
                "Forms with -დღიანი quickly encode trip length.",
                "Comparative language helps evaluate alternatives.",
                "Pricing expressions often combine what is included/excluded.",
            ],
            "phrases": [
                {"ge": "სამდღიანი ტური მთაში ძალიან პოპულარულია.", "en": "A three-day mountain tour is very popular.", "ru": "Трехдневный тур в горы очень популярен."},
                {"ge": "ტურის ფასში ტრანსფერი და გიდი შედის.", "en": "Transfer and guide are included in the tour price.", "ru": "В стоимость тура входят трансфер и гид."},
                {"ge": "ეს მარშრუტი უფრო კომფორტულია ოჯახებისთვის.", "en": "This route is more comfortable for families.", "ru": "Этот маршрут более комфортный для семей."},
                {"ge": "დაჯავშნა გამგზავრებამდე ერთი კვირით ადრე გავაკეთეთ.", "en": "We booked one week before departure.", "ru": "Мы забронировали за неделю до выезда."},
                {"ge": "დაბრუნების თარიღი უკვე დადასტურებულია.", "en": "The return date is already confirmed.", "ru": "Дата возвращения уже подтверждена."},
                {"ge": "სვანეთის ტური ყველაზე მოთხოვნადია ზაფხულში.", "en": "The Svaneti tour is the most in-demand in summer.", "ru": "Тур в Сванетию самый востребованный летом."},
            ],
            "extra_vocab": [
                {"ge": "მგზავრობის გეგმა", "en": "travel plan", "ru": "план поездки", "group": "Planning"},
                {"ge": "გეგმის ცვლილება", "en": "plan change", "ru": "изменение плана", "group": "Planning"},
                {"ge": "საექსკურსიო პროგრამა", "en": "excursion program", "ru": "экскурсионная программа", "group": "Tours"},
                {"ge": "ღამისთევა", "en": "overnight stay", "ru": "ночевка", "group": "Accommodation"},
                {"ge": "შეხვედრის ადგილი", "en": "meeting point", "ru": "место встречи", "group": "Logistics"},
                {"ge": "გაუქმების პირობა", "en": "cancellation condition", "ru": "условие отмены", "group": "Booking"},
            ],
        },
        "6": {
            "bullets": [
                "Hotel compounds describe capacity and bed type efficiently.",
                "Availability status phrases are frequent in booking dialogue.",
                "Price per night is a fixed formula with ღამეში.",
                "Amenity vocabulary supports precise room requests.",
            ],
            "phrases": [
                {"ge": "ერთადგილიანი ნომერი ორი ღამით მინდა.", "en": "I want a single room for two nights.", "ru": "Мне нужен одноместный номер на две ночи."},
                {"ge": "საუზმე ფასში შედის?", "en": "Is breakfast included in the price?", "ru": "Завтрак входит в цену?"},
                {"ge": "ორადგილიანი ნომერი ზღვის ხედით თავისუფალია.", "en": "A twin room with sea view is available.", "ru": "Двухместный номер с видом на море свободен."},
                {"ge": "ჩექ-ინი სამ საათზეა, ჩექ-აუთი თორმეტზე.", "en": "Check-in is at 3, check-out at 12.", "ru": "Заселение в 3, выезд в 12."},
                {"ge": "დაჯავშნა ელფოსტით დავადასტურეთ.", "en": "We confirmed the booking by email.", "ru": "Мы подтвердили бронь по электронной почте."},
                {"ge": "კონდიციონერი და ინტერნეტი აუცილებელია.", "en": "Air conditioning and internet are necessary.", "ru": "Кондиционер и интернет обязательны."},
            ],
            "extra_vocab": [
                {"ge": "ჯავშნის ნომერი", "en": "booking number", "ru": "номер брони", "group": "Booking"},
                {"ge": "სტანდარტული ნომერი", "en": "standard room", "ru": "стандартный номер", "group": "Room types"},
                {"ge": "ლუქსი", "en": "suite", "ru": "люкс", "group": "Room types"},
                {"ge": "გაუქმება", "en": "cancellation", "ru": "отмена", "group": "Booking"},
                {"ge": "ადრეული ჩექ-ინი", "en": "early check-in", "ru": "ранний заезд", "group": "Service"},
                {"ge": "დაგვიანებული ჩექ-აუთი", "en": "late check-out", "ru": "поздний выезд", "group": "Service"},
            ],
        },
        "7": {
            "bullets": [
                "Profile speech often alternates private and public information.",
                "Preference verbs (მიყვარს/მომწონს) shape self-description.",
                "Social media actions use productive loanword verbs/nouns.",
                "Polite online interaction uses concise message formulas.",
            ],
            "phrases": [
                {"ge": "ჩემ პროფილში პირადი ინფორმაცია მხოლოდ მეგობრებისთვისაა.", "en": "In my profile personal information is only for friends.", "ru": "В моем профиле личная информация только для друзей."},
                {"ge": "მუსიკა ძალიან მიყვარს და ხშირად ვაზიარებ პოსტებს.", "en": "I love music and often share posts.", "ru": "Я очень люблю музыку и часто делюсь постами."},
                {"ge": "საჯარო გვერდზე ახალი ფოტო ავტვირთე.", "en": "I uploaded a new photo on the public page.", "ru": "Я загрузил(а) новое фото на публичную страницу."},
                {"ge": "შეტყობინება მომივიდა ახალი გამომწერისგან.", "en": "I received a message from a new follower.", "ru": "Мне пришло сообщение от нового подписчика."},
                {"ge": "პაროლი რეგულარულად უნდა შეცვალო.", "en": "You should change your password regularly.", "ru": "Пароль нужно регулярно менять."},
                {"ge": "ჩემ შესახებ მოკლე ტექსტი დავწერე.", "en": "I wrote a short text about myself.", "ru": "Я написал(а) короткий текст о себе."},
            ],
            "extra_vocab": [
                {"ge": "ანგარიშის უსაფრთხოება", "en": "account security", "ru": "безопасность аккаунта", "group": "Security"},
                {"ge": "ორეტაპიანი დაცვა", "en": "two-step verification", "ru": "двухэтапная защита", "group": "Security"},
                {"ge": "მომხმარებლის სახელი", "en": "username", "ru": "имя пользователя", "group": "Account"},
                {"ge": "ავატარი", "en": "avatar", "ru": "аватар", "group": "Profile"},
                {"ge": "პოსტის ნახვები", "en": "post views", "ru": "просмотры поста", "group": "Analytics"},
                {"ge": "ბლოკირება", "en": "blocking", "ru": "блокировка", "group": "Moderation"},
            ],
        },
        "8": {
            "bullets": [
                "Opinion markers structure reviews: ჩემი აზრით, ვფიქრობ, მგონია.",
                "Reaction language balances positive and negative tone.",
                "Content creation verbs track production workflow clearly.",
                "Audience terms support discussion of reach and engagement.",
            ],
            "phrases": [
                {"ge": "ჩემი აზრით, ეს ვლოგი ძალიან ინფორმაციულია.", "en": "In my opinion, this vlog is very informative.", "ru": "По-моему, этот влог очень информативный."},
                {"ge": "ავტორმა ვიდეო კარგად დაარედაქტირა.", "en": "The author edited the video well.", "ru": "Автор хорошо отредактировал видео."},
                {"ge": "მაყურებლებმა დადებითი კომენტარები დატოვეს.", "en": "Viewers left positive comments.", "ru": "Зрители оставили положительные комментарии."},
                {"ge": "უარყოფითი რეაქციაც იყო, მაგრამ ცოტა.", "en": "There was also some negative reaction, but little.", "ru": "Была и негативная реакция, но немного."},
                {"ge": "არხზე ახალი ჩანაწერი ყოველ კვირას იდება.", "en": "A new entry is posted on the channel every week.", "ru": "На канале каждую неделю публикуется новая запись."},
                {"ge": "სათაური უფრო მოკლე რომ იყოს, უკეთესი იქნებოდა.", "en": "If the title were shorter, it would be better.", "ru": "Было бы лучше, если бы заголовок был короче."},
            ],
            "extra_vocab": [
                {"ge": "კონტენტი", "en": "content", "ru": "контент", "group": "Media"},
                {"ge": "გადაღება", "en": "shooting/filming", "ru": "съемка", "group": "Production"},
                {"ge": "მონტაჟი", "en": "editing/montage", "ru": "монтаж", "group": "Production"},
                {"ge": "გამოქვეყნება", "en": "publishing", "ru": "публикация", "group": "Media"},
                {"ge": "ჩართულობა", "en": "engagement", "ru": "вовлеченность", "group": "Analytics"},
                {"ge": "გამოხმაურება", "en": "feedback/reaction", "ru": "отклик", "group": "Communication"},
            ],
        },
        "9": {
            "bullets": [
                "Invitation formulas often use მოდი + together-action construction.",
                "Premiere planning combines time, ticketing, and coordination phrases.",
                "Future intention can be expressed with present-future forms.",
                "Cultural-event talk mixes logistics with emotional reactions.",
            ],
            "phrases": [
                {"ge": "მოდი, პრემიერაზე პარასკევს წავიდეთ.", "en": "Come on, let's go to the premiere on Friday.", "ru": "Давай в пятницу пойдем на премьеру."},
                {"ge": "ბილეთები წინასწარ ონლაინ ვიყიდოთ.", "en": "Let's buy tickets online in advance.", "ru": "Давайте заранее купим билеты онлайн."},
                {"ge": "სპექტაკლი რვა საათზე იწყება.", "en": "The performance starts at eight.", "ru": "Спектакль начинается в восемь."},
                {"ge": "რეჟისორთან შეხვედრაც იქნება პრემიერის შემდეგ.", "en": "There will also be a meeting with the director after the premiere.", "ru": "После премьеры будет встреча с режиссером."},
                {"ge": "დარბაზში ადგილები სწრაფად ივსება.", "en": "Seats in the hall fill quickly.", "ru": "Места в зале быстро заполняются."},
                {"ge": "ფილმის პოსტერი უკვე ქალაქში ყველგანაა.", "en": "The film poster is already everywhere in the city.", "ru": "Постер фильма уже по всему городу."},
            ],
            "extra_vocab": [
                {"ge": "სეანსი", "en": "screening/session", "ru": "сеанс", "group": "Cinema"},
                {"ge": "ბილეთების ჯავშანი", "en": "ticket reservation", "ru": "бронирование билетов", "group": "Ticketing"},
                {"ge": "რიგი", "en": "row", "ru": "ряд", "group": "Venue"},
                {"ge": "ადგილის ნომერი", "en": "seat number", "ru": "номер места", "group": "Venue"},
                {"ge": "პრემიერის თარიღი", "en": "premiere date", "ru": "дата премьеры", "group": "Planning"},
                {"ge": "მოსაწვევი ბარათი", "en": "invitation card", "ru": "пригласительный билет", "group": "Event"},
            ],
        },
        "10": {
            "bullets": [
                "რომელიც introduces descriptive clauses for plot summaries.",
                "Review language balances evaluation and recommendation.",
                "Genre labels help frame reader expectations quickly.",
                "Critical comments often use contrast markers (თუმცა, მაგრამ).",
            ],
            "phrases": [
                {"ge": "ფილმი, რომელიც გუშინ ვნახე, დრამაა.", "en": "The film I watched yesterday is a drama.", "ru": "Фильм, который я вчера посмотрел(а), — драма."},
                {"ge": "სიუჟეტი თავიდან ნელია, მაგრამ ბოლოს საინტერესო ხდება.", "en": "The plot is slow at first, but becomes interesting at the end.", "ru": "Сюжет сначала медленный, но в конце становится интересным."},
                {"ge": "ამ ფილმს ყველას ვურჩევ, ვისაც კომედია უყვარს.", "en": "I recommend this film to everyone who loves comedy.", "ru": "Рекомендую этот фильм всем, кто любит комедию."},
                {"ge": "მთავარი პერსონაჟი კარგად არის განვითარებული.", "en": "The main character is well developed.", "ru": "Главный персонаж хорошо раскрыт."},
                {"ge": "რეცენზიაში დადებითი და უარყოფითი მხარეები ავღნიშნე.", "en": "In the review I noted positive and negative sides.", "ru": "В рецензии я отметил(а) плюсы и минусы."},
                {"ge": "შეფასება საბოლოოდ შვიდი ქულაა ათიდან.", "en": "The final rating is seven out of ten.", "ru": "Итоговая оценка — семь из десяти."},
            ],
            "extra_vocab": [
                {"ge": "კადრი", "en": "frame/shot", "ru": "кадр", "group": "Cinema"},
                {"ge": "დიალოგი", "en": "dialogue", "ru": "диалог", "group": "Narrative"},
                {"ge": "ტემპი", "en": "pace", "ru": "темп", "group": "Review"},
                {"ge": "ფინალი", "en": "finale", "ru": "финал", "group": "Narrative"},
                {"ge": "შთაბეჭდილება", "en": "impression", "ru": "впечатление", "group": "Review"},
                {"ge": "შემფასებელი", "en": "reviewer/evaluator", "ru": "обозреватель", "group": "Review"},
            ],
        },
        "11": {
            "bullets": [
                "Cause connectors like იმიტომ რომ structure adaptation stories.",
                "Experience adverbs (პირველად, ხშირად, ბოლოს) anchor timeline.",
                "Culture-shock narratives benefit from contrastive clauses.",
                "Integration vocabulary mixes language, habits, and social norms.",
            ],
            "phrases": [
                {"ge": "უცხოელებს თავიდან ენის ბარიერი აქვთ.", "en": "Foreigners initially have a language barrier.", "ru": "У иностранцев сначала есть языковой барьер."},
                {"ge": "პირველად სუფრის ტრადიციები გაუკვირდათ.", "en": "At first, table traditions surprised them.", "ru": "Сначала их удивили застольные традиции."},
                {"ge": "შემდეგ ნელ-ნელა ქართულ გარემოს შეეჩვივნენ.", "en": "Then they gradually got used to the Georgian environment.", "ru": "Потом они постепенно привыкли к грузинской среде."},
                {"ge": "ინტერვიუში თქვეს, რომ ხალხი ძალიან სტუმართმოყვარეა.", "en": "In the interview they said people are very hospitable.", "ru": "В интервью они сказали, что люди очень гостеприимные."},
                {"ge": "ხშირად იმიტომ რჩებიან, რომ აქ თავს უსაფრთხოდ გრძნობენ.", "en": "They often stay because they feel safe here.", "ru": "Они часто остаются, потому что чувствуют себя здесь в безопасности."},
                {"ge": "ქართველოლოგები ქართულ დიალექტებსაც სწავლობენ.", "en": "Georgianists also study Georgian dialects.", "ru": "Картвелологи также изучают грузинские диалекты."},
            ],
            "extra_vocab": [
                {"ge": "ენის ბარიერი", "en": "language barrier", "ru": "языковой барьер", "group": "Integration"},
                {"ge": "ადაპტირება", "en": "to adapt", "ru": "адаптироваться", "group": "Integration"},
                {"ge": "სოციალური ჩვევა", "en": "social habit", "ru": "социальная привычка", "group": "Culture"},
                {"ge": "ადგილობრივი წესები", "en": "local rules", "ru": "местные правила", "group": "Culture"},
                {"ge": "კულტურული განსხვავება", "en": "cultural difference", "ru": "культурное различие", "group": "Culture"},
                {"ge": "თვითგამოხატვა", "en": "self-expression", "ru": "самовыражение", "group": "Communication"},
            ],
        },
        "12": {
            "bullets": [
                "Learning advice often uses უნდა + infinitive/verb stem.",
                "Purpose connectors (რათა, რომ) link method and goal.",
                "Habit markers (ყოველდღე, რეგულარულად) are essential in study plans.",
                "Skill-building language often groups four domains: reading, writing, listening, speaking.",
            ],
            "phrases": [
                {"ge": "ენა რომ კარგად ისწავლო, ყოველდღე ივარჯიშე.", "en": "To learn a language well, practice every day.", "ru": "Чтобы хорошо выучить язык, тренируйся каждый день."},
                {"ge": "გრამატიკა მნიშვნელოვანია, მაგრამ პრაქტიკა უფრო მნიშვნელოვანია.", "en": "Grammar is important, but practice is even more important.", "ru": "Грамматика важна, но практика еще важнее."},
                {"ge": "ახალი სიტყვები კონტექსტში დაიმახსოვრე.", "en": "Memorize new words in context.", "ru": "Запоминай новые слова в контексте."},
                {"ge": "მიზანი რომ გქონდეს, მოტივაციაც მარტივად შენარჩუნდება.", "en": "If you have a goal, motivation is easier to maintain.", "ru": "Если есть цель, мотивацию легче сохранить."},
                {"ge": "კვირაში ერთხელ მასწავლებელთან სასაუბრო პრაქტიკა გააკეთე.", "en": "Do speaking practice with a teacher once a week.", "ru": "Раз в неделю практикуй разговор с преподавателем."},
                {"ge": "რაც არ გესმის, მაშინვე ჩაინიშნე.", "en": "Write down what you do not understand immediately.", "ru": "То, что не понимаешь, сразу записывай."},
            ],
            "extra_vocab": [
                {"ge": "სასწავლო გეგმა", "en": "study plan", "ru": "учебный план", "group": "Learning"},
                {"ge": "დავალება", "en": "assignment", "ru": "задание", "group": "Learning"},
                {"ge": "თვითსწავლება", "en": "self-study", "ru": "самообучение", "group": "Learning"},
                {"ge": "გამეორების ციკლი", "en": "revision cycle", "ru": "цикл повторения", "group": "Learning"},
                {"ge": "განმარტება", "en": "explanation", "ru": "объяснение", "group": "Learning"},
                {"ge": "მეტყველების უნარი", "en": "speaking skill", "ru": "навык речи", "group": "Skills"},
            ],
        },
    },
    "b1": {
        "1": {
            "bullets": [
                "Imperfect forms present ongoing or habitual past background.",
                "Biographical narration often alternates dates and life events.",
                "First-person storytelling can shift between factual and poetic tone.",
                "Place-of-birth and family origin phrases are high-frequency.",
            ],
            "phrases": [
                {"ge": "ბავშვობაში პატარა სოფელში ვიზრდებოდი.", "en": "In childhood I grew up in a small village.", "ru": "В детстве я рос(ла) в маленькой деревне."},
                {"ge": "ჩემი ოჯახი ხშირად გადაადგილდებოდა.", "en": "My family moved often.", "ru": "Моя семья часто переезжала."},
                {"ge": "მამა სკოლაში მუშაობდა, დედა კი სახლში იყო.", "en": "My father worked at school, while my mother stayed at home.", "ru": "Отец работал в школе, а мама была дома."},
                {"ge": "მაშინ ბევრი რამ არ მესმოდა, მაგრამ ვსწავლობდი.", "en": "Back then I did not understand many things, but I was learning.", "ru": "Тогда я многого не понимал(а), но учился(лась)."},
                {"ge": "მოგონებებში ის წლები ძალიან ნათლად დარჩა.", "en": "In my memories those years remained very vivid.", "ru": "В воспоминаниях те годы остались очень яркими."},
                {"ge": "როდის დაიბადეთ და სად გაიზარდეთ?", "en": "When were you born and where did you grow up?", "ru": "Когда вы родились и где выросли?"},
            ],
            "extra_vocab": [
                {"ge": "სიცოცხლის გზა", "en": "life path", "ru": "жизненный путь", "group": "Biography"},
                {"ge": "ადრეული წლები", "en": "early years", "ru": "ранние годы", "group": "Biography"},
                {"ge": "მოსწავლის ასაკი", "en": "school age", "ru": "школьный возраст", "group": "Life stage"},
                {"ge": "გარდატეხა", "en": "turning point", "ru": "переломный момент", "group": "Narrative"},
                {"ge": "შთაგონება", "en": "inspiration", "ru": "вдохновение", "group": "Narrative"},
                {"ge": "პიროვნული განვითარება", "en": "personal development", "ru": "личностное развитие", "group": "Biography"},
            ],
        },
        "2": {
            "bullets": [
                "CV language favors concise noun-heavy structures.",
                "Date ranges are essential for education and work timelines.",
                "Section headers in Georgian often mirror international CV style.",
                "Formal register requires consistent factual phrasing.",
            ],
            "phrases": [
                {"ge": "რეზიუმეში სამუშაო გამოცდილება ქრონოლოგიურად ჩამოვწერე.", "en": "In the resume I listed work experience chronologically.", "ru": "В резюме я перечислил(а) опыт работы хронологически."},
                {"ge": "2018 წლიდან დღემდე კომპანიაში ვმუშაობ.", "en": "I have worked in the company from 2018 to present.", "ru": "С 2018 года по настоящее время работаю в компании."},
                {"ge": "განაცხადს სამოტივაციო წერილიც დავურთე.", "en": "I also attached a motivation letter to the application.", "ru": "К заявке я также приложил(а) мотивационное письмо."},
                {"ge": "ხელფასის მოლოდინი ვაკანსიაში მითითებულია.", "en": "Salary expectations are indicated in the vacancy.", "ru": "Ожидания по зарплате указаны в вакансии."},
                {"ge": "უნარ-ჩვევების სექციაში კომპიუტერული პროგრამები ჩავწერე.", "en": "In the skills section I included computer programs.", "ru": "В разделе навыков я указал(а) компьютерные программы."},
                {"ge": "კანდიდატი გასაუბრებაზე შემდეგ კვირას დაიბარეს.", "en": "The candidate was invited to an interview next week.", "ru": "Кандидата пригласили на собеседование на следующей неделе."},
            ],
            "extra_vocab": [
                {"ge": "სამუშაო ისტორია", "en": "employment history", "ru": "трудовая история", "group": "CV"},
                {"ge": "პროფესიული მიზანი", "en": "professional objective", "ru": "профессиональная цель", "group": "CV"},
                {"ge": "სარეკომენდაციო წერილი", "en": "recommendation letter", "ru": "рекомендательное письмо", "group": "Documents"},
                {"ge": "საკონტაქტო პირი", "en": "contact person", "ru": "контактное лицо", "group": "Contact"},
                {"ge": "განაცხადის ვადა", "en": "application deadline", "ru": "срок подачи заявки", "group": "Employment"},
                {"ge": "ინტერვიუს ეტაპი", "en": "interview stage", "ru": "этап интервью", "group": "Employment"},
            ],
        },
        "3": {
            "bullets": [
                "Interview answers should combine skill evidence and examples.",
                "Quality adjectives work best when tied to real experience.",
                "Modal patterns (can/have) support confident self-presentation.",
                "Preparation language includes predicted questions and rehearsed answers.",
            ],
            "phrases": [
                {"ge": "გასაუბრებისთვის წინასწარ მოვემზადე.", "en": "I prepared in advance for the interview.", "ru": "Я заранее подготовился(лась) к собеседованию."},
                {"ge": "ჩემი ძლიერი მხარე პასუხისმგებლობაა.", "en": "My strong side is responsibility.", "ru": "Моя сильная сторона — ответственность."},
                {"ge": "კომუნიკაბელური ვარ და გუნდში მუშაობა შემიძლია.", "en": "I am communicative and can work in a team.", "ru": "Я коммуникабельный(ая) и могу работать в команде."},
                {"ge": "სამუშაო გამოცდილება მომხმარებელთან ურთიერთობაში მაქვს.", "en": "I have work experience in customer interaction.", "ru": "У меня есть опыт работы с клиентами."},
                {"ge": "სუსტი მხარის გაუმჯობესებაზე აქტიურად ვმუშაობ.", "en": "I actively work on improving my weak side.", "ru": "Я активно работаю над улучшением слабой стороны."},
                {"ge": "დამსაქმებელმა მკითხა, რატომ მინდა ეს პოზიცია.", "en": "The employer asked me why I want this position.", "ru": "Работодатель спросил, почему я хочу эту позицию."},
            ],
            "extra_vocab": [
                {"ge": "პრეზენტაბელური", "en": "presentable", "ru": "презентабельный", "group": "Qualities"},
                {"ge": "დროის მართვა", "en": "time management", "ru": "управление временем", "group": "Skills"},
                {"ge": "პრობლემის გადაჭრა", "en": "problem solving", "ru": "решение проблем", "group": "Skills"},
                {"ge": "მოტივირებული", "en": "motivated", "ru": "мотивированный", "group": "Qualities"},
                {"ge": "შედეგზე ორიენტირებული", "en": "result-oriented", "ru": "ориентированный на результат", "group": "Qualities"},
                {"ge": "დასაქმების შეთავაზება", "en": "job offer", "ru": "предложение о работе", "group": "Employment"},
            ],
        },
        "4": {
            "bullets": [
                "Unusual profession descriptions need role + environment + duty.",
                "Relative clauses help define non-standard jobs clearly.",
                "Professional nouns often come from international roots.",
                "Workplace vocabulary adds realism to profession narratives.",
            ],
            "phrases": [
                {"ge": "ეს პროფესია უჩვეულოა, მაგრამ ძალიან საინტერესო.", "en": "This profession is unusual but very interesting.", "ru": "Эта профессия необычная, но очень интересная."},
                {"ge": "ფერმერი, რომელიც მთაში მუშაობს, დიდ პასუხისმგებლობას იღებს.", "en": "A farmer who works in the mountains takes great responsibility.", "ru": "Фермер, который работает в горах, берет на себя большую ответственность."},
                {"ge": "რეპორტიორი ყოველდღე სხვადასხვა ადგილას დადის.", "en": "A reporter goes to different places every day.", "ru": "Репортер каждый день ходит в разные места."},
                {"ge": "მყვინთავის სამუშაო რისკიანი, მაგრამ მოთხოვნადია.", "en": "A diver's job is risky but in demand.", "ru": "Работа дайвера рискованная, но востребованная."},
                {"ge": "სამუშაო გრაფიკი ხშირად არასტანდარტულია.", "en": "The work schedule is often non-standard.", "ru": "Рабочий график часто нестандартный."},
                {"ge": "პროფესიის აღწერაში მოვალეობები დეტალურად ჩავწერეთ.", "en": "We described duties in detail in the profession description.", "ru": "В описании профессии мы подробно указали обязанности."},
            ],
            "extra_vocab": [
                {"ge": "არასტანდარტული", "en": "non-standard", "ru": "нестандартный", "group": "Descriptions"},
                {"ge": "მოთხოვნადი", "en": "in demand", "ru": "востребованный", "group": "Employment"},
                {"ge": "პროფესიული გზა", "en": "career path", "ru": "профессиональный путь", "group": "Career"},
                {"ge": "გამოცდის პერიოდი", "en": "trial period", "ru": "испытательный срок", "group": "Employment"},
                {"ge": "შრომითი პირობები", "en": "working conditions", "ru": "условия труда", "group": "Employment"},
                {"ge": "სამუშაო გარემო", "en": "work environment", "ru": "рабочая среда", "group": "Employment"},
            ],
        },
        "5": {
            "bullets": [
                "Instruction language prefers concise command chains.",
                "Safety warnings combine hazard noun + action prohibition.",
                "Map-symbol vocabulary needs precise noun control.",
                "Formal imperative is standard in technical directions.",
            ],
            "phrases": [
                {"ge": "მარშრუტს ყურადღებით მიჰყევით.", "en": "Follow the route carefully.", "ru": "Внимательно следуйте маршруту."},
                {"ge": "ამ მონაკვეთზე ქვათაცვენის საფრთხეა.", "en": "There is a risk of rockfall on this section.", "ru": "На этом участке есть опасность камнепада."},
                {"ge": "დაიცავით უსაფრთხოების ინსტრუქცია.", "en": "Follow the safety instruction.", "ru": "Соблюдайте инструкцию безопасности."},
                {"ge": "თოკი სწორად დაამაგრეთ ჩასვლამდე.", "en": "Secure the rope correctly before descending.", "ru": "Правильно закрепите веревку перед спуском."},
                {"ge": "საშიშ ზონაში არ გადაინაცვლოთ.", "en": "Do not move into the dangerous zone.", "ru": "Не перемещайтесь в опасную зону."},
                {"ge": "რუკაზე პირობითი ნიშნები წინასწარ შეისწავლეთ.", "en": "Study map symbols in advance.", "ru": "Заранее изучите условные обозначения на карте."},
            ],
            "extra_vocab": [
                {"ge": "უსაფრთხოების წესები", "en": "safety rules", "ru": "правила безопасности", "group": "Safety"},
                {"ge": "საფრთხის ზონა", "en": "danger zone", "ru": "опасная зона", "group": "Safety"},
                {"ge": "აღჭურვილობა", "en": "equipment", "ru": "снаряжение", "group": "Mountaineering"},
                {"ge": "გადარჩენა", "en": "rescue/survival", "ru": "спасение", "group": "Safety"},
                {"ge": "აღმართი", "en": "ascent", "ru": "подъем", "group": "Terrain"},
                {"ge": "დაშვება", "en": "descent", "ru": "спуск", "group": "Terrain"},
            ],
        },
        "6": {
            "bullets": [
                "Sports narratives often alternate event timeline and results.",
                "Past verbs mark key moments: start, win, finish.",
                "Olympic descriptions mix history, ritual, and competition terms.",
                "Frequency phrases (every four years) are fixed and useful.",
            ],
            "phrases": [
                {"ge": "ოლიმპიური თამაშები ოთხ წელიწადში ერთხელ ტარდება.", "en": "The Olympic Games are held every four years.", "ru": "Олимпийские игры проводятся раз в четыре года."},
                {"ge": "ქართველმა სპორტსმენმა ოქროს მედალი მოიგო.", "en": "A Georgian athlete won a gold medal.", "ru": "Грузинский спортсмен выиграл золотую медаль."},
                {"ge": "შეჯიბრება საზეიმოდ დაიწყო.", "en": "The competition began ceremonially.", "ru": "Соревнование началось торжественно."},
                {"ge": "გუნდმა ფინალში დამაჯერებლად გაიმარჯვა.", "en": "The team won convincingly in the final.", "ru": "Команда уверенно победила в финале."},
                {"ge": "მწვრთნელმა ტაქტიკა ზუსტად შეარჩია.", "en": "The coach chose the strategy precisely.", "ru": "Тренер точно выбрал тактику."},
                {"ge": "ახალი რეკორდი დამყარდა შეჯიბრზე.", "en": "A new record was set at the competition.", "ru": "На соревновании установлен новый рекорд."},
            ],
            "extra_vocab": [
                {"ge": "სპორტსმენი", "en": "athlete", "ru": "спортсмен", "group": "Sport"},
                {"ge": "ფინალი", "en": "final", "ru": "финал", "group": "Sport event"},
                {"ge": "ნახევარფინალი", "en": "semi-final", "ru": "полуфинал", "group": "Sport event"},
                {"ge": "ტაქტიკა", "en": "tactics", "ru": "тактика", "group": "Sport"},
                {"ge": "ვარჯიშის პროცესი", "en": "training process", "ru": "тренировочный процесс", "group": "Sport"},
                {"ge": "დამსახურებული გამარჯვება", "en": "deserved victory", "ru": "заслуженная победа", "group": "Result"},
            ],
        },
        "7": {
            "bullets": [
                "Free-time topics combine habit verbs with preference structures.",
                "Music discussions often use genre and emotion vocabulary.",
                "Suggestion forms soften invitations and plans.",
                "Time-spending verb patterns are central: როგორ ატარებ დროს.",
            ],
            "phrases": [
                {"ge": "თავისუფალ დროს ჯაზს ვუსმენ.", "en": "In my free time I listen to jazz.", "ru": "В свободное время я слушаю джаз."},
                {"ge": "მეგობრებთან ერთად კონცერტზე ხშირად დავდივარ.", "en": "I often go to concerts with friends.", "ru": "Я часто хожу на концерты с друзьями."},
                {"ge": "კარგი იქნებოდა თუ შაბათს ფესტივალზე წავიდოდით.", "en": "It would be good if we went to the festival on Saturday.", "ru": "Было бы хорошо, если бы в субботу мы пошли на фестиваль."},
                {"ge": "სიმღერის მელოდია ძალიან მშვიდია.", "en": "The song melody is very calm.", "ru": "Мелодия песни очень спокойная."},
                {"ge": "დასვენებისთვის კითხვა და მუსიკა საუკეთესოა.", "en": "For relaxation, reading and music are the best.", "ru": "Для отдыха лучше всего чтение и музыка."},
                {"ge": "ახალი ალბომი უკვე მოვისმინე.", "en": "I have already listened to the new album.", "ru": "Я уже послушал(а) новый альбом."},
            ],
            "extra_vocab": [
                {"ge": "მუსიკალური ჟანრი", "en": "music genre", "ru": "музыкальный жанр", "group": "Music"},
                {"ge": "ალბომი", "en": "album", "ru": "альбом", "group": "Music"},
                {"ge": "რეპეტიცია", "en": "rehearsal", "ru": "репетиция", "group": "Music"},
                {"ge": "დაკვრა", "en": "playing an instrument", "ru": "игра на инструменте", "group": "Music"},
                {"ge": "დირიჟორი", "en": "conductor", "ru": "дирижер", "group": "Music"},
                {"ge": "შემსრულებელი", "en": "performer", "ru": "исполнитель", "group": "Music"},
            ],
        },
        "8": {
            "bullets": [
                "Relative clause marker რომელიც is key in event descriptions.",
                "Social-phenomena writing needs clear cause and effect links.",
                "Flash mob language balances planning and spontaneity.",
                "Linking words improve coherence in B1-level explanations.",
            ],
            "phrases": [
                {"ge": "ფლეშმობი, რომელიც ცენტრში გაიმართა, ბევრს მოეწონა.", "en": "The flash mob that took place downtown was liked by many.", "ru": "Флешмоб, который прошел в центре, многим понравился."},
                {"ge": "ორგანიზატორებმა მონაწილეები წინასწარ გააფრთხილეს.", "en": "The organizers warned participants in advance.", "ru": "Организаторы заранее предупредили участников."},
                {"ge": "გამვლელები ჯერ გაკვირვებულები იყვნენ, შემდეგ შეუერთდნენ.", "en": "Passersby were surprised at first, then joined.", "ru": "Прохожие сначала удивились, потом присоединились."},
                {"ge": "ვიდეოჩანაწერი სოციალურ ქსელებში სწრაფად გავრცელდა.", "en": "The video recording spread quickly on social networks.", "ru": "Видеозапись быстро распространилась в соцсетях."},
                {"ge": "ეს ფენომენი საზოგადოებრივ აქტიურობას ზრდის.", "en": "This phenomenon increases civic activity.", "ru": "Это явление повышает общественную активность."},
                {"ge": "რაც უკეთ დაგეგმავ, მით მშვიდად ჩაივლის ღონისძიება.", "en": "The better you plan, the smoother the event goes.", "ru": "Чем лучше спланируешь, тем спокойнее пройдет мероприятие."},
            ],
            "extra_vocab": [
                {"ge": "საზოგადოებრივი სივრცე", "en": "public space", "ru": "общественное пространство", "group": "Society"},
                {"ge": "საზოგადოებრივი რეაქცია", "en": "public reaction", "ru": "общественная реакция", "group": "Society"},
                {"ge": "ინიციატივა", "en": "initiative", "ru": "инициатива", "group": "Society"},
                {"ge": "დაგეგმვა", "en": "planning", "ru": "планирование", "group": "Process"},
                {"ge": "კოორდინაცია", "en": "coordination", "ru": "координация", "group": "Process"},
                {"ge": "გავრცელება", "en": "spread/dissemination", "ru": "распространение", "group": "Media"},
            ],
        },
        "9": {
            "bullets": [
                "Online shopping language combines future, advice, and commands.",
                "Payment and delivery are usually expressed in fixed collocations.",
                "Consumer actions are step-by-step and sequence-based.",
                "Modal უნდა often signals recommendation in instructions.",
            ],
            "phrases": [
                {"ge": "ონლაინმაღაზიაში შეკვეთას დღეს გავაფორმებ.", "en": "I will place the order in the online store today.", "ru": "Сегодня я оформлю заказ в интернет-магазине."},
                {"ge": "მიწოდების მისამართი სწორად უნდა შეიყვანო.", "en": "You should enter the delivery address correctly.", "ru": "Адрес доставки нужно ввести правильно."},
                {"ge": "საბანკო ბარათით გადახდა ყველაზე სწრაფია.", "en": "Paying by bank card is the fastest.", "ru": "Оплата банковской картой самая быстрая."},
                {"ge": "ფასდაკლება მოქმედებს მხოლოდ ონლაინ შეკვეთებზე.", "en": "The discount applies only to online orders.", "ru": "Скидка действует только на онлайн-заказы."},
                {"ge": "თუ პროდუქტი არ მოგეწონება, დაბრუნება შეგიძლია.", "en": "If you do not like the product, you can return it.", "ru": "Если товар не понравится, его можно вернуть."},
                {"ge": "განვადებით ყიდვა უფრო მოსახერხებელია დიდი ტექნიკისთვის.", "en": "Buying in installments is more convenient for large electronics.", "ru": "Покупка в рассрочку удобнее для крупной техники."},
            ],
            "extra_vocab": [
                {"ge": "ტრეკინგის ნომერი", "en": "tracking number", "ru": "трек-номер", "group": "Delivery"},
                {"ge": "კურიერი", "en": "courier", "ru": "курьер", "group": "Delivery"},
                {"ge": "საფასური", "en": "fee/charge", "ru": "сбор/плата", "group": "Payment"},
                {"ge": "გადახდის დადასტურება", "en": "payment confirmation", "ru": "подтверждение оплаты", "group": "Payment"},
                {"ge": "მომხმარებლის შეფასება", "en": "customer review", "ru": "отзыв покупателя", "group": "E-commerce"},
                {"ge": "პროდუქტის რეიტინგი", "en": "product rating", "ru": "рейтинг товара", "group": "E-commerce"},
            ],
        },
        "10": {
            "bullets": [
                "Complaint writing needs formal register and clear structure.",
                "Consumer-rights arguments require evidence (receipt, contract, date).",
                "Imperative forms can express legal requests politely.",
                "Tax and rights vocabulary overlaps in formal documents.",
            ],
            "phrases": [
                {"ge": "ოფიციალური საჩივარი მომხმარებელთა დაცვის სამსახურში გავაგზავნე.", "en": "I sent an official complaint to the consumer protection service.", "ru": "Я отправил(а) официальную жалобу в службу защиты потребителей."},
                {"ge": "ჩეკის გარეშე დაბრუნება ვერ მოხერხდა.", "en": "Return was not possible without a receipt.", "ru": "Возврат без чека оказался невозможен."},
                {"ge": "კონტრაქტის პირობები არ იყო სრულად შესრულებული.", "en": "The contract terms were not fully met.", "ru": "Условия контракта были выполнены не полностью."},
                {"ge": "მომხმარებელს ხარისხიანი მომსახურების მიღების უფლება აქვს.", "en": "The consumer has the right to receive quality service.", "ru": "Потребитель имеет право получать качественную услугу."},
                {"ge": "ანაზღაურება კანონის საფუძველზე მოვითხოვეთ.", "en": "We requested compensation on legal grounds.", "ru": "Мы потребовали компенсацию на основании закона."},
                {"ge": "განცხადებაში ფაქტები და თარიღები ზუსტად მივუთითე.", "en": "I indicated facts and dates precisely in the statement.", "ru": "В заявлении я точно указал(а) факты и даты."},
            ],
            "extra_vocab": [
                {"ge": "იურიდიული კონსულტაცია", "en": "legal consultation", "ru": "юридическая консультация", "group": "Law"},
                {"ge": "სარჩელი", "en": "claim/lawsuit", "ru": "иск", "group": "Law"},
                {"ge": "მტკიცებულება", "en": "evidence", "ru": "доказательство", "group": "Law"},
                {"ge": "დარღვევა", "en": "violation", "ru": "нарушение", "group": "Law"},
                {"ge": "საგადასახადო ორგანო", "en": "tax authority", "ru": "налоговый орган", "group": "Tax"},
                {"ge": "განხილვის ვადა", "en": "review period", "ru": "срок рассмотрения", "group": "Documents"},
            ],
        },
        "11": {
            "bullets": [
                "Regional adjectives identify culinary origin precisely.",
                "Recipe discourse uses sequence verbs and ingredient nouns.",
                "Hospitality contexts combine food vocabulary and etiquette.",
                "Cuisine comparison often uses taste and preparation contrast.",
            ],
            "phrases": [
                {"ge": "იმერული ხაჭაპური უფრო რბილია, ვიდრე აჭარული.", "en": "Imeretian khachapuri is softer than Adjarian.", "ru": "Имеретинский хачапури мягче, чем аджарский."},
                {"ge": "რეცეპტში ყველა ინგრედიენტი ზუსტადაა მითითებული.", "en": "All ingredients are listed precisely in the recipe.", "ru": "В рецепте точно указаны все ингредиенты."},
                {"ge": "სვანური მარილი კერძს განსაკუთრებულ გემოს აძლევს.", "en": "Svan salt gives the dish a special flavor.", "ru": "Сванская соль придает блюду особый вкус."},
                {"ge": "ტრადიციულ სუფრაზე სტუმარმასპინძლობა მნიშვნელოვანია.", "en": "Hospitality is important at a traditional feast table.", "ru": "На традиционном застолье важно гостеприимство."},
                {"ge": "ჩიხირთმა ზამთარში განსაკუთრებით პოპულარულია.", "en": "Chikhirtma is especially popular in winter.", "ru": "Чихиртма особенно популярна зимой."},
                {"ge": "რესტორნის მენიუში რეგიონული კერძების ცალკე სექციაა.", "en": "The restaurant menu has a separate section for regional dishes.", "ru": "В меню ресторана есть отдельный раздел региональных блюд."},
            ],
            "extra_vocab": [
                {"ge": "სუფრის კულტურა", "en": "table culture", "ru": "культура застолья", "group": "Culture"},
                {"ge": "სამზარეულოს ტრადიცია", "en": "culinary tradition", "ru": "кулинарная традиция", "group": "Cuisine"},
                {"ge": "ნოყიერი", "en": "hearty/nutritious", "ru": "сытный", "group": "Food descriptions"},
                {"ge": "სურნელოვანი", "en": "aromatic", "ru": "ароматный", "group": "Food descriptions"},
                {"ge": "გარნირი", "en": "side dish/garnish", "ru": "гарнир", "group": "Cuisine"},
                {"ge": "მთავარი კერძი", "en": "main course", "ru": "основное блюдо", "group": "Cuisine"},
            ],
        },
        "12": {
            "bullets": [
                "Healthy-lifestyle arguments rely on cause and consequence links.",
                "Advice language uses modal and recommendation structures.",
                "Nutrition terms often pair beneficial vs harmful contrasts.",
                "Geographic context (Caucasus) enriches cultural discussion.",
            ],
            "phrases": [
                {"ge": "ჯანსაღი კვება და რეგულარული ვარჯიში აუცილებელია.", "en": "Healthy eating and regular exercise are essential.", "ru": "Здоровое питание и регулярные упражнения необходимы."},
                {"ge": "სწრაფი კვება ხშირ შემთხვევაში მავნეა.", "en": "Fast food is harmful in many cases.", "ru": "Фастфуд во многих случаях вреден."},
                {"ge": "დაბალანსებული დიეტა ენერგიას გაძლევს.", "en": "A balanced diet gives you energy.", "ru": "Сбалансированная диета дает энергию."},
                {"ge": "კავკასიის რეგიონში ტრადიციული კვება განსხვავებულია.", "en": "Traditional nutrition differs in the Caucasus region.", "ru": "Традиционное питание в Кавказском регионе отличается."},
                {"ge": "ექიმის რეკომენდაციები ყოველთვის უნდა გაითვალისწინო.", "en": "You should always take a doctor's recommendations into account.", "ru": "Рекомендации врача всегда нужно учитывать."},
                {"ge": "ჯანსაღი ძილი და სეირნობა სტრესს ამცირებს.", "en": "Healthy sleep and walking reduce stress.", "ru": "Здоровый сон и прогулки снижают стресс."},
            ],
            "extra_vocab": [
                {"ge": "იმუნიტეტი", "en": "immunity", "ru": "иммунитет", "group": "Health"},
                {"ge": "წყლის ბალანსი", "en": "water balance", "ru": "водный баланс", "group": "Health"},
                {"ge": "კვებითი რეჟიმი", "en": "dietary regimen", "ru": "режим питания", "group": "Nutrition"},
                {"ge": "ფიზიკური აქტივობა", "en": "physical activity", "ru": "физическая активность", "group": "Health"},
                {"ge": "გულისხმიერი დამოკიდებულება", "en": "mindful attitude", "ru": "осознанный подход", "group": "Lifestyle"},
                {"ge": "პროფილაქტიკური შემოწმება", "en": "preventive check-up", "ru": "профилактический осмотр", "group": "Medical care"},
            ],
        },
    },
}
