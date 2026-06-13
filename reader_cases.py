"""Case & declension tables merged into reader lessons (not Telegram)."""

from reader_extras import _tbl


def get_case_tables(book, num):
    key = str(num)
    tables = CASE_TABLES.get(book, {}).get(key)
    return list(tables) if tables else []


CASE_TABLES = {
    "a1": {
        "1": [
            _tbl(
                "Georgian has 7 cases — preview",
                ["Case", "Georgian name", "Main use at A1"],
                [
                    ["Nominative", "სახელობითი", "subject: ეს არის კაფე"],
                    ["Dative", "მიცემითი", "to/for: მინდა ყავა · მაქვს"],
                    ["Genitive", "ნათესაობითი", "of / 's: ანას ფოტო"],
                    ["Instrumental", "მოქმედებითი", "by/with: ავტობუსით"],
                ],
                "No gender on nouns — endings change, not the word itself.",
            ),
            _tbl(
                "Nominative → dative (-ს)",
                ["Noun (nom.)", "Dative", "English"],
                [
                    ["კაფე", "კაფეს", "café"],
                    ["სტუდენტი", "სტუდენტს", "student"],
                    ["ტელეფონი", "ტელეფონს", "phone"],
                    ["აეროპორტი", "აეროპორთს", "airport"],
                ],
                "Most A1 nouns add -ს in dative. Used with მინდა, მაქვს, and -ში.",
            ),
        ],
        "3": [
            _tbl(
                "Dative + experiencer verbs",
                ["Structure", "Example", "Meaning"],
                [
                    ["მე + მინდა", "მინდა ყავა", "I want coffee"],
                    ["შენ + გინდა", "რა გინდა?", "What do you want?"],
                    ["მას + უნდა", "უნდა წყალი", "He/she wants water"],
                ],
                "The person is in dative (like Russian «мне хочется»). The thing wanted stays nominative.",
            ),
        ],
        "5": [
            _tbl(
                "Genitive (-ის / -ს) — possession",
                ["Pattern", "Example", "English"],
                [
                    ["name + ს (vowel)", "ანას ფოტო", "Ana's photo"],
                    ["name + ის (consonant)", "გიორგის ფოტო", "Giorgi's photo"],
                    ["noun + ის", "დედის ფოტო", "mother's photo"],
                    ["ჩემი / შენი / მისი", "ჩემი დედა", "my mother"],
                ],
            ),
            _tbl(
                "Noun declension — family words",
                ["Nom.", "Dat. (-ს)", "Gen. (-ის)", "English"],
                [
                    ["დედა", "დედას", "დედის", "mother"],
                    ["მამა", "მამას", "მამის", "father"],
                    ["და", "დას", "დის", "sister"],
                    ["ძმა", "ძმას", "ძმის", "brother"],
                    ["შვილი", "შვილს", "შვილის", "child"],
                ],
            ),
        ],
        "8": [
            _tbl(
                "Noun cases — shopping & places",
                ["Nom.", "Dat. (-ს)", "Inst. (-ით)", "English"],
                [
                    ["მაღაზია", "მაღაზიას", "მაღაზიით", "shop"],
                    ["ბაზარი", "ბაზარს", "ბაზრით", "market"],
                    ["ფასი", "ფასს", "ფასით", "price"],
                    ["რიცხვი", "რიცხვს", "რიცხვით", "date"],
                ],
                "მაღაზიაში = in the shop (dative + -ში).",
            ),
        ],
        "9": [
            _tbl(
                "Dative + motion / location",
                ["Phrase", "Case used", "English"],
                [
                    ["მუზეუმში", "dative + -ში", "in the museum"],
                    ["ტყეში", "dative + -ში", "in the forest"],
                    ["ზღვაზე", "dative + -ზე", "on the sea"],
                    ["პარკში", "dative + -ში", "in the park"],
                ],
            ),
            _tbl(
                "Past tense — motion verbs",
                ["Present", "Past (I)", "English"],
                [
                    ["მიდის", "წავედი", "I went"],
                    ["მოდის", "მოვედი", "I came"],
                    ["სეირნობს", "ვსეირნობდი", "I was walking"],
                ],
            ),
        ],
        "10": [
            _tbl(
                "The 7 cases — A1 essentials",
                ["Ending", "Case", "Example"],
                [
                    ["(base)", "Nominative", "სახლი = house"],
                    ["-ს", "Dative", "სახლს → სახლში"],
                    ["-ის", "Genitive", "სახლის = of the house"],
                    ["-ით", "Instrumental", "სახლით / ავტობუსით"],
                    ["-ში", "in (postposition)", "სახლში = at home"],
                    ["-ზე", "on", "მაგიდაზე = on the table"],
                    ["-თან", "near", "ბანკთან = near the bank"],
                ],
            ),
            _tbl(
                "City nouns — declension",
                ["Nom.", "Dat. (-ს)", "Locative", "English"],
                [
                    ["სახლი", "სახლს", "სახლში", "house / home"],
                    ["ბანკი", "ბანკს", "ბანკში", "bank"],
                    ["სადგური", "სადგურს", "სადგურში", "station"],
                    ["ავტობუსი", "ავტობუსს", "ავტობუსით", "bus / by bus"],
                    ["ქუჩა", "ქუჩას", "ქუჩაში", "street"],
                ],
            ),
        ],
        "11": [
            _tbl(
                "Dative subject — მაქვს / მყავს",
                ["Person", "Have (thing)", "Have (living)", "English"],
                [
                    ["მე", "მაქვს", "მყავს", "I have"],
                    ["შენ", "გაქვს", "გყავს", "you have"],
                    ["მას", "აქვს", "ყავს", "he/she has"],
                    ["ჩვენ", "გვაქვს", "გვყავს", "we have"],
                ],
                "მე is dative — literally «to me there is». Same pattern as მინდა.",
            ),
            _tbl(
                "Home vocabulary — cases",
                ["Nom.", "Dat. (-ს)", "Gen. (-ის)", "English"],
                [
                    ["ბინა", "ბინას", "ბინის", "apartment"],
                    ["ოთახი", "ოთახს", "ოთახის", "room"],
                    ["სამზარეულო", "სამზარეულოს", "სამზარეულოს", "kitchen"],
                    ["მაგიდა", "მაგიდას", "მაგიდის", "table"],
                    ["კატა", "კატას", "კატის", "cat"],
                ],
            ),
        ],
        "12": [
            _tbl(
                "Past · present · future — review",
                ["Tense", "ვარ (I am)", "მაქვს (I have)", "ვსწავლობ"],
                [
                    ["Present", "ვარ", "მაქვს", "ვსწავლობ"],
                    ["Past", "ვიყავი", "მქონდა", "ვსწავლობდი"],
                    ["Future", "ვიქნები", "მექნება", "ვისწავლი"],
                ],
            ),
            _tbl(
                "Letter-writing phrases",
                ["Georgian", "English"],
                [
                    ["ძვირფასო …", "Dear …"],
                    ["პატივისცემით", "Respectfully / Yours sincerely"],
                    ["გთხოვთ, დამიკავშირდეთ", "Please contact me"],
                    ["გმადლობთ ყურადღებისთვის", "Thank you for your attention"],
                ],
            ),
        ],
    },
    "a2": {
        "1": [
            _tbl(
                "Genitive with dates and time ranges",
                ["Pattern", "Example", "Meaning"],
                [
                    ["X-ის Y", "მაისის დასაწყისი", "the beginning of May"],
                    ["A-დან B-მდე", "ორშაბათიდან პარასკევამდე", "from Monday to Friday"],
                    ["დღის/კვირის + ნაწილი", "დღის ბოლოს", "at the end of the day"],
                    ["წლის + სეზონი", "ზაფხულის ბოლოს", "at the end of summer"],
                ],
                "Genitive often appears in time expressions and range boundaries.",
            ),
            _tbl(
                "Time nouns in key cases",
                ["Nominative", "Genitive", "Dative", "English"],
                [
                    ["დღე", "დღის", "დღეს", "day"],
                    ["კვირა", "კვირის", "კვირას", "week / on Sunday"],
                    ["თვე", "თვის", "თვეს", "month"],
                    ["წელი", "წლის", "წელს", "year / this year"],
                ],
            ),
        ],
        "2": [
            _tbl(
                "Instrumental -ით (means, tool, transport)",
                ["Pattern", "Example", "Meaning"],
                [
                    ["noun + ით", "ავტობუსით მივდივარ", "I go by bus"],
                    ["noun + ით", "დანა-ჩანგლით ვჭამ", "I eat with knife and fork"],
                    ["noun + ით", "ქართულად, მაგრამ აქცენტით", "with an accent"],
                    ["time + ით", "ერთ საათით", "for one hour / by one hour"],
                ],
            ),
            _tbl(
                "Common instrumental forms",
                ["Nominative", "Instrumental", "English"],
                [
                    ["ავტობუსი", "ავტობუსით", "bus / by bus"],
                    ["მანქანა", "მანქანით", "car / by car"],
                    ["კალამი", "კალმით", "pen / with a pen"],
                    ["მეგობარი", "მეგობრით", "friend / with a friend"],
                ],
            ),
        ],
        "3": [
            _tbl(
                "Adjective + noun order and case",
                ["Pattern", "Example", "Meaning"],
                [
                    ["adj + noun (nom.)", "დიდი სახლი", "a big house"],
                    ["adj + noun (dat.)", "დიდ სახლს", "to the big house"],
                    ["adj + noun (gen.)", "დიდი სახლის კარი", "door of the big house"],
                    ["adj + noun (pl.)", "დიდი სახლები", "big houses"],
                ],
                "Adjective usually precedes noun and follows case context in the phrase.",
            ),
        ],
        "4": [
            _tbl(
                "Ordinals and past-time references",
                ["Type", "Example", "Meaning"],
                [
                    ["ordinal", "პირველი გაკვეთილი", "first lesson"],
                    ["ordinal", "მეორე სართული", "second floor"],
                    ["past adverb", "გუშინ წავედი", "I went yesterday"],
                    ["past phrase", "გასულ კვირას შევხვდით", "we met last week"],
                ],
            ),
            _tbl(
                "Past forms (high-frequency verbs)",
                ["Infinitive", "Past (I)", "Past (he/she)", "English"],
                [
                    ["წასვლა", "წავედი", "წავიდა", "to go"],
                    ["მოსვლა", "მოვედი", "მოვიდა", "to come"],
                    ["ნახვა", "ვნახე", "ნახა", "to see"],
                    ["კითხვა", "ვიკითხე", "იკითხა", "to ask/read"],
                ],
            ),
        ],
        "5": [
            _tbl(
                "Comparative and superlative",
                ["Degree", "Pattern", "Example"],
                [
                    ["positive", "adj", "დიდი"],
                    ["comparative", "უფრო + adj", "უფრო დიდი"],
                    ["superlative", "ყველაზე + adj", "ყველაზე დიდი"],
                    ["equative", "ისეთივე + adj", "ისეთივე ძვირი"],
                ],
            ),
        ],
        "6": [
            _tbl(
                "Using უფრო for comparison",
                ["Structure", "Example", "Meaning"],
                [
                    ["A უფრო adj, ვიდრე B", "ეს უფრო იაფია, ვიდრე ის", "This is cheaper than that"],
                    ["verb + უფრო კარგად", "ახლა უფრო კარგად ვლაპარაკობ", "I speak better now"],
                    ["quantity + უფრო მეტი", "უფრო მეტი დრო", "more time"],
                    ["frequency + უფრო ხშირად", "უფრო ხშირად ვკითხულობ", "I read more often"],
                ],
                "ვიდრე introduces the second item in many formal comparisons.",
            ),
        ],
        "7": [
            _tbl(
                "Core conjunctions",
                ["Conjunction", "Use", "Example"],
                [
                    ["და", "addition", "ჩაი და ყავა"],
                    ["მაგრამ", "contrast", "მინდა, მაგრამ ვერ ვახერხებ"],
                    ["ან", "choice", "ავტობუსით ან მეტროთი"],
                    ["რადგან", "reason", "ვრჩები სახლში, რადგან წვიმს"],
                    ["თუ", "condition", "თუ დრო გაქვს, წავიდეთ"],
                ],
            ),
            _tbl(
                "Clause linking patterns",
                ["Pattern", "Example", "Meaning"],
                [
                    ["X, რადგან Y", "დავიღალე, რადგან ბევრი ვიმუშავე", "I got tired because I worked a lot"],
                    ["თუ X, Y", "თუ მოიცლი, დამირეკე", "If you can, call me"],
                    ["X და Y", "წავედი მაღაზიაში და ვიყიდე პური", "I went to the shop and bought bread"],
                ],
            ),
        ],
        "8": [
            _tbl(
                "Genitive + შესახებ (about)",
                ["Pattern", "Example", "Meaning"],
                [
                    ["noun(gen.) + შესახებ", "პროექტის შესახებ", "about the project"],
                    ["pronoun(gen.) + შესახებ", "ამის შესახებ", "about this"],
                    ["person(gen.) + შესახებ", "ნინოს შესახებ", "about Nino"],
                    ["question", "რის შესახებ?", "about what?"],
                ],
                "შესახებ requires genitive form before it.",
            ),
        ],
        "9": [
            _tbl(
                "Modals: possibility, need, desire",
                ["Modal", "Pattern", "Example"],
                [
                    ["შეიძლება", "შეიძლება + infinitive", "აქ დაჯდომა შეიძლება"],
                    ["უნდა", "dative person + უნდა", "მე უნდა წავიდე"],
                    ["მინდა", "dative person + მინდა + noun/verb", "მინდა დასვენება"],
                    ["შემიძლია", "dative person + შემიძლია", "შემიძლია დახმარება"],
                ],
            ),
            _tbl(
                "Modal mini-paradigm",
                ["Person", "want", "must", "can"],
                [
                    ["მე", "მინდა", "უნდა", "შემიძლია"],
                    ["შენ", "გინდა", "უნდა", "შეგიძლია"],
                    ["მას", "უნდა", "უნდა", "შეუძლია"],
                ],
            ),
        ],
        "10": [
            _tbl(
                "Imperative basics",
                ["Verb", "Singular command", "Plural/polite", "Meaning"],
                [
                    ["მოსვლა", "მოდი", "მოდით", "come"],
                    ["წასვლა", "წადი", "წადით", "go"],
                    ["დაჯდომა", "დაჯექი", "დაჯექით", "sit down"],
                    ["მოცდა", "მოიცადე", "მოიცადეთ", "wait"],
                ],
            ),
            _tbl(
                "Negative commands",
                ["Pattern", "Example", "Meaning"],
                [
                    ["ნუ + verb", "ნუ ღელავ", "don't worry"],
                    ["არ + future/present", "არ წახვიდე", "don't go"],
                    ["თხოვნა", "გთხოვ, გაიმეორე", "please repeat"],
                ],
            ),
        ],
        "11": [
            _tbl(
                "Location postpositions",
                ["Ending/postposition", "Example", "Meaning"],
                [
                    ["-ში", "სახლში", "in the house"],
                    ["-ზე", "მაგიდაზე", "on the table"],
                    ["-თან", "ბანკთან", "near/by the bank"],
                    ["-დან", "თბილისიდან", "from Tbilisi"],
                    ["-მდე", "სადგურამდე", "up to the station"],
                ],
            ),
            _tbl(
                "Where? From where? To where?",
                ["Question", "Typical form", "Example"],
                [
                    ["სად?", "dative + -ში/-ზე", "სად ხარ? ოფისში."],
                    ["საიდან?", "noun + -დან", "საიდან მოდიხარ? სახლიდან."],
                    ["სადამდე?", "noun + -მდე", "სადამდე მიდიხარ? მეტრომდე."],
                ],
            ),
        ],
        "12": [
            _tbl(
                "Similative -ივით (like/as)",
                ["Pattern", "Example", "Meaning"],
                [
                    ["noun + ივით", "ბავშვივით", "like a child"],
                    ["pronoun + ივით", "შენივით", "like you"],
                    ["time expression", "დღეს გუშინდელივით ცხელა", "today is as hot as yesterday"],
                    ["manner", "ქარივით სწრაფად", "as fast as wind"],
                ],
                "-ივით often expresses resemblance in manner or quality.",
            ),
        ],
    },
    "a2plus": {
        "1": [
            _tbl(
                "Passive formation with -ებ-",
                ["Type", "Example", "Meaning"],
                [
                    ["present passive", "იხსნება", "it is opened"],
                    ["causative/passive stem", "იგეგმება", "it is being planned"],
                    ["habitual passive", "იცვლება", "it changes / is changed"],
                    ["formal notice", "აკრძალულია მოწევა", "smoking is prohibited"],
                ],
                "A2+ introduces common impersonal/passive-style public language.",
            ),
            _tbl(
                "Active vs passive viewpoint",
                ["View", "Example", "Meaning"],
                [
                    ["active", "ადმინისტრაცია ცვლის წესს", "administration changes the rule"],
                    ["passive", "წესი იცვლება", "the rule is changed"],
                    ["impersonal", "აქ ინგლისურად ლაპარაკობენ", "English is spoken here"],
                ],
            ),
        ],
        "2": [
            _tbl(
                "Genitive labels and signs",
                ["Label type", "Example", "Meaning"],
                [
                    ["place + genitive", "ექიმის კაბინეტი", "doctor's office"],
                    ["owner + genitive", "კომპანიის ოფისი", "company office"],
                    ["category + genitive", "ქალების ტანსაცმელი", "women's clothing"],
                    ["service + genitive", "ბილეთების სალარო", "ticket office"],
                ],
            ),
        ],
        "3": [
            _tbl(
                "Emergency imperatives",
                ["Function", "Command", "Meaning"],
                [
                    ["warning", "ფრთხილად!", "careful!"],
                    ["immediate action", "დარეკე 112-ზე!", "call 112!"],
                    ["negative command", "არ შეეხო!", "don't touch!"],
                    ["evacuation", "სასწრაფოდ გამოდით!", "leave immediately!"],
                ],
                "Emergency language favors short direct imperatives.",
            ),
            _tbl(
                "Polite emergency requests",
                ["Pattern", "Example", "Meaning"],
                [
                    ["გთხოვთ + imperative", "გთხოვთ, დაელოდეთ", "please wait"],
                    ["შეიძლება + request", "შეიძლება სასწრაფო დახმარება?", "could we get an ambulance?"],
                    ["დამეხმარეთ", "დამეხმარეთ, გთხოვთ", "please help me"],
                ],
            ),
        ],
        "4": [
            _tbl(
                "Lost items: reporting structures",
                ["Pattern", "Example", "Meaning"],
                [
                    ["დამეკარგა + noun", "დამეკარგა პასპორტი", "I lost my passport"],
                    ["მომპარეს + noun", "მომპარეს ჩანთა", "my bag was stolen"],
                    ["სად + verb?", "სად ნახეთ ეს ნივთი?", "where did you find this item?"],
                    ["აღწერა", "შავი საფულე, პატარა", "black small wallet"],
                ],
            ),
        ],
        "5": [
            _tbl(
                "Tour duration and schedule",
                ["Pattern", "Example", "Meaning"],
                [
                    ["duration + გრძელდება", "ტური ორი საათი გრძელდება", "the tour lasts two hours"],
                    ["დან ... მდე", "ათი საათიდან თორმეტამდე", "from 10 to 12"],
                    ["time adverbial", "ყოველ დილით", "every morning"],
                    ["frequency", "კვირაში ორჯერ", "twice a week"],
                ],
            ),
        ],
        "6": [
            _tbl(
                "Hotel room descriptions",
                ["Feature", "Example phrase", "Meaning"],
                [
                    ["type", "ორადგილიანი ოთახი", "double room"],
                    ["view", "ოთახი ზღვის ხედით", "room with sea view"],
                    ["availability", "თავისუფალი ოთახი", "available room"],
                    ["preference", "მშვიდი ოთახი მინდა", "I want a quiet room"],
                ],
            ),
            _tbl(
                "Booking requests and modals",
                ["Pattern", "Example", "Meaning"],
                [
                    ["მინდა + noun", "მინდა ნომერი", "I want a room"],
                    ["შეიძლება + question", "შეიძლება უფრო დიდი?", "is a bigger one possible?"],
                    ["უნდა + verb", "უნდა შევავსო ფორმა?", "must I fill in a form?"],
                ],
            ),
        ],
        "7": [
            _tbl(
                "მიყვარს vs მომწონს",
                ["Verb", "Typical object", "Example", "Meaning"],
                [
                    ["მიყვარს", "person/activity strongly", "მიყვარს მოგზაურობა", "I love traveling"],
                    ["მომწონს", "thing/opinion preference", "მომწონს ეს ფილმი", "I like this film"],
                    ["არ მიყვარს", "negative love", "არ მიყვარს ხმაური", "I don't love noise"],
                    ["არ მომწონს", "negative like", "არ მომწონს გემო", "I don't like the taste"],
                ],
                "Both use dative-style experiencer forms.",
            ),
        ],
        "8": [
            _tbl(
                "Expressing opinions",
                ["Pattern", "Example", "Meaning"],
                [
                    ["მე ვფიქრობ, რომ ...", "მე ვფიქრობ, რომ კარგია", "I think that it's good"],
                    ["ჩემი აზრით", "ჩემი აზრით, ეს სწორი არაა", "in my opinion, this isn't right"],
                    ["ვეთანხმები / არ ვეთანხმები", "არ გეთანხმები", "I don't agree with you"],
                    ["ალბათ", "ალბათ დაგვაგვიანდება", "probably we'll be late"],
                ],
            ),
        ],
        "9": [
            _tbl(
                "Invitations and responses",
                ["Function", "Example", "Meaning"],
                [
                    ["invite", "შაბათს ჩვენთან მოდი", "come to us on Saturday"],
                    ["polite invite", "გსურთ შემოგვიერთდეთ?", "would you like to join us?"],
                    ["accept", "სიამოვნებით მოვალ", "I'd be happy to come"],
                    ["decline", "სამწუხაროდ, ვერ მოვალ", "unfortunately I can't come"],
                ],
            ),
            _tbl(
                "Future in invitation context",
                ["Pattern", "Example", "Meaning"],
                [
                    ["მე + future", "მოგწერ ხვალ", "I'll write tomorrow"],
                    ["შევხვდეთ + time", "შევხვდეთ შვიდზე", "let's meet at seven"],
                    ["თუ + შეძლება", "თუ შეძლებ, მოდი", "if you can, come"],
                ],
            ),
        ],
        "10": [
            _tbl(
                "Relative pronoun რომელიც",
                ["Pattern", "Example", "Meaning"],
                [
                    ["noun + რომელიც ...", "კაცი, რომელიც იქ დგას", "the man who is standing there"],
                    ["object clause", "წიგნი, რომელიც ვიყიდე", "the book that I bought"],
                    ["place clause", "ქალაქი, რომელიც მიყვარს", "the city that I love"],
                    ["time clause", "დღე, რომელიც მახსოვს", "the day that I remember"],
                ],
                "რომელიც links two clauses and agrees with the referenced noun semantically.",
            ),
        ],
        "11": [
            _tbl(
                "Culture topic language patterns",
                ["Pattern", "Example", "Meaning"],
                [
                    ["tradition + genitive", "საქართველოს კულტურა", "culture of Georgia"],
                    ["comparison", "ძველი და თანამედროვე ტრადიციები", "old and modern traditions"],
                    ["opinion", "ჩემი აზრით, ეს მნიშვნელოვანია", "in my opinion, this is important"],
                    ["reason", "რადგან ისტორიასთან არის დაკავშირებული", "because it is connected with history"],
                ],
            ),
        ],
        "12": [
            _tbl(
                "Purpose clause with რათა",
                ["Pattern", "Example", "Meaning"],
                [
                    ["X, რათა Y", "ვსწავლობ, რათა უკეთ ვიმუშაო", "I study so that I work better"],
                    ["movement + purpose", "ბიბლიოთეკაში მივედი, რათა მასალა მეპოვა", "I went to the library to find material"],
                    ["request + purpose", "ნელა ილაპარაკე, რათა გავიგო", "speak slowly so that I understand"],
                    ["formal writing", "პროექტი შეიქმნა, რათა დაეხმაროს სტუდენტებს", "project was created to help students"],
                ],
            ),
            _tbl(
                "Purpose connectors compared",
                ["Connector", "Register", "Example"],
                [
                    ["რათა", "formal/neutral", "ვმეცადინეობ, რათა ჩავაბარო"],
                    ["რომ", "very common", "ვმეცადინეობ, რომ ჩავაბარო"],
                    ["იმისთვის, რომ", "explicit purpose", "წავედი, იმისთვის რომ მეყიდა"],
                ],
            ),
        ],
    },
    "b1": {
        "1": [
            _tbl(
                "Imperfect tense formation and use",
                ["Use", "Example", "Meaning"],
                [
                    ["habit in past", "ყოველ დღე ვკითხულობდი", "I used to read every day"],
                    ["ongoing past", "როცა დამირეკე, ვმუშაობდი", "I was working when you called"],
                    ["background", "წვიმდა და ციოდა", "it was raining and cold"],
                    ["state", "ბავშვობაში თბილისში ვცხოვრობდი", "I lived in Tbilisi in childhood"],
                ],
            ),
            _tbl(
                "Present vs imperfect",
                ["Verb", "Present", "Imperfect", "English"],
                [
                    ["ცხოვრება", "ვცხოვრობ", "ვცხოვრობდი", "live / used to live"],
                    ["მუშაობა", "ვმუშაობ", "ვმუშაობდი", "work / was working"],
                    ["კითხვა", "ვკითხულობ", "ვკითხულობდი", "read / was reading"],
                ],
            ),
        ],
        "2": [
            _tbl(
                "CV language: dates and periods",
                ["Pattern", "Example", "Meaning"],
                [
                    ["year range", "2019-დან 2022-მდე", "from 2019 to 2022"],
                    ["month + year", "2021 წლის მაისი", "May 2021"],
                    ["present marker", "2023 წლიდან დღემდე", "from 2023 until now"],
                    ["experience", "სამწლიანი გამოცდილება", "three years of experience"],
                ],
                "B1 CV texts rely on genitive year phrases and range markers.",
            ),
        ],
        "3": [
            _tbl(
                "Interview question structures",
                ["Function", "Example", "Meaning"],
                [
                    ["experience", "რა გამოცდილება გაქვთ?", "what experience do you have?"],
                    ["motivation", "რატომ გინდათ ეს პოზიცია?", "why do you want this position?"],
                    ["strength", "რა არის თქვენი ძლიერი მხარე?", "what is your strength?"],
                    ["future", "როგორ ხედავთ თავს ხუთ წელში?", "how do you see yourself in five years?"],
                ],
            ),
            _tbl(
                "Polite formal forms",
                ["Informal", "Formal/polite", "Use"],
                [
                    ["გინდა", "გსურთ", "interview politeness"],
                    ["შეგიძლია", "შეგიძლიათ", "ability question"],
                    ["მოდი", "მობრძანდით", "formal invitation"],
                ],
            ),
        ],
        "4": [
            _tbl(
                "რომელიც in professional descriptions",
                ["Pattern", "Example", "Meaning"],
                [
                    ["role + რომელიც", "პროექტი, რომელიც დავასრულე", "project that I completed"],
                    ["company + რომელიც", "კომპანია, რომელიც იზრდება", "company that is growing"],
                    ["skill + რომელიც", "უნარი, რომელიც მნიშვნელოვანია", "skill that is important"],
                    ["goal + რომელიც", "მიზანი, რომელსაც მივაღწიე", "goal that I achieved"],
                ],
            ),
        ],
        "5": [
            _tbl(
                "Safety instructions (imperatives)",
                ["Type", "Example", "Meaning"],
                [
                    ["positive imperative", "შეიკარით ღვედი", "fasten your seatbelt"],
                    ["negative imperative", "არ გამოიყენოთ ლიფტი", "do not use the elevator"],
                    ["sequence", "პირველ რიგში გამოიძახეთ დახმარება", "first call for help"],
                    ["warning", "ფრთხილად იყავით", "be careful"],
                ],
            ),
        ],
        "6": [
            _tbl(
                "Past narrative sequencing",
                ["Connector", "Example", "Narrative role"],
                [
                    ["თავიდან", "თავიდან ყველაფერი კარგად იყო", "opening"],
                    ["შემდეგ", "შემდეგ პრობლემა დაიწყო", "next event"],
                    ["ამ დროს", "ამ დროს ტელეფონმა დარეკა", "parallel action"],
                    ["ბოლოს", "ბოლოს გამოსავალი ვიპოვეთ", "ending"],
                ],
            ),
            _tbl(
                "Narrative tense mix",
                ["Function", "Typical tense", "Example"],
                [
                    ["background", "imperfect", "წვიმდა"],
                    ["main event", "aorist/past", "კარი გაიღო"],
                    ["result", "perfect/statement", "ყველაფერი შეიცვალა"],
                ],
            ),
        ],
        "7": [
            _tbl(
                "Free-time preferences",
                ["Pattern", "Example", "Meaning"],
                [
                    ["მიყვარს + activity", "მიყვარს სირბილი", "I love running"],
                    ["მირჩევნია + dative alternative", "ფილმი მირჩევნია სერიალს", "I prefer film to series"],
                    ["ჩვეულებრივ + verb", "ჩვეულებრივ ვკითხულობ საღამოს", "I usually read in the evening"],
                    ["ხოლმე", "შაბათობით ვთამაშობ ხოლმე", "I tend to play on Saturdays"],
                ],
            ),
        ],
        "8": [
            _tbl(
                "Relative clauses at B1",
                ["Clause type", "Example", "Meaning"],
                [
                    ["subject relative", "ადამიანი, რომელიც მეხმარება", "the person who helps me"],
                    ["object relative", "წიგნი, რომელსაც კითხულობ", "the book you read"],
                    ["place relative", "ადგილი, სადაც ვცხოვრობ", "the place where I live"],
                    ["time relative", "დღე, როცა შევხვდით", "the day when we met"],
                ],
            ),
            _tbl(
                "Relative pronoun case hints",
                ["Role in clause", "Form", "Example"],
                [
                    ["subject", "რომელიც", "ქალი, რომელიც მღერის"],
                    ["object (dat.)", "რომელსაც", "კაცი, რომელსაც ვიცნობ"],
                    ["genitive relation", "რომლის", "ქალაქი, რომლის ცენტრი"],
                ],
            ),
        ],
        "9": [
            _tbl(
                "Future plans and უნდა in shopping",
                ["Pattern", "Example", "Meaning"],
                [
                    ["future intention", "ხვალ ბაზარში წავალ", "I will go to the market tomorrow"],
                    ["necessity", "პური უნდა ვიყიდო", "I need to buy bread"],
                    ["budget", "უფრო იაფი უნდა ვიპოვო", "I must find a cheaper one"],
                    ["advice", "ეს უნდა აიღო", "you should take this"],
                ],
            ),
            _tbl(
                "უნდა mini-paradigm",
                ["Person", "Form", "Example"],
                [
                    ["მე", "უნდა", "მე უნდა წავიდე"],
                    ["შენ", "უნდა", "შენ უნდა ნახო"],
                    ["მას", "უნდა", "მას უნდა იყიდოს"],
                ],
            ),
        ],
        "10": [
            _tbl(
                "Consumer rights language",
                ["Function", "Example", "Meaning"],
                [
                    ["complaint", "ჩეკი მაქვს და დაბრუნება მინდა", "I have the receipt and want a return"],
                    ["right", "მომხმარებელს აქვს უფლება", "the consumer has the right"],
                    ["condition", "თუ პროდუქტი დაზიანებულია", "if the product is damaged"],
                    ["request", "გთხოვთ თანხის დაბრუნება", "please refund the money"],
                ],
            ),
        ],
        "11": [
            _tbl(
                "Regional adjectives with -ური",
                ["Noun", "Adjective (-ური)", "Example"],
                [
                    ["აჭარა", "აჭარული", "აჭარული ხაჭაპური"],
                    ["იმერეთი", "იმერული", "იმერული კერძები"],
                    ["გურია", "გურული", "გურული ტრადიცია"],
                    ["კახეთი", "კახური", "კახური ღვინო"],
                ],
                "-ური/-ული family forms create regional/cultural adjectives.",
            ),
            _tbl(
                "Cuisine descriptions",
                ["Pattern", "Example", "Meaning"],
                [
                    ["adj + dish", "ცხარე სოუსი", "spicy sauce"],
                    ["region + specialty", "კახური მწვადი", "Kakhetian barbecue"],
                    ["comparison", "ეს უფრო მსუბუქია", "this is lighter"],
                ],
            ),
        ],
        "12": [
            _tbl(
                "Health argumentation language",
                ["Function", "Connector/pattern", "Example"],
                [
                    ["state opinion", "ჩემი აზრით", "ჩემი აზრით, ვარჯიში აუცილებელია"],
                    ["give reason", "რადგან", "რადგან ჯანმრთელობას აძლიერებს"],
                    ["counter-argument", "თუმცა", "თუმცა ყველა ვერ პოულობს დროს"],
                    ["conclusion", "ამიტომ", "ამიტომ მცირე ნაბიჯით უნდა დავიწყოთ"],
                ],
            ),
            _tbl(
                "Advice and obligation in health context",
                ["Pattern", "Example", "Meaning"],
                [
                    ["უნდა + verb", "უნდა დავისვენოთ", "we should rest"],
                    ["სჯობს + infinitive", "სჯობს მეტი წყლის დალევა", "it is better to drink more water"],
                    ["არ უნდა + verb", "არ უნდა გადავიღალოთ", "we should not overwork"],
                ],
            ),
        ],
    },
}
