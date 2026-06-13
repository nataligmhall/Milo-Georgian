"""Multiple-choice sentence builder exercises per lesson (reader only)."""

from reader_verbs import FOCUS_VERBS


def _m(en, template, answer, *distractors):
    opts = [answer] + list(distractors)
    return {"en": en, "template": template, "answer": answer, "options": opts}


def _from_verb_rows(verb, limit=3):
    """Auto MCQ: pick the correct verb form."""
    rows = verb.get("rows") or []
    out = []
    pool = [r[1] for r in rows if len(r) >= 2 and r[1] and r[0]]
    for row in rows:
        if len(out) >= limit:
            break
        if len(row) < 3 or not row[0] or not row[1]:
            continue
        person, form, meaning = row[0], row[1], row[2]
        wrong = [f for f in pool if f != form][:2]
        if len(wrong) < 2:
            continue
        out.append(_m(
            f"Choose the form for «{person}» ({meaning})",
            f"___  ({person})",
            form,
            wrong[0],
            wrong[1],
        ))
    return out


HAND_CRAFTED = {
    "a1": {
        "1": [
            _m("This is a café.", "ეს კაფე___", "ა", "არის", "აი"),
            _m("Here is a phone.", "აი ___", "ტელეფონი", "კაფე", "ეს"),
            _m("This is not an office.", "ეს არ არის ___", "ოფისი", "კაფეა", "აი"),
        ],
        "2": [
            _m("Hello! How are you?", "გამარჯობა! როგორ ___?", "ხარ", "ვარ", "არის"),
            _m("I am in Tbilisi.", "თბილისში ___", "ვარ", "ხარ", "არის"),
            _m("My name is Nino.", "მე მქვია ___", "ნინო", "თბილისი", "გამარჯობა"),
        ],
        "3": [
            _m("I want coffee.", "მინდა ___", "ყავა", "ლუდი", "არ"),
            _m("I don't want beer.", "არ მინდა ___", "ლუდი", "ყავა", "მინდა"),
            _m("What do you want?", "რა ___?", "გინდა", "მინდა", "არის"),
        ],
        "4": [
            _m("I am a student.", "მე სტუდენტი ___", "ვარ", "ხარ", "არიან"),
            _m("Here is a doctor.", "აქ არის ___", "ექიმი", "ექიმები", "იქ"),
            _m("There are students.", "იქ ___ სტუდენტები", "არიან", "არის", "ვარ"),
        ],
        "5": [
            _m("This is my mother.", "ეს ჩემი ___ა", "დედა", "მამა", "ძმა"),
            _m("I am twenty years old.", "ოცი წლის ___", "ვარ", "არის", "მაქვს"),
            _m("Whose photo is this?", "ვისი ეს ___ა?", "ფოტო", "დედა", "ჩემი"),
        ],
        "6": [
            _m("I am Georgian.", "მე ქართველი ___", "ვარ", "ხარ", "ცხოვრობს"),
            _m("What time is it?", "რამდენია ___?", "საათი", "დღე", "წელი"),
            _m("It's three o'clock.", "სამი ___", "საათია", "საათი", "სამი"),
        ],
        "7": [
            _m("A beautiful face.", "ლამაზი ___", "სახე", "სახეა", "თმა"),
            _m("This skirt is pink.", "ეს ქვედაბოლო ___", "ვარდისფერია", "ლამაზი", "წითელი"),
            _m("What color is it?", "რა ___ა?", "ფერი", "ფერ", "სახე"),
        ],
        "8": [
            _m("He/she is coming.", "ის ___", "მოდის", "მიდის", "შედის"),
            _m("The cheapest.", "ყველაზე ___", "იაფი", "ძვირი", "მეხუთე"),
            _m("Today is the fifth.", "დღეს ___ რიცხვია", "მეხუთე", "მეორე", "პირველი"),
        ],
        "9": [
            _m("I can read.", "შემიძლია ___", "კითხვა", "წერა", "მომწონს"),
            _m("I like the film.", "მომწონს ___", "ფილმი", "შემიძლია", "არ"),
            _m("I went (away).", "გუშინ ___", "წავედი", "მოვედი", "მიდის"),
        ],
        "10": [
            _m("I am at home.", "სახლში ___", "ვარ", "მივდივარ", "აქვს"),
            _m("I go by bus.", "ავტობუსით ___", "მივდივარ", "ფეხით", "ვარ"),
            _m("To the right.", "___", "მარჯვნივ", "მარცხნივ", "პირდაპირ"),
        ],
        "11": [
            _m("I have an apartment.", "მაქვს ___", "ბინა", "კატა", "მყავს"),
            _m("I have a cat.", "მყავს ___", "კატა", "ბინა", "მაქვს"),
            _m("There is a big table.", "დიდი ___", "მაგიდა", "საწოლი", "მაქვს"),
        ],
        "12": [
            _m("I study Georgian.", "ვსწავლობ ___", "ქართულს", "წერილს", "მაქვს"),
            _m("Thank you!", "___!", "გმადლობ", "გამარჯობა", "ნახვამდის"),
            _m("I've been studying for two years.", "ორი წელია ___ ქართულს", "ვსწავლობ", "ვიყავი", "მაქვს"),
        ],
    },
    "a2": {
        "1": [
            _m("From Monday to Friday.", "ორშაბათიდან პარასკევ___", "ამდე", "იდან", "ში"),
            _m("I study economics.", "ვსწავლობ ___", "ეკონომიკას", "ბიზნესს", "ოჯახს"),
            _m("She has siblings.", "მას ყავს და-___", "ძმა", "დედა", "ბიძა"),
        ],
        "2": [
            _m("Georgia is mountainous.", "საქართველო მთ___ ქვეყანაა", "იანი", "ანი", "ელი"),
            _m("I go by bus.", "ავტობუს___ მივდივარ", "ით", "ში", "ზე"),
            _m("It is often rainy.", "ხშირად წვიმი___ა", "ან", "იანი", "ელი"),
        ],
        "3": [
            _m("In the morning I read.", "დილით ვ___", "კითხულობ", "მუშაობ", "ცხოვრობ"),
            _m("A bright room.", "ნათელი ___", "ოთახი", "ოთახში", "ბნელი"),
            _m("Our apartment is spacious.", "ჩვენი ბინა ___", "ფართოა", "ბნელია", "ვიწრო"),
        ],
        "4": [
            _m("He was a famous footballer.", "ის ცნობილი ფეხბურთელი ___", "იყო", "არის", "იქნება"),
            _m("On the second floor.", "მე___ სართულზე", "ორე", "პირველ", "მესამე"),
            _m("Everyone said bravo.", "ყველა ___ ეუბნებოდა", "ყოჩაღ", "ცნობილი", "იყო"),
        ],
        "5": [
            _m("The most interesting bridge.", "ყველაზე საინტერესო ___", "ხიდი", "ხიდია", "ქალაქი"),
            _m("Someone is taking a photo.", "ვინმე ფოტოს ___", "იღებს", "ჩანს", "მოდის"),
            _m("Nobody is here.", "აქ ___ არ არის", "არავინ", "ვინმე", "ყველა"),
        ],
        "6": [
            _m("Usually I drink tea.", "ჩვეულებრივ ჩაის ___", "ვსვამ", "ვჭამ", "ვამზადებ"),
            _m("My morning is faster.", "ჩემი დილა უფრო სწრაფია, ___", "ვიდრე", "როგორც", "და"),
            _m("Sometimes I prepare meat.", "ხანდახან შემწვარ ხორცს ___", "ვამზადებ", "ვსვამ", "ვჭამ"),
        ],
        "7": [
            _m("On Saturday I go to the market.", "შაბათს ბაზარში ___", "ვდივარ", "ვიყიდი", "ვცდი"),
            _m("I know that there is a big selection.", "ვიცი, რომ დიდი ___ა", "არჩევანი", "ბაზარი", "ხილი"),
            _m("But not everything is cheap.", "მაგრამ ყველაფერი იაფი ___", "არ არის", "არის", "იყო"),
        ],
        "8": [
            _m("I will speak with a consultant.", "კონსულტანტს ___", "დაველაპარაკები", "ველაპარაკები", "ელაპარაკება"),
            _m("About the loan.", "კრედიტის ___", "შესახებ", "გამო", "ში"),
            _m("I need a bank card.", "საბანკო ბარათი ___", "მჭირდება", "მაქვს", "აქვს"),
        ],
        "9": [
            _m("I don't feel well.", "არ ვგრძნობ თავს ___", "კარგად", "ცუდად", "ექიმი"),
            _m("I went to the doctor.", "ექიმთან ___", "მივედი", "ვგრძნობ", "ვიყიდი"),
            _m("I bought medicine.", "წამალს ___", "ვიყიდე", "მჭირდება", "მაქვს"),
        ],
        "10": [
            _m("I'm looking for a new apartment.", "ახალი ბინა ___", "ვეძებ", "ვიყიდი", "მაქვს"),
            _m("More spacious than my old one.", "უფრო ფართოა, ___", "ვიდრე", "როგორც", "და"),
            _m("I decided to buy it.", "გადავწყვიტე, რომ ___", "ვიყიდო", "ვეძებ", "მაქვს"),
        ],
        "11": [
            _m("Georgian wine is famous.", "ქართული ღვინო ძალიან ___", "ცნობილია", "იაფია", "მოდის"),
            _m("I try white wine.", "თეთრ ღვინოს ___", "ვცდი", "ვსვამ", "ვთხოვ"),
            _m("I said hello to everyone.", "ყველას გამარჯობა ___", "ვუთქვი", "ვცდი", "ჩანს"),
        ],
        "12": [
            _m("I am a guest in a Georgian family.", "სტუმრად ვარ ქართულ ___", "ოჯახში", "ბანკში", "ბაზარში"),
            _m("The host is very kind.", "მასპინძელი ძალიან ___", "კეთილია", "ძვირია", "მოდის"),
            _m("Thank you (formal).", "___!", "გმადლობთ", "გმადლობ", "გამარჯობა"),
        ],
    },
}


def get_sentence_exercises(book, num):
    key = str(num)
    if book in HAND_CRAFTED and key in HAND_CRAFTED[book]:
        return HAND_CRAFTED[book][key]
    verb = FOCUS_VERBS.get(book, {}).get(key)
    if verb:
        auto = _from_verb_rows(verb, limit=3)
        if auto:
            return auto
    return []
