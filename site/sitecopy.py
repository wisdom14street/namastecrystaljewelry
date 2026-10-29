"""Namaste Crystal Jewelry (namastecrystaljewelry.com): the full crystal and gemstone jewelry shop. All copy is written for this site only."""
import re
from copybase import E, stone_color, intent_color, kinds_phrase, kind_one, plist, tradition, hood_list, HOODS as HOOD_DATA

AISLES = {
 'pendant':  ('Crystal Pendants', 'Pendants', 'crystal-pendants', 'Points, cabochons, wire-wrapped stones and sterling settings to wear on a chain or cord.', '#8e5bb5'),
 'necklace': ('Necklaces & Chains', 'Necklaces', 'necklaces-chains', 'Finished stone necklaces, chokers, cord necklaces and sterling or plated chains for your pendants.', '#4f7894'),
 'ring':     ('Gemstone Rings', 'Rings', 'gemstone-rings', 'Sterling silver gemstone rings by size, adjustable rings and stacking bands.', '#c9a227'),
 'beaded':   ('Beaded Crystal Bracelets', 'Beaded Bracelets', 'beaded-bracelets', 'Stretch bracelets in natural stone beads from 4 mm minis to 12 mm statement strands.', '#e7a2b4'),
 'bracelet': ('Cuffs, Bangles & Chain Bracelets', 'Cuffs & Bangles', 'cuffs-bangles', 'Copper cuffs, sterling link bracelets, bangles, string and leather bracelets.', '#a8702a'),
 'earrings': ('Gemstone Earrings', 'Earrings', 'gemstone-earrings', 'Studs, drops and hoops set with real stones in sterling, plated and brass settings.', '#2fb3aa'),
 'mala':     ('Malas & Bead Strands', 'Malas', 'malas', '108-bead and wrist malas, plus loose stone strands.', '#7a4a2b'),
 'anklet':   ('Anklets & Charms', 'Anklets & Charms', 'anklets-charms', 'Anklets, charms and little extras to finish a stack.', '#5b4a6b'),
}
def assign(x):
    b = x['base']
    if b == 'meditation': return None
    return {'chain': 'necklace', 'beads': 'mala', 'charm': 'anklet'}.get(b, b)
LABELS = {'stone': 'Stone', 'metal': 'Metal'}
PRICE_BANDS = [('0-15', 'Under $15'), ('0-30', 'Under $30'), ('30-75', '$30 to $75'), ('75-150', '$75 to $150'), ('150-99999', '$150 and up')]
BRAND_BANDS = [('Under $25', 0, 25), ('$25 to $75', 25, 75), ('$75 and up', 75, 1e9)]
STONE_MIN = 6; INTENT_MIN = 6; NAV_INTENTS = True

VISIT_EYEBROW = 'See the jewelry case in person'
def STORE_DESC(S): return f'Crystal and gemstone jewelry shop steps from Union Square in Manhattan with about {S.ABOUT_N:,} pendants, rings, bracelets, necklaces and earrings set with real stones.'
REVIEW_TITLE = 'Found your stone on 14th Street?'
REVIEW_TEXT = 'A quick Google review helps other New Yorkers looking for crystal jewelry near Union Square find the case you shopped.'
LOGO_SVG = '<svg viewBox="0 0 40 40"><path d="M10 15l5-6h10l5 6-10 17z" fill="none" stroke="#c9a0ff" stroke-width="2.2" stroke-linejoin="round"/><path d="M10 15h20M15 9l5 23 5-23" fill="none" stroke="currentColor" stroke-width="1.3"/></svg>'
WORDMARK = 'Namaste <b>Crystal Jewelry</b>'
BAR_TEXT = 'Jewelry case at 2 West 14th Street, by Union Square'
SEARCH_PLACEHOLDER = 'Search stones, rings, pendants, sterling'

QUIZ = {
 'slug': 'stone-finder', 'nav': 'Stone finder', 'cta': 'Find my stone',
 'title': 'Crystal Jewelry Stone Finder', 'desc': 'Pick an intention, a piece and a budget, and get crystal jewelry matches from what is in stock at 2 West 14th Street near Union Square.',
 'h1': 'Find your stone', 'lead': 'Three taps and we pull real, in-stock jewelry that fits. Nothing you choose is saved or sent; the quiz runs only in your browser. Stone meanings come from crystal tradition, not science.',
 'submit': 'Show my jewelry',
 'questions': [
  {'q': 'What would you like your jewelry to stand for?', 'options': [
    {'label': 'Protection', 'filter': {'intent': ['protection']}}, {'label': 'Love', 'filter': {'intent': ['love']}},
    {'label': 'Calm', 'filter': {'intent': ['calm']}}, {'label': 'Luck and abundance', 'filter': {'intent': ['abundance']}}, {'label': 'Intuition', 'filter': {'intent': ['intuition']}}]},
  {'q': 'What do you want to wear?', 'options': [
    {'label': 'A pendant or necklace', 'filter': {'aisle': ['pendant', 'necklace']}}, {'label': 'A ring', 'filter': {'aisle': ['ring']}},
    {'label': 'A bracelet', 'filter': {'aisle': ['beaded', 'bracelet']}}, {'label': 'Earrings', 'filter': {'aisle': ['earrings']}}]},
  {'q': 'Budget?', 'options': [{'label': 'Under $30', 'filter': {'maxp': 30}}, {'label': 'Under $75', 'filter': {'maxp': 75}}, {'label': 'Show me the best pieces', 'filter': {}}]},
 ]}

def FOOTER_EXPLORE(S):
    return [('Shop by stone', '/stones/'), ('Shop by intention', '/intentions/'), ('Stone finder quiz', '/stone-finder/'), ('Crystal jewelry in Manhattan', '/crystal-jewelry-manhattan/'),
            ('Ring size guide', '/guide/ring-size-guide/'), ('Caring for crystal jewelry', '/guide/crystal-jewelry-care/'), ('Gifts under $25', '/crystal-jewelry-gifts-under-25/')]
FOOT_BLURB = 'Real stones you can wear: pendants, rings, bracelets, necklaces and earrings, with a case full of them on 14th Street.'
HERO_BASES = ('pendant', 'ring', 'beaded', 'necklace', 'earrings')
def HERO(S):
    return {'eyebrow': 'Crystal &amp; gemstone jewelry &middot; 2 West 14th Street &middot; NYC',
            'h1': 'Wear the stone you came for, <em>from a case on 14th Street.</em>',
            'lede': f'About {S.ABOUT_N:,} pieces of crystal and gemstone jewelry: {S.SILVER_N:,} in sterling silver, beaded bracelets, rings by size and pendants from {S.money(S.MIN_PRICE)}. Two minutes from Union Square, open daily from 11 AM.' + (f' Reserve online and pick it up; orders are {S.READY.lower()}.' if S.PICKUP_ON else ''),
            'shop_cta': 'Browse the jewelry'}

def _stones(S):
    keys = [k for k in S.STONE_KEYS if k not in S.NON_STONE][:12]
    tiles = ''.join(f'<a class="scent" href="/stones/{k}/" style="--c:{stone_color(k)}"><b>{E(S.STONE_NAME[k])}</b><span>{E(stone_tile(S, k))}</span><small>{S.stone_any[k]} pieces</small></a>' for k in keys)
    return f'<section class="wrap"><div class="sechead"><h2>Shop by stone</h2><a href="/stones/">All {len(S.STONE_KEYS)} stones &rarr;</a></div><div class="scents">{tiles}</div></section>'
def _intents(S):
    chips = ''.join(f'<a class="chip" href="/intentions/{k}/">{E(S.INTENT_NAME[k])} <small>{S.intent_count[k]}</small></a>' for k in S.INTENT_KEYS)
    return f'<section class="wrap"><div class="sechead"><h2>Shop by intention</h2><a href="/intentions/">What the traditions say &rarr;</a></div><div class="chips">{chips}</div><p class="small">Intentions follow popular crystal traditions and are shared as belief, not as proven effects.</p></section>'
def _near(S):
    return f'<section class="wrap"><div class="sechead"><h2>Coming from nearby?</h2><a href="/visit/">Hours &amp; map &rarr;</a></div>{hood_list(S, "/near/")}</section>'
def _whys(S):
    return [(f'About {S.ABOUT_N:,} pieces', 'Every stone, setting and size listed online with its own photos and price, so you can choose before you walk in.'),
            (f'{S.SILVER_N:,} in sterling silver', 'Solid .925 settings for rings, pendants and earrings, plus plated, copper and brass styles.'),
            (('Reserve, then pick up', f'Buy online, pick Pickup at checkout and collect at the shop. Orders are {S.READY.lower()}.') if S.PICKUP_ON else ('', '')),
            ('Rings by size', 'Sterling rings are listed size by size, so you can see which sizes are actually in the case.'),
            ('Open every day', 'From 11 AM daily, until 8 PM Monday to Thursday, 9 PM Friday and Saturday and 7 PM Sunday.'),
            ('Right off Union Square', 'On 14th Street at Fifth Avenue, about 0.2 miles from both the Union Square and Sixth Avenue subway stations.')]
def _new(S): return S.by_rank([x for x in S.leaders if not x['noimg']][:40])[:8]
def _best(S): return S.by_rank(S.leaders)[:8] if S.HAS_RANK else []
def _silver(S): return S.by_rank([x for x in S.leaders if x['metal'] == 'Sterling silver' and x['base'] in ('pendant', 'ring', 'earrings')])[:8]
HOME_SECTIONS = [
 {'type': 'html', 'html': _stones},
 {'type': 'grid', 'title': 'Best-selling crystal jewelry', 'select': _best, 'href': '/shop/', 'link': 'Shop everything', 'intro': 'Ordered by what sells most on namastebookshop.com, refreshed daily.'},
 {'type': 'visit'},
 {'type': 'collections', 'title': 'Start here', 'items': [
   {'title': 'Sterling silver gemstone jewelry', 'blurb': 'Solid .925 settings with real stones.', 'href': '/sterling-silver-crystal-jewelry/', 'filter': {'metal': ['Sterling silver']}},
   {'title': 'Wire-wrapped pendants', 'blurb': 'Hand-wrapped stones on wire.', 'href': '/wire-wrapped-crystal-pendants/', 'filter': {'style': ['Wire wrapped']}},
   {'title': 'Raw crystal jewelry', 'blurb': 'Rough, natural and druzy stones.', 'href': '/raw-crystal-jewelry/', 'filter': {'style': ['Raw & natural']}},
   {'title': 'Evil eye & hamsa', 'blurb': 'Charms of protection lore.', 'href': '/evil-eye-jewelry/', 'filter': {'style': ['Evil eye & hamsa']}},
   {'title': 'Moon & celestial', 'blurb': 'Crescents, stars and zodiac.', 'href': '/moon-celestial-jewelry/', 'filter': {'style': ['Moon & celestial']}},
   {'title': 'Gifts under $25', 'blurb': 'Easy yeses for birthdays.', 'href': '/crystal-jewelry-gifts-under-25/', 'filter': {'maxp': 25}}]},
 {'type': 'html', 'html': _intents},
 {'type': 'grid', 'title': 'Fresh in the case', 'select': _new, 'href': '/shop/?sort=new', 'link': 'All new arrivals'},
 {'type': 'whys', 'title': 'Why shop the case', 'items': _whys},
 {'type': 'grid', 'title': 'Sterling silver favorites', 'select': _silver, 'href': '/sterling-silver-crystal-jewelry/', 'link': 'All sterling'},
 {'type': 'quiz', 'title': 'Which stone is yours?', 'text': 'Pick an intention, a piece and a budget. We do the digging.'},
 {'type': 'brands', 'title': 'Makers in the case', 'n': 12},
 {'type': 'html', 'html': _near},
 {'type': 'review'},
 {'type': 'band', 'title': 'Reserve it online, wear it out of the shop', 'text': lambda S: 'Every piece online is a real listing with live stock. Reserve it and pick it up on 14th Street, or have it shipped from New York City.',
  'steps': lambda S: [('Pick your piece', 'Filter by stone, metal, style, brand or price.'), ('Choose Pickup at checkout', f'Secure Shopify checkout. Orders are {S.READY.lower() or "usually ready the same day"}.'), ('Come get it', S.STORE_ADDR + '.')]},
]
def HOME_TITLE(S): return 'Namaste Crystal Jewelry | Crystal & Gemstone Jewelry near Union Square, NYC'
def HOME_DESC(S): return f'Crystal jewelry shop at {S.STORE_ADDR}, by Union Square: about {S.ABOUT_N:,} gemstone pendants, rings, bracelets, necklaces and earrings, {S.SILVER_N:,} in sterling silver. In-store pickup, open daily.'
def SHOP_TITLE(S): return 'Shop Crystal & Gemstone Jewelry Online, Pick Up in NYC | Namaste Crystal Jewelry'
def SHOP_DESC(S): return f'Browse {S.N:,} crystal and gemstone jewelry pieces: pendants, rings, beaded bracelets, necklaces and earrings from {S.money(S.MIN_PRICE)}. Pick up at 2 West 14th Street or ship.'
SHOP_H1 = 'All crystal jewelry'
def SHOP_SUB(S): return f'{S.N:,} pieces in stock across {len(S.AISLE_KEYS)} aisles. Filter by stone, metal, style, brand and price.'
def AISLE_TITLE(S, k): return f'{AISLES[k][0]} near Union Square, NYC | Namaste Crystal Jewelry'
def AISLE_DESC(S, k): return f'{AISLES[k][3]} {S.cat_count[k]} in stock at 2 West 14th Street, Manhattan. Reserve for pickup or ship.'

def LANDINGS(S):
    return [
     {'path': '/sterling-silver-crystal-jewelry/', 'title': 'Sterling Silver Crystal Jewelry in NYC | Namaste Crystal Jewelry', 'desc': f'{S.SILVER_N:,} sterling silver gemstone rings, pendants, earrings and bracelets at 2 West 14th Street near Union Square.',
      'h1': 'Sterling silver crystal jewelry', 'sub': 'Real stones in solid .925 silver settings.', 'filter': {'metal': ['Sterling silver']},
      'intro': '<p class="intro">Sterling silver is 92.5 percent silver, which is why you will see .925 in so many titles. It can tarnish over time; a soft polishing cloth brings it back. Rings here are listed one size per listing, so what you see is what is in the case.</p>'},
     {'path': '/wire-wrapped-crystal-pendants/', 'title': 'Wire Wrapped Crystal Pendants in NYC | Namaste Crystal Jewelry', 'desc': 'Wire-wrapped crystal and gemstone pendants in sterling, silver-plated and copper wire, at 2 West 14th Street by Union Square.',
      'h1': 'Wire-wrapped pendants', 'sub': 'Stones held by hand-wrapped wire instead of a cast setting.', 'filter': {'style': ['Wire wrapped']}},
     {'path': '/raw-crystal-jewelry/', 'title': 'Raw Crystal Jewelry: Rough & Natural Stones | Namaste Crystal Jewelry', 'desc': 'Raw, rough, druzy and natural-shape crystal jewelry at 2 West 14th Street, Manhattan.',
      'h1': 'Raw crystal jewelry', 'sub': 'Stones left close to how they came out of the ground.', 'filter': {'style': ['Raw & natural']}},
     {'path': '/evil-eye-jewelry/', 'title': 'Evil Eye & Hamsa Jewelry in NYC | Namaste Crystal Jewelry', 'desc': 'Evil eye, nazar and hamsa bracelets, pendants, rings and earrings near Union Square, Manhattan.',
      'h1': 'Evil eye & hamsa jewelry', 'sub': 'Symbols that many cultures wear to ward off envy, according to folklore.', 'filter': {'style': ['Evil eye & hamsa']}},
     {'path': '/moon-celestial-jewelry/', 'title': 'Moon, Star & Celestial Jewelry in NYC | Namaste Crystal Jewelry', 'desc': 'Crescent moon, star, sun and zodiac jewelry with real stones at 2 West 14th Street.',
      'h1': 'Moon & celestial jewelry', 'sub': 'Crescents, stars, suns and zodiac pieces.', 'filter': {'style': ['Moon & celestial']}},
     {'path': '/crystal-jewelry-gifts-under-25/', 'title': 'Crystal Jewelry Gifts Under $25 | Namaste Crystal Jewelry NYC', 'desc': f'{sum(1 for x in S.products if x["price"] < 25):,} crystal jewelry gifts under $25 at 2 West 14th Street, steps from Union Square.',
      'h1': 'Crystal jewelry gifts under $25', 'sub': 'Beaded bracelets, pendants and adjustable rings that are easy to give.', 'filter': {'maxp': 25}},
    ]

def stone_tile(S, k):
    tr = tradition(S, k)
    return (f'Linked in crystal lore with {plist(tr[:2])}.' if tr else 'A favorite in the case.')
def STONE_PAGE(S, k, xs):
    n = S.STONE_NAME[k]; tr = tradition(S, k); kc = S.kinds_of(xs)
    lo = min(x['price'] for x in xs); silver = sum(1 for x in xs if x['metal'] == 'Sterling silver')
    intro = (f'<p class="intro">We have {len(xs)} pieces with {E(n.lower())} right now: {kinds_phrase(kc)}, from {S.money(lo)}.'
             + (f' {silver} of them are set in sterling silver.' if silver else '') + '</p>'
             + (f'<p class="note-belief">In crystal tradition, {E(n.lower())} is associated with {plist(tr)}. These are beliefs passed down by practitioners, not proven effects.</p>' if tr else ''))
    faq = [(f'Where can I buy {n.lower()} jewelry in NYC?', f'At Namaste Crystal Jewelry, {S.STORE_ADDR}, about a 4-minute walk from Union Square. We have {len(xs)} {n.lower()} pieces listed today.'),
           (f'How much is {n.lower()} jewelry here?', f'From {S.money(lo)} to {S.money(max(x["price"] for x in xs))}. Prices update daily.')]
    if tr: faq.append((f'What is {n.lower()} said to mean?', f'Crystal traditions link {n.lower()} with {plist(tr)}. It is a belief, not a medical or scientific claim.'))
    return {'title': f'{n} Jewelry in NYC: Rings, Pendants & Bracelets | Namaste Crystal Jewelry', 'desc': f'{len(xs)} {n.lower()} jewelry pieces from {S.money(lo)}: {kinds_phrase(kc)}. At 2 West 14th Street near Union Square.',
            'h1': f'{n} jewelry', 'sub': f'{len(xs)} pieces with {n.lower()}, in stock today.', 'intro': intro, 'faq': faq, 'faq_title': f'{n} jewelry questions'}
def intent_tile(S, k):
    st = [S.STONE_NAME[s] for ik, _, sts, _ in S.INTENTS if ik == k for s in sts if s in S.STONE_NAME][:3]
    return f'Often paired with {plist(st)}.' if st else 'Symbols and stones chosen for this intention.'
def INTENT_PAGE(S, k, xs):
    n = S.INTENT_NAME[k]; st = [S.STONE_NAME[s] for ik, _, sts, _ in S.INTENTS if ik == k for s in sts if s in S.STONE_NAME]
    intro = (f'<p class="intro">{len(xs)} pieces chosen for {E(n.lower())}' + (f', led by {E(plist(st[:4]).lower())}' if st else '') + '.</p>'
             '<p class="note-belief">The stones on this page are the ones crystal traditions most often connect with this intention. We share that lore because many customers ask; it is belief, not a promise of any effect.</p>')
    return {'title': f'{n} Crystal Jewelry in NYC | Namaste Crystal Jewelry', 'desc': f'{len(xs)} crystal jewelry pieces for {n.lower()}' + (f', including {plist(st[:3]).lower()}' if st else '') + ', at 2 West 14th Street near Union Square.',
            'h1': f'Crystal jewelry for {n.lower()}', 'sub': f'{len(xs)} pieces in stock.', 'intro': intro,
            'faq': [(f'Which stones are linked with {n.lower()}?', (f'Crystal traditions most often name {plist(st[:5]).lower()}.' if st else 'This page gathers symbols and pieces made around this intention.') + ' These associations are folklore, not science.')]}
def STONES_HUB(S): return {'title': 'Crystal Jewelry by Stone | Namaste Crystal Jewelry NYC', 'desc': f'Shop crystal jewelry by stone: {len(S.STONE_KEYS)} stones from amethyst to turquoise at 2 West 14th Street.', 'h1': 'Shop by stone',
                           'lead': f'{len(S.STONE_KEYS)} stones with at least {STONE_MIN} pieces in stock. Each page lists every piece with its price.'}
def INTENTS_HUB(S): return {'title': 'Crystal Jewelry by Intention | Namaste Crystal Jewelry NYC', 'desc': 'Crystal jewelry grouped by the intentions crystal traditions give each stone: protection, love, calm, abundance and more.', 'h1': 'Shop by intention',
                            'lead': 'Grouped by the meanings crystal traditions give each stone. We share them as lore; they are not medical or scientific claims.'}

def brand_intro(S, k, st):
    name = S.BRAND_NAME[k]; xs = st['xs']
    stones = [S.STONE_NAME[s] for s, _ in __import__('collections').Counter(x['family'] for x in xs if x['family']).most_common(3)]
    metals = [m for m, _ in __import__('collections').Counter(x['metal'] for x in xs if x['metal']).most_common(2)]
    t = f'The case holds {st["n"]} {E(name)} piece{"s" if st["n"] != 1 else ""} today: {kinds_phrase(S.kinds_of(xs))}, from {S.money(st["min"])}.'
    if stones: t += f' Stones you will see most: {E(plist(stones))}.'
    if metals: t += f' Mostly {E(plist(metals).lower())}.'
    t += ' Reserve online and pick up at 2 West 14th Street.' if st['pickup'] else ' Call ahead before you visit.'
    return f'<p>{t}</p>'
def brand_faq(S, k, st):
    name = S.BRAND_NAME[k]
    q = [(f'Where can I see {name} jewelry in New York?', f'At Namaste Crystal Jewelry, {S.STORE_ADDR}, a short walk from Union Square. {st["n"]} pieces are listed today.'),
         (f'What do {name} pieces cost?', (f'From {S.money(st["min"])} to {S.money(st["max"])}.' if st['max'] > st['min'] else f'{S.money(st["min"])}.') + ' Prices refresh daily.')]
    if st['pickup']: q.append((f'Can I reserve {name} jewelry for pickup?', 'Yes: tap Buy now, choose Pickup at checkout and collect it on 14th Street.' + (f' Orders are {S.READY.lower()}.' if S.READY else '')))
    return q
def BRAND_H1(S, k): return f'{S.BRAND_NAME[k]} jewelry'
def BRAND_TITLE(S, k, st): return f'{S.BRAND_NAME[k]} Jewelry in NYC near Union Square | Namaste Crystal Jewelry'
def BRAND_DESC(S, k, st): return f'{S.BRAND_NAME[k]}: {st["n"]} jewelry piece{"s" if st["n"] != 1 else ""} from {S.money(st["min"])} at 2 West 14th Street, Manhattan. Pick up or ship.'
def BRANDS_TITLE(S): return 'Jewelry Brands & Makers A to Z | Namaste Crystal Jewelry NYC'
def BRANDS_DESC(S): return 'Every named jewelry brand and maker in our case at 2 West 14th Street, with live piece counts.'
BRANDS_H1 = 'Brands & makers A to Z'
def BRANDS_LEAD(S, n): return f'{n} named brands and makers are in the case today. Much of our jewelry is sourced from independent suppliers without a public brand name, so it appears in the shop and on the stone pages instead. Looking for something? Call <a href="tel:{S.TEL}">{S.PHONE}</a>.'

PAIR = {'pendant': ['chain', 'necklace'], 'ring': ['earrings', 'pendant'], 'beaded': ['beaded'], 'bracelet': ['ring'], 'earrings': ['pendant', 'ring'], 'necklace': ['earrings'], 'chain': ['pendant'], 'mala': ['beaded'], 'anklet': ['beaded'], 'charm': ['chain', 'bracelet'], 'beads': ['mala']}
REL_BRAND = 'More from {brand}'
REL_SCENT = 'More {scent} to wear'
REL_PAIR = 'Wear it with'
REL_MORE = 'More {aisle}'
CARE = {'pendant': 'Take pendants off before swimming or showering and store them apart so stones do not scratch each other.',
        'ring': 'Rings take the most knocks: remove them for the gym, cleaning and swimming, and wipe with a soft dry cloth.',
        'beaded': 'Roll a stretch bracelet on and off instead of pulling it, and keep it away from lotions and water so the cord lasts.',
        'bracelet': 'Copper and brass naturally darken with wear; a jewelry cloth brightens them. Keep leather and string dry.',
        'earrings': 'Store earrings in pairs and clean posts gently with a little rubbing alcohol on a cloth.',
        'necklace': 'Fasten the clasp before storing so the chain does not tangle.', 'chain': 'Lay chains flat or hang them to prevent knots; polish sterling with a silver cloth.',
        'mala': 'Store a mala loose rather than wound tight, and keep knotted cords dry.', 'anklet': 'Take anklets off for the beach; sand and salt wear the clasp.', 'charm': 'Clip charms on with the clasp closed fully.', 'beads': 'Keep strands knotted until you are ready to string them.'}
def describe(S, x):
    s = []; k = x['base']; stn = x['stones']; by = f' by {S.BRAND_NAME[x["brand"]]}' if x['brand'] else ''
    metal = f" in {x['metal'].lower()}" if x['metal'] and x['metal'] != 'Cord, elastic & leather' else ''
    s.append(f"{E(x['title'])} is a {kind_one(k)}{by}{metal}" + (f", made with {E(plist([S.STONE_NAME[t] for t in stn[:3]]).lower())}." if stn else '.'))
    if x['mm']: s.append(f"The beads are about {x['mm']:g} mm.")
    if x['size']: s.append(f"This listing is ring size {E(x['size'])}; other sizes appear as separate listings when we have them.")
    if stn and stn[0] not in S.NON_STONE:
        tr = tradition(S, stn[0])
        if tr: s.append(f"In crystal tradition, {E(S.STONE_NAME[stn[0]].lower())} is associated with {plist(tr)}. That is lore, not a proven effect.")
    s.append('Natural stones vary in color, pattern and size, so yours may differ a little from the photo.')
    s.append(CARE.get(k, ''))
    s.append('Ships from New York City, or see it in the case at 2 West 14th Street, steps from Union Square. Checkout is completed securely on Shopify through namastebookshop.com.')
    return [t for t in s if t]
def PRODUCT_DESC(S, x, v0):
    return f"{x['title']}, {S.money(v0['price'])}. " + ('Reserve online and pick up at 2 West 14th Street by Union Square, or ship from NYC.' if x['pickup'] else 'In our case at 2 West 14th Street by Union Square, or shipped from NYC.')

def ABOUT_DESC(S): return 'About Namaste Crystal Jewelry, the crystal and gemstone jewelry shop at 2 West 14th Street by Union Square. A brand of Wealth Edge Ventures Inc.'
ABOUT_H1 = 'About Namaste Crystal Jewelry'
def ABOUT(S):
    return f'''<p class="lead">Namaste Crystal Jewelry is the jewelry case at {S.STORE_ADDR}, on 14th Street just west of Fifth Avenue and a few minutes from Union Square.</p>
<p>We stock jewelry made with real stones, and nothing else: pendants, gemstone rings, beaded bracelets, necklaces, chains, earrings, malas and anklets. About {S.ABOUT_N:,} pieces are listed online with photos and live prices, {S.SILVER_N:,} of them in sterling silver.{" Reserve any of them and choose Pickup at checkout to collect in store." if S.PICKUP_ON else ""}</p>
<h2>Visit</h2><p>{S.STORE_ADDR}. Call <a href="tel:{S.TEL}">{S.PHONE}</a>.</p>{S.hours_html()}{S.visit_buttons()}<p><a href="/visit/">Directions, subway lines and pickup details &rarr;</a></p>
<h2>Who we are</h2><p>{S.LEGAL} Online orders are checked out on Shopify through <a href="{S.SHOP}" rel="noopener">namastebookshop.com</a>, which processes payment and fulfills orders, including in-store pickups.</p>
<h2>What we carry</h2><ul>{''.join(f'<li><a href="/shop/{AISLES[k][2]}/">{E(AISLES[k][0])}</a>: {E(AISLES[k][3])}</li>' for k in S.AISLE_KEYS)}</ul>
<h2>About stone meanings</h2><p>You will see crystal traditions mentioned on this site, such as amethyst and calm or black tourmaline and protection. We include them because customers ask, and we always present them as belief. They are not medical advice or scientific claims.</p>'''
VISIT_TITLE = 'Visit Our Crystal Jewelry Shop near Union Square'
def VISIT_DESC(S): return f'Directions, hours, subway lines and in-store pickup for Namaste Crystal Jewelry at {S.STORE_ADDR}, steps from Union Square.'
def VISIT_LEAD(S): return f'Find the jewelry case at {S.STORE_ADDR}, on 14th Street just west of Fifth Avenue, where Union Square, the Village, Chelsea and Flatiron meet.'
def FAQ_DESC(S): return 'Answers about Namaste Crystal Jewelry: location, hours, pickup, shipping, ring sizes, sterling silver and caring for crystal jewelry.'
FAQ_H1 = 'Crystal jewelry questions'
def FAQ(S):
    return [('Where is the shop?', f'At {S.STORE_ADDR}, on 14th Street just west of Fifth Avenue, about a 4-minute walk from the 14 St&ndash;Union Square station.'),
            ('When are you open?', 'Monday to Thursday 11 AM to 8 PM, Friday and Saturday 11 AM to 9 PM, Sunday 11 AM to 7 PM. Holiday hours can change, so call before a special trip.'),
            ('Can I reserve a piece and pick it up?', 'Yes. Tap Buy now, choose Pickup at checkout and collect it at 2 West 14th Street.' + (f' Orders are {S.READY.lower()}.' if S.READY else '')),
            ('Do you ship?', 'Yes, from New York City. Shipping options and costs show at checkout before you pay. Checkout runs on Shopify through namastebookshop.com.'),
            ('Are the stones real?', 'Each listing names the stone as our suppliers describe it. A few popular materials are man-made by nature, such as goldstone, opalite and cubic zirconia, and aura quartz is quartz with a metallic coating. Ask us in the shop if you want a closer look.'),
            ('How do I find my ring size?', 'Sterling rings are listed one size per listing. Our <a href="/guide/ring-size-guide/">ring size guide</a> explains how to measure at home, or come in and try a few on.'),
            ('Will sterling silver tarnish?', 'It can, especially with humidity and lotions. Store it dry and polish with a silver cloth. See <a href="/guide/crystal-jewelry-care/">caring for crystal jewelry</a>.'),
            ('Do the stones have powers?', 'Many traditions give stones meanings, and we mention them because people ask. We present them as belief only; they are not medical advice.'),
            ('Which brands do you carry?', f'{len(S.brand_count)} named brands and makers, plus many independent pieces. See the <a href="/brands/">brand directory</a>.')]

def GUIDES(S):
    return [
     {'path': '/guide/ring-size-guide/', 'title': 'Ring Size Guide: Measure Your Ring Size at Home', 'desc': 'How to find your ring size at home with string or a ring you own, plus how our sterling gemstone rings are listed by size.', 'h1': 'Ring size guide',
      'html': '''<p class="lead">Our sterling gemstone rings are listed one size per listing, so it helps to know your size before you shop.</p>
<h2>Measure with a ring you already own</h2><ol><li>Pick a ring that fits the finger you plan to wear the new one on.</li><li>Measure the inside diameter in millimeters, edge to edge.</li><li>Match it: about 15.7 mm is a US 5, 16.5 mm a 6, 17.3 mm a 7, 18.1 mm an 8, 19.0 mm a 9 and 19.8 mm a 10.</li></ol>
<h2>Measure with string</h2><ol><li>Wrap string or a paper strip around the base of your finger.</li><li>Mark where it overlaps and measure the length in millimeters.</li><li>Divide by 3.14 to get the diameter and use the chart above.</li></ol>
<h2>Tips</h2><ul><li>Fingers swell in heat and later in the day; measure in the afternoon.</li><li>Wide bands fit tighter, so consider a half size up.</li><li>Adjustable rings in base metal or brass fit most sizes.</li></ul><p><a class="btn" href="/shop/gemstone-rings/">Shop gemstone rings</a></p>'''},
     {'path': '/guide/crystal-jewelry-care/', 'title': 'How to Care for Crystal & Gemstone Jewelry', 'desc': 'Simple care for crystal jewelry: cleaning sterling silver, which stones dislike water or heat, and how to store beaded bracelets.', 'h1': 'Caring for crystal jewelry',
      'html': '''<p class="lead">A few habits keep stones bright and settings tight.</p>
<h2>Everyday care</h2><ul><li>Put jewelry on last, after lotion, perfume and hairspray.</li><li>Take it off to swim, shower, clean or work out.</li><li>Wipe with a soft dry cloth after wearing.</li></ul>
<h2>Stones that need extra care</h2><ul><li><b>Selenite</b> is very soft and dissolves in water; keep it dry.</li><li><b>Malachite</b> and <b>turquoise</b> are soft and porous; avoid water, oils and cleaners.</li><li><b>Opal</b> can crack with sudden temperature changes.</li><li><b>Pearls</b> and shell scratch easily; store them separately.</li></ul>
<h2>Metals</h2><ul><li>Polish <a href="/sterling-silver-crystal-jewelry/">sterling silver</a> with a silver cloth; store it in a pouch to slow tarnish.</li><li>Copper and brass darken naturally and may leave a mark on skin; a jewelry cloth brightens them.</li><li>Plated pieces wear over time; avoid abrasive polish.</li></ul>
<h2>Beaded bracelets</h2><p>Roll them on and off instead of stretching, and keep the elastic away from water and lotion.</p>'''},
     {'path': '/crystal-jewelry-manhattan/', 'title': 'Where to Buy Crystal Jewelry in Manhattan, near Union Square', 'store_ld': True,
      'desc': f'Looking for crystal or gemstone jewelry in Manhattan? Namaste Crystal Jewelry is at {S.STORE_ADDR}, steps from Union Square, with about {S.ABOUT_N:,} pieces and in-store pickup.',
      'h1': 'Crystal jewelry in Manhattan', 'html': f'''<p class="lead">Shopping for a stone you can wear? Our case on 14th Street at Fifth Avenue holds about {S.ABOUT_N:,} pieces, and every one of them is online first, so you can pick before you come.</p>
<h2>In the case</h2><ul><li>{kinds_phrase(S.kind_count, 5).capitalize()}.</li><li>{S.SILVER_N:,} pieces in sterling silver; {S.UNDER30:,} pieces under $30.</li><li>{len(S.STONE_KEYS)} stones with their own page, from <a href="/stones/amethyst/">amethyst</a> to <a href="/stones/turquoise/">turquoise</a>.</li>{f"<li>Reserve online and pick up; orders are {S.READY.lower()}.</li>" if S.PICKUP_ON else ""}</ul>
<h2>Getting here</h2>{hood_list(S, "/near/")}{S.visit_block()}'''},
    ]
HOOD_ANGLE = {
 'union-square': 'Between the Greenmarket and Fifth Avenue, it is the closest crystal jewelry case to the square.',
 'east-village': 'If you shop St. Marks and East 14th for stones, our case is a straight run west on the same street.',
 'chelsea': 'From the galleries and the High Line, 14th Street takes you right to our door.',
 'flatiron': 'Ten blocks down Fifth from the Flatiron Building, with more stones in one case than most boutiques carry.',
 'greenwich-village': 'Up Fifth Avenue from Washington Square Park, past NYU, and you are here.',
 'midtown': 'A short subway ride from Times Square or Herald Square, with rings in your size waiting for pickup.',
}
def HOODS(S):
    out = []
    picks = S.by_rank([x for x in S.leaders if not x['noimg']])[:8]
    for k, n, route in HOOD_DATA:
        out.append({'path': f'/near/{k}/', 'title': f'Crystal Jewelry near {n}, NYC | Namaste Crystal Jewelry', 'h1': f'Crystal jewelry near {n}',
                    'desc': f'Crystal and gemstone jewelry near {n}: about {S.ABOUT_N:,} pieces at {S.STORE_ADDR}. Directions from {n}, hours and in-store pickup.',
                    'html': f'<p class="lead">{E(HOOD_ANGLE[k])} About {S.ABOUT_N:,} pendants, rings, bracelets and earrings with real stones, {S.SILVER_N:,} of them sterling.</p>'
                            f'<h2>From {E(n)}</h2><p>{E(route)}</p><h2>Popular right now</h2>{S.grid(picks)}{S.visit_block()}<h2>Other neighborhoods</h2>{hood_list(S, "/near/", k)}'})
    return out
NOT_FOUND = 'That piece has left the case'
