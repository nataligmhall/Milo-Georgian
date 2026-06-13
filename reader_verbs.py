"""One focus verb + conjugation table per lesson (reader only)."""


def _v(ge, en, rows, note=None, tense="Present"):
    return {
        "ge": ge,
        "en": en,
        "tense": tense,
        "note": note,
        "rows": rows,
    }


# Person labels reused across tables
_P6 = [
    ("I", "you (sg.)", "he/she", "we", "you (pl.)", "they"),
]


def _rows6(forms, en_stem):
    persons = ["I", "you (sg.)", "he/she", "we", "you (pl.)", "they"]
    return [[persons[i], forms[i], f"{en_stem}"] for i in range(6)]


FOCUS_VERBS = {
    "a1": {
        "1": _v("არის", "to be (is)", [
            ["he/she/it", "არის", "is / there is"],
            ["this is…", "ეს X-ა", "short form (noun + -ა)"],
            ["not", "არ არის", "is not"],
        ], "Full ვარ paradigm comes in L4 — start with არის for identifying things."),
        "2": _v("ვარ", "to be (I am)", [
            ["I", "ვარ", "I am"],
            ["you", "ხარ", "you are"],
            ["he/she", "არის", "he/she is"],
        ], "Three core forms — full six-person table in L4."),
        "3": _v("მინდა", "to want", [
            ["I", "მინდა", "I want"],
            ["you", "გინდა", "you want"],
            ["he/she", "უნდა", "he/she wants"],
            ["we", "გვინდა", "we want"],
            ["you (pl.)", "გინდათ", "you want"],
            ["they", "უნდათ", "they want"],
        ], "Built from მ- + root. Essential for ordering: მინდა ყავა."),
        "4": _v("ვარ", "to be (all persons)", _rows6(
            ["ვარ", "ხარ", "არის", "ვართ", "ხართ", "არიან"], "am/are/is"
        ), "The #1 verb. Use with noun/adjective: მე სტუდენტი ვარ."),
        "5": _v("ცხოვრობს", "to live", [
            ["I", "ვცხოვრობ", "I live"],
            ["you", "ცხოვრობ", "you live"],
            ["he/she", "ცხოვრობს", "he/she lives"],
            ["we", "ვცხოვრობთ", "we live"],
            ["you (pl.)", "ცხოვრობთ", "you live"],
            ["they", "ცხოვრობენ", "they live"],
        ], "Family & home: თბილისში ვცხოვრობ."),
        "6": _v("ვმუშაობ", "to work", [
            ["I", "ვმუშაობ", "I work"],
            ["you", "მუშაობ", "you work"],
            ["he/she", "მუშაობს", "he/she works"],
            ["we", "ვმუშაობთ", "we work"],
            ["you (pl.)", "მუშაობთ", "you work"],
            ["they", "მუშაობენ", "they work"],
        ], "Daily routine: ყოველდღე ვმუშაობ."),
        "7": _v("აქვს", "to have (he/she has)", [
            ["I", "მაქვს", "I have (thing)"],
            ["you", "გაქვს", "you have"],
            ["he/she", "აქვს", "he/she has"],
            ["we", "გვაქვს", "we have"],
            ["you (pl.)", "გაქვთ", "you have"],
            ["they", "აქვს", "they have"],
        ], "Dative subject verb — like Russian «у него есть». ლამაზი სახე აქვს = he/she has a beautiful face."),
        "8": _v("მიდის", "to go (away)", [
            ["I", "ვდივარ", "I go"],
            ["you", "დიხარ", "you go"],
            ["he/she", "მიდის", "he/she goes"],
            ["we", "ვდივართ", "we go"],
            ["you (pl.)", "დიხართ", "you go"],
            ["they", "მიდიან", "they go"],
        ], "Pair with მოდის (comes). ის მიდის = he/she is going away."),
        "9": _v("შემიძლია", "can / to be able", [
            ["I", "შემიძლია", "I can"],
            ["you", "შეგიძლია", "you can"],
            ["he/she", "შეუძლია", "he/she can"],
            ["we", "შეგვიძლია", "we can"],
            ["you (pl.)", "შეგიძლიათ", "you can"],
            ["they", "შეუძლიათ", "they can"],
        ], "Modal verb — no infinitive marker. შემიძლია კითხვა = I can read."),
        "10": _v("მივდივარ", "to go (habitually)", [
            ["I", "მივდივარ", "I go (there)"],
            ["you", "მიდიხარ", "you go"],
            ["he/she", "მიდის", "he/she goes"],
            ["we", "მივდივართ", "we go"],
            ["you (pl.)", "მიდიხართ", "you go"],
            ["they", "მიდიან", "they go"],
        ], "Directional series. ავტობუსით მივდივარ = I go by bus."),
        "11": _v("მაქვს / მყავს", "to have", [
            ["I (thing)", "მაქვს", "I have"],
            ["I (person/pet)", "მყავს", "I have"],
            ["you (thing)", "გაქვს", "you have"],
            ["you (living)", "გყავს", "you have"],
            ["he/she (thing)", "აქვს", "he/she has"],
            ["he/she (living)", "ყავს", "he/she has"],
        ], "Things → მაქვს. People & animals → მყავს."),
        "12": _v("ვსწავლობ", "to study / learn", [
            ["I", "ვსწავლობ", "I study"],
            ["you", "სწავლობ", "you study"],
            ["he/she", "სწავლობს", "he/she studies"],
            ["we", "ვსწავლობთ", "we study"],
            ["you (pl.)", "სწავლობთ", "you study"],
            ["they", "სწავლობენ", "they study"],
        ], "A1 capstone: ორი წელია ვსწავლობ ქართულს."),
    },
    "a2": {
        "1": _v("ვსწავლობ", "to study / learn", [
            ["I", "ვსწავლობ", "I study"],
            ["you", "სწავლობ", "you study"],
            ["he/she", "სწავლობს", "he/she studies"],
            ["we", "ვსწავლობთ", "we study"],
            ["you (pl.)", "სწავლობთ", "you study"],
            ["they", "სწავლობენ", "they study"],
        ]),
        "2": _v("მივდივარ", "to go (by transport)", _rows6(
            ["მივდივარ", "მიდიხარ", "მიდის", "მივდივართ", "მიდიხართ", "მიდიან"], "go"
        ), "Use with -ით: ავტობუსით მივდივარ."),
        "3": _v("ვკითხულობ", "to read", [
            ["I", "ვკითხულობ", "I read"],
            ["you", "კითხულობ", "you read"],
            ["he/she", "კითხულობს", "he/she reads"],
            ["we", "ვკითხულობთ", "we read"],
            ["you (pl.)", "კითხულობთ", "you read"],
            ["they", "კითხულობენ", "they read"],
        ]),
        "4": _v("იყო", "to be (past)", [
            ["I", "ვიყავი", "I was"],
            ["you", "იყავი", "you were"],
            ["he/she", "იყო", "he/she was"],
            ["we", "ვიყავით", "we were"],
            ["you (pl.)", "იყავით", "you were"],
            ["they", "იყვნენ", "they were"],
        ], "Past of ვარ. Also: ჰქონდა (had thing), ჰყავდა (had person)."),
        "5": _v("ჩანს", "to seem / be visible", [
            ["", "ჩანს", "it seems / is visible"],
            ["", "არ ჩანს", "it's not visible"],
        ], "Impersonal — very common in descriptions."),
        "6": _v("ვსვამ", "to drink", [
            ["I", "ვსვამ", "I drink"],
            ["you", "სვამ", "you drink"],
            ["he/she", "სვამს", "he/she drinks"],
            ["we", "ვსვამთ", "we drink"],
            ["you (pl.)", "სვამთ", "you drink"],
            ["they", "სვამენ", "they drink"],
        ]),
        "7": _v("ვიყიდი", "to buy", [
            ["I", "ვიყიდი", "I buy"],
            ["you", "იყიდი", "you buy"],
            ["he/she", "იყიდის", "he/she buys"],
            ["we", "ვიყიდით", "we buy"],
            ["you (pl.)", "იყიდით", "you buy"],
            ["they", "იყიდიან", "they buy"],
        ]),
        "8": _v("ველაპარაკები", "to speak / talk", [
            ["I", "ველაპარაკები", "I speak"],
            ["you", "ელაპარაკები", "you speak"],
            ["he/she", "ელაპარაკება", "he/she speaks"],
            ["we", "ველაპარაკებით", "we speak"],
            ["you (pl.)", "ელაპარაკებით", "you speak"],
            ["they", "ელაპარაკებენ", "they speak"],
        ], "Future: დაველაპარაკები = I will speak."),
        "9": _v("ვგრძნობ", "to feel", [
            ["I", "ვგრძნობ", "I feel"],
            ["you", "გრძნობ", "you feel"],
            ["he/she", "გრძნობს", "he/she feels"],
            ["we", "ვგრძნობთ", "we feel"],
            ["you (pl.)", "გრძნობთ", "you feel"],
            ["they", "გრძნობენ", "they feel"],
        ], "არ ვგრძნობ თავს კარგად = I don't feel well."),
        "10": _v("ვეძებ", "to look for / seek", [
            ["I", "ვეძებ", "I look for"],
            ["you", "ეძებ", "you look for"],
            ["he/she", "ეძებს", "he/she looks for"],
            ["we", "ვეძებთ", "we look for"],
            ["you (pl.)", "ეძებთ", "you look for"],
            ["they", "ეძებენ", "they look for"],
        ]),
        "11": _v("ვცდი", "to try / taste", [
            ["I", "ვცდი", "I try"],
            ["you", "ცდი", "you try"],
            ["he/she", "ცდის", "he/she tries"],
            ["we", "ვცდით", "we try"],
            ["you (pl.)", "ცდით", "you try"],
            ["they", "ცდიან", "they try"],
        ]),
        "12": _v("ვთხოვ", "to ask / request", [
            ["I", "ვთხოვ", "I ask"],
            ["you", "თხოვ", "you ask"],
            ["he/she", "თხოვს", "he/she asks"],
            ["we", "ვთხოვთ", "we ask"],
            ["you (pl.)", "თხოვთ", "you ask"],
            ["they", "თხოვენ", "they ask"],
        ], "Also means 'please' in set phrases: გთხოვ."),
    },
    "a2plus": {
        "1": _v("ვაწარმოებ", "to produce", [
            ["I", "ვაწარმოებ", "I produce"],
            ["you", "აწარმოებ", "you produce"],
            ["he/she", "აწარმოებს", "he/she produces"],
            ["we", "ვაწარმოებთ", "we produce"],
            ["they", "აწარმოებენ", "they produce"],
        ]),
        "2": _v("ვკითხულობ", "to read (labels)", [
            ["I", "ვკითხულობ", "I read"],
            ["he/she", "კითხულობს", "he/she reads"],
        ], "Review — essential for product labels."),
        "3": _v("ვურეკავ", "to call (phone)", [
            ["I", "ვურეკავ", "I call"],
            ["you", "ურეკავ", "you call"],
            ["he/she", "ურეკავს", "he/she calls"],
            ["past", "დავურეკე", "I called"],
        ]),
        "4": _v("ვკარგავ", "to lose", [
            ["I", "ვკარგავ", "I lose"],
            ["he/she", "კარგავს", "he/she loses"],
            ["happened to me", "დამეკარგა", "I lost (it)"],
        ], "დამეკარგა = it got lost to me (very Georgian!)."),
        "5": _v("ვმოგზაურობ", "to travel", [
            ["I", "ვმოგზაურობ", "I travel"],
            ["you", "მოგზაურობ", "you travel"],
            ["he/she", "მოგზაურობს", "he/she travels"],
        ]),
        "6": _v("ვაჯავშნობ", "to book / reserve", [
            ["I", "ვაჯავშნობ", "I book"],
            ["you", "აჯავშნებ", "you book"],
            ["he/she", "აჯავშნებს", "he/she books"],
            ["past", "დავაჯავშნე", "I booked"],
        ]),
        "7": _v("ვწერ", "to write", [
            ["I", "ვწერ", "I write"],
            ["you", "წერ", "you write"],
            ["he/she", "წერს", "he/she writes"],
            ["we", "ვწერთ", "we write"],
            ["they", "წერენ", "they write"],
        ]),
        "8": _v("ვაქვეყნებ", "to publish", [
            ["I", "ვაქვეყნებ", "I publish"],
            ["he/she", "აქვეყნებს", "he/she publishes"],
        ]),
        "9": _v("ვუყურებ", "to watch", [
            ["I", "ვუყურებ", "I watch"],
            ["you", "უყურებ", "you watch"],
            ["he/she", "უყურებს", "he/she watches"],
        ]),
        "10": _v("მომწონს", "to like", [
            ["I", "მომწონს", "I like"],
            ["you", "მოგწონს", "you like"],
            ["he/she", "მოსწონს", "he/she likes"],
        ], "Dative subject: 'it pleases me' = I like it."),
        "11": _v("ცხოვრობს", "to live (reside)", [
            ["he/she", "ცხოვრობს", "lives"],
            ["they", "ცხოვრობენ", "they live"],
            ["many", "ბევრი ცხოვრობს", "many live"],
        ]),
        "12": _v("ვცდილობ", "to try / attempt", [
            ["I", "ვცდილობ", "I try"],
            ["you", "ცდილობ", "you try"],
            ["he/she", "ცდილობს", "he/she tries"],
        ], "Pair with ვსწავლობ — learning strategy verbs."),
    },
    "b1": {
        "1": _v("იბადებოდა", "to be born (imperfect)", [
            ["he/she", "იბადებოდა", "was being born"],
            ["they", "იბადებოდნენ", "were being born"],
            ["I", "ვიბადებოდი", "I was being born"],
        ], "Imperfect = ongoing/repeated past. Biography tense."),
        "2": _v("ვმუშაობ", "to work", _rows6(
            ["ვმუშაობ", "მუშაობ", "მუშაობს", "ვმუშაობთ", "მუშაობთ", "მუშაობენ"], "work"
        ), "CV vocabulary — describe experience."),
        "3": _v("შემიძლია", "can / be able", [
            ["I", "შემიძლია", "I can"],
            ["you", "შეგიძლია", "you can"],
            ["we", "შეგვიძლია", "we can"],
            ["team", "შეგვიძლია გუნდში", "we can (work) in a team"],
        ]),
        "4": _v("მუშაობს", "to work (3rd person)", [
            ["he/she", "მუშაობს", "works"],
            ["who", "რომელიც მუშაობს", "who works"],
            ["where", "მთებში მუშაობს", "works in mountains"],
        ]),
        "5": _v("დაიცავით", "observe! (formal imperative)", [
            ["you (formal pl.)", "დაიცავით", "observe!"],
            ["don't move", "არ გადაინაცვლოთ", "do not move"],
            ["help", "დაგეხმარებით", "you will help"],
        ], "Instructions & safety — formal plural commands."),
        "6": _v("გაიმარჯვა", "to win (aorist)", [
            ["he/she", "გაიმარჯვა", "won"],
            ["it", "დაიწყო", "began"],
            ["it", "დასრულდა", "finished"],
        ], "Aorist (single completed action) — sports results."),
        "7": _v("ვსმენ", "to listen", [
            ["I", "ვსმენ", "I listen"],
            ["you", "სმენ", "you listen"],
            ["he/she", "სმენის", "he/she listens"],
            ["we", "ვსმენით", "we listen"],
        ]),
        "8": _v("იწყება", "to begin (impersonal)", [
            ["it", "იწყება", "begins"],
            ["it", "დაიწყო", "began"],
            ["it", "გავრცელდა", "spread"],
        ]),
        "9": _v("ვყიდულობ", "to buy (online)", [
            ["I", "ვყიდულობ", "I buy"],
            ["you", "ყიდულობ", "you buy"],
            ["he/she", "ყიდულობს", "he/she buys"],
            ["passive", "იყიდება", "is sold"],
        ]),
        "10": _v("უნდა", "must / should", [
            ["I", "მინდა / უნდა", "I must"],
            ["you", "გინდა / უნდა", "you must"],
            ["everyone", "ყველას უნდა", "everyone must"],
            ["pay", "გადავიხადოს", "should pay"],
        ], "Obligation — like Russian «нужно»."),
        "11": _v("გემრიელებს", "to taste good", [
            ["it", "გემრიელებს", "tastes good"],
            ["everything", "ყველაფერი გემრიელებს", "everything tastes good"],
            ["is famous", "ცნობილია", "is famous"],
        ]),
        "12": _v("ვაკეთებ", "to do / make / exercise", [
            ["I", "ვაკეთებ", "I do / make"],
            ["you", "აკეთებ", "you do"],
            ["he/she", "აკეთებს", "he/she does"],
            ["we", "ვაკეთებთ", "we do"],
            ["exercise", "ვარჯიშს ვაკეთებ", "I exercise"],
        ]),
    },
}
