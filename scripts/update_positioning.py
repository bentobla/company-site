#!/usr/bin/env python3
"""Update site messaging to focus on what we build.

This performs targeted, deterministic replacements in a small set of pages:
- */index.html
- */about.html
- */principles.html

It intentionally does NOT touch contact pages or legal/privacy pages.

Usage:
  python3 scripts/update_positioning.py            # apply changes
  python3 scripts/update_positioning.py --check   # no writes, just report
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Replacement:
    old: str
    new: str
    label: str


def apply_replacements(text: str, replacements: Iterable[Replacement], *, file_label: str) -> tuple[str, list[str]]:
    changed_labels: list[str] = []
    for repl in replacements:
        if repl.old not in text:
            continue
        text = text.replace(repl.old, repl.new)
        changed_labels.append(repl.label)

    return text, changed_labels


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Only report changes; do not write files")
    args = parser.parse_args()

    targets: dict[Path, list[Replacement]] = {}

    def add(rel_path: str, *repls: Replacement) -> None:
        targets[ROOT / rel_path] = list(repls)

    # --- INDEX pages ---
    add(
        "en/index.html",
        Replacement(
            old='            <p class="lead">We build focused, practical software that uses artificial intelligence where it provides clear value. No hype. No subscriptions. No data harvesting.</p>',
            new='            <p class="lead">Some say AI will save us. Others say doomsday is near. We see a helpful tool—when used with care. We build focused applications that help people use AI to their advantage.</p>',
            label="en:index:lead",
        ),
        Replacement(
            old='            <p>We build applications as products, not services. We don\'t offer custom development or consulting. Each application we create reflects our approach to thoughtful, restrained technology.</p>',
            new='            <p>We build applications as products, not services. We focus on shipping and improving our own tools—each one reflects our approach to thoughtful, restrained technology.</p>',
            label="en:index:how-we-work",
        ),
        Replacement(
            old='            <p>We focus on problems where AI genuinely helps, not where it creates complexity or removes agency.</p>',
            new='            <p>We focus on problems where AI genuinely helps, and we keep the result simple, understandable, and user-controlled.</p>',
            label="en:index:good-ai-detail",
        ),
        Replacement(
            old='                <p>A learning application built around the idea that you bring the content, we provide the methods. AI assists where it adds clarity, not where it replaces understanding.</p>',
            new='                <p>A learning application built around the idea that you bring the content, we provide the methods. AI assists with structure and clarity—while understanding stays with the learner.</p>',
            label="en:index:project-ai-line",
        ),
    )

    add(
        "de/index.html",
        Replacement(
            old='            <p class="lead">Wir entwickeln fokussierte, praktische Software, die künstliche Intelligenz dort einsetzt, wo sie klaren Nutzen bringt. Kein Hype. Keine Abos. Kein Datensammeln.</p>',
            new='            <p class="lead">Manche sagen, KI sei unser Retter. Andere sagen, der Untergang sei nah. Wir sehen ein hilfreiches Werkzeug – wenn es richtig eingesetzt wird. Wir bauen fokussierte Anwendungen, die Menschen helfen, KI zu ihrem Vorteil zu nutzen.</p>',
            label="de:index:lead",
        ),
        Replacement(
            old='            <p>Wir entwickeln Anwendungen als Produkte, nicht als Dienstleistungen. Wir bieten keine individuelle Entwicklung oder Beratung an. Jede Anwendung, die wir erstellen, spiegelt unseren Ansatz zu durchdachter, zurückhaltender Technologie wider.</p>',
            new='            <p>Wir entwickeln Anwendungen als Produkte, nicht als Dienstleistungen. Wir konzentrieren uns darauf, eigene Werkzeuge zu entwickeln, zu veröffentlichen und zu verbessern – jede Anwendung spiegelt unseren Ansatz zu durchdachter, zurückhaltender Technologie wider.</p>',
            label="de:index:how-we-work",
        ),
        Replacement(
            old='            <p>Wir konzentrieren uns auf Probleme, bei denen KI tatsächlich hilft – nicht dort, wo sie Komplexität schafft oder Handlungsfähigkeit nimmt.</p>',
            new='            <p>Wir konzentrieren uns auf Probleme, bei denen KI tatsächlich hilft – und halten das Ergebnis bewusst einfach, verständlich und nutzerkontrolliert.</p>',
            label="de:index:good-ai-detail",
        ),
        Replacement(
            old='                <p>Eine Lernanwendung, die auf der Idee basiert, dass du die Inhalte mitbringst und wir die Methoden bereitstellen. KI unterstützt dort, wo sie Klarheit schafft – nicht dort, wo sie Verstehen ersetzt.</p>',
            new='                <p>Eine Lernanwendung, die auf der Idee basiert, dass du die Inhalte mitbringst und wir die Methoden bereitstellen. KI unterstützt mit Struktur und Klarheit – während das Verstehen bei dir bleibt.</p>',
            label="de:index:project-ai-line",
        ),
    )

    add(
        "fr/index.html",
        Replacement(
            old='            <p class="lead">Nous créons des logiciels ciblés et pratiques qui utilisent l\'intelligence artificielle là où elle apporte une valeur claire. Pas de battage médiatique. Pas d\'abonnements. Pas de collecte de données.</p>',
            new='            <p class="lead">Certains disent que l\'IA nous sauvera, d\'autres que la fin est proche. Nous y voyons surtout un outil utile — lorsqu\'il est bien utilisé. Nous construisons des applications ciblées qui aident les gens à tirer parti de l\'IA.</p>',
            label="fr:index:lead",
        ),
        Replacement(
            old='            <p>Nous créons des applications en tant que produits, pas en tant que services. Nous ne proposons pas de développement personnalisé ni de conseil. Chaque application que nous créons reflète notre approche d\'une technologie réfléchie et mesurée.</p>',
            new='            <p>Nous créons des applications en tant que produits, pas en tant que services. Nous nous concentrons sur la création, la publication et l\'amélioration de nos propres outils — chaque application reflète notre approche d\'une technologie réfléchie et mesurée.</p>',
            label="fr:index:how-we-work",
        ),
        Replacement(
            old='            <p>Nous nous concentrons sur les problèmes où l\'IA aide réellement, et non là où elle crée de la complexité ou retire l\'autonomie.</p>',
            new='            <p>Nous nous concentrons sur les problèmes où l\'IA aide réellement, tout en gardant le résultat simple, compréhensible et sous le contrôle de l\'utilisateur.</p>',
            label="fr:index:good-ai-detail",
        ),
        Replacement(
            old='                <p>Une application d\'apprentissage basée sur l\'idée que vous apportez le contenu et nous fournissons les méthodes. L\'IA assiste là où elle apporte de la clarté, pas là où elle remplace la compréhension.</p>',
            new='                <p>Une application d\'apprentissage basée sur l\'idée que vous apportez le contenu et nous fournissons les méthodes. L\'IA assiste avec structure et clarté — tout en laissant la compréhension à l\'apprenant.</p>',
            label="fr:index:project-ai-line",
        ),
    )

    add(
        "es/index.html",
        Replacement(
            old='            <p class="lead">Construimos software enfocado y práctico que usa inteligencia artificial donde aporta valor claro. Sin exageraciones. Sin suscripciones. Sin recopilación de datos.</p>',
            new='            <p class="lead">Algunos dicen que la IA será nuestro salvador; otros, que el fin está cerca. Nosotros la vemos como una herramienta útil, si se usa bien. Construimos aplicaciones enfocadas que ayudan a las personas a aprovechar la IA a su favor.</p>',
            label="es:index:lead",
        ),
        Replacement(
            old='            <p>Construimos aplicaciones como productos, no como servicios. No ofrecemos desarrollo personalizado ni consultoría. Cada aplicación que creamos refleja nuestro enfoque hacia la tecnología reflexiva y moderada.</p>',
            new='            <p>Construimos aplicaciones como productos, no como servicios. Nos enfocamos en crear, lanzar y mejorar nuestras propias herramientas; cada aplicación refleja nuestro enfoque hacia la tecnología reflexiva y moderada.</p>',
            label="es:index:how-we-work",
        ),
        Replacement(
            old='            <p>Nos enfocamos en problemas donde la IA realmente ayuda, no donde crea complejidad o quita autonomía.</p>',
            new='            <p>Nos enfocamos en problemas donde la IA realmente ayuda, manteniendo el resultado simple, comprensible y bajo control del usuario.</p>',
            label="es:index:good-ai-detail",
        ),
        Replacement(
            old='                <p>Una aplicación de aprendizaje basada en la idea de que tú aportas el contenido y nosotros proporcionamos los métodos. La IA asiste donde aporta claridad, no donde reemplaza la comprensión.</p>',
            new='                <p>Una aplicación de aprendizaje basada en la idea de que tú aportas el contenido y nosotros proporcionamos los métodos. La IA asiste con estructura y claridad, mientras el entendimiento sigue siendo tuyo.</p>',
            label="es:index:project-ai-line",
        ),
    )

    add(
        "it/index.html",
        Replacement(
            old='            <p class="lead">Costruiamo software mirato e pratico che utilizza l\'intelligenza artificiale dove apporta valore chiaro. Niente hype. Niente abbonamenti. Niente raccolta dati.</p>',
            new='            <p class="lead">C\'è chi dice che l\'IA ci salverà e chi parla di fine imminente. Noi la vediamo come uno strumento utile, se usato bene. Costruiamo applicazioni mirate che aiutano le persone a usare l\'IA a proprio vantaggio.</p>',
            label="it:index:lead",
        ),
        Replacement(
            old='            <p>Costruiamo applicazioni come prodotti, non come servizi. Non offriamo sviluppo personalizzato o consulenza. Ogni applicazione che creiamo riflette il nostro approccio a una tecnologia ponderata e moderata.</p>',
            new='            <p>Costruiamo applicazioni come prodotti, non come servizi. Ci concentriamo sul creare, rilasciare e migliorare i nostri strumenti; ogni applicazione riflette il nostro approccio a una tecnologia ponderata e moderata.</p>',
            label="it:index:how-we-work",
        ),
        Replacement(
            old='            <p>Ci concentriamo sui problemi dove l\'IA aiuta davvero, non dove crea complessità o toglie autonomia.</p>',
            new='            <p>Ci concentriamo sui problemi dove l\'IA aiuta davvero, mantenendo il risultato semplice, comprensibile e sotto il controllo dell\'utente.</p>',
            label="it:index:good-ai-detail",
        ),
        Replacement(
            old='                <p>Un\'applicazione di apprendimento basata sull\'idea che tu porti i contenuti e noi forniamo i metodi. L\'IA assiste dove apporta chiarezza, non dove sostituisce la comprensione.</p>',
            new='                <p>Un\'applicazione di apprendimento basata sull\'idea che tu porti i contenuti e noi forniamo i metodi. L\'IA assiste con struttura e chiarezza — mentre la comprensione resta a te.</p>',
            label="it:index:project-ai-line",
        ),
    )

    add(
        "nl/index.html",
        Replacement(
            old='            <p class="lead">We bouwen gerichte, praktische software die kunstmatige intelligentie gebruikt waar het duidelijke waarde biedt. Geen hype. Geen abonnementen. Geen dataverzameling.</p>',
            new='            <p class="lead">Sommigen zeggen dat AI onze redder is, anderen dat het einde nabij is. Wij zien vooral een handig hulpmiddel—als je het goed inzet. We bouwen gerichte applicaties die mensen helpen AI in hun voordeel te gebruiken.</p>',
            label="nl:index:lead",
        ),
        Replacement(
            old='            <p>We bouwen applicaties als producten, niet als diensten. We bieden geen maatwerkontwikkeling of advies aan. Elke applicatie die we creëren weerspiegelt onze benadering van doordachte, terughoudende technologie.</p>',
            new='            <p>We bouwen applicaties als producten, niet als diensten. We focussen op het bouwen, uitbrengen en verbeteren van onze eigen hulpmiddelen; elke applicatie weerspiegelt onze benadering van doordachte, terughoudende technologie.</p>',
            label="nl:index:how-we-work",
        ),
        Replacement(
            old='            <p>We focussen op problemen waar AI echt helpt, niet waar het complexiteit creëert of autonomie wegneemt.</p>',
            new='            <p>We focussen op problemen waar AI echt helpt, en we houden het resultaat simpel, begrijpelijk en onder controle van de gebruiker.</p>',
            label="nl:index:good-ai-detail",
        ),
        Replacement(
            old='                <p>Een leerapplicatie gebaseerd op het idee dat jij de inhoud meebrengt en wij de methoden bieden. AI assisteert waar het duidelijkheid biedt, niet waar het begrip vervangt.</p>',
            new='                <p>Een leerapplicatie gebaseerd op het idee dat jij de inhoud meebrengt en wij de methoden bieden. AI helpt met structuur en duidelijkheid—terwijl begrip bij de leerling blijft.</p>',
            label="nl:index:project-ai-line",
        ),
    )

    # --- ABOUT pages ---
    add(
        "en/about.html",
        Replacement(
            old='            <h2>What we don\'t do</h2>',
            new='            <h2>What we build</h2>',
            label="en:about:heading",
        ),
        Replacement(
            old='            <p>We are not a software agency, development studio, or consultancy. We don\'t build custom solutions or offer technical services. We build focused applications and release them as products.</p>',
            new='            <p>We build small, focused applications with clear boundaries—tools that help people learn, work, and make decisions with AI in a practical way. We ship products, iterate, and keep the scope tight.</p>',
            label="en:about:section",
        ),
        Replacement(
            old='            <p>We focus on one project at a time. We don\'t take client work or build on commission. This allows us to make decisions based on what makes sense, not what sells.</p>',
            new='            <p>We focus on one project at a time. We build our own products rather than taking on client work. This allows us to make decisions based on what makes sense, not what sells.</p>',
            label="en:about:how-we-build",
        ),
        Replacement(
            old='            <p>We use AI where it provides clear, understandable value. We avoid it where it adds complexity, removes agency, or replaces genuine understanding with approximation.</p>',
            new='            <p>We use AI where it provides clear, understandable value—and keep the experience understandable, calm, and under the user\'s control.</p>',
            label="en:about:ai-paragraph",
        ),
        Replacement(
            old='            <p>Our applications are products with clear boundaries. We charge for them transparently when appropriate. We don\'t rely on advertising or user data as a business model.</p>',
            new='            <p>Our applications are products with clear boundaries. We charge for them transparently when appropriate. Our business model is product-first, with no dependence on advertising or user-data brokerage.</p>',
            label="en:about:business-model",
        ),
    )

    add(
        "de/about.html",
        Replacement(
            old='            <h2>Was wir nicht tun</h2>',
            new='            <h2>Was wir bauen</h2>',
            label="de:about:heading",
        ),
        Replacement(
            old='            <p>Wir sind keine Softwareagentur, kein Entwicklungsstudio und keine Beratung. Wir entwickeln keine maßgeschneiderten Lösungen und bieten keine technischen Dienstleistungen an. Wir entwickeln fokussierte Anwendungen und veröffentlichen sie als Produkte.</p>',
            new='            <p>Wir bauen kleine, fokussierte Anwendungen mit klaren Grenzen – Werkzeuge, die Menschen dabei helfen, KI im Alltag sinnvoll zu nutzen. Wir veröffentlichen Produkte, verbessern sie iterativ und halten den Umfang bewusst schlank.</p>',
            label="de:about:section",
        ),
        Replacement(
            old='            <p>Wir konzentrieren uns auf jeweils ein Projekt. Wir nehmen keine Kundenaufträge an und entwickeln nicht auf Auftrag. Das erlaubt uns, Entscheidungen danach zu treffen, was sinnvoll ist – nicht danach, was sich verkauft.</p>',
            new='            <p>Wir konzentrieren uns auf jeweils ein Projekt. Wir entwickeln eigene Produkte statt Kundenaufträge anzunehmen. Das erlaubt uns, Entscheidungen danach zu treffen, was sinnvoll ist – nicht danach, was sich verkauft.</p>',
            label="de:about:how-we-build",
        ),
        Replacement(
            old='            <p>Wir setzen KI dort ein, wo sie klaren, verständlichen Nutzen bringt. Wir vermeiden sie dort, wo sie Komplexität schafft, Handlungsfähigkeit nimmt oder echtes Verstehen durch Annäherung ersetzt.</p>',
            new='            <p>Wir setzen KI dort ein, wo sie klaren, verständlichen Nutzen bringt – und gestalten Anwendungen so, dass sie verständlich bleiben, ruhig wirken und die Kontrolle beim Nutzer lassen.</p>',
            label="de:about:ai-paragraph",
        ),
        Replacement(
            old='            <p>Unsere Anwendungen sind Produkte mit klaren Grenzen. Wir verlangen transparent Geld dafür, wenn es angemessen ist. Wir stützen uns nicht auf Werbung oder Nutzerdaten als Geschäftsmodell.</p>',
            new='            <p>Unsere Anwendungen sind Produkte mit klaren Grenzen. Wir verlangen transparent Geld dafür, wenn es angemessen ist. Unser Modell ist produktorientiert – ohne Abhängigkeit von Werbung oder dem Handel mit Nutzerdaten.</p>',
            label="de:about:business-model",
        ),
    )

    add(
        "fr/about.html",
        Replacement(
            old='            <h2>Ce que nous ne faisons pas</h2>',
            new='            <h2>Ce que nous construisons</h2>',
            label="fr:about:heading",
        ),
        Replacement(
            old='            <p>Nous ne sommes pas une agence logicielle, un studio de développement ou un cabinet de conseil. Nous ne construisons pas de solutions personnalisées et n\'offrons pas de services techniques. Nous créons des applications ciblées et les publions en tant que produits.</p>',
            new='            <p>Nous construisons de petites applications ciblées, avec des limites claires — des outils qui aident à apprendre, travailler et décider avec l\'IA de manière pragmatique. Nous publions des produits, les améliorons itérativement et gardons un périmètre volontairement restreint.</p>',
            label="fr:about:section",
        ),
        Replacement(
            old='            <p>Nous nous concentrons sur un projet à la fois. Nous ne prenons pas de travaux clients ni ne construisons sur commande. Cela nous permet de prendre des décisions basées sur ce qui a du sens, pas sur ce qui se vend.</p>',
            new='            <p>Nous nous concentrons sur un projet à la fois. Nous construisons nos propres produits plutôt que de prendre des travaux clients. Cela nous permet de prendre des décisions basées sur ce qui a du sens, pas sur ce qui se vend.</p>',
            label="fr:about:how-we-build",
        ),
        Replacement(
            old='            <p>Nous utilisons l\'IA là où elle apporte une valeur claire et compréhensible. Nous l\'évitons là où elle ajoute de la complexité, retire l\'autonomie ou remplace une véritable compréhension par une approximation.</p>',
            new='            <p>Nous utilisons l\'IA là où elle apporte une valeur claire et compréhensible — tout en gardant l\'expérience compréhensible, calme et sous le contrôle de l\'utilisateur.</p>',
            label="fr:about:ai-paragraph",
        ),
        Replacement(
            old='            <p>Nos applications sont des produits avec des limites claires. Nous les facturons de manière transparente lorsque cela est approprié. Nous ne nous appuyons pas sur la publicité ou les données utilisateur comme modèle commercial.</p>',
            new='            <p>Nos applications sont des produits avec des limites claires. Nous les facturons de manière transparente lorsque cela est approprié. Notre modèle est orienté produit, sans dépendance à la publicité ni à la monétisation des données utilisateur.</p>',
            label="fr:about:business-model",
        ),
    )

    add(
        "es/about.html",
        Replacement(
            old='            <h2>Lo que no hacemos</h2>',
            new='            <h2>Lo que construimos</h2>',
            label="es:about:heading",
        ),
        Replacement(
            old='            <p>No somos una agencia de software, estudio de desarrollo o consultoría. No construimos soluciones personalizadas ni ofrecemos servicios técnicos. Construimos aplicaciones enfocadas y las lanzamos como productos.</p>',
            new='            <p>Construimos aplicaciones pequeñas y enfocadas, con límites claros: herramientas que ayudan a aprender, trabajar y tomar decisiones con IA de forma práctica. Lanzamos productos, iteramos y mantenemos el alcance deliberadamente ajustado.</p>',
            label="es:about:section",
        ),
        Replacement(
            old='            <p>Nos enfocamos en un proyecto a la vez. No aceptamos trabajos de clientes ni construimos por encargo. Esto nos permite tomar decisiones basadas en lo que tiene sentido, no en lo que se vende.</p>',
            new='            <p>Nos enfocamos en un proyecto a la vez. Construimos nuestros propios productos en lugar de aceptar trabajos de clientes. Esto nos permite tomar decisiones basadas en lo que tiene sentido, no en lo que se vende.</p>',
            label="es:about:how-we-build",
        ),
        Replacement(
            old='            <p>Usamos IA donde aporta valor claro y comprensible. La evitamos donde agrega complejidad, quita autonomía o reemplaza la comprensión genuina con aproximación.</p>',
            new='            <p>Usamos IA donde aporta valor claro y comprensible, manteniendo la experiencia entendible, tranquila y bajo control del usuario.</p>',
            label="es:about:ai-paragraph",
        ),
        Replacement(
            old='            <p>Nuestras aplicaciones son productos con límites claros. Cobramos por ellas de manera transparente cuando es apropiado. No dependemos de publicidad o datos de usuario como modelo de negocio.</p>',
            new='            <p>Nuestras aplicaciones son productos con límites claros. Cobramos por ellas de manera transparente cuando es apropiado. Nuestro modelo es orientado a producto, sin depender de publicidad ni de la monetización de datos de usuario.</p>',
            label="es:about:business-model",
        ),
    )

    add(
        "it/about.html",
        Replacement(
            old='            <h2>Cosa non facciamo</h2>',
            new='            <h2>Cosa costruiamo</h2>',
            label="it:about:heading",
        ),
        Replacement(
            old='            <p>Non siamo un\'agenzia software, uno studio di sviluppo o una consulenza. Non costruiamo soluzioni personalizzate né offriamo servizi tecnici. Costruiamo applicazioni mirate e le rilasciamo come prodotti.</p>',
            new='            <p>Costruiamo piccole applicazioni mirate, con confini chiari: strumenti che aiutano a imparare, lavorare e prendere decisioni con l\'IA in modo pratico. Rilasciamo prodotti, iteriamo e manteniamo lo scopo volutamente ristretto.</p>',
            label="it:about:section",
        ),
        Replacement(
            old='            <p>Ci concentriamo su un progetto alla volta. Non accettiamo lavori su commissione né costruiamo su ordinazione. Questo ci consente di prendere decisioni basate su ciò che ha senso, non su ciò che vende.</p>',
            new='            <p>Ci concentriamo su un progetto alla volta. Costruiamo i nostri prodotti invece di accettare lavori su commissione. Questo ci consente di prendere decisioni basate su ciò che ha senso, non su ciò che vende.</p>',
            label="it:about:how-we-build",
        ),
        Replacement(
            old='            <p>Usiamo l\'IA dove apporta valore chiaro e comprensibile. La evitiamo dove aggiunge complessità, toglie autonomia o sostituisce una vera comprensione con un\'approssimazione.</p>',
            new='            <p>Usiamo l\'IA dove apporta valore chiaro e comprensibile, mantenendo l\'esperienza comprensibile, calma e sotto il controllo dell\'utente.</p>',
            label="it:about:ai-paragraph",
        ),
        Replacement(
            old='            <p>Le nostre applicazioni sono prodotti con confini chiari. Le facciamo pagare in modo trasparente quando appropriato. Non ci affidiamo a pubblicità o dati utente come modello di business.</p>',
            new='            <p>Le nostre applicazioni sono prodotti con confini chiari. Le facciamo pagare in modo trasparente quando appropriato. Il nostro modello è orientato al prodotto, senza dipendere da pubblicità o dalla monetizzazione dei dati utente.</p>',
            label="it:about:business-model",
        ),
    )

    add(
        "nl/about.html",
        Replacement(
            old='            <h2>Wat we niet doen</h2>',
            new='            <h2>Wat we bouwen</h2>',
            label="nl:about:heading",
        ),
        Replacement(
            old='            <p>We zijn geen softwarebureau, ontwikkelstudio of adviesbureau. We bouwen geen maatwerk oplossingen en bieden geen technische diensten aan. We bouwen gerichte applicaties en brengen ze uit als producten.</p>',
            new='            <p>We bouwen kleine, gerichte applicaties met duidelijke grenzen—hulpmiddelen die mensen praktisch helpen leren, werken en beslissen met AI. We brengen producten uit, verbeteren ze iteratief en houden de scope bewust strak.</p>',
            label="nl:about:section",
        ),
        Replacement(
            old='            <p>We focussen op één project tegelijk. We accepteren geen klantwerk en bouwen niet op bestelling. Dit stelt ons in staat beslissingen te nemen op basis van wat zinvol is, niet wat verkoopt.</p>',
            new='            <p>We focussen op één project tegelijk. We bouwen onze eigen producten in plaats van klantwerk aan te nemen. Dit stelt ons in staat beslissingen te nemen op basis van wat zinvol is, niet wat verkoopt.</p>',
            label="nl:about:how-we-build",
        ),
        Replacement(
            old='            <p>We gebruiken AI waar het duidelijke, begrijpelijke waarde biedt. We vermijden het waar het complexiteit toevoegt, autonomie wegneemt of echt begrip vervangt door benadering.</p>',
            new='            <p>We gebruiken AI waar het duidelijke, begrijpelijke waarde biedt, terwijl we de ervaring begrijpelijk, kalm en onder controle van de gebruiker houden.</p>',
            label="nl:about:ai-paragraph",
        ),
        Replacement(
            old='            <p>Onze applicaties zijn producten met duidelijke grenzen. We rekenen er transparant voor wanneer dat gepast is. We vertrouwen niet op advertenties of gebruikersgegevens als bedrijfsmodel.</p>',
            new='            <p>Onze applicaties zijn producten met duidelijke grenzen. We rekenen er transparant voor wanneer dat gepast is. Ons model is productgericht, zonder afhankelijk te zijn van advertenties of het vermarkten van gebruikersgegevens.</p>',
            label="nl:about:business-model",
        ),
    )

    # --- PRINCIPLES pages ---
    add(
        "en/principles.html",
        Replacement(
            old='                <h3>No subscriptions</h3>\n                <p>We charge for applications when appropriate, but we don\'t lock features behind recurring payments. If you buy something, you own it.</p>',
            new='                <h3>Ownership-first pricing</h3>\n                <p>When an application costs money, we price it in a way that feels like buying a product. If you buy something, you own it.</p>',
            label="en:principles:pricing",
        ),
        Replacement(
            old='                <h3>No dark patterns</h3>\n                <p>Every interaction is designed to be clear and honest. We don\'t manipulate users into decisions they don\'t want to make.</p>',
            new='                <h3>Honest interfaces</h3>\n                <p>Every interaction is designed to be clear and honest. People should understand what\'s happening and why.</p>',
            label="en:principles:ux",
        ),
        Replacement(
            old='                <h3>No data harvesting</h3>\n                <p>We don\'t collect user data for profiling or resale. If data needs to be stored, we\'re explicit about what, why, and for how long.</p>',
            new='                <h3>Data minimization</h3>\n                <p>We minimize data collection and keep it purpose-driven. If data needs to be stored, we\'re explicit about what, why, and for how long.</p>',
            label="en:principles:data",
        ),
        Replacement(
            old='                <h3>Transparent monetization</h3>\n                <p>If an application costs money, we\'re direct about it. No hidden fees, no surprise charges, no ad-based business models.</p>',
            new='                <h3>Transparent monetization</h3>\n                <p>If an application costs money, we\'re direct about it: clear pricing, predictable costs, and a product-first model.</p>',
            label="en:principles:monetization",
        ),
        Replacement(
            old='                <h3>AI only where useful</h3>\n                <p>We use AI where it provides clear, understandable value. We don\'t use it to obscure functionality or replace genuine understanding with approximation.</p>',
            new='                <h3>AI only where useful</h3>\n                <p>We use AI to add clear, understandable value. Functionality stays transparent, and the user stays in control.</p>',
            label="en:principles:ai",
        ),
        Replacement(
            old='                <h3>Restrained by default</h3>\n                <p>Applications should be calm and focused. No unnecessary notifications, no gamification for engagement, no features designed to create dependency.</p>',
            new='                <h3>Restrained by default</h3>\n                <p>Applications should be calm and focused. Notifications are used sparingly, and features are designed to support goals rather than create dependency.</p>',
            label="en:principles:restrained",
        ),
        Replacement(
            old='                <h3>Clear boundaries</h3>\n                <p>Each application has a specific purpose. We don\'t build platforms that expand endlessly. We build tools that do one thing well.</p>',
            new='                <h3>Clear boundaries</h3>\n                <p>Each application has a specific purpose. We build tools with a tight scope that do one thing well.</p>',
            label="en:principles:boundaries",
        ),
    )

    add(
        "de/principles.html",
        Replacement(
            old='                <h3>Keine Abos</h3>\n                <p>Wir verlangen Geld für Anwendungen, wenn es angemessen ist, aber wir sperren keine Funktionen hinter wiederkehrenden Zahlungen. Wenn du etwas kaufst, gehört es dir.</p>',
            new='                <h3>Einmal kaufen, besitzen</h3>\n                <p>Wenn eine Anwendung Geld kostet, bepreisen wir sie wie ein Produkt. Wenn du etwas kaufst, gehört es dir.</p>',
            label="de:principles:pricing",
        ),
        Replacement(
            old='                <h3>Keine Dark Patterns</h3>\n                <p>Jede Interaktion ist so gestaltet, dass sie klar und ehrlich ist. Wir manipulieren Nutzer nicht zu Entscheidungen, die sie nicht treffen wollen.</p>',
            new='                <h3>Ehrliche Interfaces</h3>\n                <p>Jede Interaktion ist so gestaltet, dass sie klar und ehrlich ist. Menschen sollen verstehen, was passiert – und warum.</p>',
            label="de:principles:ux",
        ),
        Replacement(
            old='                <h3>Kein Datensammeln</h3>\n                <p>Wir sammeln keine Nutzerdaten für Profiling oder Weiterverkauf. Wenn Daten gespeichert werden müssen, sind wir explizit darüber, was, warum und wie lange.</p>',
            new='                <h3>Datenminimierung</h3>\n                <p>Wir minimieren Datenerhebung und halten sie zweckgebunden. Wenn Daten gespeichert werden müssen, sind wir explizit darüber, was, warum und wie lange.</p>',
            label="de:principles:data",
        ),
        Replacement(
            old='                <h3>Transparente Monetarisierung</h3>\n                <p>Wenn eine Anwendung Geld kostet, sind wir direkt damit. Keine versteckten Gebühren, keine Überraschungskosten, keine werbebasierten Geschäftsmodelle.</p>',
            new='                <h3>Transparente Monetarisierung</h3>\n                <p>Wenn eine Anwendung Geld kostet, sind wir direkt damit: klare Preise, planbare Kosten und ein produktorientiertes Modell.</p>',
            label="de:principles:monetization",
        ),
        Replacement(
            old='                <h3>KI nur wo nützlich</h3>\n                <p>Wir setzen KI dort ein, wo sie klaren, verständlichen Nutzen bringt. Wir nutzen sie nicht, um Funktionalität zu verschleiern oder echtes Verstehen durch Annäherung zu ersetzen.</p>',
            new='                <h3>KI nur wo nützlich</h3>\n                <p>Wir setzen KI ein, um klaren, verständlichen Nutzen zu schaffen. Funktionen bleiben transparent, und die Kontrolle bleibt beim Nutzer.</p>',
            label="de:principles:ai",
        ),
        Replacement(
            old='                <h3>Standardmäßig zurückhaltend</h3>\n                <p>Anwendungen sollten ruhig und fokussiert sein. Keine unnötigen Benachrichtigungen, keine Gamification für Engagement, keine Features, die Abhängigkeit schaffen sollen.</p>',
            new='                <h3>Standardmäßig zurückhaltend</h3>\n                <p>Anwendungen sollten ruhig und fokussiert sein. Benachrichtigungen werden sparsam eingesetzt, und Features unterstützen Ziele statt Abhängigkeit zu erzeugen.</p>',
            label="de:principles:restrained",
        ),
        Replacement(
            old='                <h3>Klare Grenzen</h3>\n                <p>Jede Anwendung hat einen spezifischen Zweck. Wir bauen keine Plattformen, die sich endlos erweitern. Wir bauen Werkzeuge, die eine Sache gut machen.</p>',
            new='                <h3>Klare Grenzen</h3>\n                <p>Jede Anwendung hat einen spezifischen Zweck. Wir bauen Werkzeuge mit bewusst engem Umfang, die eine Sache gut machen.</p>',
            label="de:principles:boundaries",
        ),
    )

    add(
        "fr/principles.html",
        Replacement(
            old='                <h3>Pas d\'abonnements</h3>\n                <p>Nous facturons les applications lorsque cela est approprié, mais nous ne verrouillons pas les fonctionnalités derrière des paiements récurrents. Si vous achetez quelque chose, vous le possédez.</p>',
            new='                <h3>Prix clair, esprit produit</h3>\n                <p>Quand une application coûte de l\'argent, nous la tarifons comme un produit. Si vous achetez quelque chose, vous le possédez.</p>',
            label="fr:principles:pricing",
        ),
        Replacement(
            old='                <h3>Pas de dark patterns</h3>\n                <p>Chaque interaction est conçue pour être claire et honnête. Nous ne manipulons pas les utilisateurs vers des décisions qu\'ils ne veulent pas prendre.</p>',
            new='                <h3>Interfaces honnêtes</h3>\n                <p>Chaque interaction est conçue pour être claire et honnête. Les gens doivent comprendre ce qui se passe — et pourquoi.</p>',
            label="fr:principles:ux",
        ),
        Replacement(
            old='                <h3>Pas de collecte de données</h3>\n                <p>Nous ne collectons pas de données utilisateur pour le profilage ou la revente. Si des données doivent être stockées, nous sommes explicites sur quoi, pourquoi et pour combien de temps.</p>',
            new='                <h3>Minimisation des données</h3>\n                <p>Nous minimisons la collecte de données et la gardons strictement liée à un objectif. Si des données doivent être stockées, nous sommes explicites sur quoi, pourquoi et pour combien de temps.</p>',
            label="fr:principles:data",
        ),
        Replacement(
            old='                <h3>Monétisation transparente</h3>\n                <p>Si une application coûte de l\'argent, nous sommes directs à ce sujet. Pas de frais cachés, pas de frais surprises, pas de modèles commerciaux basés sur la publicité.</p>',
            new='                <h3>Monétisation transparente</h3>\n                <p>Si une application coûte de l\'argent, nous sommes directs : prix clairs, coûts prévisibles et un modèle orienté produit.</p>',
            label="fr:principles:monetization",
        ),
        Replacement(
            old='                <h3>IA uniquement où utile</h3>\n                <p>Nous utilisons l\'IA là où elle apporte une valeur claire et compréhensible. Nous ne l\'utilisons pas pour obscurcir la fonctionnalité ou remplacer une véritable compréhension par une approximation.</p>',
            new='                <h3>IA uniquement où utile</h3>\n                <p>Nous utilisons l\'IA pour apporter une valeur claire et compréhensible. Les fonctionnalités restent transparentes, et l\'utilisateur garde le contrôle.</p>',
            label="fr:principles:ai",
        ),
        Replacement(
            old='                <h3>Retenue par défaut</h3>\n                <p>Les applications doivent être calmes et ciblées. Pas de notifications inutiles, pas de gamification pour l\'engagement, pas de fonctionnalités conçues pour créer une dépendance.</p>',
            new='                <h3>Retenue par défaut</h3>\n                <p>Les applications doivent être calmes et ciblées. Les notifications sont utilisées avec parcimonie, et les fonctionnalités soutiennent des objectifs plutôt que de créer une dépendance.</p>',
            label="fr:principles:restrained",
        ),
        Replacement(
            old='                <h3>Limites claires</h3>\n                <p>Chaque application a un objectif spécifique. Nous ne construisons pas de plateformes qui s\'étendent sans fin. Nous construisons des outils qui font bien une chose.</p>',
            new='                <h3>Limites claires</h3>\n                <p>Chaque application a un objectif spécifique. Nous construisons des outils au périmètre resserré qui font bien une chose.</p>',
            label="fr:principles:boundaries",
        ),
    )

    add(
        "es/principles.html",
        Replacement(
            old='                <h3>Sin suscripciones</h3>\n                <p>Cobramos por aplicaciones cuando es apropiado, pero no bloqueamos características detrás de pagos recurrentes. Si compras algo, te pertenece.</p>',
            new='                <h3>Precio claro, como producto</h3>\n                <p>Cuando una aplicación cuesta dinero, la cobramos como un producto. Si compras algo, te pertenece.</p>',
            label="es:principles:pricing",
        ),
        Replacement(
            old='                <h3>Sin patrones oscuros</h3>\n                <p>Cada interacción está diseñada para ser clara y honesta. No manipulamos a los usuarios hacia decisiones que no quieren tomar.</p>',
            new='                <h3>Interfaces honestas</h3>\n                <p>Cada interacción está diseñada para ser clara y honesta. Las personas deben entender qué pasa y por qué.</p>',
            label="es:principles:ux",
        ),
        Replacement(
            old='                <h3>Sin recopilación de datos</h3>\n                <p>No recopilamos datos de usuario para perfiles o reventa. Si es necesario almacenar datos, somos explícitos sobre qué, por qué y durante cuánto tiempo.</p>',
            new='                <h3>Minimización de datos</h3>\n                <p>Minimizamos la recopilación de datos y la mantenemos ligada a un propósito. Si es necesario almacenar datos, somos explícitos sobre qué, por qué y durante cuánto tiempo.</p>',
            label="es:principles:data",
        ),
        Replacement(
            old='                <h3>Monetización transparente</h3>\n                <p>Si una aplicación cuesta dinero, somos directos al respecto. Sin tarifas ocultas, sin cargos sorpresa, sin modelos de negocio basados en publicidad.</p>',
            new='                <h3>Monetización transparente</h3>\n                <p>Si una aplicación cuesta dinero, somos directos: precios claros, costos predecibles y un modelo orientado a producto.</p>',
            label="es:principles:monetization",
        ),
        Replacement(
            old='                <h3>IA solo donde sea útil</h3>\n                <p>Usamos IA donde aporta valor claro y comprensible. No la usamos para oscurecer funcionalidad o reemplazar comprensión genuina con aproximación.</p>',
            new='                <h3>IA solo donde sea útil</h3>\n                <p>Usamos IA para aportar valor claro y comprensible. La funcionalidad se mantiene transparente y el usuario conserva el control.</p>',
            label="es:principles:ai",
        ),
        Replacement(
            old='                <h3>Moderado por defecto</h3>\n                <p>Las aplicaciones deben ser tranquilas y enfocadas. Sin notificaciones innecesarias, sin gamificación para el compromiso, sin características diseñadas para crear dependencia.</p>',
            new='                <h3>Moderado por defecto</h3>\n                <p>Las aplicaciones deben ser tranquilas y enfocadas. Las notificaciones se usan con moderación, y las características apoyan objetivos en lugar de crear dependencia.</p>',
            label="es:principles:restrained",
        ),
        Replacement(
            old='                <h3>Límites claros</h3>\n                <p>Cada aplicación tiene un propósito específico. No construimos plataformas que se expanden sin fin. Construimos herramientas que hacen bien una cosa.</p>',
            new='                <h3>Límites claros</h3>\n                <p>Cada aplicación tiene un propósito específico. Construimos herramientas con un alcance deliberadamente ajustado que hacen bien una cosa.</p>',
            label="es:principles:boundaries",
        ),
    )

    add(
        "it/principles.html",
        Replacement(
            old='                <h3>Niente abbonamenti</h3>\n                <p>Facciamo pagare le applicazioni quando appropriato, ma non blocchiamo le funzionalità dietro pagamenti ricorrenti. Se acquisti qualcosa, è tuo.</p>',
            new='                <h3>Prezzo chiaro, spirito prodotto</h3>\n                <p>Quando un\'applicazione costa denaro, la prezziamo come un prodotto. Se acquisti qualcosa, è tuo.</p>',
            label="it:principles:pricing",
        ),
        Replacement(
            old='                <h3>Niente dark pattern</h3>\n                <p>Ogni interazione è progettata per essere chiara e onesta. Non manipoliamo gli utenti verso decisioni che non vogliono prendere.</p>',
            new='                <h3>Interfacce oneste</h3>\n                <p>Ogni interazione è progettata per essere chiara e onesta. Le persone devono capire cosa succede e perché.</p>',
            label="it:principles:ux",
        ),
        Replacement(
            old='                <h3>Niente raccolta dati</h3>\n                <p>Non raccogliamo dati utente per profilazione o rivendita. Se i dati devono essere archiviati, siamo espliciti su cosa, perché e per quanto tempo.</p>',
            new='                <h3>Minimizzazione dei dati</h3>\n                <p>Minimizziamo la raccolta dati e la manteniamo legata a uno scopo. Se i dati devono essere archiviati, siamo espliciti su cosa, perché e per quanto tempo.</p>',
            label="it:principles:data",
        ),
        Replacement(
            old='                <h3>Monetizzazione trasparente</h3>\n                <p>Se un\'applicazione costa denaro, siamo diretti al riguardo. Niente tariffe nascoste, niente costi sorpresa, niente modelli di business basati su pubblicità.</p>',
            new='                <h3>Monetizzazione trasparente</h3>\n                <p>Se un\'applicazione costa denaro, siamo diretti: prezzi chiari, costi prevedibili e un modello orientato al prodotto.</p>',
            label="it:principles:monetization",
        ),
        Replacement(
            old='                <h3>IA solo dove utile</h3>\n                <p>Usiamo l\'IA dove apporta valore chiaro e comprensibile. Non la usiamo per oscurare la funzionalità o sostituire una vera comprensione con un\'approssimazione.</p>',
            new='                <h3>IA solo dove utile</h3>\n                <p>Usiamo l\'IA per apportare valore chiaro e comprensibile. Le funzionalità restano trasparenti e l\'utente mantiene il controllo.</p>',
            label="it:principles:ai",
        ),
        Replacement(
            old='                <h3>Moderato per impostazione predefinita</h3>\n                <p>Le applicazioni dovrebbero essere calme e mirate. Niente notifiche inutili, niente gamification per il coinvolgimento, niente funzionalità progettate per creare dipendenza.</p>',
            new='                <h3>Moderato per impostazione predefinita</h3>\n                <p>Le applicazioni dovrebbero essere calme e mirate. Le notifiche sono usate con parsimonia, e le funzionalità supportano obiettivi invece di creare dipendenza.</p>',
            label="it:principles:restrained",
        ),
        Replacement(
            old='                <h3>Confini chiari</h3>\n                <p>Ogni applicazione ha uno scopo specifico. Non costruiamo piattaforme che si espandono all\'infinito. Costruiamo strumenti che fanno bene una cosa.</p>',
            new='                <h3>Confini chiari</h3>\n                <p>Ogni applicazione ha uno scopo specifico. Costruiamo strumenti con uno scopo volutamente ristretto che fanno bene una cosa.</p>',
            label="it:principles:boundaries",
        ),
    )

    add(
        "nl/principles.html",
        Replacement(
            old='                <h3>Geen abonnementen</h3>\n                <p>We rekenen voor applicaties wanneer dat gepast is, maar we vergrendelen functies niet achter terugkerende betalingen. Als je iets koopt, bezit je het.</p>',
            new='                <h3>Eerlijk geprijsd als product</h3>\n                <p>Als een applicatie geld kost, prijzen we die als een product. Als je iets koopt, bezit je het.</p>',
            label="nl:principles:pricing",
        ),
        Replacement(
            old='                <h3>Geen dark patterns</h3>\n                <p>Elke interactie is ontworpen om duidelijk en eerlijk te zijn. We manipuleren gebruikers niet naar beslissingen die ze niet willen nemen.</p>',
            new='                <h3>Eerlijke interfaces</h3>\n                <p>Elke interactie is ontworpen om duidelijk en eerlijk te zijn. Mensen moeten begrijpen wat er gebeurt en waarom.</p>',
            label="nl:principles:ux",
        ),
        Replacement(
            old='                <h3>Geen dataverzameling</h3>\n                <p>We verzamelen geen gebruikersgegevens voor profilering of doorverkoop. Als gegevens moeten worden opgeslagen, zijn we expliciet over wat, waarom en voor hoe lang.</p>',
            new='                <h3>Dataminimalisatie</h3>\n                <p>We minimaliseren dataverzameling en houden het doelgericht. Als gegevens moeten worden opgeslagen, zijn we expliciet over wat, waarom en voor hoe lang.</p>',
            label="nl:principles:data",
        ),
        Replacement(
            old='                <h3>Transparante monetisatie</h3>\n                <p>Als een applicatie geld kost, zijn we daar direct over. Geen verborgen kosten, geen verrassingskosten, geen op advertenties gebaseerde bedrijfsmodellen.</p>',
            new='                <h3>Transparante monetisatie</h3>\n                <p>Als een applicatie geld kost, zijn we daar direct over: duidelijke prijzen, voorspelbare kosten en een productgericht model.</p>',
            label="nl:principles:monetization",
        ),
        Replacement(
            old='                <h3>AI alleen waar nuttig</h3>\n                <p>We gebruiken AI waar het duidelijke, begrijpelijke waarde biedt. We gebruiken het niet om functionaliteit te verdoezelen of echt begrip te vervangen door benadering.</p>',
            new='                <h3>AI alleen waar nuttig</h3>\n                <p>We gebruiken AI om duidelijke, begrijpelijke waarde te leveren. Functionaliteit blijft transparant en de gebruiker houdt de controle.</p>',
            label="nl:principles:ai",
        ),
        Replacement(
            old='                <h3>Standaard terughoudend</h3>\n                <p>Applicaties moeten kalm en gericht zijn. Geen onnodige meldingen, geen gamificatie voor betrokkenheid, geen functies ontworpen om afhankelijkheid te creëren.</p>',
            new='                <h3>Standaard terughoudend</h3>\n                <p>Applicaties moeten kalm en gericht zijn. Meldingen worden spaarzaam gebruikt, en functies ondersteunen doelen in plaats van afhankelijkheid te creëren.</p>',
            label="nl:principles:restrained",
        ),
        Replacement(
            old='                <h3>Duidelijke grenzen</h3>\n                <p>Elke applicatie heeft een specifiek doel. We bouwen geen platforms die eindeloos uitbreiden. We bouwen hulpmiddelen die één ding goed doen.</p>',
            new='                <h3>Duidelijke grenzen</h3>\n                <p>Elke applicatie heeft een specifiek doel. We bouwen hulpmiddelen met een bewust strakke scope die één ding goed doen.</p>',
            label="nl:principles:boundaries",
        ),
    )

    # Apply changes
    any_changed = False
    for path, repls in targets.items():
        if not path.exists():
            print(f"[WARN] Missing: {path.relative_to(ROOT)}")
            continue

        original = path.read_text(encoding="utf-8")
        updated, changed = apply_replacements(original, repls, file_label=str(path))

        if not changed:
            print(f"[OK]   {path.relative_to(ROOT)} (no changes)")
            continue

        any_changed = True
        print(f"[EDIT] {path.relative_to(ROOT)} -> {', '.join(changed)}")

        if not args.check:
            path.write_text(updated, encoding="utf-8")

    if args.check:
        return 0

    if not any_changed:
        print("No changes applied.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
