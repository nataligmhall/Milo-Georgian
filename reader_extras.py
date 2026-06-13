"""Reader-only enrichments: grammar tables, can-do goals, short readings.

Merged at build time by build_reader_site.py (not required in Telegram).
"""

import copy


def _tbl(title, headers, rows, note=None):
    t = {"title": title, "headers": headers, "rows": rows}
    if note:
        t["note"] = note
    return t


def _ex(can_do, reading_ge, reading_en, tables=None):
    e = {
        "can_do": can_do,
        "reading": {"ge": reading_ge, "en": reading_en},
    }
    if tables:
        e["grammar_tables"] = tables
    return e


READER_EXTRAS = {
    "a1": {
        "1": _ex(
            [
                "Point at something and say აი + noun (here is…)",
                "Say what something is: ეს კაფეა / ეს არ არის ოფისი",
                "Recognise common loanwords (ტელეფონი, კომპიუტერი, კაფე)",
            ],
            "აი ოფისი. ეს ოფისია. აი ტელეფონი და კომპიუტერი. ეს არ არის კაფე — ეს სუპერმარკეტია. აი სტუდენტი. აი ტურისტი ფოტოსთან.",
            "Here is an office. This is an office. Here is a phone and a computer. This is not a café — this is a supermarket. Here is a student. Here is a tourist by the photo.",
            [
                _tbl(
                    "აი / ეს — pointing & identifying",
                    ["Pattern", "Georgian", "Meaning"],
                    [
                        ["Here is…", "აი + noun", "Here is / look — …"],
                        ["This is…", "ეს არის X", "This is X"],
                        ["Short form", "ეს X-ა", "This is X (noun ends in -ი)"],
                        ["Not…", "ეს არ არის X", "This is not X"],
                    ],
                    "After nouns ending in -ი, drop არის and add -ა: კაფე → კაფეა.",
                ),
            ],
        ),
        "2": _ex(
            [
                "Greet someone: გამარჯობა! and answer გაგიმარჯოს",
                "Ask and answer როგორ ხარ? — კარგად, გმადლობ",
                "Ask someone's name: რა გქვია? / მე მქვია …",
                "Ask where someone is from: სად ხარ? / თბილისში ვარ",
            ],
            "გამარჯობა! როგორ ხარ? — კარგად, გმადლობ. რა გქვია? — მე მქვია ნინო. ეს ნინოა? — დიახ, ეს ნინოა. სად ხარ? — თბილისში ვარ. საქართველო ლამაზი ქვეყანაა.",
            "Hello! How are you? — Fine, thank you. What's your name? — My name is Nino. Is this Nino? — Yes, this is Nino. Where are you? — I am in Tbilisi. Georgia is a beautiful country.",
            [
                _tbl(
                    "Basic questions",
                    ["Georgian", "English", "Russian hint"],
                    [
                        ["ვინ?", "who?", "кто?"],
                        ["რა?", "what?", "что?"],
                        ["სად?", "where?", "где?"],
                        ["როგორ ხარ?", "how are you?", "как дела?"],
                        ["რა გქვია?", "what's your name?", "как зовут?"],
                    ],
                ),
            ],
        ),
        "3": _ex(
            [
                "Order at a café: მინდა ყავა, გთხოვ",
                "Say what you don't want: არ მინდა ლუდი",
                "Name Georgian foods and drinks",
                "Ask what someone wants: რა გინდა?",
            ],
            "კაფეში ვარ. მინდა ყავა, გთხოვ. არ მინდა ღვინო — მინდა წყალი. ერთი ხაჭაპური და ჩაი. რა გინდა? — მინდა ხინკალი და ლიმონი.",
            "I'm at a café. I'd like coffee, please. I don't want wine — I want water. One khachapuri and tea. What do you want? — I want khinkali and lemon.",
            [
                _tbl(
                    "Ordering pattern",
                    ["Want", "Don't want", "Please"],
                    [
                        ["მინდა ყავა", "არ მინდა ლუდი", "გთხოვ"],
                        ["მინდა ჩაი", "არ მინდა ღვინო", "ერთი …"],
                        ["მინდა წყალი", "არ მინდა რძე", "რა გინდა?"],
                    ],
                    "არ goes directly before the verb, like Russian «не».",
                ),
            ],
        ),
        "4": _ex(
            [
                "Use ვარ/ხარ/არის for I/you/he-she-it",
                "Make plurals with -ები and say აქ/იქ",
                "Count 1–10 and ask რამდენი?",
                "Name professions and ask სად არის …?",
            ],
            "აქ არის ექიმი. იქ არიან სტუდენტები. სად არის ბანკი? ორი სტუდენტი და სამი ექიმი აქ არის. მე სტუდენტი ვარ. შენ ინჟინერი ხარ?",
            "Here is a doctor. There are students. Where is the bank? Two students and three doctors are here. I am a student. Are you an engineer?",
            [
                _tbl(
                    "ვარ — to be (present)",
                    ["Person", "Georgian", "English"],
                    [
                        ["I", "ვარ", "I am"],
                        ["you (sg.)", "ხარ", "you are"],
                        ["he/she/it", "არის", "he/she/it is"],
                        ["we", "ვართ", "we are"],
                        ["you (pl.)", "ხართ", "you are"],
                        ["they", "არიან", "they are"],
                    ],
                ),
                _tbl(
                    "Plural & place",
                    ["Singular", "Plural", "Place"],
                    [
                        ["სტუდენტი", "სტუდენტები", "აქ = here"],
                        ["ექიმი", "ექიმები", "იქ = there"],
                        ["", "", "სად? = where?"],
                    ],
                ),
            ],
        ),
        "5": _ex(
            [
                "Introduce family: ეს ჩემი დედაა",
                "Use possessives: ჩემი, შენი, მისი",
                "Say whose something is: ანას ფოტო / გიორგის ფოტო",
                "Say your age: ოცი წლის ვარ",
            ],
            "ეს ჩემი დედაა. ეს მისი ძმაა. ვისი ეს ფოტოა? — ანას ფოტო. გიორგის ფოტო ძალიან ლამაზია. ოცი წლის ვარ. ჩვენი ოჯახი დიდია.",
            "This is my mother. This is his brother. Whose photo is this? — Ana's photo. Giorgi's photo is very beautiful. I am twenty years old. Our family is big.",
            [
                _tbl(
                    "Possessive pronouns",
                    ["Georgian", "English", "Russian"],
                    [
                        ["ჩემი", "my", "мой"],
                        ["შენი", "your", "твой"],
                        ["მისი", "his / her", "его / её"],
                        ["ჩვენი", "our", "наш"],
                        ["თქვენი", "your (pl.)", "ваш"],
                        ["მათი", "their", "их"],
                    ],
                ),
                _tbl(
                    "Name possession (genitive)",
                    ["Name ends in…", "Pattern", "Example"],
                    [
                        ["vowel", "name + ს", "ანას ფოტო"],
                        ["consonant", "name + ის", "გიორგის ფოტო"],
                        ["age", "X წლის ვარ", "ოცი წლის ვარ"],
                    ],
                ),
            ],
        ),
        "6": _ex(
            [
                "Say your nationality: მე ქართველი ვარ",
                "Ask the time: რამდენია საათი?",
                "Name days, months, and frequency words",
                "Talk about routine: ყოველდღე / ხშირად",
            ],
            "მე ქართველი ვარ, შენ ამერიკელი ხარ. რამდენია საათი? — სამი საათია. ორშაბათს ვმუშაობ. ყოველდღე ვსწავლობ ქართულს. ხშირად ვსეირნობ პარკში.",
            "I am Georgian, you are American. What time is it? — It's three o'clock. On Monday I work. Every day I study Georgian. I often walk in the park.",
            [
                _tbl(
                    "Country → nationality (-ელი)",
                    ["Country", "Person", "English"],
                    [
                        ["საქართველო", "ქართველი", "Georgian"],
                        ["ამერიკა", "ამერიკელი", "American"],
                        ["ინგლისი", "ინგლისელი", "English"],
                        ["გერმანია", "გერმანელი", "German"],
                        ["საფრანგეთი", "ფრანგი", "French"],
                    ],
                ),
                _tbl(
                    "Time & frequency",
                    ["Georgian", "English"],
                    [
                        ["რამდენია საათი?", "What time is it?"],
                        ["სამი საათია", "It's three o'clock"],
                        ["ყოველდღე", "every day"],
                        ["ხშირად", "often"],
                        ["არასოდეს", "never"],
                    ],
                ),
            ],
        ),
        "7": _ex(
            [
                "Describe appearance with adjective + noun",
                "Name body parts, clothing, and colors",
                "Use -ც for 'also/too': ლამაზიც",
                "Ask what color something is: რა ფერია?",
            ],
            "ნინოს ლამაზი სახე აქვს. წითელი პერანგი და შავი შარვალი. ეს ქვედაბოლო ვარდისფერია. ლამაზია და ჭკვიანიც. რა ფერია ჩანთა? — ლურჯი.",
            "Nino has a beautiful face. A red shirt and black trousers. This skirt is pink. She is beautiful and smart too. What color is the bag? — Blue.",
            [
                _tbl(
                    "Adjective + noun & -ც",
                    ["Pattern", "Example", "Meaning"],
                    [
                        ["adj. + noun", "ლამაზი სახე", "beautiful face"],
                        ["noun + -ც", "ლამაზიც", "beautiful too"],
                        ["question", "რა ფერია?", "what color?"],
                        ["", "ეს … წითელია", "this … is red"],
                    ],
                    "Adjective comes BEFORE the noun. Particle ც attaches to the END of the word.",
                ),
            ],
        ),
        "8": _ex(
            [
                "Name seasons and talk about weather",
                "Compare prices: იაფი / ძვირი / ყველაზე იაფი",
                "Use motion verbs: მიდის, მოდის, შედის, გადის",
                "Say dates with ordinals",
            ],
            "გაზაფხულში ყვითელი ყვავილებია. ზაფხულში ცხელა. ბაზარზე ხილი იაფია, მაგრამ ყველაზე იაფი პურია. ის მოდის მაღაზიაში. დღეს მეხუთე რიცხვია.",
            "In spring there are yellow flowers. In summer it's hot. At the market fruit is cheap, but bread is the cheapest. He/she is coming into the shop. Today is the fifth.",
            [
                _tbl(
                    "Motion verbs (3rd person)",
                    ["Georgian", "English", "Direction"],
                    [
                        ["მიდის", "goes (away)", "away from here"],
                        ["მოდის", "comes", "toward here"],
                        ["შედის", "enters", "into"],
                        ["გადის", "goes out / crosses", "out / across"],
                    ],
                ),
                _tbl(
                    "Ordinals 1–5",
                    ["#", "Georgian", "English"],
                    [
                        ["1", "პირველი", "first"],
                        ["2", "მეორე", "second"],
                        ["3", "მესამე", "third"],
                        ["4", "მეოთხე", "fourth"],
                        ["5", "მეხუთე", "fifth"],
                    ],
                ),
            ],
        ),
        "9": _ex(
            [
                "Say what you can do: შემიძლია კითხვა",
                "Say what you like: მომწონს ფილმი",
                "Talk about hobbies and nature",
                "Use simple past: წავედი / მოვედი",
            ],
            "შემიძლია კითხვა და წერა. მომწონს ფილმი და თეატრი. ხშირად ვსეირნობ ტყეში. გუშინ წავედი მუზეუმში და მოვედი საღამოს. ზღვა და მთა ძალიან ლამაზია.",
            "I can read and write. I like films and the theatre. I often walk in the forest. Yesterday I went to the museum and came back in the evening. The sea and mountains are very beautiful.",
            [
                _tbl(
                    "Can / like / past",
                    ["Georgian", "English"],
                    [
                        ["შემიძლია", "I can"],
                        ["მომწონს", "I like (it pleases me)"],
                        ["არ მომწონს", "I don't like"],
                        ["წავედი", "I went (away)"],
                        ["მოვედი", "I came"],
                    ],
                ),
            ],
        ),
        "10": _ex(
            [
                "Say where you are: სახლში ვარ",
                "Give directions: მარჯვნივ, მარცხნივ, პირდაპირ",
                "Name transport and say how you travel: ავტობუსით",
                "Describe city places",
            ],
            "სახლში ვარ. ბანკი ახლოსაა, მაგრამ სადგური შორსაა. მეტროთი მივდივარ ქალაქში. ფეხით მარჯვნივ, შემდეგ პირდაპირ. ეს ქუჩა ძალიან ვიწროა.",
            "I am at home. The bank is near, but the station is far. I go to the city by metro. On foot to the right, then straight ahead. This street is very narrow.",
            [
                _tbl(
                    "Postpositions (locative)",
                    ["Suffix", "Meaning", "Example"],
                    [
                        ["-ში", "in / at", "სახლში = at home"],
                        ["-ზე", "on", "მაგიდაზე = on the table"],
                        ["-თან", "near / with", "ბანკთან = near the bank"],
                    ],
                ),
                _tbl(
                    "Transport (-ით = by)",
                    ["Georgian", "English"],
                    [
                        ["ავტობუსით", "by bus"],
                        ["მეტროთი", "by metro"],
                        ["ფეხით", "on foot"],
                        ["მარჯვნივ", "to the right"],
                        ["პირდაპირ", "straight ahead"],
                    ],
                ),
            ],
        ),
        "11": _ex(
            [
                "Say what you have: მაქვს ბინა",
                "Say who lives with you: მყავს კატა",
                "Describe rooms and furniture",
                "Distinguish things (მაქვს) vs. living beings (მყავს)",
            ],
            "მაქვს ბინა სამი ოთახით. მყავს კატა და ძაღლი. სამზარეულოში დიდი მაგიდაა. საძინებელში საწოლი და კარადა. მაცივარი და ტელევიზორი მაქვს.",
            "I have an apartment with three rooms. I have a cat and a dog. There is a big table in the kitchen. A bed and wardrobe in the bedroom. I have a fridge and a TV.",
            [
                _tbl(
                    "მაქვს vs. მყავს — to have",
                    ["Georgian", "Use for", "Example"],
                    [
                        ["მაქვს", "things", "მაქვს ბინა"],
                        ["მყავს", "people & animals", "მყავს კატა"],
                        ["", "like Russian", "у меня есть"],
                    ],
                    "The 'owner' is in the dative case — same idea as Russian «у меня».",
                ),
            ],
        ),
        "12": _ex(
            [
                "Write a short letter or email in Georgian",
                "Use polite phrases: გმადლობ, გთხოვ, უკაცრავად",
                "Say how long you've studied: X წელია ვსწავლობ",
                "Review A1 grammar across all 12 lessons",
            ],
            "გამარჯობა, ნინო! ორი წელია ვსწავლობ ქართულს. ვიყავი სტუდენტი, ახლა ვმუშაობ ოფისში. მაქვს ბინა თბილისში. გმადლობ დახმარებისთვის! ნახვამდის.",
            "Hello, Nino! I've been studying Georgian for two years. I was a student, now I work in an office. I have an apartment in Tbilisi. Thank you for your help! Goodbye.",
            [
                _tbl(
                    "A1 review — key verbs",
                    ["Georgian", "English", "Lesson"],
                    [
                        ["ვარ / ხარ / არის", "to be", "L4"],
                        ["მინდა / არ მინდა", "want / don't want", "L3"],
                        ["მაქვს / მყავს", "have (thing / person)", "L11"],
                        ["შემიძლია", "I can", "L9"],
                        ["ვსწავლობ", "I study", "L12"],
                    ],
                ),
            ],
        ),
    },
    "a2": {
        "1": _ex(
            ["Talk about extended family and cousins", "Say when you're at university: X-იდან Y-ამდე", "Use compound words: და-ძმა, დედ-მამა", "Describe someone's life and habits"],
            "ანას ოჯახი დიდია. მას ყავს და-ძმა და ბიძაშვილი. ორშაბათიდან პარასკევამდე უნივერსიტეტშია. ხშირად სტუმრობს მეგობრებს. ბიძაჩემი ეკონომიკას სწავლობს.",
            "Ana's family is big. She has siblings and a cousin. From Monday to Friday she is at the university. She often hosts friends. My uncle studies economics.",
            [_tbl("Time range", ["Pattern", "Example"], [["X-იდან Y-ამდე", "ორშაბათიდან პარასკევამდე"], ["from … to …", "from Monday to Friday"]])],
        ),
        "2": _ex(
            ["Describe Georgia's geography and weather", "Use -ით for means: ავტობუსით", "Form adjectives with -იანი: მზიანი, წვიმიანი", "Talk about neighbors and regions"],
            "საქართველო მთიანი და მზიანი ქვეყანაა. ჩრდილოეთში მთებია, სამხრეთში ზღვა. ხშირად წვიმიანია, ზამთარში თოვლიანი. მეზობელი ქართველია. ავტობუსით მივდივარ სოფელში.",
            "Georgia is a mountainous and sunny country. In the north there are mountains, in the south the sea. It is often rainy, snowy in winter. My neighbor is Georgian. I go to the village by bus.",
            [_tbl("Adjectives -იანი", ["Noun", "Adjective", "English"], [["მზე", "მზიანი", "sunny"], ["წვიმა", "წვიმიანი", "rainy"], ["თოვლი", "თოვლიანი", "snowy"]])],
        ),
        "3": _ex(
            ["Describe an apartment in detail", "Use adjective before noun: დიდი სახლი", "Talk about time of day: დილით, საღამოთი", "Describe relatives and household members"],
            "დილით ნათელ ოთახში ვკითხულობ. ჩვენი ბინა ფართოა — ხუთი ოთახი, აივანი და ლიფტი. მამიდა მზის ოთახში ზის. ქვემოთ სადარბაზო ბნელია, ზემოთ კი ნათელი.",
            "In the morning I read in a bright room. Our apartment is spacious — five rooms, a balcony and an elevator. My aunt sits in the sunny room. The entrance hall downstairs is dark, upstairs it's bright.",
            [_tbl("Time adverbs", ["Georgian", "English"], [["დილით", "in the morning"], ["საღამოთი", "in the evening"], ["ღამით", "at night"]])],
        ),
        "4": _ex(
            ["Describe people's appearance and character", "Use ordinals beyond fifth", "Talk about professions and relationship status", "Use past: იყო, ჰყავდა, ჰქონდა"],
            "ის ცნობილი ფეხბურთელი იყო. ყველა ყოჩაღო ეუბნებოდა. ჩემს მეგობარს ჰყავდა მნიშვნელოვანი საქმე. მეორე სართულზე ცოლიანი ეკონომისტი ცხოვრობს.",
            "He was a famous footballer. Everyone told him 'bravo'. My friend had an important job. On the second floor a married economist lives.",
            [_tbl("Past 'have'", ["Person", "Thing", "Person/animal"], [["", "ჰქონდა", "ჰყავდა"], ["he/she", "had (thing)", "had (living)"]])],
        ),
        "5": _ex(
            ["Show a foreign guest around Tbilisi", "Use superlative: ყველაზე + adjective", "Use indefinite pronouns: ვინმე, რამე, არავინ", "Describe architecture and sights"],
            "ეს ყველაზე საინტერესო ხიდია ქალაქში. მოგზაური ვინმე ფოტოს იღებს. აქ არავინ არ არის — ყველა მუზეუმშია. იმედია, რამე შესანიშნავი ვიპოვით.",
            "This is the most interesting bridge in the city. Some traveler is taking a photo. Nobody is here — everyone is at the museum. Hopefully we'll find something wonderful.",
            [_tbl("Indefinite pronouns", ["Georgian", "English"], [["ვინმე", "someone"], ["რამე", "something"], ["არავინ", "nobody"], ["არაფერი", "nothing"]])],
        ),
        "6": _ex(
            ["Describe your daily routine in detail", "Compare with უფრო…ვიდრე", "Talk about cooking and kitchen items", "Use frequency adverbs"],
            "ჩემი დილა უფრო სწრაფია, ვიდრე საღამო. ჩვეულებრივ დილით ჩაის ვსვამ და პურს ვჭამ. ხანდახან შემწვარ ხორცს ვამზადებ. საღამოს ნელა ვსეირნობ.",
            "My morning is faster-paced than my evening. Usually in the morning I drink tea and eat bread. Sometimes I prepare fried meat. In the evening I walk slowly.",
            [_tbl("Comparison", ["Pattern", "Example"], [["უფრო … ვიდრე", "უფრო სწრაფია, ვიდრე"], ["ისეთივე … როგორც", "as … as"]])],
        ),
        "7": _ex(
            ["Shop at a market on the weekend", "Name fruits and vegetables in Georgian", "Use conjunctions: და, მაგრამ, რომ", "Talk about selection and prices"],
            "შაბათს ბაზარზე ვდივარ. ფორთოხალი და კივი იაფია, მაგრამ ყველაფერი იაფი არ არის. ვიცი, რომ დიდი არჩევანია. ვიყიდი მარწყვს, სტაფილოს და მურაბას.",
            "On Saturday I go to the market. Oranges and kiwi are cheap, but not everything is cheap. I know there is a big selection. I buy strawberries, carrots and jam.",
            [_tbl("Conjunctions", ["Georgian", "English"], [["და", "and"], ["მაგრამ", "but"], ["რომ", "that"], ["იმიტომ რომ", "because"]])],
        ),
        "8": _ex(
            ["Handle a bank conversation", "Use purpose nouns: სა- + stem", "Talk about loans, accounts, and cards", "Use postpositions with genitive"],
            "ბანკში ვარ. კრედიტის შესახებ კონსულტანტს დაველაპარაკები. საბანკო ბარათი მჭირდება. ფული ანგარიშზეა. კრიზისის გამო ხანდახან რთულია.",
            "I'm at the bank. I'll speak with a consultant about the loan. I need a bank card. The money is in the account. Because of the crisis sometimes it's difficult.",
            [_tbl("Purpose nouns (სა-)", ["Room", "Georgian", "English"], [["bedroom", "საძინებელი", "for sleeping"], ["kitchen", "სამზარეულო", "for cooking"], ["dining", "სასადილო", "for eating"]])],
        ),
        "9": _ex(
            ["Talk about health and the body", "Visit a doctor or pharmacy", "Describe symptoms and treatment", "Use formal polite phrases"],
            "არ ვგრძნობ თავს კარგად. ექიმთან მივედი. მან თქვა, რომ დასვენება მჭირდება. აფთიაქში წამალს ვიყიდე. იმედია, ხვალ უკეთესად ვიქნები.",
            "I don't feel well. I went to the doctor. He said I need rest. I bought medicine at the pharmacy. Hopefully tomorrow I'll be better.",
            [_tbl("Health phrases", ["Georgian", "English"], [["ვგრძნობ თავს", "I feel (myself)"], ["მჭირდება", "I need"], ["აფთიაქი", "pharmacy"]])],
        ),
        "10": _ex(
            ["Shop for a new apartment", "Compare apartments: bigger, cheaper, brighter", "Name household items and repairs", "Negotiate with a seller"],
            "ახალი ბინა ვეძებ. ეს უფრო ფართოა, ვიდრე ჩემი ძველი. მაგრამ ძვირია. ფანჯრები დიდია, აივანიც კარგია. გადავწყვიტე, რომ ვიყიდო.",
            "I'm looking for a new apartment. This one is more spacious than my old one. But it's expensive. The windows are big, the balcony is good too. I decided to buy it.",
        ),
        "11": _ex(
            ["Talk about Georgian wine and toasts", "Describe a festival atmosphere", "Use festival and vineyard vocabulary", "Participate in a wine tasting conversation"],
            "ღვინის ფესტივალზე ვარ. ქართული ღვინო ძალიან ცნობილია. მეგობარი მიმიყვანს ჯარიმაში. ვცდი თეთრ და წითელ ღვინოს. ყველას გამარჯობა ვუთხრა!",
            "I'm at the wine festival. Georgian wine is very famous. A friend took me to the cellar. I try white and red wine. I said hello to everyone!",
        ),
        "12": _ex(
            ["Be a guest in a Georgian family", "Use hospitality phrases and toasts", "Describe a supra and traditions", "Thank hosts warmly"],
            "სტუმრად ვარ ქართულ ოჯახში. მასპინძელი ძალიან კეთილია. მაგიდა სავსეა — ხაჭაპური, ხინკალი, ღვინო. გამარჯობა ვთქვი და გმადლობთ ვუთხარი. ნამდვილი ქართული სტუმართმოფრთხილებაა!",
            "I'm a guest in a Georgian family. The host is very kind. The table is full — khachapuri, khinkali, wine. I said hello and thanked them. Real Georgian hospitality!",
        ),
    },
    "a2plus": {
        "1": _ex(
            ["Discuss Georgian exports and products", "Talk about business and trade", "Describe what a country produces", "Use formal register for economics"],
            "საქართველოს ეროვნული პროდუქტი ცნობილია. ღვინო და ჩაი ექსპორტზეა. ბიზნესმენები ახალ ბაზრებს ეძებენ. ჩვენი პროდუქცია ხარისხიანია.",
            "Georgia's national product is well known. Wine and tea are for export. Businessmen are looking for new markets. Our production is high quality.",
        ),
        "2": _ex(
            ["Read product labels in Georgian", "Talk about organic and local food", "Discuss Agrohub and farming", "Compare product quality"],
            "ეტიკეტზე ყველაფერი ქართულადაა. ეს პროდუქტი ორგანუკურია. ადგილობრივი ფერმერების პროდუქცია უკეთესია. Agrohub-ში ბევრი საინტერესო პროდუქტია.",
            "Everything on the label is in Georgian. This product is organic. Local farmers' produce is better. There are many interesting products at Agrohub.",
        ),
        "3": _ex(
            ["Call or talk about emergency 112", "Describe an emergency clearly", "Follow instructions from operators", "Stay calm and give location"],
            "ავარია მოხდა! დავურეკე 112-ს. ოპერატორმა კითხვები დამისვა: სად ხარ? რა მოხდა? მისამართი ვთქვი და დახმარება მალე მოვიდა.",
            "An accident happened! I called 112. The operator asked questions: where are you? what happened? I gave the address and help came quickly.",
        ),
        "4": _ex(
            ["Report lost items to police", "Describe what you lost and where", "Fill in basic forms at a station", "Use past tense for what happened"],
            "პასპორტი დამეკარგა. პოლიციაში მივედი და ანკეტა შევავსე. ვთქვი, სად იყო და როდის. იმედია, მალე ვიპოვი.",
            "I lost my passport. I went to the police and filled in a form. I said where it was and when. Hopefully I'll find it soon.",
        ),
        "5": _ex(
            ["Plan a holiday and choose destinations", "Talk about tours and travel agencies", "Compare resorts and regions", "Book a trip in Georgian"],
            "ზაფხულისთვის ტურს ვეძებ. საქართველოში ბევრი საინტერესო ადგილია — ბათუმი, კახეთი, სვანეთი. ტურისტული კომპანია კარგ წინადადებებს გვთავაზობს.",
            "I'm looking for a tour for summer. There are many interesting places in Georgia — Batumi, Kakheti, Svaneti. The travel company offers good deals.",
        ),
        "6": _ex(
            ["Choose and book a hotel", "Compare rooms, prices, and amenities", "Ask about breakfast and Wi-Fi", "Make a reservation by phone"],
            "სასტუმროს ვეძებ ბათუმში. ოთახი ზღვისპირა უნდა იყოს. ერთი ღამე საკმარისია. საუზმე შედის? დავაჯავშნე ინტერნეტით.",
            "I'm looking for a hotel in Batumi. The room should be seaside. One night is enough. Is breakfast included? I booked online.",
        ),
        "7": _ex(
            ["Write a social media profile in Georgian", "Talk about hobbies, work, and interests", "Describe yourself for an online audience", "Use present tense self-description"],
            "ჩემს პროფილში ვწერ: მე ნინო ვარ, თბილისში ვცხოვრობ. ვმუშაობ ჟურნალისტად. მომწონს მუსიკა და მოგზაურობა. ახალ მეგობრებს ვეძებ.",
            "On my profile I write: I am Nino, I live in Tbilisi. I work as a journalist. I like music and travel. I'm looking for new friends.",
        ),
        "8": _ex(
            ["Talk about blogging and vlogging", "Describe your channel and content", "Invite people to subscribe", "Discuss social media habits"],
            "მე ვლოგს ვიწერ ქართულად. ყოველ კვირას ახალ ვიდეოს ვაქვეყნებ. თემა — ქართული კულტურა და ენა. გამოიწერე ჩემი არხი!",
            "I write a vlog in Georgian. Every week I publish a new video. The topic is Georgian culture and language. Subscribe to my channel!",
        ),
        "9": _ex(
            ["Talk about a film premiere", "Describe the event and celebrities", "Share your impressions", "Invite someone to the cinema"],
            "გუშინ პრემიერაზე ვიყავი. ფილმი ძალიან საინტერესო იყო. მსახიობები და რეჟისორი იქ იყვნენ. ყველას მოვწონს. ხვალ კინოში მივდივართ?",
            "Yesterday I was at the premiere. The film was very interesting. The actors and director were there. Everyone liked it. Shall we go to the cinema tomorrow?",
        ),
        "10": _ex(
            ["Summarise a film plot in Georgian", "Write or give a short review", "Express opinion: მომწონს / არ მომწონს", "Recommend films to friends"],
            "ფილმის სიუჟეტი ასეთია: მთავარი გმირი თბილისში ცხოვრობს. ბოლოს ყველაფერი კარგად მთავრდება. მომწონს, რადგან ძალიან საინტერესოა. გირჩევნია!",
            "The plot is like this: the main character lives in Tbilisi. In the end everything turns out fine. I like it because it's very interesting. I recommend it!",
        ),
        "11": _ex(
            ["Talk about foreigners living in Georgia", "Compare cultures and adaptation", "Discuss why people move to Georgia", "Share experiences of expat life"],
            "უცხოელი ბევრი ცხოვრობს თბილისში. მათ მოწონთ ქართული კულტურა და სამზარეულო. ზოგი ქართულს სწავლობს, ზოგი მუშაობს. საქართველო მეგობრული ქვეყანაა.",
            "Many foreigners live in Tbilisi. They like Georgian culture and cuisine. Some study Georgian, some work. Georgia is a friendly country.",
        ),
        "12": _ex(
            ["Discuss language learning strategies", "Set goals for your Georgian study", "Talk about grammar, reading, and practice", "Encourage another learner"],
            "ქართულის სწავლა რთულია, მაგრამ საინტერესო. ყოველდღე ვკითხულობ და ვცდილობ ლაპარაკს. გრამატიკა მნიშვნელოვანია. რათა უკეთესად ვისაუბრო, ბევრს ვვარჯიშობ.",
            "Learning Georgian is hard but interesting. Every day I read and try to speak. Grammar is important. So that I speak better, I practice a lot.",
            [_tbl("Learning verbs", ["Georgian", "English"], [["ვსწავლობ", "I study"], ["ვცდილობ", "I try"], ["ვკითხულობ", "I read"], ["რათა", "so that"]])],
        ),
    },
    "b1": {
        "1": _ex(
            ["Read and discuss a short biography", "Use imperfect past: იბადებოდა, მიდიოდა", "Talk about someone's life journey", "Narrate events in sequence"],
            "გოდერძი ჩოხელიშვილი ქართველი მწერალი იყო. იგი სოფელში იბადებოდა და თბილისში მიდიოდა სწავლისთვის. მისი ცხოვრება საინტერესო იყო. მკითხველები მას უყვარდათ.",
            "Goderdzi Chokhelishvili was a Georgian writer. He was born in a village and went to Tbilisi to study. His life was interesting. Readers loved him.",
            [_tbl("Imperfect past", ["Georgian", "English"], [["იბადებოდა", "was being born"], ["მიდიოდა", "was going"], ["აღწევდა", "was reaching"]])],
        ),
        "2": _ex(
            ["Write or talk about your CV", "Describe work experience and skills", "Read job vacancies in Georgian", "Apply for a position"],
            "ჩემი CV ასე გამოიყურება: ორწლიანი გამოცდილება მაქვს ჟურნალისტიკაში. ვსწავლობდი უნივერსიტეტში. ვაკანსიაზე ვწერ, რადგან ახალი სამუშაო მინდა.",
            "My CV looks like this: I have two years of experience in journalism. I studied at university. I'm applying for the vacancy because I want a new job.",
        ),
        "3": _ex(
            ["Prepare for a job interview", "Answer questions about experience and skills", "Use formal register", "Ask questions back to the interviewer"],
            "გასაუბრებაზე მივედი. მკითხეს, რა გამოცდილება მაქვს. ვთქვი, რომ ბევრი პროექტი გამიკეთებია. შემიძლია გუნდში მუშაობა. მათაც მომწონთ ჩემი პასუხები.",
            "I went to the interview. They asked what experience I have. I said I've done many projects. I can work in a team. They liked my answers too.",
            [_tbl("Interview phrases", ["Georgian", "English"], [["შემიძლია", "I can"], ["აქვს", "he/she has"], ["მოვემზადოთ", "let us prepare"]])],
        ),
        "4": _ex(
            ["Talk about unusual professions", "Describe what different jobs involve", "Use relative clauses: რომელიც", "Compare ordinary and unusual careers"],
            "ზოგი პროფესია უჩვეულოა. მაგალითად, ალპინისტი, რომელიც მთებში მუშაობს. ან ფოტოგრაფი, რომელიც ღამით ცხოვრობს. ყველას სხვადასხვა სამუშაო მოწონს.",
            "Some professions are unusual. For example, an alpinist who works in the mountains. Or a photographer who lives at night. Everyone likes different work.",
        ),
        "5": _ex(
            ["Understand safety instructions", "Give and follow commands formally", "Talk about alpinism and risk", "Use imperative forms politely"],
            "ინსტრუქცია ასეთია: დაიცავით წესები! არ გადაინაცვლოთ საშიში ადგილიდან. ალპინისტები ყოველთვის ერთმანეთს ეხმარებიან. უსაფრთხოება პირველ რიგშია.",
            "The instruction is like this: observe the rules! Do not move from the dangerous place. Alpinists always help each other. Safety comes first.",
            [_tbl("Formal imperatives", ["Georgian", "English"], [["დაიცავით", "observe! (formal)"], ["არ გადაინაცვლოთ", "do not move"]])],
        ),
        "6": _ex(
            ["Discuss sports and the Olympics", "Talk about winning and losing", "Describe a sporting event", "Use past narrative for results"],
            "ოლიამპიადაზე ქართველი სპორტსმენები კარგად გამოიყურებიან. ერთმა გაიმარჯვა, მეორემა კი ვერა. მატჩი დიდი იყო. ყველამ ყურადღებით უყურა.",
            "At the Olympics Georgian athletes look good. One won, another didn't. The match was big. Everyone watched attentively.",
            [_tbl("Result verbs", ["Georgian", "English"], [["გაიმარჯვა", "won"], ["დაიწყო", "began"], ["დასრულდა", "finished"]])],
        ),
        "7": _ex(
            ["Talk about free time and music", "Say how you spend evenings", "Express likes with მომწონს", "Discuss concerts and hobbies"],
            "თავისუფალ დროს მუსიკას ვსმენ. მომწონს ქართული და კლასიკური მუსიკა. ხშირად კონცერტზე ვდივარ. კვირანდელს ვატარებ მეგობრებთან.",
            "In my free time I listen to music. I like Georgian and classical music. I often go to concerts. I spend the weekend with friends.",
        ),
        "8": _ex(
            ["Discuss flash mobs and social phenomena", "Describe a crowd event", "Use linking words in longer sentences", "Give your opinion on trends"],
            "ფლეშმობი ქუჩაში მოულოდნელად დაიწყო. ბევრი ახალგაზრდა შეიკრა. ვიდეო გავრცელდა ინტერნეტში. ეს საინტერესო სოციალური მოვლენაა.",
            "The flash mob started unexpectedly in the street. Many young people gathered. A video spread on the internet. This is an interesting social phenomenon.",
            [_tbl("Linking", ["Georgian", "English"], [["რომელიც", "which / who"], ["მაკავშირებელი სიტყვა", "linking word"]])],
        ),
        "9": _ex(
            ["Shop online in Georgian", "Describe delivery and returns", "Compare prices on websites", "Talk about future plans with უნდა"],
            "ინტერნეტში ვყიდულობ ტანსაცმელს. ფასი იაფია, მაგრამ მიწოდება ძვირია. უნდა ვიცადო ორი დღე. თუ არ მომწონს, დავაბრუნებ.",
            "I buy clothes online. The price is cheap, but delivery is expensive. I have to wait two days. If I don't like it, I'll return it.",
            [_tbl("Future & obligation", ["Georgian", "English"], [["უნდა", "should / must"], ["იყიდება", "is sold"], ["მომავალი დრო", "future tense"]])],
        ),
        "10": _ex(
            ["Discuss taxes and consumer rights", "Talk about receipts and refunds", "Understand basic legal vocabulary", "Assert your rights as a consumer"],
            "მომხმარებელს უფლება აქვს ხარისხიანი პროდუქტის. გადასახადი ყველას უნდა გადავიხადოს. ქვითარი შეინახეთ. თუ პრობლემაა, საჩივრის დაწერა შეგიძლიათ.",
            "The consumer has the right to quality product. Everyone must pay tax. Keep the receipt. If there's a problem, you can file a complaint.",
        ),
        "11": _ex(
            ["Talk about regional Georgian cuisine", "Name dishes from different regions", "Describe cooking methods and ingredients", "Recommend food to visitors"],
            "ყველა რეგიონს საკუთარი სამზარეულო აქვს. კახეთში ხინკალი და ღვინო, სვანეთში კუბდარი. იმერეთში ყველის პური ცნობილია. ყველაფერი ძალიან გემრიელია!",
            "Every region has its own cuisine. In Kakheti khinkali and wine, in Svaneti kubdari. Imereti is famous for cheese bread. Everything is very tasty!",
        ),
        "12": _ex(
            ["Discuss healthy living in the Caucasus", "Talk about diet, sport, and nature", "Compare city and mountain life", "Give advice on wellness"],
            "ჯანსაღი ცხოვრება მნიშვნელოვანია. კავკასიაში სუფთა ჰაერი და მთებია. ვარჯიშს ვაკეთებ და ბოსტნეულს ვჭამ. ნაკლები შაქარი, მეტი წყალი — ეს კარგია.",
            "Healthy living is important. In the Caucasus there is clean air and mountains. I exercise and eat vegetables. Less sugar, more water — that's good.",
        ),
    },
}


def merge_reader_extras(lesson, book, num):
    """Return lesson dict with reader extras merged in (shallow copy)."""
    from reader_verbs import FOCUS_VERBS

    out = copy.deepcopy(lesson)
    extra = READER_EXTRAS.get(book, {}).get(str(num), {})
    if not extra:
        extra = {}

    if extra.get("can_do"):
        out["can_do"] = extra["can_do"]
    if extra.get("reading"):
        out["reading"] = extra["reading"]
    if extra.get("grammar_tables"):
        g = out.setdefault("grammar", {})
        g["tables"] = extra["grammar_tables"]

    verb = FOCUS_VERBS.get(book, {}).get(str(num))
    if verb:
        out["focus_verb"] = verb

    from reader_sentences import get_sentence_exercises
    exercises = get_sentence_exercises(book, num)
    if exercises:
        out["sentence_builder"] = exercises

    if lesson.get("practice_audio"):
        out["practice_audio"] = lesson["practice_audio"]

    return out
