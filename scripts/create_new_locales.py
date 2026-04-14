#!/usr/bin/env python3
"""
Script to generate PL, PT-BR, and PT-PT locale directories for the
Jetzt & Dahanna Technologies website.

Run from the project root:
  python3 scripts/create_new_locales.py
"""

import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# All existing locale codes (for the lang-switch selects)
# ---------------------------------------------------------------------------
ALL_LOCALES_BASE = ["de", "en", "fr", "es", "it", "nl", "sv", "pl", "pt-br", "pt-pt"]

# Display labels in the <select>
LOCALE_LABELS = {
    "de": "DE", "en": "EN", "fr": "FR", "es": "ES",
    "it": "IT", "nl": "NL", "sv": "SV",
    "pl": "PL", "pt-br": "PT-BR", "pt-pt": "PT-PT",
}

# Folder name on disk (pt-br → pt-br)
LOCALE_DIRS = {lc: lc for lc in ALL_LOCALES_BASE}

# ---------------------------------------------------------------------------
# Translations for the three new locales
# ---------------------------------------------------------------------------

TRANSLATIONS = {
    "pl": {
        "lang_attr": "pl",
        "skip_link": "Przejdź do treści",
        "lang_switch_aria": "Wybierz język",
        "nav": {
            "home": "Strona główna",
            "about": "O nas",
            "projects": "Projekty",
            "principles": "Zasady",
            "contact": "Kontakt",
        },
        "footer_imprint": "Informacje prawne",
        "footer_privacy": "Polityka prywatności",
        # index.html
        "index": {
            "meta_desc": "Tworzymy skupione, praktyczne aplikacje wykorzystujące sztuczną inteligencję. Dobra AI oznacza pragmatyczność, powściągliwość i użyteczność.",
            "h1": "Tworzenie użytecznych aplikacji z AI",
            "lead": "Budujemy spokojne, skupione produkty do nauki i pracy. Używamy AI tam, gdzie wnosi wyraźną wartość — i utrzymujemy proste, zrozumiałe doświadczenie pod kontrolą użytkownika.",
            "h2_good_ai": "Dobra AI",
            "p_good_ai_1": "Wierzymy, że AI jest narzędziem, a nie rozwiązaniem każdego problemu. Dobra AI oznacza używanie jej z rozsądkiem i powściągliwością. Oznacza budowanie aplikacji, które pozostają zrozumiałe i pozwalają użytkownikom zachować kontrolę.",
            "p_good_ai_2": "Skupiamy się na problemach, gdzie AI rzeczywiście pomaga, i utrzymujemy wynik prosty, zrozumiały i pod kontrolą użytkownika.",
            "h2_current": "Aktualny projekt",
            "loern_desc": "Fiszki offline: twórz własne karty, organizuj talie i ucz się dzięki aktywnemu przypominaniu — bez konta, bez chmury. Importuj treści, w tym karty wygenerowane przez własną AI.",
            "loern_aria_badges": "Pobierz Lœrn",
            "loern_learn_more": "Dowiedz się więcej o Lœrn",
            "h2_how": "Jak pracujemy",
            "p_how_1": "Budujemy aplikacje jako produkty, nie usługi. Skupiamy się na tworzeniu, udostępnianiu i ulepszaniu własnych narzędzi — każde z nich odzwierciedla nasze podejście do przemyślanej, powściągliwej technologii.",
            "p_how_2": "Przeczytaj nasze zasady",
        },
        # about.html
        "about": {
            "meta_desc": "Mała, niezależna firma tworząca skupione aplikacje z przemyślanym wykorzystaniem AI.",
            "title_prefix": "O nas",
            "h1": "O nas",
            "h2_perspective": "Perspektywa",
            "p_persp_1": "Jetzt &amp; Dahanna Technologies to mała, niezależna firma. Budujemy aplikacje, nie usługi. Każdy produkt odzwierciedla decyzję o tym, jak powinna działać technologia.",
            "p_persp_2": "Wierzymy, że dobre oprogramowanie szanuje użytkowników. Oznacza to brak ciemnych wzorców, pułapek subskrypcyjnych i zbierania danych. Oznacza jasność co do tego, co robi narzędzie, i pozostawienie ludziom kontroli.",
            "h2_expect": "Czego oczekiwać",
            "p_expect_1": "<strong>Produkt na pierwszym miejscu:</strong> budujemy i utrzymujemy własne aplikacje (brak pracy dla klientów).",
            "p_expect_2": "<strong>Spokój jako standard:</strong> wyraźne granice, minimalne powiadomienia, brak ciemnych wzorców.",
            "p_expect_3": "<strong>Prywatność przede wszystkim:</strong> minimalizacja danych i przejrzysta monetyzacja.",
            "h2_build": "Jak budujemy",
            "p_build_1": "Skupiamy się na jednym projekcie na raz. Budujemy własne produkty zamiast przyjmować zlecenia od klientów. Dzięki temu możemy podejmować decyzje oparte na tym, co ma sens, a nie co się sprzedaje.",
            "p_build_2": "Nasz model biznesowy stawia produkt na pierwszym miejscu. Wyceniamy przejrzyście, gdy jest to odpowiednie, i możemy używać reklam do wspierania bezpłatnych funkcji, ale nie sprzedajemy danych użytkowników.",
            "h2_what": "Co budujemy",
            "p_what": "Budujemy małe, skupione aplikacje z wyraźnymi granicami — narzędzia pomagające ludziom uczyć się, pracować i podejmować decyzje z AI w praktyczny sposób. Tworzymy produkty, rozwijamy je iteracyjnie i utrzymujemy wąski zakres.",
        },
        # principles.html
        "principles": {
            "meta_desc": "Zasady, które kierują sposobem budowania aplikacji.",
            "title_prefix": "Zasady",
            "h1": "Zasady",
            "lead": "Te zasady kierują sposobem budowania aplikacji. To nie są aspiracje. To decyzje odzwierciedlone w każdym produkcie, który tworzymy.",
            "items": [
                ("Ceny oparte na własności", "Gdy aplikacja kosztuje pieniądze, wyceniamy ją tak, by przypominało to kupowanie produktu. Jeśli coś kupujesz, posiadasz to."),
                ("Uczciwe interfejsy", "Każda interakcja jest zaprojektowana tak, by być przejrzysta i uczciwa. Ludzie powinni rozumieć, co się dzieje i dlaczego."),
                ("Minimalizacja danych", "Minimalizujemy zbieranie danych i utrzymujemy je celowe. Jeśli dane muszą być przechowywane, jesteśmy przejrzyści co do tego, co, dlaczego i jak długo."),
                ("Przejrzysta monetyzacja", "Jeśli aplikacja kosztuje pieniądze, mówimy o tym wprost: jasne ceny, przewidywalne koszty i model stawiający produkt na pierwszym miejscu."),
                ("Użytkownik zachowuje kontrolę", "Funkcje są zaprojektowane tak, by wspierać cele użytkownika, a nie tworzyć wskaźniki zaangażowania. Ludzie powinni zachować kontrolę nad swoim doświadczeniem i danymi."),
                ("AI tylko tam, gdzie jest użyteczna", "Używamy AI, by dodać wyraźną, zrozumiałą wartość. Funkcjonalność pozostaje przejrzysta, a użytkownik zachowuje kontrolę."),
                ("Powściągliwość jako standard", "Aplikacje powinny być spokojne i skupione. Powiadomienia są używane oszczędnie, a funkcje zaprojektowane tak, by wspierać cele, a nie tworzyć zależność."),
                ("Wyraźne granice", "Każda aplikacja ma określony cel. Budujemy narzędzia o wąskim zakresie, które robią jedną rzecz dobrze."),
            ],
        },
        # contact.html
        "contact": {
            "meta_desc": "Skontaktuj się z Jetzt & Dahanna Technologies.",
            "title_prefix": "Kontakt",
            "h1": "Kontakt",
            "p_intro": "W sprawie pytań, opinii lub zapytań dotyczących naszych aplikacji:",
            "h2_note": "Uwaga",
            "p_note": "Nie oferujemy niestandardowego tworzenia oprogramowania, usług doradczych ani pracy dla klientów. Budujemy skupione aplikacje jako produkty.",
        },
        # projects.html
        "projects": {
            "meta_desc": "Aplikacje, które tworzymy z przemyślanym wykorzystaniem AI.",
            "title_prefix": "Projekty",
            "h1": "Projekty",
            "loern_desc": "Fiszki offline: twórz własne karty, organizuj talie i ucz się dzięki aktywnemu przypominaniu — bez konta, bez chmury. Importuj treści, w tym karty wygenerowane przez własną AI.",
            "loern_aria_badges": "Pobierz Lœrn",
            "loern_offline": "Działa offline. Bez konta. Twoje dane do nauki pozostają na Twoim urządzeniu.",
            "loern_more": "Więcej o Lœrn",
        },
        # legal/imprint.html
        "imprint": {
            "meta_desc": "Informacje prawne.",
            "title_prefix": "Informacje prawne",
            "h1": "Informacje prawne",
            "h2_info": "Informacje zgodnie z § 5 TMG",
            "h2_contact": "Kontakt",
            "h2_vat": "Numer identyfikacji VAT",
            "p_vat": "Numer identyfikacji podatkowej VAT zgodnie z § 27a UStG:<br>\n            DE459368102",
            "h2_responsible": "Odpowiedzialny za treść",
            "p_responsible": "Tobias Blankenhorn (adres jak powyżej)",
        },
        # legal/privacy.html
        "privacy": {
            "meta_desc": "Polityka prywatności dla jetztunddahanna.com.",
            "title_prefix": "Polityka prywatności",
            "h1": "Polityka prywatności",
            "h2_general": "Ogólne",
            "p_general_1": "Niniejsza polityka prywatności dotyczy strony internetowej jetztunddahanna.com.",
            "p_general_2": "Odpowiedzialny za przetwarzanie danych:<br>\n            Tobias Blankenhorn<br>\n            Richard-Wagner-Str. 17/1<br>\n            71116 Gaertringen<br>\n            Niemcy<br>\n            E-mail: <a href=\"mailto:info@jetztunddahanna.com\" class=\"text-link\">info@jetztunddahanna.com</a>",
            "h2_collection": "Zbieranie danych na tej stronie",
            "p_collection_1": "Ta strona to statyczna witryna hostowana na GitHub Pages. Nie zbieramy, nie przechowujemy ani nie przetwarzamy danych osobowych przez tę stronę.",
            "p_collection_2": "Nie używamy plików cookie, narzędzi analitycznych ani żadnych mechanizmów śledzenia.",
            "h2_logs": "Logi serwera",
            "p_logs": "Dostawca hostingu (GitHub) może automatycznie zbierać i przechowywać informacje w logach serwera. Może to obejmować:",
            "log_items": ["Typ i wersja przeglądarki", "System operacyjny", "Adres URL strony odsyłającej", "Nazwa hosta komputera uzyskującego dostęp", "Czas żądania serwera", "Adres IP"],
            "p_logs_2": "Te dane nie są łączone z innymi źródłami danych i są przechowywane przez GitHub zgodnie z jego polityką prywatności.",
            "h2_contact_section": "Kontakt",
            "p_contact": "Jeśli kontaktujesz się z nami przez e-mail, Twoja wiadomość i podane dane (w tym adres e-mail i imię) będą przechowywane w celu przetworzenia zapytania i ewentualnych pytań uzupełniających. Nie udostępniamy tych danych bez Twojej zgody.",
            "h2_rights": "Twoje prawa",
            "p_rights_intro": "Masz prawo do:",
            "rights_items": ["Żądania informacji o przechowywanych danych osobowych", "Żądania poprawienia nieprawidłowych danych", "Żądania usunięcia danych", "Żądania ograniczenia przetwarzania danych", "Sprzeciwu wobec przetwarzania danych", "Żądania przenośności danych"],
            "p_rights_contact": "Aby skorzystać z tych praw, skontaktuj się: <a href=\"mailto:info@jetztunddahanna.com\" class=\"text-link\">info@jetztunddahanna.com</a>",
        },
        # Google Play / App Store badge assets
        "gplay_badge": "GetItOnGooglePlay_Badge_Web_color_Polish.svg",
        "gplay_alt": "Pobierz z Google Play",
        "gplay_aria": "Pobierz z Google Play",
        "appstore_folder": "PL",
        "appstore_file": "Download_on_the_App_Store_Badge_PL_RGB_blk_100317.svg",
        "appstore_alt": "Pobierz z App Store",
        "appstore_aria": "Pobierz z App Store",
    },

    "pt-br": {
        "lang_attr": "pt-BR",
        "skip_link": "Ir para o conteúdo",
        "lang_switch_aria": "Escolher idioma",
        "nav": {
            "home": "Início",
            "about": "Sobre",
            "projects": "Projetos",
            "principles": "Princípios",
            "contact": "Contato",
        },
        "footer_imprint": "Informações legais",
        "footer_privacy": "Privacidade",
        "index": {
            "meta_desc": "Criamos aplicações práticas e focadas usando inteligência artificial. Boa IA significa pragmática, comedida e útil.",
            "h1": "Criamos aplicações úteis com IA",
            "lead": "Desenvolvemos produtos calmos e focados para aprender e trabalhar. Usamos IA onde ela agrega valor real — e mantemos a experiência simples, compreensível e sob controle do usuário.",
            "h2_good_ai": "Boa IA",
            "p_good_ai_1": "Acreditamos que a IA é uma ferramenta, não uma solução para todo problema. Boa IA significa usá-la com critério e comedimento. Significa criar aplicações que permaneçam compreensíveis e mantenham os usuários no controle.",
            "p_good_ai_2": "Focamos em problemas onde a IA realmente ajuda e mantemos o resultado simples, compreensível e sob controle do usuário.",
            "h2_current": "Projeto atual",
            "loern_desc": "Flashcards offline: crie seus próprios cartões, organize decks e estude com recuperação ativa — sem conta, sem nuvem. Importe conteúdo, incluindo cartões gerados com sua própria IA.",
            "loern_aria_badges": "Baixar Lœrn",
            "loern_learn_more": "Saiba mais sobre Lœrn",
            "h2_how": "Como trabalhamos",
            "p_how_1": "Desenvolvemos aplicações como produtos, não serviços. Focamos em lançar e aprimorar nossas próprias ferramentas — cada uma reflete nossa abordagem de tecnologia pensada e comedida.",
            "p_how_2": "Leia nossos princípios",
        },
        "about": {
            "meta_desc": "Uma empresa pequena e independente criando aplicações focadas com uso criterioso de IA.",
            "title_prefix": "Sobre",
            "h1": "Sobre",
            "h2_perspective": "Perspectiva",
            "p_persp_1": "Jetzt &amp; Dahanna Technologies é uma empresa pequena e independente. Desenvolvemos aplicações, não serviços. Cada produto reflete uma decisão sobre como a tecnologia deveria funcionar.",
            "p_persp_2": "Acreditamos que um bom software respeita os usuários. Isso significa sem padrões obscuros, sem armadilhas de assinatura e sem coleta de dados. Significa ser claro sobre o que uma ferramenta faz e deixar as pessoas no controle.",
            "h2_expect": "O que esperar",
            "p_expect_1": "<strong>Produto em primeiro lugar:</strong> desenvolvemos e mantemos nossas próprias aplicações (sem trabalho para clientes).",
            "p_expect_2": "<strong>Calmo por padrão:</strong> limites claros, notificações mínimas, sem padrões obscuros.",
            "p_expect_3": "<strong>Privacidade em primeiro lugar:</strong> minimização de dados e monetização transparente.",
            "h2_build": "Como desenvolvemos",
            "p_build_1": "Focamos em um projeto por vez. Desenvolvemos nossos próprios produtos em vez de aceitar trabalho de clientes. Isso nos permite tomar decisões com base no que faz sentido, não no que vende.",
            "p_build_2": "Nosso modelo de negócios coloca o produto em primeiro lugar. Cobramos de forma transparente quando apropriado e podemos usar publicidade para suportar recursos gratuitos, mas não vendemos dados de usuários.",
            "h2_what": "O que desenvolvemos",
            "p_what": "Desenvolvemos aplicações pequenas e focadas com limites claros — ferramentas que ajudam pessoas a aprender, trabalhar e tomar decisões com IA de forma prática. Lançamos produtos, iteramos e mantemos o escopo restrito.",
        },
        "principles": {
            "meta_desc": "Os princípios que guiam como desenvolvemos aplicações.",
            "title_prefix": "Princípios",
            "h1": "Princípios",
            "lead": "Esses princípios guiam como desenvolvemos aplicações. Não são aspirações. São decisões refletidas em cada produto que criamos.",
            "items": [
                ("Preço baseado em propriedade", "Quando uma aplicação custa dinheiro, precificamos de forma que pareça comprar um produto. Se você compra algo, você o possui."),
                ("Interfaces honestas", "Cada interação é projetada para ser clara e honesta. As pessoas devem entender o que está acontecendo e por quê."),
                ("Minimização de dados", "Minimizamos a coleta de dados e a mantemos orientada a propósitos. Se os dados precisam ser armazenados, somos explícitos sobre o quê, por quê e por quanto tempo."),
                ("Monetização transparente", "Se uma aplicação custa dinheiro, somos diretos sobre isso: preços claros, custos previsíveis e um modelo que coloca o produto em primeiro lugar."),
                ("Usuários mantêm o controle", "Os recursos são projetados para apoiar os objetivos dos usuários, não para criar métricas de engajamento. As pessoas devem permanecer no controle de sua experiência e seus dados."),
                ("IA apenas onde é útil", "Usamos IA para agregar valor claro e compreensível. A funcionalidade permanece transparente e o usuário mantém o controle."),
                ("Comedido por padrão", "As aplicações devem ser calmas e focadas. As notificações são usadas com parcimônia e os recursos são projetados para apoiar objetivos em vez de criar dependência."),
                ("Limites claros", "Cada aplicação tem um propósito específico. Desenvolvemos ferramentas com escopo restrito que fazem uma coisa bem."),
            ],
        },
        "contact": {
            "meta_desc": "Entre em contato com a Jetzt & Dahanna Technologies.",
            "title_prefix": "Contato",
            "h1": "Contato",
            "p_intro": "Para perguntas, feedback ou consultas sobre nossas aplicações:",
            "h2_note": "Observação",
            "p_note": "Não oferecemos desenvolvimento personalizado, serviços de consultoria ou trabalho para clientes. Desenvolvemos aplicações focadas como produtos.",
        },
        "projects": {
            "meta_desc": "Aplicações que desenvolvemos com uso criterioso de IA.",
            "title_prefix": "Projetos",
            "h1": "Projetos",
            "loern_desc": "Flashcards offline: crie seus próprios cartões, organize decks e estude com recuperação ativa — sem conta, sem nuvem. Importe conteúdo, incluindo cartões gerados com sua própria IA.",
            "loern_aria_badges": "Baixar Lœrn",
            "loern_offline": "Offline primeiro. Sem conta. Seus dados de aprendizado ficam no seu dispositivo.",
            "loern_more": "Mais sobre Lœrn",
        },
        "imprint": {
            "meta_desc": "Informações legais.",
            "title_prefix": "Informações legais",
            "h1": "Informações legais",
            "h2_info": "Informações conforme § 5 TMG",
            "h2_contact": "Contato",
            "h2_vat": "Número de identificação de IVA",
            "p_vat": "Número de identificação fiscal de IVA conforme § 27a UStG:<br>\n            DE459368102",
            "h2_responsible": "Responsável pelo conteúdo",
            "p_responsible": "Tobias Blankenhorn (endereço acima)",
        },
        "privacy": {
            "meta_desc": "Política de privacidade para jetztunddahanna.com.",
            "title_prefix": "Política de privacidade",
            "h1": "Política de privacidade",
            "h2_general": "Geral",
            "p_general_1": "Esta política de privacidade se aplica ao site jetztunddahanna.com.",
            "p_general_2": "Responsável pelo tratamento de dados:<br>\n            Tobias Blankenhorn<br>\n            Richard-Wagner-Str. 17/1<br>\n            71116 Gaertringen<br>\n            Alemanha<br>\n            E-mail: <a href=\"mailto:info@jetztunddahanna.com\" class=\"text-link\">info@jetztunddahanna.com</a>",
            "h2_collection": "Coleta de dados neste site",
            "p_collection_1": "Este site é um site estático hospedado no GitHub Pages. Não coletamos, armazenamos nem processamos dados pessoais por este site.",
            "p_collection_2": "Não usamos cookies, ferramentas de análise ou quaisquer mecanismos de rastreamento.",
            "h2_logs": "Arquivos de log do servidor",
            "p_logs": "O provedor de hospedagem (GitHub) pode coletar e armazenar automaticamente informações nos arquivos de log do servidor. Isso pode incluir:",
            "log_items": ["Tipo e versão do navegador", "Sistema operacional", "URL de referência", "Nome do host do computador acessando", "Hora da solicitação do servidor", "Endereço IP"],
            "p_logs_2": "Esses dados não são combinados com outras fontes de dados e são armazenados pelo GitHub de acordo com sua política de privacidade.",
            "h2_contact_section": "Contato",
            "p_contact": "Se você nos contatar por e-mail, sua mensagem e os dados que você fornecer (incluindo endereço de e-mail e nome) serão armazenados para fins de processamento de sua consulta e para possíveis perguntas de acompanhamento. Não compartilhamos esses dados sem o seu consentimento.",
            "h2_rights": "Seus direitos",
            "p_rights_intro": "Você tem o direito de:",
            "rights_items": ["Solicitar informações sobre dados pessoais armazenados", "Solicitar correção de dados incorretos", "Solicitar exclusão de seus dados", "Solicitar restrição do processamento de dados", "Contestar o processamento de dados", "Solicitar portabilidade de dados"],
            "p_rights_contact": "Para exercer esses direitos, entre em contato: <a href=\"mailto:info@jetztunddahanna.com\" class=\"text-link\">info@jetztunddahanna.com</a>",
        },
        "gplay_badge": "GetItOnGooglePlay_Badge_Web_color_Portuguese-Brazil.svg",
        "gplay_alt": "Disponível no Google Play",
        "gplay_aria": "Disponível no Google Play",
        "appstore_folder": "PTBR",
        "appstore_file": "Download_on_the_App_Store_Badge_PTBR_RGB_blk_092917.svg",
        "appstore_alt": "Baixar na App Store",
        "appstore_aria": "Baixar na App Store",
    },

    "pt-pt": {
        "lang_attr": "pt-PT",
        "skip_link": "Ir para o conteúdo",
        "lang_switch_aria": "Escolher idioma",
        "nav": {
            "home": "Início",
            "about": "Sobre",
            "projects": "Projetos",
            "principles": "Princípios",
            "contact": "Contacto",
        },
        "footer_imprint": "Informações legais",
        "footer_privacy": "Privacidade",
        "index": {
            "meta_desc": "Criamos aplicações práticas e focadas usando inteligência artificial. Boa IA significa pragmática, comedida e útil.",
            "h1": "Criar aplicações úteis com IA",
            "lead": "Desenvolvemos produtos calmos e focados para aprender e trabalhar. Usamos IA onde acrescenta valor real — e mantemos a experiência simples, compreensível e sob controlo do utilizador.",
            "h2_good_ai": "Boa IA",
            "p_good_ai_1": "Acreditamos que a IA é uma ferramenta, não uma solução para todos os problemas. Boa IA significa utilizá-la com discernimento e comedimento. Significa criar aplicações que permaneçam compreensíveis e mantenham os utilizadores no controlo.",
            "p_good_ai_2": "Focamo-nos em problemas onde a IA realmente ajuda e mantemos o resultado simples, compreensível e sob controlo do utilizador.",
            "h2_current": "Projeto atual",
            "loern_desc": "Flashcards offline: crie os seus próprios cartões, organize baralhos e estude com recuperação ativa — sem conta, sem nuvem. Importe conteúdo, incluindo cartões gerados com a sua própria IA.",
            "loern_aria_badges": "Transferir Lœrn",
            "loern_learn_more": "Saiba mais sobre Lœrn",
            "h2_how": "Como trabalhamos",
            "p_how_1": "Desenvolvemos aplicações como produtos, não serviços. Focamo-nos em lançar e melhorar as nossas próprias ferramentas — cada uma reflete a nossa abordagem de tecnologia pensada e comedida.",
            "p_how_2": "Leia os nossos princípios",
        },
        "about": {
            "meta_desc": "Uma empresa pequena e independente que cria aplicações focadas com uso criterioso de IA.",
            "title_prefix": "Sobre",
            "h1": "Sobre",
            "h2_perspective": "Perspetiva",
            "p_persp_1": "Jetzt &amp; Dahanna Technologies é uma empresa pequena e independente. Desenvolvemos aplicações, não serviços. Cada produto reflete uma decisão sobre como a tecnologia deveria funcionar.",
            "p_persp_2": "Acreditamos que um bom software respeita os utilizadores. Isto significa ausência de padrões obscuros, de armadilhas de subscrição e de recolha de dados. Significa ser claro sobre o que uma ferramenta faz e deixar as pessoas no controlo.",
            "h2_expect": "O que esperar",
            "p_expect_1": "<strong>Produto em primeiro lugar:</strong> desenvolvemos e mantemos as nossas próprias aplicações (sem trabalho para clientes).",
            "p_expect_2": "<strong>Calmo por defeito:</strong> limites claros, notificações mínimas, sem padrões obscuros.",
            "p_expect_3": "<strong>Privacidade em primeiro lugar:</strong> minimização de dados e monetização transparente.",
            "h2_build": "Como desenvolvemos",
            "p_build_1": "Focamo-nos num projeto de cada vez. Desenvolvemos os nossos próprios produtos em vez de aceitar trabalho de clientes. Isso permite-nos tomar decisões com base no que faz sentido, não no que vende.",
            "p_build_2": "O nosso modelo de negócio coloca o produto em primeiro lugar. Cobramos de forma transparente quando apropriado e podemos usar publicidade para suportar funcionalidades gratuitas, mas não vendemos dados de utilizadores.",
            "h2_what": "O que desenvolvemos",
            "p_what": "Desenvolvemos aplicações pequenas e focadas com limites claros — ferramentas que ajudam as pessoas a aprender, trabalhar e tomar decisões com IA de forma prática. Lançamos produtos, iteramos e mantemos o âmbito restrito.",
        },
        "principles": {
            "meta_desc": "Os princípios que guiam a forma como desenvolvemos aplicações.",
            "title_prefix": "Princípios",
            "h1": "Princípios",
            "lead": "Estes princípios guiam a forma como desenvolvemos aplicações. Não são aspirações. São decisões refletidas em cada produto que criamos.",
            "items": [
                ("Preço baseado em propriedade", "Quando uma aplicação custa dinheiro, estabelecemos um preço de forma que pareça comprar um produto. Se compra algo, possui-o."),
                ("Interfaces honestas", "Cada interação é projetada para ser clara e honesta. As pessoas devem compreender o que está a acontecer e porquê."),
                ("Minimização de dados", "Minimizamos a recolha de dados e mantemo-la orientada para fins. Se os dados precisam de ser armazenados, somos explícitos sobre o quê, porquê e por quanto tempo."),
                ("Monetização transparente", "Se uma aplicação custa dinheiro, somos diretos sobre isso: preços claros, custos previsíveis e um modelo que coloca o produto em primeiro lugar."),
                ("Utilizadores mantêm o controlo", "As funcionalidades são projetadas para apoiar os objetivos dos utilizadores, não para criar métricas de envolvimento. As pessoas devem permanecer no controlo da sua experiência e dos seus dados."),
                ("IA apenas onde é útil", "Usamos IA para acrescentar valor claro e compreensível. A funcionalidade permanece transparente e o utilizador mantém o controlo."),
                ("Comedido por defeito", "As aplicações devem ser calmas e focadas. As notificações são usadas com parcimónia e as funcionalidades são projetadas para apoiar objetivos em vez de criar dependência."),
                ("Limites claros", "Cada aplicação tem um propósito específico. Desenvolvemos ferramentas com âmbito restrito que fazem uma coisa bem."),
            ],
        },
        "contact": {
            "meta_desc": "Entre em contacto com a Jetzt & Dahanna Technologies.",
            "title_prefix": "Contacto",
            "h1": "Contacto",
            "p_intro": "Para perguntas, feedback ou consultas sobre as nossas aplicações:",
            "h2_note": "Nota",
            "p_note": "Não oferecemos desenvolvimento personalizado, serviços de consultoria ou trabalho para clientes. Desenvolvemos aplicações focadas como produtos.",
        },
        "projects": {
            "meta_desc": "Aplicações que desenvolvemos com uso criterioso de IA.",
            "title_prefix": "Projetos",
            "h1": "Projetos",
            "loern_desc": "Flashcards offline: crie os seus próprios cartões, organize baralhos e estude com recuperação ativa — sem conta, sem nuvem. Importe conteúdo, incluindo cartões gerados com a sua própria IA.",
            "loern_aria_badges": "Transferir Lœrn",
            "loern_offline": "Offline em primeiro lugar. Sem conta. Os seus dados de aprendizagem ficam no seu dispositivo.",
            "loern_more": "Mais sobre Lœrn",
        },
        "imprint": {
            "meta_desc": "Informações legais.",
            "title_prefix": "Informações legais",
            "h1": "Informações legais",
            "h2_info": "Informações conforme § 5 TMG",
            "h2_contact": "Contacto",
            "h2_vat": "Número de identificação de IVA",
            "p_vat": "Número de identificação fiscal de IVA conforme § 27a UStG:<br>\n            DE459368102",
            "h2_responsible": "Responsável pelo conteúdo",
            "p_responsible": "Tobias Blankenhorn (morada acima)",
        },
        "privacy": {
            "meta_desc": "Política de privacidade para jetztunddahanna.com.",
            "title_prefix": "Política de privacidade",
            "h1": "Política de privacidade",
            "h2_general": "Geral",
            "p_general_1": "Esta política de privacidade aplica-se ao site jetztunddahanna.com.",
            "p_general_2": "Responsável pelo tratamento de dados:<br>\n            Tobias Blankenhorn<br>\n            Richard-Wagner-Str. 17/1<br>\n            71116 Gaertringen<br>\n            Alemanha<br>\n            E-mail: <a href=\"mailto:info@jetztunddahanna.com\" class=\"text-link\">info@jetztunddahanna.com</a>",
            "h2_collection": "Recolha de dados neste site",
            "p_collection_1": "Este site é um site estático alojado no GitHub Pages. Não recolhemos, armazenamos nem processamos dados pessoais através deste site.",
            "p_collection_2": "Não utilizamos cookies, ferramentas de análise ou quaisquer mecanismos de rastreamento.",
            "h2_logs": "Ficheiros de registo do servidor",
            "p_logs": "O fornecedor de alojamento (GitHub) pode recolher e armazenar automaticamente informações nos ficheiros de registo do servidor. Isto pode incluir:",
            "log_items": ["Tipo e versão do navegador", "Sistema operativo", "URL de referência", "Nome do anfitrião do computador a aceder", "Hora do pedido ao servidor", "Endereço IP"],
            "p_logs_2": "Estes dados não são combinados com outras fontes de dados e são armazenados pelo GitHub de acordo com a sua política de privacidade.",
            "h2_contact_section": "Contacto",
            "p_contact": "Se nos contactar por e-mail, a sua mensagem e os dados que fornecer (incluindo endereço de e-mail e nome) serão armazenados para fins de processamento do seu pedido e para possíveis perguntas de acompanhamento. Não partilhamos estes dados sem o seu consentimento.",
            "h2_rights": "Os seus direitos",
            "p_rights_intro": "Tem o direito de:",
            "rights_items": ["Solicitar informações sobre dados pessoais armazenados", "Solicitar correção de dados incorretos", "Solicitar eliminação dos seus dados", "Solicitar restrição do tratamento de dados", "Opor-se ao tratamento de dados", "Solicitar portabilidade de dados"],
            "p_rights_contact": "Para exercer estes direitos, contacte: <a href=\"mailto:info@jetztunddahanna.com\" class=\"text-link\">info@jetztunddahanna.com</a>",
        },
        "gplay_badge": "GetItOnGooglePlay_Badge_Web_color_Portuguese-Portugal.svg",
        "gplay_alt": "Disponível no Google Play",
        "gplay_aria": "Disponível no Google Play",
        "appstore_folder": "PTPT",
        "appstore_file": "Download_on_the_App_Store_Badge_PTPT_RGB_blk_100317.svg",
        "appstore_alt": "Transferir na App Store",
        "appstore_aria": "Transferir na App Store",
    },
}

NEW_LOCALES = ["pl", "pt-br", "pt-pt"]


LOERN_PAGE_TRANSLATIONS = {
    "pl": {
        "meta_desc": "Aplikacja do fiszek offline: twórz i ucz się własnych treści — bez konta, bez chmury.",
        "pill": "Dostępna na Androida i iOS",
        "lead": "Aplikacja do fiszek offline: twórz i ucz się własnych treści — bez konta, bez chmury.",
        "privacy_link": "Oświadczenie o prywatności",
        "no_cloud": "Bez chmury. Bez zbierania danych. Bez kont. Twoje dane pozostają na urządzeniu, chyba że je wyeksportujesz lub udostępnisz.",
        "what_h2": "Czym jest",
        "what_p1": "Lœrn to aplikacja do fiszek, która pozwala tworzyć i uczyć się własnych treści — całkowicie offline i bez konta w chmurze. Twórz talie do szkoły, na studia, do nauki języków lub przygotowań do egzaminów i ucz się w elastycznych sesjach z aktywnym przypominaniem.",
        "what_p2": "Ty decydujesz, czego i jak się uczysz.",
        "what_p2_tail": "Twoje dane pozostają na Twoim urządzeniu.",
        "why_h2": "Dlaczego to działa",
        "why_1_h3": "Do codziennej nauki",
        "why_1_p": "Twórz talie na dowolny temat — do egzaminów, podróży albo nawet do rozwijania swojego hobby.",
        "why_2_h3": "Dla uczniów i studentów",
        "why_2_p": "Szybko twórz talie na podstawie notatek przez import, ucz się skutecznie dzięki aktywnemu przypominaniu i śledź postępy na urządzeniu. Eksportuj talie, aby udostępniać je znajomym.",
        "why_3_h3": "Dla nauczycieli",
        "why_3_p": "Porządkuj materiały w uporządkowanych taliach i udostępniaj je uczniom przez eksport — to dobry sposób na skuteczne i motywujące sesje nauki.",
        "features_h2": "Funkcje",
        "feature_1_h3": "Tworzenie fiszek i organizacja talii",
        "feature_1_p": "Uporządkowane talie do wszystkiego, czego się uczysz — łatwe do zbudowania i utrzymania.",
        "feature_2_h3": "Aktywne przypominanie i samosprawdzanie",
        "feature_2_p": "Tryby nauki zaprojektowane z myślą o przypominaniu, rozumieniu i powtórkach.",
        "feature_3_h3": "Nauka offline — bez konta",
        "feature_3_p": "Bez logowania i bez chmury: Twoje treści pozostają na urządzeniu.",
        "feature_4_h3": "Import i eksport",
        "feature_4_p": "Importuj treści z tekstu, notatek lub innych źródeł; eksportuj je na potrzeby kopii zapasowych albo udostępniania.",
        "feature_5_h3": "Elastyczne sesje nauki",
        "feature_5_p": "Krótkie powtórki lub dłuższe sesje — Ty wybierasz tempo i zakres.",
        "feature_6_h3": "Korzystaj z własnej AI",
        "feature_6_p": "Brak wbudowanej płatnej AI: generuj karty w dowolnym narzędziu AI i importuj je do Lœrn.",
        "screenshots_h2": "Zrzuty ekranu",
        "screenshots_p": "Zrzuty ekranu z aktualnej wersji na Androida.",
    },
    "pt-br": {
        "meta_desc": "App de flashcards offline: crie e estude seu próprio conteúdo — sem conta, sem nuvem.",
        "pill": "Disponível para Android e iOS",
        "lead": "Um app de flashcards offline: crie e estude seu próprio conteúdo — sem conta, sem nuvem.",
        "privacy_link": "Política de privacidade",
        "no_cloud": "Sem nuvem. Sem coleta de dados. Sem contas. Seus dados ficam no dispositivo, a menos que você exporte ou compartilhe.",
        "what_h2": "O que é",
        "what_p1": "Lœrn é um app de flashcards para criar e estudar seu próprio conteúdo — totalmente offline e sem conta na nuvem. Monte decks para escola, faculdade, idiomas ou preparação para provas e estude em sessões flexíveis com recuperação ativa.",
        "what_p2": "Você decide o que aprender e como aprender.",
        "what_p2_tail": "Seus dados ficam no seu dispositivo.",
        "why_h2": "Por que é útil",
        "why_1_h3": "Para o aprendizado do dia a dia",
        "why_1_p": "Crie decks sobre qualquer assunto que importe para você — preparação para provas, viagens ou até para evoluir em um hobby.",
        "why_2_h3": "Para estudantes",
        "why_2_p": "Crie decks rapidamente a partir das suas anotações por importação, estude com recuperação ativa e acompanhe seu progresso no dispositivo. Exporte decks para compartilhar com amigos.",
        "why_3_h3": "Para professores",
        "why_3_p": "Organize seu material em decks estruturados e compartilhe com seus alunos por exportação — ótimo para sessões de aprendizagem eficazes e motivadoras.",
        "features_h2": "Recursos",
        "feature_1_h3": "Criar flashcards e organizar decks",
        "feature_1_p": "Decks estruturados para tudo o que você está aprendendo — fáceis de montar e manter.",
        "feature_2_h3": "Recuperação ativa e autoavaliação",
        "feature_2_p": "Modos de estudo pensados para lembrança, compreensão e repetição.",
        "feature_3_h3": "Aprendizado offline — sem conta",
        "feature_3_p": "Sem login e sem nuvem: seu conteúdo fica no seu dispositivo.",
        "feature_4_h3": "Importação e exportação",
        "feature_4_p": "Traga conteúdo de texto, anotações ou fontes externas; exporte para backup ou compartilhamento.",
        "feature_5_h3": "Sessões de estudo flexíveis",
        "feature_5_p": "Revisões rápidas ou sessões mais longas — você escolhe o ritmo e o escopo.",
        "feature_6_h3": "Use sua própria IA",
        "feature_6_p": "Sem IA paga embutida: gere cartões com a ferramenta de IA que preferir e importe para o Lœrn.",
        "screenshots_h2": "Capturas de tela",
        "screenshots_p": "Capturas de tela da versão atual para Android.",
    },
    "pt-pt": {
        "meta_desc": "Aplicação de flashcards offline: crie e estude o seu próprio conteúdo — sem conta, sem nuvem.",
        "pill": "Disponível para Android e iOS",
        "lead": "Uma aplicação de flashcards offline: crie e estude o seu próprio conteúdo — sem conta, sem nuvem.",
        "privacy_link": "Política de privacidade",
        "no_cloud": "Sem nuvem. Sem recolha de dados. Sem contas. Os seus dados ficam no dispositivo, a menos que os exporte ou partilhe.",
        "what_h2": "O que é",
        "what_p1": "Lœrn é uma aplicação de flashcards para criar e estudar o seu próprio conteúdo — totalmente offline e sem conta na nuvem. Crie baralhos para a escola, universidade, idiomas ou preparação para exames e estude em sessões flexíveis com recuperação ativa.",
        "what_p2": "Decide o que aprender e como aprender.",
        "what_p2_tail": "Os seus dados ficam no seu dispositivo.",
        "why_h2": "Porque é útil",
        "why_1_h3": "Para a aprendizagem do dia a dia",
        "why_1_p": "Crie baralhos sobre qualquer tema que lhe interesse — preparação para exames, viagens ou até para desenvolver um hobby.",
        "why_2_h3": "Para estudantes",
        "why_2_p": "Crie baralhos rapidamente a partir das suas notas por importação, estude com recuperação ativa e acompanhe o seu progresso no dispositivo. Exporte baralhos para os partilhar com amigos.",
        "why_3_h3": "Para professores",
        "why_3_p": "Organize o seu material em baralhos estruturados e partilhe-os com os alunos por exportação — ótimo para sessões de aprendizagem eficazes e motivadoras.",
        "features_h2": "Funcionalidades",
        "feature_1_h3": "Criar flashcards e organizar baralhos",
        "feature_1_p": "Baralhos estruturados para tudo o que está a aprender — fáceis de criar e manter.",
        "feature_2_h3": "Recuperação ativa e autoavaliação",
        "feature_2_p": "Modos de estudo pensados para recordar, compreender e repetir.",
        "feature_3_h3": "Aprendizagem offline — sem conta",
        "feature_3_p": "Sem login e sem nuvem: o seu conteúdo fica no seu dispositivo.",
        "feature_4_h3": "Importação e exportação",
        "feature_4_p": "Traga conteúdo de texto, notas ou fontes externas; exporte para cópias de segurança ou partilha.",
        "feature_5_h3": "Sessões de estudo flexíveis",
        "feature_5_p": "Revisões rápidas ou sessões mais longas — escolhe o ritmo e o âmbito.",
        "feature_6_h3": "Use a sua própria IA",
        "feature_6_p": "Sem IA paga integrada: gere cartões com a ferramenta de IA que preferir e importe-os para o Lœrn.",
        "screenshots_h2": "Capturas de ecrã",
        "screenshots_p": "Capturas de ecrã da versão atual para Android.",
    },
}


LOERN_PRIVACY_TRANSLATIONS = {
    "pl": {
        "title": "Oświadczenie o prywatności",
        "meta_desc": "Oświadczenie o prywatności dla aplikacji Lœrn.",
        "h1": "Oświadczenie o prywatności dla aplikacji Lœrn",
        "updated": "Ostatnia aktualizacja: 5 lutego 2026",
        "sections": {
            "intro": ("Wprowadzenie", [
                "To oświadczenie o prywatności wyjaśnia, w jaki sposób Lœrn (\"my\", \"nas\" lub \"aplikacja\") obchodzi się z informacjami. Lœrn został zaprojektowany z myślą o prywatności jako podstawowej zasadzie. Wierzymy, że Twoje dane dotyczące nauki powinny zawsze pozostawać pod Twoją kontrolą.",
                "Poza sytuacjami, w których wyraźnie zdecydujesz się wyeksportować lub udostępnić treści, Lœrn nie przesyła Twoich danych poza urządzenie.",
            ]),
            "core": ("Podstawowe zasady prywatności", "Prywatność przede wszystkim", "Lœrn został stworzony od podstaw tak, aby chronić Twoją prywatność:", [
                "<strong>Priorytet dla działania offline:</strong> podstawowe funkcje nauki działają bez połączenia z internetem",
                "<strong>Brak kont użytkownika:</strong> brak rejestracji, logowania i haseł",
                "<strong>Brak śledzenia:</strong> brak analityki zachowań i profilowania",
                "<strong>Dane przechowywane wyłącznie lokalnie:</strong> dane dotyczące nauki pozostają na urządzeniu, chyba że wyraźnie zdecydujesz się je wyeksportować lub udostępnić",
                "<strong>Kontrola użytkownika:</strong> dane opuszczają urządzenie tylko wtedy, gdy świadomie zainicjujesz taką czynność",
            ]),
            "not_collect": ("Dane, których nie zbieramy", "NIE zbieramy, nie przechowujemy ani nie przesyłamy:", [
                "Danych osobowych (imię i nazwisko, adres e-mail, numer telefonu, adres)",
                "Kont użytkownika ani danych uwierzytelniających",
                "Treści do nauki ani materiałów, które tworzysz lub importujesz",
                "Postępów w nauce, wyników ani statystyk",
                "Danych analitycznych ani telemetrycznych",
                "Raportów o awariach ani danych diagnostycznych",
                "Danych lokalizacyjnych",
                "List kontaktów ani powiązań społecznościowych",
            ], "W wersji darmowej partnerzy reklamowi mogą otrzymywać ograniczone dane techniczne potrzebne do wyświetlania reklam (zobacz sekcję dotyczącą reklam)."),
            "storage": ("Przechowywanie danych", "Wyłącznie lokalnie", "Wszystkie dane związane z nauką są przechowywane wyłącznie na Twoim urządzeniu:", [
                "Talie i fiszki",
                "Postępy w nauce i statystyki",
                "Historia powtórek i dane dotyczące powtórek interwałowych",
                "Preferencje i ustawienia użytkownika",
                "Lokalne informacje o profilu (nazwa profilu, ikona, preferowany język)",
            ], "Dane te są przechowywane w lokalnej bazie SQLite w prywatnej pamięci aplikacji i chronione przez mechanizmy bezpieczeństwa urządzenia (iOS Data Protection, Android Keystore).", "Brak synchronizacji z chmurą", "Lœrn nie oferuje synchronizacji z chmurą, kopii zapasowych w chmurze ani przechowywania danych po stronie serwera. Nie prowadzimy serwerów, które odbierają lub przechowują Twoje dane dotyczące nauki."),
            "internet": ("Łączność z internetem", "Podstawowe funkcje nauki offline", "Podstawowe funkcje Lœrn działają w pełni offline i nie wymagają dostępu do sieci.", "Reklamy (tylko wersja darmowa)", "Jeśli korzystasz z darmowej wersji Lœrn, aplikacja wyświetla reklamy. Tylko moduł reklamowy łączy się z internetem, aby:", [
                "Pobierać treści reklamowe",
                "Raportować wyświetlenia reklam i interakcje",
                "Spełniać wymagania sieci reklamowych",
            ], "Sam mechanizm nauki nie przesyła danych o nauce, treści ani postępów.", "Partnerzy reklamowi", "Darmowa wersja korzysta z Google AdMob. AdMob może zbierać pewne informacje zgodnie ze swoją polityką prywatności, w tym:", [
                "Identyfikator reklamowy urządzenia",
                "Adres IP",
                "Typ urządzenia i system operacyjny",
                "Dane o interakcjach z reklamami",
            ], "Szczegóły dotyczące praktyk Google znajdziesz tutaj:", "Wersja premium", "Jeśli kupisz wersję premium (jednorazowy zakup):", [
                "Wszystkie reklamy zostaną usunięte",
                "Moduł reklamowy nie jest inicjalizowany",
                "Aplikacja nie wymaga dostępu do internetu do zwykłego użytkowania",
                "Aplikacja nie wykonuje żadnej komunikacji sieciowej",
            ]),
            "iap": ("Zakupy w aplikacji", "Obsługa płatności", "Zakupy premium są obsługiwane w całości przez Apple App Store lub Google Play Store.", [
                "Nie zbieramy ani nie przechowujemy danych płatniczych",
                "Nie otrzymujemy danych karty kredytowej ani rozliczeniowych",
                "Otrzymujemy jedynie potwierdzenie, że zakup został zrealizowany",
            ], "Status premium jest przechowywany lokalnie na urządzeniu. Zakup jest powiązany z Twoim kontem App Store lub Play Store, a nie z żadnym kontem Lœrn."),
            "share": ("Import, eksport i udostępnianie", "Lokalny import i eksport plików", "Lœrn pozwala importować i eksportować talie do nauki przy użyciu plików JSON lub ZIP:", [
                "Importowane pliki są przetwarzane lokalnie na urządzeniu",
                "Eksportowane pliki zawierają wyłącznie treści edukacyjne (pytania, odpowiedzi, metadane)",
                "Domyślnie eksportowane pliki nie zawierają danych osobowych",
            ], "Udostępnianie inicjowane przez użytkownika", "Możesz zdecydować się na udostępnienie wyeksportowanych plików przy użyciu standardowych funkcji udostępniania w urządzeniu.", "Ważne wyjaśnienia:", [
                "Dane są udostępniane tylko wtedy, gdy wyraźnie zainicjujesz udostępnianie",
                "Lœrn nie przesyła danych automatycznie",
                "Lœrn nie wie, komu udostępniasz dane",
                "Po udostępnieniu dane są obsługiwane przez aplikację, usługę lub odbiorcę zgodnie z ich własnymi zasadami prywatności",
            ], "Ponosisz pełną odpowiedzialność za to, jak i gdzie udostępniasz wyeksportowane pliki.", "Prawa autorskie i odpowiedzialność za treści", "Lœrn jest narzędziem, a nie dostawcą treści. Odpowiadasz za:", [
                "Upewnienie się, że masz prawo do korzystania z importowanych treści",
                "Przestrzeganie praw autorskich przy udostępnianiu wyeksportowanych talii",
                "Legalność materiałów przechowywanych lub udostępnianych za pomocą aplikacji",
            ]),
            "profiles": ("Profile", "Obsługa wielu profili", "Lœrn obsługuje wiele lokalnych profili użytkowników na jednym urządzeniu:", [
                "Każdy profil ma odseparowane dane dotyczące nauki",
                "Profile są identyfikowane tylko przez wybraną przez Ciebie nazwę i ikonę",
                "Dane profilu są przechowywane lokalnie i nigdy nie są przesyłane przez aplikację",
                "Usunięcie profilu trwale usuwa jego dane z urządzenia",
            ], "Status premium", "Zakup premium dotyczy wszystkich profili na tym samym urządzeniu i koncie sklepu."),
            "notifications": ("Powiadomienia (opcjonalne)", "Przypomnienia o nauce", "Możesz opcjonalnie włączyć przypomnienia o nauce:", [
                "Przypomnienia są planowane lokalnie na urządzeniu",
                "Do dostarczania przypomnień nie są używane żadne zewnętrzne serwery",
                "Możesz wyłączyć przypomnienia w dowolnym momencie",
                "Uprawnienia do powiadomień można cofnąć w ustawieniach urządzenia",
            ]),
            "permissions": ("Uprawnienia", "Aplikacja może prosić o następujące uprawnienia:", "Pamięć (Android)", [
                "<strong>Cel:</strong> import i eksport plików z taliami",
                "<strong>Zakres:</strong> tylko pliki, które wyraźnie wybierzesz",
            ], "Internet (tylko wersja darmowa)", [
                "<strong>Cel:</strong> wyświetlanie reklam",
                "<strong>Nieużywane:</strong> wersja premium",
            ], "Powiadomienia (opcjonalne)", [
                "<strong>Cel:</strong> przypomnienia o nauce",
                "<strong>Kontrola:</strong> samodzielnie wybierasz częstotliwość i porę",
            ]),
            "third_party": ("Usługi zewnętrzne", "Reklamy (tylko wersja darmowa)", "Darmowa wersja korzysta z Google AdMob.", "Nie korzystamy z:", [
                "Usług analitycznych",
                "Usług raportowania awarii",
                "Dostawców chmury",
                "Integracji z mediami społecznościowymi",
                "Zewnętrznych SDK śledzących",
            ]),
            "children": ("Prywatność dzieci", [
                "Lœrn jest przeznaczony dla studentów i starszych uczniów. Nie zbieramy świadomie danych osobowych dzieci poniżej 13. roku życia (lub odpowiedniego wieku w Twojej jurysdykcji).",
                "Ponieważ Lœrn nie zbiera danych osobowych, jest zgodny z przepisami dotyczącymi prywatności dzieci, takimi jak COPPA.",
            ]),
            "security": ("Bezpieczeństwo danych", "Bezpieczeństwo urządzenia", "Twoje dane są chronione przez:", [
                "Szyfrowanie na poziomie urządzenia",
                "Sandbox aplikacji",
                "Mechanizmy uwierzytelniania urządzenia",
            ], "Brak ryzyka po stronie serwera", "Ponieważ Lœrn nie przechowuje danych na serwerach, nie występuje ryzyko:", [
                "Naruszeń bezpieczeństwa serwerów",
                "Wycieków danych z chmury",
                "Nieuprawnionego dostępu stron trzecich",
            ], "Twoja odpowiedzialność", "Odpowiadasz za:", [
                "Zabezpieczenie urządzenia",
                "Zarządzanie kopiami zapasowymi urządzenia (iCloud / Google backup)",
                "Bezpieczne przechowywanie wyeksportowanych plików",
            ]),
            "rights": ("Twoje prawa i kontrola", "Masz pełną kontrolę nad swoimi danymi:", [
                "Wszystkie dane dotyczące nauki są przechowywane lokalnie",
                "Możesz eksportować dane w dowolnym momencie",
                "Możesz usuwać talie lub profile",
                "Odinstalowanie aplikacji usuwa wszystkie dane lokalne",
            ]),
            "retention": ("Przechowywanie danych", "Tylko na urządzeniu", "Dane pozostają na Twoim urządzeniu do momentu, gdy:", [
                "Usuniesz treści lub profile",
                "Wyczyszczysz dane aplikacji",
                "Odinstalujesz aplikację",
            ], "Brak przechowywania na serwerze", "Nie przechowujemy danych na serwerach, ponieważ ich nie prowadzimy.", "Kopie zapasowe urządzenia", "Jeśli ta opcja jest włączona, system operacyjny może tworzyć kopie zapasowe danych aplikacji zgodnie z własnymi zasadami. Zarządzają tym Apple lub Google, a nie Lœrn."),
            "gdpr": ("Podstawa prawna (RODO)", "Dla użytkowników z EOG:", [
                "Nie przetwarzamy danych osobowych jako administrator",
                "Reklamy (wersja darmowa) opierają się na uzasadnionym interesie",
                "Możesz uniknąć reklam, kupując wersję premium",
            ]),
            "ccpa": ("Prawa prywatności w Kalifornii (CCPA)", [
                "Nie sprzedajemy danych osobowych",
                "Nie udostępniamy danych osobowych do celów marketingowych",
                "Większość obowiązków CCPA nie ma zastosowania z uwagi na brak zbierania danych",
            ]),
            "transfers": ("Międzynarodowe przekazywanie danych", "Nie przekazujemy danych dotyczących nauki za granicę, ponieważ:", [
                "Dane są przechowywane lokalnie na urządzeniu",
                "Nie prowadzimy serwerów",
                "Dane opuszczają urządzenie tylko w wyniku działań zainicjowanych przez użytkownika",
            ]),
            "changes": ("Zmiany w tym oświadczeniu", [
                "Możemy aktualizować to oświadczenie, aby odzwierciedlało zmiany w aplikacji lub prawie.",
                "Będziemy informować użytkowników poprzez:",
            ], [
                "Aktualizację daty „Ostatnia aktualizacja”",
                "Opublikowanie zaktualizowanego oświadczenia",
                "Wyświetlenie informacji w aplikacji w przypadku istotnych zmian",
            ]),
            "contact": ("Kontakt", "Jeśli masz pytania dotyczące tego oświadczenia o prywatności:", "Pamiętaj, że nie mamy dostępu do Twoich danych dotyczących nauki, ponieważ są one przechowywane lokalnie na Twoim urządzeniu."),
            "commitment": ("Nasze zobowiązanie do prywatności", "Lœrn powstał z przekonania, że nauka powinna być domyślnie prywatna. Twoje dane pozostają pod Twoją kontrolą, a Ty decydujesz, czy i kiedy je udostępnić."),
            "summary": ("Podsumowanie", [
                "Twoje dane dotyczące nauki pozostają na Twoim urządzeniu",
                "Nie zbieramy danych osobowych",
                "Nie śledzimy, czego ani jak się uczysz",
                "Wersja darmowa wyświetla reklamy (AdMob może zbierać dane związane z reklamami)",
                "Wersja premium nie zawiera reklam i nie wymaga dostępu do sieci",
                "Możesz eksportować i udostępniać dane, jeśli chcesz",
                "Odinstalowanie aplikacji usuwa wszystkie dane lokalne",
            ]),
        },
    },
    "pt-br": {
        "title": "Política de privacidade",
        "meta_desc": "Política de privacidade do aplicativo Lœrn.",
        "h1": "Política de privacidade do app Lœrn",
        "updated": "Última atualização: 5 de fevereiro de 2026",
        "sections": {
            "intro": ("Introdução", [
                "Esta política de privacidade explica como o Lœrn (\"nós\", \"nosso\" ou \"o app\") lida com informações. O Lœrn foi projetado com a privacidade como princípio central. Acreditamos que seus dados de aprendizagem devem permanecer sempre sob seu controle.",
                "Exceto quando você escolhe explicitamente exportar ou compartilhar conteúdo, o Lœrn não transmite seus dados para fora do dispositivo.",
            ]),
            "core": ("Princípios centrais de privacidade", "Privacidade em primeiro lugar", "O Lœrn foi desenvolvido do zero para proteger sua privacidade:", [
                "<strong>Offline-first por design:</strong> os recursos principais de aprendizagem funcionam sem conexão com a internet",
                "<strong>Sem contas de usuário:</strong> sem cadastro, sem login, sem senhas",
                "<strong>Sem rastreamento:</strong> sem analytics comportamental e sem perfilamento",
                "<strong>Armazenamento apenas local:</strong> os dados de aprendizagem ficam no seu dispositivo, a menos que você decida exportar ou compartilhar",
                "<strong>Controle do usuário:</strong> os dados só saem do dispositivo por ações iniciadas intencionalmente por você",
            ]),
            "not_collect": ("Dados que não coletamos", "NÃO coletamos, armazenamos nem transmitimos:", [
                "Informações pessoais (nome, e-mail, telefone, endereço)",
                "Contas de usuário ou credenciais de autenticação",
                "Conteúdo de estudo ou materiais que você cria ou importa",
                "Progresso de aprendizagem, pontuações ou estatísticas",
                "Dados de analytics ou telemetria",
                "Relatórios de falha ou dados de diagnóstico",
                "Dados de localização",
                "Lista de contatos ou conexões sociais",
            ], "Para usuários da versão gratuita, parceiros de publicidade podem receber dados técnicos limitados necessários para exibir anúncios (veja a seção sobre publicidade abaixo)."),
            "storage": ("Armazenamento de dados", "Somente armazenamento local", "Todos os dados relacionados à aprendizagem são armazenados exclusivamente no seu dispositivo:", [
                "Decks e flashcards",
                "Progresso de estudo e estatísticas",
                "Histórico de revisão e dados de repetição espaçada",
                "Preferências e configurações do usuário",
                "Informações locais de perfil (nome do perfil, ícone, preferência de idioma)",
            ], "Esses dados são armazenados em um banco SQLite local dentro da área privada do app e protegidos pelos mecanismos nativos de segurança do dispositivo (iOS Data Protection, Android Keystore).", "Sem sincronização em nuvem", "O Lœrn não oferece sincronização em nuvem, backup em nuvem nem armazenamento em servidor. Não operamos servidores que recebam ou armazenem seus dados de aprendizagem."),
            "internet": ("Conectividade com a internet", "Base do aprendizado offline", "A funcionalidade principal de aprendizagem do Lœrn é totalmente offline e não requer acesso à rede.", "Publicidade (somente versão gratuita)", "Se você usa a versão gratuita do Lœrn, o app exibe anúncios. Apenas o módulo de publicidade acessa a internet para:", [
                "Carregar conteúdo publicitário",
                "Registrar impressões e interações com anúncios",
                "Cumprir requisitos das redes de publicidade",
            ], "O núcleo de aprendizagem em si não transmite dados de estudo, conteúdo nem progresso.", "Parceiros de publicidade", "A versão gratuita usa o Google AdMob. O AdMob pode coletar determinadas informações de acordo com sua própria política de privacidade, incluindo:", [
                "Identificador de publicidade do dispositivo",
                "Endereço IP",
                "Tipo de dispositivo e sistema operacional",
                "Dados de interação com anúncios",
            ], "Para detalhes sobre as práticas de dados do Google, veja:", "Versão premium", "Se você comprar a versão premium (pagamento único):", [
                "Todos os anúncios são removidos",
                "O módulo de publicidade não é inicializado",
                "O app não precisa de internet para uso normal",
                "Nenhuma comunicação de rede é realizada pelo app",
            ]),
            "iap": ("Compras no app", "Processamento da compra", "As compras premium são processadas integralmente pela Apple App Store ou Google Play Store.", [
                "Não coletamos nem armazenamos informações de pagamento",
                "Não recebemos dados de cartão de crédito nem de cobrança",
                "Recebemos apenas a confirmação de que a compra foi concluída",
            ], "O status premium é armazenado localmente no seu dispositivo. A compra fica vinculada à sua conta da App Store ou Play Store, e não a uma conta Lœrn."),
            "share": ("Importação, exportação e compartilhamento", "Importação e exportação local por arquivos", "O Lœrn permite importar e exportar decks de estudo usando arquivos JSON ou ZIP:", [
                "Os arquivos importados são processados localmente no seu dispositivo",
                "Os arquivos exportados contêm apenas conteúdo de aprendizagem (perguntas, respostas e metadados)",
                "Os arquivos exportados não incluem identificadores pessoais por padrão",
            ], "Compartilhamento iniciado pelo usuário", "Você pode optar por compartilhar arquivos exportados usando os recursos padrão de compartilhamento do seu dispositivo.", "Esclarecimentos importantes:", [
                "Os dados só são compartilhados quando você inicia esse compartilhamento de forma explícita",
                "O Lœrn não transmite dados automaticamente",
                "O Lœrn não sabe com quem você compartilha os dados",
                "Depois de compartilhados, os dados passam a ser tratados pelo app, serviço ou destinatário conforme as práticas de privacidade deles",
            ], "Você é o único responsável por como e onde os arquivos exportados são compartilhados.", "Direitos autorais e responsabilidade pelo conteúdo", "O Lœrn é uma ferramenta, não um provedor de conteúdo. Você é responsável por:", [
                "Garantir que tem direito de usar o conteúdo importado",
                "Cumprir a legislação de direitos autorais ao compartilhar decks exportados",
                "A legalidade de quaisquer materiais armazenados ou compartilhados usando o app",
            ]),
            "profiles": ("Perfis", "Suporte a múltiplos perfis", "O Lœrn suporta múltiplos perfis locais de usuário em um único dispositivo:", [
                "Cada perfil tem dados de aprendizagem isolados",
                "Os perfis são identificados apenas por um nome e um ícone escolhidos por você",
                "Os dados do perfil são armazenados localmente e nunca transmitidos pelo app",
                "Excluir um perfil remove permanentemente seus dados do dispositivo",
            ], "Status premium", "O status da compra premium vale para todos os perfis no mesmo dispositivo e na mesma conta da loja."),
            "notifications": ("Notificações (opcional)", "Lembretes de estudo", "Você pode ativar lembretes de estudo opcionalmente:", [
                "Os lembretes são agendados localmente no dispositivo",
                "Nenhum servidor externo é usado para enviar os lembretes",
                "Você pode desativar os lembretes a qualquer momento",
                "As permissões de notificação podem ser revogadas nas configurações do dispositivo",
            ]),
            "permissions": ("Permissões", "O app pode solicitar as seguintes permissões:", "Armazenamento (Android)", [
                "<strong>Finalidade:</strong> importar e exportar arquivos de decks",
                "<strong>Escopo:</strong> apenas os arquivos que você selecionar explicitamente",
            ], "Internet (somente versão gratuita)", [
                "<strong>Finalidade:</strong> exibir anúncios",
                "<strong>Não usado:</strong> versão premium",
            ], "Notificações (opcional)", [
                "<strong>Finalidade:</strong> lembretes de estudo",
                "<strong>Controle:</strong> você escolhe frequência e horário",
            ]),
            "third_party": ("Serviços de terceiros", "Publicidade (somente versão gratuita)", "A versão gratuita usa o Google AdMob.", "Não usamos:", [
                "Serviços de analytics",
                "Serviços de relatório de falhas",
                "Provedores de armazenamento em nuvem",
                "Integrações com redes sociais",
                "SDKs de rastreamento de terceiros",
            ]),
            "children": ("Privacidade infantil", [
                "O Lœrn foi pensado para estudantes universitários e outros aprendizes mais velhos. Não coletamos conscientemente informações pessoais de crianças menores de 13 anos (ou da idade aplicável na sua jurisdição).",
                "Como o Lœrn não coleta dados pessoais, ele está em conformidade com normas de privacidade infantil, como a COPPA.",
            ]),
            "security": ("Segurança de dados", "Segurança local do dispositivo", "Seus dados são protegidos por:", [
                "Criptografia em nível de dispositivo",
                "Isolamento do app (sandbox)",
                "Mecanismos de autenticação do dispositivo",
            ], "Sem risco de servidor", "Como o Lœrn não armazena dados em servidores, não há risco de:", [
                "Violação de servidores",
                "Vazamento de dados em nuvem",
                "Acesso não autorizado por terceiros",
            ], "Sua responsabilidade", "Você é responsável por:", [
                "Proteger o seu dispositivo",
                "Gerenciar backups do dispositivo (iCloud / Google backup)",
                "Armazenar com segurança os arquivos exportados",
            ]),
            "rights": ("Seus direitos e controle", "Você tem controle total sobre seus dados:", [
                "Todos os dados de aprendizagem são armazenados localmente",
                "Você pode exportar dados a qualquer momento",
                "Você pode excluir decks ou perfis",
                "Desinstalar o app remove todos os dados locais",
            ]),
            "retention": ("Retenção de dados", "Somente no dispositivo", "Os dados permanecem no seu dispositivo até que você:", [
                "Exclua conteúdo ou perfis",
                "Limpe os dados do app",
                "Desinstale o app",
            ], "Sem retenção em servidor", "Não retemos dados em servidores porque não operamos nenhum.", "Backups do dispositivo", "Se estiver habilitado, o seu sistema operativo pode fazer backup dos dados do app de acordo com as próprias políticas. Isso é controlado pela Apple ou pelo Google, e não pelo Lœrn."),
            "gdpr": ("Base legal (GDPR)", "Para usuários no EEE:", [
                "Não tratamos dados pessoais como controlador",
                "A publicidade (versão gratuita) baseia-se em interesse legítimo",
                "Você pode evitar a publicidade adquirindo a versão premium",
            ]),
            "ccpa": ("Direitos de privacidade da Califórnia (CCPA)", [
                "Não vendemos informações pessoais",
                "Não compartilhamos informações pessoais para marketing",
                "A maior parte das obrigações da CCPA não se aplica devido à ausência de coleta de dados",
            ]),
            "transfers": ("Transferências internacionais de dados", "Não transferimos dados de aprendizagem internacionalmente porque:", [
                "Os dados são armazenados localmente no seu dispositivo",
                "Não operamos servidores",
                "Os dados só saem do dispositivo quando o usuário inicia um compartilhamento",
            ]),
            "changes": ("Alterações nesta política", [
                "Podemos atualizar esta política para refletir mudanças no app ou na legislação.",
                "Avisaremos os usuários por meio de:",
            ], [
                "Atualização da data de “Última atualização”",
                "Publicação da política atualizada",
                "Exibição de um aviso no app em caso de alterações relevantes",
            ]),
            "contact": ("Contato", "Se você tiver dúvidas sobre esta política de privacidade:", "Observe que não temos acesso aos seus dados de aprendizagem, pois eles ficam armazenados localmente no seu dispositivo."),
            "commitment": ("Compromisso com a privacidade", "O Lœrn foi construído com a convicção de que aprender deve ser privado por padrão. Seus dados ficam sob seu controle, e você decide se e quando eles serão compartilhados."),
            "summary": ("Resumo", [
                "Seus dados de aprendizagem ficam no seu dispositivo",
                "Não coletamos informações pessoais",
                "Não rastreamos o que ou como você estuda",
                "A versão gratuita exibe anúncios (o AdMob pode coletar dados relacionados a anúncios)",
                "A versão premium não tem anúncios e não requer acesso à rede",
                "Você pode exportar e compartilhar dados se quiser",
                "Desinstalar o app remove todos os dados locais",
            ]),
        },
    },
    "pt-pt": {
        "title": "Política de privacidade",
        "meta_desc": "Política de privacidade da aplicação Lœrn.",
        "h1": "Política de privacidade da app Lœrn",
        "updated": "Última atualização: 5 de fevereiro de 2026",
        "sections": {
            "intro": ("Introdução", [
                "Esta política de privacidade explica como o Lœrn (\"nós\", \"nosso\" ou \"a app\") trata a informação. O Lœrn foi concebido com a privacidade como princípio central. Acreditamos que os seus dados de aprendizagem devem permanecer sempre sob o seu controlo.",
                "Exceto quando escolhe explicitamente exportar ou partilhar conteúdo, o Lœrn não transmite os seus dados para fora do dispositivo.",
            ]),
            "core": ("Princípios centrais de privacidade", "Privacidade em primeiro lugar", "O Lœrn foi desenvolvido de raiz para proteger a sua privacidade:", [
                "<strong>Offline-first por conceção:</strong> as funcionalidades principais de aprendizagem funcionam sem ligação à internet",
                "<strong>Sem contas de utilizador:</strong> sem registo, sem login e sem palavras-passe",
                "<strong>Sem rastreamento:</strong> sem análise comportamental nem criação de perfis",
                "<strong>Armazenamento apenas local:</strong> os dados de aprendizagem ficam no seu dispositivo, a menos que decida exportá-los ou partilhá-los",
                "<strong>Controlo do utilizador:</strong> os dados só saem do dispositivo por ações iniciadas intencionalmente por si",
            ]),
            "not_collect": ("Dados que não recolhemos", "NÃO recolhemos, armazenamos nem transmitimos:", [
                "Informação pessoal (nome, e-mail, número de telefone, morada)",
                "Contas de utilizador ou credenciais de autenticação",
                "Conteúdo de estudo ou materiais que cria ou importa",
                "Progresso de aprendizagem, resultados ou estatísticas",
                "Dados de análise ou telemetria",
                "Relatórios de falha ou dados de diagnóstico",
                "Dados de localização",
                "Listas de contactos ou ligações sociais",
            ], "Para utilizadores da versão gratuita, parceiros de publicidade podem receber dados técnicos limitados necessários para apresentar anúncios (ver a secção de publicidade abaixo)."),
            "storage": ("Armazenamento de dados", "Apenas armazenamento local", "Todos os dados relacionados com a aprendizagem são armazenados exclusivamente no seu dispositivo:", [
                "Baralhos e flashcards",
                "Progresso de estudo e estatísticas",
                "Histórico de revisão e dados de repetição espaçada",
                "Preferências e definições do utilizador",
                "Informação local de perfil (nome do perfil, ícone, preferência de idioma)",
            ], "Estes dados são armazenados numa base de dados SQLite local dentro do armazenamento privado da app e protegidos pelos mecanismos de segurança nativos do dispositivo (iOS Data Protection, Android Keystore).", "Sem sincronização na nuvem", "O Lœrn não oferece sincronização na nuvem, cópia de segurança na nuvem nem armazenamento em servidor. Não operamos servidores que recebam ou armazenem os seus dados de aprendizagem."),
            "internet": ("Conectividade à internet", "Base da aprendizagem offline", "A funcionalidade principal de aprendizagem do Lœrn é totalmente offline e não requer acesso à rede.", "Publicidade (apenas versão gratuita)", "Se utiliza a versão gratuita do Lœrn, a app apresenta anúncios. Apenas o módulo de publicidade acede à internet para:", [
                "Carregar conteúdo publicitário",
                "Registar impressões e interações com anúncios",
                "Cumprir os requisitos das redes publicitárias",
            ], "O núcleo de aprendizagem em si não transmite dados de estudo, conteúdo nem progresso.", "Parceiros de publicidade", "A versão gratuita utiliza o Google AdMob. O AdMob pode recolher determinadas informações de acordo com a sua própria política de privacidade, incluindo:", [
                "Identificador publicitário do dispositivo",
                "Endereço IP",
                "Tipo de dispositivo e sistema operativo",
                "Dados de interação com anúncios",
            ], "Para detalhes sobre as práticas de dados da Google, consulte:", "Versão premium", "Se adquirir a versão premium (pagamento único):", [
                "Todos os anúncios são removidos",
                "O módulo de publicidade não é inicializado",
                "A app não necessita de internet para utilização normal",
                "A app não efetua qualquer comunicação de rede",
            ]),
            "iap": ("Compras na app", "Processamento da compra", "As compras premium são processadas integralmente pela Apple App Store ou Google Play Store.", [
                "Não recolhemos nem armazenamos informações de pagamento",
                "Não recebemos dados de cartão de crédito nem de faturação",
                "Recebemos apenas a confirmação de que a compra foi concluída",
            ], "O estado premium é armazenado localmente no seu dispositivo. A compra fica associada à sua conta da App Store ou Play Store, e não a qualquer conta Lœrn."),
            "share": ("Importação, exportação e partilha", "Importação e exportação local por ficheiros", "O Lœrn permite importar e exportar baralhos de estudo utilizando ficheiros JSON ou ZIP:", [
                "Os ficheiros importados são processados localmente no seu dispositivo",
                "Os ficheiros exportados contêm apenas conteúdo de aprendizagem (perguntas, respostas e metadados)",
                "Os ficheiros exportados não incluem identificadores pessoais por defeito",
            ], "Partilha iniciada pelo utilizador", "Pode optar por partilhar ficheiros exportados usando as funcionalidades padrão de partilha do dispositivo.", "Esclarecimentos importantes:", [
                "Os dados só são partilhados quando inicia explicitamente essa partilha",
                "O Lœrn não transmite dados automaticamente",
                "O Lœrn não sabe com quem partilha os dados",
                "Depois de partilhados, os dados passam a ser tratados pela app, serviço ou destinatário de acordo com as respetivas práticas de privacidade",
            ], "É o único responsável pela forma e pelo local onde os ficheiros exportados são partilhados.", "Direitos de autor e responsabilidade pelo conteúdo", "O Lœrn é uma ferramenta, não um fornecedor de conteúdos. É responsável por:", [
                "Garantir que tem o direito de utilizar o conteúdo importado",
                "Cumprir a legislação de direitos de autor ao partilhar baralhos exportados",
                "A legalidade de quaisquer materiais armazenados ou partilhados através da app",
            ]),
            "profiles": ("Perfis", "Suporte a vários perfis", "O Lœrn suporta vários perfis locais de utilizador num único dispositivo:", [
                "Cada perfil tem dados de aprendizagem isolados",
                "Os perfis são identificados apenas por um nome e um ícone escolhidos por si",
                "Os dados do perfil são armazenados localmente e nunca transmitidos pela app",
                "Eliminar um perfil remove permanentemente os seus dados do dispositivo",
            ], "Estado premium", "O estado da compra premium aplica-se a todos os perfis no mesmo dispositivo e na mesma conta da loja."),
            "notifications": ("Notificações (opcional)", "Lembretes de estudo", "Pode ativar lembretes de estudo opcionalmente:", [
                "Os lembretes são agendados localmente no dispositivo",
                "Nenhum servidor externo é utilizado para enviar os lembretes",
                "Pode desativar os lembretes a qualquer momento",
                "As permissões de notificação podem ser revogadas nas definições do dispositivo",
            ]),
            "permissions": ("Permissões", "A app pode solicitar as seguintes permissões:", "Armazenamento (Android)", [
                "<strong>Finalidade:</strong> importar e exportar ficheiros de baralhos",
                "<strong>Âmbito:</strong> apenas os ficheiros que selecionar explicitamente",
            ], "Internet (apenas versão gratuita)", [
                "<strong>Finalidade:</strong> apresentar anúncios",
                "<strong>Não utilizado:</strong> versão premium",
            ], "Notificações (opcional)", [
                "<strong>Finalidade:</strong> lembretes de estudo",
                "<strong>Controlo:</strong> escolhe a frequência e o horário",
            ]),
            "third_party": ("Serviços de terceiros", "Publicidade (apenas versão gratuita)", "A versão gratuita utiliza o Google AdMob.", "Não utilizamos:", [
                "Serviços de análise",
                "Serviços de relatório de falhas",
                "Fornecedores de armazenamento na nuvem",
                "Integrações com redes sociais",
                "SDKs de rastreamento de terceiros",
            ]),
            "children": ("Privacidade das crianças", [
                "O Lœrn destina-se a estudantes universitários e outros aprendentes mais velhos. Não recolhemos conscientemente informação pessoal de crianças com menos de 13 anos (ou da idade aplicável na sua jurisdição).",
                "Como o Lœrn não recolhe dados pessoais, cumpre regulamentos de privacidade infantil, como a COPPA.",
            ]),
            "security": ("Segurança dos dados", "Segurança local do dispositivo", "Os seus dados são protegidos por:", [
                "Encriptação ao nível do dispositivo",
                "Isolamento da app (sandbox)",
                "Mecanismos de autenticação do dispositivo",
            ], "Sem risco de servidor", "Como o Lœrn não armazena dados em servidores, não existe risco de:", [
                "Violação de servidores",
                "Fugas de dados na nuvem",
                "Acesso não autorizado por terceiros",
            ], "A sua responsabilidade", "É responsável por:", [
                "Proteger o seu dispositivo",
                "Gerir cópias de segurança do dispositivo (iCloud / Google backup)",
                "Guardar em segurança os ficheiros exportados",
            ]),
            "rights": ("Os seus direitos e controlo", "Tem controlo total sobre os seus dados:", [
                "Todos os dados de aprendizagem são armazenados localmente",
                "Pode exportar dados a qualquer momento",
                "Pode eliminar baralhos ou perfis",
                "Desinstalar a app remove todos os dados locais",
            ]),
            "retention": ("Retenção de dados", "Apenas no dispositivo", "Os dados permanecem no seu dispositivo até que:", [
                "Elimine conteúdo ou perfis",
                "Limpe os dados da app",
                "Desinstale a app",
            ], "Sem retenção em servidor", "Não retemos dados em servidores porque não operamos nenhum.", "Cópias de segurança do dispositivo", "Se estiver ativado, o sistema operativo pode fazer cópia de segurança dos dados da app de acordo com as suas próprias políticas. Isto é controlado pela Apple ou pela Google, e não pelo Lœrn."),
            "gdpr": ("Base legal (RGPD)", "Para utilizadores no EEE:", [
                "Não tratamos dados pessoais como responsável pelo tratamento",
                "A publicidade (versão gratuita) baseia-se em interesse legítimo",
                "Pode evitar a publicidade adquirindo a versão premium",
            ]),
            "ccpa": ("Direitos de privacidade da Califórnia (CCPA)", [
                "Não vendemos informação pessoal",
                "Não partilhamos informação pessoal para marketing",
                "A maioria das obrigações da CCPA não se aplica devido à ausência de recolha de dados",
            ]),
            "transfers": ("Transferências internacionais de dados", "Não transferimos dados de aprendizagem internacionalmente porque:", [
                "Os dados são armazenados localmente no seu dispositivo",
                "Não operamos servidores",
                "Os dados só saem do dispositivo quando o utilizador inicia uma partilha",
            ]),
            "changes": ("Alterações a esta política", [
                "Podemos atualizar esta política para refletir alterações na app ou na legislação.",
                "Informaremos os utilizadores através de:",
            ], [
                "Atualização da data de “Última atualização”",
                "Publicação da política atualizada",
                "Apresentação de um aviso na app em caso de alterações relevantes",
            ]),
            "contact": ("Contacto", "Se tiver questões sobre esta política de privacidade:", "Tenha em conta que não podemos aceder aos seus dados de aprendizagem, uma vez que estão armazenados localmente no seu dispositivo."),
            "commitment": ("Compromisso com a privacidade", "O Lœrn foi construído com a convicção de que aprender deve ser privado por defeito. Os seus dados permanecem sob o seu controlo, e é você quem decide se e quando os partilha."),
            "summary": ("Resumo", [
                "Os seus dados de aprendizagem ficam no seu dispositivo",
                "Não recolhemos informação pessoal",
                "Não rastreamos o que ou como estuda",
                "A versão gratuita apresenta anúncios (o AdMob pode recolher dados relacionados com anúncios)",
                "A versão premium não tem anúncios e não requer acesso à rede",
                "Pode exportar e partilhar dados se quiser",
                "Desinstalar a app remove todos os dados locais",
            ]),
        },
    },
}


def lang_switch_options(current_locale):
    """Render all <option> elements for the lang switcher."""
    lines = []
    for lc in ALL_LOCALES_BASE:
        label = LOCALE_LABELS[lc]
        selected = ' selected' if lc == current_locale else ''
        lines.append(f'                    <option value="{lc}"{selected}>{label}</option>')
    return "\n".join(lines)


def lang_switch_pages(page_path):
    """Render the JS pages map for lang switcher for a given page path template.

    page_path examples:
      ""          -> index (e.g. ../de/)
      "about.html"
      "projects/loern.html"
      "legal/imprint.html"
      "projects/loern/privacy.html"
    """
    lines = []
    for lc in ALL_LOCALES_BASE:
        folder = LOCALE_DIRS[lc]
        depth = page_path.count("/")
        prefix = "../" * (depth + 1)
        if page_path == "":
            target = f"{prefix}{folder}/"
        else:
            target = f"{prefix}{folder}/{page_path}"
        lines.append(f'        "{lc}": "{target}",')
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Template builders
# ---------------------------------------------------------------------------

def header_html(locale, t, brand_prefix, page_nav_options_html):
    """Shared header snippet."""
    options_html = lang_switch_options(locale)
    logo_src = "../company_logo.png" if brand_prefix == "./" else f"{brand_prefix}../company_logo.png"
    return f'''\
    <a class="skip-link" href="#main">{t["skip_link"]}</a>
    <header class="site-header">
        <div class="header-content">
        <a href="{brand_prefix}" class="brand">
            <div class="brand-logo">
                <img src="{logo_src}" alt="Jetzt &amp; Dahanna Technologies">
            </div>
            <div class="brand-text">
                <span class="brand-name">JETZT &amp; DAHANNA</span>
                <span class="brand-tagline">Technologies</span>
            </div>
        </a>

        <nav class="main-nav">
            
            <select id="page-nav-select" aria-label="{t["nav"]["home"]}">
{page_nav_options_html}
            </select>
            <a href="{brand_prefix}about.html">{t["nav"]["about"]}</a>
            <a href="{brand_prefix}projects.html">{t["nav"]["projects"]}</a>
            <a href="{brand_prefix}principles.html">{t["nav"]["principles"]}</a>
            <a href="{brand_prefix}contact.html" class="nav-cta">{t["nav"]["contact"]}</a>

            <select id="lang-switch" aria-label="{t["lang_switch_aria"]}">
{options_html}
</select>
        </nav>
        </div>
    </header>'''


def lang_switcher_script(page_path):
    pages = lang_switch_pages(page_path)
    return f'''\
    <script>
// Language switcher
document.getElementById("lang-switch").addEventListener("change", function() {{
    var lang = this.value;
    try {{ localStorage.setItem("jd_lang", lang); }} catch (e) {{}}
    var pages = {{
{pages}
    }};
    if (pages[lang]) {{
        window.location.href = pages[lang];
    }}
}});

// Page navigation
var pageNav = document.getElementById("page-nav-select");
if (pageNav) {{
    pageNav.addEventListener("change", function() {{
        window.location.href = this.value;
    }});
}}
</script>'''


# ---------------------------------------------------------------------------
# Page generators
# ---------------------------------------------------------------------------

def make_index(locale, t):
    ti = t["index"]
    folder = LOCALE_DIRS[locale]
    page_nav = (
        f'                <option value="./" selected>{t["nav"]["home"]}</option>\n'
        f'                <option value="about.html">{t["nav"]["about"]}</option>\n'
        f'                <option value="projects.html">{t["nav"]["projects"]}</option>\n'
        f'                <option value="principles.html">{t["nav"]["principles"]}</option>\n'
        f'                <option value="contact.html">{t["nav"]["contact"]}</option>'
    )
    hdr = header_html(locale, t, "./", page_nav)
    script = lang_switcher_script("")
    return f'''\
<!DOCTYPE html>
<html lang="{t["lang_attr"]}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jetzt &amp; Dahanna Technologies</title>
    <meta name="description" content="{ti["meta_desc"]}">
    <link rel="canonical" href="https://jetztunddahanna.com/{folder}/">
    <link rel="stylesheet" href="../style.css">
</head>
<body>
{hdr}

    <main id="main" class="page">
        <section>
            <h1>{ti["h1"]}</h1>
            <p class="lead">{ti["lead"]}</p>
        </section>

        <section>
            <h2>{ti["h2_good_ai"]}</h2>
            <p>{ti["p_good_ai_1"]}</p>
            <p>{ti["p_good_ai_2"]}</p>
        </section>

        <section>
            <h2>{ti["h2_current"]}</h2>
            <div class="project-card">
                <div class="project-card-header">
                    <div class="project-card-logo" aria-hidden="true">
                        <img src="../Loern_full_white.png" alt="">
                    </div>
                    <h3 style="margin: 0;">L\u0153rn</h3>
                </div>
                <p>{ti["loern_desc"]}</p>
                <div class="project-card-badges" aria-label="{ti["loern_aria_badges"]}">
                    <a href="https://play.google.com/store/apps/details?id=com.jetztunddahanna.loern" target="_blank" rel="noopener noreferrer" aria-label="{t["gplay_aria"]}" style="display: inline-flex; align-items: center; padding: 0; background: transparent; border: 0; text-decoration: none;">
                        <img src="../Google%20Play%20Badge%20guidelines/Get%20it%20on%20Google%20Play%20Badges/Digital/svg/{t["gplay_badge"]}" alt="{t["gplay_alt"]}">
                    </a>
                    <a href="https://apps.apple.com/app/l%C5%93rn/id6759726662" target="_blank" rel="noopener noreferrer" aria-label="{t["appstore_aria"]}" style="display: inline-flex; align-items: center; padding: 0; background: transparent; border: 0; text-decoration: none;">
                        <img src="../Download-on-the-App-Store/{t["appstore_folder"]}/Download_on_App_Store/Black_lockup/SVG/{t["appstore_file"]}" alt="{t["appstore_alt"]}">
                    </a></div>
                <p><a href="projects/loern.html" class="text-link">{ti["loern_learn_more"]}</a></p>
            </div>
        </section>

        <section>
            <h2>{ti["h2_how"]}</h2>
            <p>{ti["p_how_1"]}</p>
            <p><a href="principles.html" class="text-link">{ti["p_how_2"]}</a></p>
        </section>
    </main>

    <footer class="site-footer">
        <div class="footer-links">
            <a href="legal/imprint.html">{t["footer_imprint"]}</a>
            <a href="legal/privacy.html">{t["footer_privacy"]}</a>
        </div>
    </footer>
    <script src="../site.js"></script>
{script}
</body>
</html>
'''


def make_about(locale, t):
    ta = t["about"]
    folder = LOCALE_DIRS[locale]
    page_nav = (
        f'                <option value="./">{t["nav"]["home"]}</option>\n'
        f'                <option value="about.html" selected>{t["nav"]["about"]}</option>\n'
        f'                <option value="projects.html">{t["nav"]["projects"]}</option>\n'
        f'                <option value="principles.html">{t["nav"]["principles"]}</option>\n'
        f'                <option value="contact.html">{t["nav"]["contact"]}</option>'
    )
    hdr = header_html(locale, t, "./", page_nav)
    script = lang_switcher_script("about.html")
    return f'''\
<!DOCTYPE html>
<html lang="{t["lang_attr"]}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ta["title_prefix"]} \u2013 Jetzt &amp; Dahanna Technologies</title>
    <meta name="description" content="{ta["meta_desc"]}">
    <link rel="canonical" href="https://jetztunddahanna.com/{folder}/about.html">
    <link rel="stylesheet" href="../style.css">
</head>
<body>
{hdr}

    <main id="main" class="page narrow">
        <h1>{ta["h1"]}</h1>
        
        <section>
            <h2>{ta["h2_perspective"]}</h2>
            <p>{ta["p_persp_1"]}</p>
            <p>{ta["p_persp_2"]}</p>
        </section>

        <section>
            <h2>{ta["h2_expect"]}</h2>
            <p>{ta["p_expect_1"]}</p>
            <p>{ta["p_expect_2"]}</p>
            <p>{ta["p_expect_3"]}</p>
        </section>

        <section>
            <h2>{ta["h2_build"]}</h2>
            <p>{ta["p_build_1"]}</p>
            <p>{ta["p_build_2"]}</p>
        </section>

        <section>
            <h2>{ta["h2_what"]}</h2>
            <p>{ta["p_what"]}</p>
        </section>
    </main>

    <footer class="site-footer">
        <div class="footer-links">
            <a href="legal/imprint.html">{t["footer_imprint"]}</a>
            <a href="legal/privacy.html">{t["footer_privacy"]}</a>
        </div>
    </footer>
    <script src="../site.js"></script>
{script}
</body>
</html>
'''


def make_principles(locale, t):
    tp = t["principles"]
    folder = LOCALE_DIRS[locale]
    page_nav = (
        f'                <option value="./">{t["nav"]["home"]}</option>\n'
        f'                <option value="about.html">{t["nav"]["about"]}</option>\n'
        f'                <option value="projects.html">{t["nav"]["projects"]}</option>\n'
        f'                <option value="principles.html" selected>{t["nav"]["principles"]}</option>\n'
        f'                <option value="contact.html">{t["nav"]["contact"]}</option>'
    )
    hdr = header_html(locale, t, "./", page_nav)
    script = lang_switcher_script("principles.html")
    items_html = ""
    for h3, p in tp["items"]:
        items_html += f'''\
            <li>
                <h3>{h3}</h3>
                <p>{p}</p>
            </li>
            
'''
    return f'''\
<!DOCTYPE html>
<html lang="{t["lang_attr"]}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{tp["title_prefix"]} \u2013 Jetzt &amp; Dahanna Technologies</title>
    <meta name="description" content="{tp["meta_desc"]}">
    <link rel="canonical" href="https://jetztunddahanna.com/{folder}/principles.html">
    <link rel="stylesheet" href="../style.css">
</head>
<body>
{hdr}

    <main id="main" class="page narrow">
        <h1>{tp["h1"]}</h1>
        <p class="lead">{tp["lead"]}</p>
        
        <ul class="principles-list">
            {items_html.strip()}
        </ul>
    </main>

    <footer class="site-footer">
        <div class="footer-links">
            <a href="legal/imprint.html">{t["footer_imprint"]}</a>
            <a href="legal/privacy.html">{t["footer_privacy"]}</a>
        </div>
    </footer>
    <script src="../site.js"></script>
{script}
</body>
</html>
'''


def make_contact(locale, t):
    tc = t["contact"]
    folder = LOCALE_DIRS[locale]
    page_nav = (
        f'                <option value="./">{t["nav"]["home"]}</option>\n'
        f'                <option value="about.html">{t["nav"]["about"]}</option>\n'
        f'                <option value="projects.html">{t["nav"]["projects"]}</option>\n'
        f'                <option value="principles.html">{t["nav"]["principles"]}</option>\n'
        f'                <option value="contact.html" selected>{t["nav"]["contact"]}</option>'
    )
    hdr = header_html(locale, t, "./", page_nav)
    script = lang_switcher_script("contact.html")
    return f'''\
<!DOCTYPE html>
<html lang="{t["lang_attr"]}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{tc["title_prefix"]} \u2013 Jetzt &amp; Dahanna Technologies</title>
    <meta name="description" content="{tc["meta_desc"]}">
    <link rel="canonical" href="https://jetztunddahanna.com/{folder}/contact.html">
    <link rel="stylesheet" href="../style.css">
</head>
<body>
{hdr}

    <main id="main" class="page narrow">
        <h1>{tc["h1"]}</h1>
        
        <section>
            <p>{tc["p_intro"]}</p>
            
            <div class="contact-info">
                <p><a href="mailto:info@jetztunddahanna.com" class="text-link">info@jetztunddahanna.com</a></p>
            </div>
        </section>

        <section>
            <h2>{tc["h2_note"]}</h2>
            <p>{tc["p_note"]}</p>
        </section>
    </main>

    <footer class="site-footer">
        <div class="footer-links">
            <a href="legal/imprint.html">{t["footer_imprint"]}</a>
            <a href="legal/privacy.html">{t["footer_privacy"]}</a>
        </div>
    </footer>
    <script src="../site.js"></script>
{script}
</body>
</html>
'''


def make_projects(locale, t):
    tp = t["projects"]
    folder = LOCALE_DIRS[locale]
    page_nav = (
        f'                <option value="./">{t["nav"]["home"]}</option>\n'
        f'                <option value="about.html">{t["nav"]["about"]}</option>\n'
        f'                <option value="projects.html" selected>{t["nav"]["projects"]}</option>\n'
        f'                <option value="principles.html">{t["nav"]["principles"]}</option>\n'
        f'                <option value="contact.html">{t["nav"]["contact"]}</option>'
    )
    hdr = header_html(locale, t, "./", page_nav)
    script = lang_switcher_script("projects.html")
    return f'''\
<!DOCTYPE html>
<html lang="{t["lang_attr"]}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{tp["title_prefix"]} \u2013 Jetzt &amp; Dahanna Technologies</title>
    <meta name="description" content="{tp["meta_desc"]}">
    <link rel="canonical" href="https://jetztunddahanna.com/{folder}/projects.html">
    <link rel="stylesheet" href="../style.css">
</head>
<body>
{hdr}

    <main id="main" class="page narrow">
        <h1>{tp["h1"]}</h1>
        
        <section>
            <div class="project-card">
                <div class="project-card-header">
                    <div class="project-card-logo" aria-hidden="true">
                        <img src="../Loern_full_white.png" alt="">
                    </div>
                    <h3 style="margin: 0;">L\u0153rn</h3>
                </div>
                <p>{tp["loern_desc"]}</p>
                <div class="project-card-badges" aria-label="{tp["loern_aria_badges"]}">
                    <a href="https://play.google.com/store/apps/details?id=com.jetztunddahanna.loern" target="_blank" rel="noopener noreferrer" aria-label="{t["gplay_aria"]}" style="display: inline-flex; align-items: center; padding: 0; background: transparent; border: 0; text-decoration: none;">
                        <img src="../Google%20Play%20Badge%20guidelines/Get%20it%20on%20Google%20Play%20Badges/Digital/svg/{t["gplay_badge"]}" alt="{t["gplay_alt"]}">
                    </a>
                    <a href="https://apps.apple.com/app/l%C5%93rn/id6759726662" target="_blank" rel="noopener noreferrer" aria-label="{t["appstore_aria"]}" style="display: inline-flex; align-items: center; padding: 0; background: transparent; border: 0; text-decoration: none;">
                        <img src="../Download-on-the-App-Store/{t["appstore_folder"]}/Download_on_App_Store/Black_lockup/SVG/{t["appstore_file"]}" alt="{t["appstore_alt"]}">
                    </a>
                </div>
                <p>{tp["loern_offline"]}</p>
                <p><a href="projects/loern.html" class="text-link">{tp["loern_more"]}</a></p>
            </div>
        </section>
    </main>

    <footer class="site-footer">
        <div class="footer-links">
            <a href="legal/imprint.html">{t["footer_imprint"]}</a>
            <a href="legal/privacy.html">{t["footer_privacy"]}</a>
        </div>
    </footer>
    <script src="../site.js"></script>
{script}
</body>
</html>
'''


def make_imprint(locale, t):
    ti = t["imprint"]
    folder = LOCALE_DIRS[locale]
    page_nav = (
        f'                <option value="../">{t["nav"]["home"]}</option>\n'
        f'                <option value="../about.html">{t["nav"]["about"]}</option>\n'
        f'                <option value="../projects.html">{t["nav"]["projects"]}</option>\n'
        f'                <option value="../principles.html">{t["nav"]["principles"]}</option>\n'
        f'                <option value="../contact.html">{t["nav"]["contact"]}</option>'
    )
    hdr = header_html(locale, t, "../", page_nav)
    script = lang_switcher_script("legal/imprint.html")
    return f'''\
<!DOCTYPE html>
<html lang="{t["lang_attr"]}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ti["title_prefix"]} \u2013 Jetzt &amp; Dahanna Technologies</title>
    <meta name="description" content="{ti["meta_desc"]}">
    <link rel="canonical" href="https://jetztunddahanna.com/{folder}/legal/imprint.html">
    <link rel="stylesheet" href="../../style.css">
</head>
<body>
{hdr}

    <main id="main" class="page narrow legal-content">
        <h1>{ti["h1"]}</h1>
        
        <section>
            <h2>{ti["h2_info"]}</h2>
            <p>
                Tobias Blankenhorn<br>
                Richard-Wagner-Str. 17/1<br>
                71116 Gaertringen<br>
                Germany
            </p>
        </section>

        <section>
            <h2>{ti["h2_contact"]}</h2>
            <p>Email: <a href="mailto:info@jetztunddahanna.com" class="text-link">info@jetztunddahanna.com</a></p>
        </section>

        <section>
            <h2>{ti["h2_vat"]}</h2>
            <p>{ti["p_vat"]}</p>
        </section>

        <section>
            <h2>{ti["h2_responsible"]}</h2>
            <p>{ti["p_responsible"]}</p>
        </section>
    </main>

    <footer class="site-footer">
        <div class="footer-links">
            <a href="imprint.html">{t["footer_imprint"]}</a>
            <a href="privacy.html">{t["footer_privacy"]}</a>
        </div>
    </footer>
    <script src="../../site.js"></script>
{script}
</body>
</html>
'''


def make_privacy_site(locale, t):
    tp = t["privacy"]
    folder = LOCALE_DIRS[locale]
    page_nav = (
        f'                <option value="../">{t["nav"]["home"]}</option>\n'
        f'                <option value="../about.html">{t["nav"]["about"]}</option>\n'
        f'                <option value="../projects.html">{t["nav"]["projects"]}</option>\n'
        f'                <option value="../principles.html">{t["nav"]["principles"]}</option>\n'
        f'                <option value="../contact.html">{t["nav"]["contact"]}</option>'
    )
    hdr = header_html(locale, t, "../", page_nav)
    script = lang_switcher_script("legal/privacy.html")
    log_items_html = "\n".join(f"                <li>{item}</li>" for item in tp["log_items"])
    rights_items_html = "\n".join(f"                <li>{item}</li>" for item in tp["rights_items"])
    return f'''\
<!DOCTYPE html>
<html lang="{t["lang_attr"]}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{tp["title_prefix"]} \u2013 Jetzt &amp; Dahanna Technologies</title>
    <meta name="description" content="{tp["meta_desc"]}">
    <link rel="canonical" href="https://jetztunddahanna.com/{folder}/legal/privacy.html">
    <link rel="stylesheet" href="../../style.css">
</head>
<body>
{hdr}

    <main id="main" class="page narrow legal-content">
        <h1>{tp["h1"]}</h1>
        
        <section>
            <h2>{tp["h2_general"]}</h2>
            <p>{tp["p_general_1"]}</p>
            <p>{tp["p_general_2"]}</p>
        </section>

        <section>
            <h2>{tp["h2_collection"]}</h2>
            <p>{tp["p_collection_1"]}</p>
            <p>{tp["p_collection_2"]}</p>
        </section>

        <section>
            <h2>{tp["h2_logs"]}</h2>
            <p>{tp["p_logs"]}</p>
            <ul>
{log_items_html}
            </ul>
            <p>{tp["p_logs_2"]}</p>
        </section>

        <section>
            <h2>{tp["h2_contact_section"]}</h2>
            <p>{tp["p_contact"]}</p>
        </section>

        <section>
            <h2>{tp["h2_rights"]}</h2>
            <p>{tp["p_rights_intro"]}</p>
            <ul>
{rights_items_html}
            </ul>
            <p>{tp["p_rights_contact"]}</p>
        </section>
    </main>

    <footer class="site-footer">
        <div class="footer-links">
            <a href="imprint.html">{t["footer_imprint"]}</a>
            <a href="privacy.html">{t["footer_privacy"]}</a>
        </div>
    </footer>
    <script src="../../site.js"></script>
{script}
</body>
</html>
'''


def make_loern(locale, t):
    """projects/loern.html fully localized for the new locales."""
    folder = LOCALE_DIRS[locale]
    lp = LOERN_PAGE_TRANSLATIONS[locale]
    page_nav = (
        f'                <option value="../">{t["nav"]["home"]}</option>\n'
        f'                <option value="../about.html">{t["nav"]["about"]}</option>\n'
        f'                <option value="../projects.html" selected>{t["nav"]["projects"]}</option>\n'
        f'                <option value="../principles.html">{t["nav"]["principles"]}</option>\n'
        f'                <option value="../contact.html">{t["nav"]["contact"]}</option>'
    )
    hdr = header_html(locale, t, "../", page_nav)
    script = lang_switcher_script("projects/loern.html")

    return f'''\
<!DOCTYPE html>
<html lang="{t["lang_attr"]}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>L\u0153rn \u2013 Jetzt &amp; Dahanna Technologies</title>
    <meta name="description" content="{lp["meta_desc"]}">
    <link rel="canonical" href="https://jetztunddahanna.com/{folder}/projects/loern.html">
    <link rel="stylesheet" href="../../style.css">
</head>
<body>
{hdr}

    <main id="main" class="page narrow loern-page">
        <div class="loern-hero">
            <div>
                <span class="loern-pill">{lp["pill"]}</span>
                <h1>L\u0153rn</h1>
                <p class="loern-lead">{lp["lead"]}</p>

                <div class="loern-cta">
                    <a href="https://play.google.com/store/apps/details?id=com.jetztunddahanna.loern" target="_blank" rel="noopener noreferrer" aria-label="{t["gplay_aria"]}" style="display: inline-flex; align-items: center; padding: 0; background: transparent; border: 0; text-decoration: none;">
                        <img src="../../Google%20Play%20Badge%20guidelines/Get%20it%20on%20Google%20Play%20Badges/Digital/svg/{t["gplay_badge"]}" alt="{t["gplay_alt"]}" style="height: 44px; width: auto; display: block;">
                    </a>
                    <a href="https://apps.apple.com/app/l%C5%93rn/id6759726662" target="_blank" rel="noopener noreferrer" aria-label="{t["appstore_aria"]}" style="display: inline-flex; align-items: center; padding: 0; background: transparent; border: 0; text-decoration: none;">
                        <img src="../../Download-on-the-App-Store/{t["appstore_folder"]}/Download_on_App_Store/Black_lockup/SVG/{t["appstore_file"]}" alt="{t["appstore_alt"]}" style="height: 44px; width: auto; display: block;">
                    </a>
                    <a class="loern-btn secondary" href="loern/privacy.html">{lp["privacy_link"]}</a>
                </div>
                <p style="color: var(--loern-text-secondary); margin-bottom: 0;">
                    {lp["no_cloud"]}
                </p>
            </div>

            <div class="loern-logo-card" aria-label="L\u0153rn logo">
                <img src="../../Loern_full_white.png" alt="L\u0153rn">
            </div>
        </div>

        <section>
            <h2>{lp["what_h2"]}</h2>
            <p>{lp["what_p1"]}</p>
            <p><strong>{lp["what_p2"]}</strong> {lp["what_p2_tail"]}</p>
        </section>

        <section>
            <h2>{lp["why_h2"]}</h2>
            <div class="loern-grid">
                <div class="loern-feature">
                    <div class="loern-icon" aria-hidden="true">\u2726</div>
                    <div>
                        <h3>{lp["why_1_h3"]}</h3>
                        <p>{lp["why_1_p"]}</p>
                    </div>
                </div>
                <div class="loern-feature">
                    <div class="loern-icon" aria-hidden="true">\u27b2</div>
                    <div>
                        <h3>{lp["why_2_h3"]}</h3>
                        <p>{lp["why_2_p"]}</p>
                    </div>
                </div>
                <div class="loern-feature">
                    <div class="loern-icon" aria-hidden="true">\u25a6</div>
                    <div>
                        <h3>{lp["why_3_h3"]}</h3>
                        <p>{lp["why_3_p"]}</p>
                    </div>
                </div>
            </div>
        </section>

        <section>
            <h2>{lp["features_h2"]}</h2>
            <div class="loern-grid">
                <div class="loern-feature">
                    <div class="loern-icon" aria-hidden="true">\u25a6</div>
                    <div>
                        <h3>{lp["feature_1_h3"]}</h3>
                        <p>{lp["feature_1_p"]}</p>
                    </div>
                </div>
                <div class="loern-feature">
                    <div class="loern-icon" aria-hidden="true">\u27b2</div>
                    <div>
                        <h3>{lp["feature_2_h3"]}</h3>
                        <p>{lp["feature_2_p"]}</p>
                    </div>
                </div>
                <div class="loern-feature">
                    <div class="loern-icon" aria-hidden="true">\u25a3</div>
                    <div>
                        <h3>{lp["feature_3_h3"]}</h3>
                        <p>{lp["feature_3_p"]}</p>
                    </div>
                </div>
                <div class="loern-feature">
                    <div class="loern-icon" aria-hidden="true">\u21c5</div>
                    <div>
                        <h3>{lp["feature_4_h3"]}</h3>
                        <p>{lp["feature_4_p"]}</p>
                    </div>
                </div>
                <div class="loern-feature">
                    <div class="loern-icon" aria-hidden="true">\u270e</div>
                    <div>
                        <h3>{lp["feature_5_h3"]}</h3>
                        <p>{lp["feature_5_p"]}</p>
                    </div>
                </div>
                <div class="loern-feature">
                    <div class="loern-icon" aria-hidden="true">\u2726</div>
                    <div>
                        <h3>{lp["feature_6_h3"]}</h3>
                        <p>{lp["feature_6_p"]}</p>
                    </div>
                </div>
            </div>
        </section>

        <section>
            <h2>{lp["screenshots_h2"]}</h2>
            <p>{lp["screenshots_p"]}</p>
            <div class="loern-screenshots">
                <div class="loern-shot"><img src="../../Screenshot_20260211_130442.png" alt="L\u0153rn screenshot" loading="lazy"></div>
                <div class="loern-shot"><img src="../../Screenshot_20260211_130532.png" alt="L\u0153rn screenshot" loading="lazy"></div>
                <div class="loern-shot"><img src="../../Screenshot_20260211_130551.png" alt="L\u0153rn screenshot" loading="lazy"></div>
                <div class="loern-shot"><img src="../../Screenshot_20260211_130638.png" alt="L\u0153rn screenshot" loading="lazy"></div>
                <div class="loern-shot"><img src="../../Screenshot_20260211_130711.png" alt="L\u0153rn screenshot" loading="lazy"></div>
            </div>
        </section>
    </main>

    <footer class="site-footer">
        <div class="footer-links">
            <a href="../legal/imprint.html">{t["footer_imprint"]}</a>
            <a href="../legal/privacy.html">{t["footer_privacy"]}</a>
        </div>
    </footer>
    <script src="../../site.js"></script>
{script}
</body>
</html>
'''


def make_loern_privacy(locale, t):
    """projects/loern/privacy.html fully localized for the new locales."""
    folder = LOCALE_DIRS[locale]
    lp = LOERN_PRIVACY_TRANSLATIONS[locale]
    sections = lp["sections"]
    page_nav = (
        f'                <option value="../../">{t["nav"]["home"]}</option>\n'
        f'                <option value="../../about.html">{t["nav"]["about"]}</option>\n'
        f'                <option value="../../projects.html">{t["nav"]["projects"]}</option>\n'
        f'                <option value="../../principles.html">{t["nav"]["principles"]}</option>\n'
        f'                <option value="../../contact.html">{t["nav"]["contact"]}</option>'
    )
    hdr = header_html(locale, t, "../../", page_nav)
    script = lang_switcher_script("projects/loern/privacy.html")
    return f'''\
<!DOCTYPE html>
<html lang="{t["lang_attr"]}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{lp["title"]} \u2013 L\u0153rn</title>
    <meta name="description" content="{lp["meta_desc"]}">
    <link rel="canonical" href="https://jetztunddahanna.com/{folder}/projects/loern/privacy.html">
    <link rel="stylesheet" href="../../../style.css">
</head>
<body>
{hdr}

    <main id="main" class="page narrow legal-content">
        <h1>{lp["h1"]}</h1>
        <p><em>{lp["updated"]}</em></p>
        
        <section>
            <h2>{sections["intro"][0]}</h2>
            <p>{sections["intro"][1][0]}</p>
            <p>{sections["intro"][1][1]}</p>
        </section>

        <section>
            <h2>{sections["core"][0]}</h2>
            <h3>{sections["core"][1]}</h3>
            <p>{sections["core"][2]}</p>
            <ul>
                <li>{sections["core"][3][0]}</li>
                <li>{sections["core"][3][1]}</li>
                <li>{sections["core"][3][2]}</li>
                <li>{sections["core"][3][3]}</li>
                <li>{sections["core"][3][4]}</li>
            </ul>
        </section>

        <section>
            <h2>{sections["not_collect"][0]}</h2>
            <p>{sections["not_collect"][1]}</p>
            <ul>
                <li>{sections["not_collect"][2][0]}</li>
                <li>{sections["not_collect"][2][1]}</li>
                <li>{sections["not_collect"][2][2]}</li>
                <li>{sections["not_collect"][2][3]}</li>
                <li>{sections["not_collect"][2][4]}</li>
                <li>{sections["not_collect"][2][5]}</li>
                <li>{sections["not_collect"][2][6]}</li>
                <li>{sections["not_collect"][2][7]}</li>
            </ul>
            <p>{sections["not_collect"][3]}</p>
        </section>

        <section>
            <h2>{sections["storage"][0]}</h2>
            <h3>{sections["storage"][1]}</h3>
            <p>{sections["storage"][2]}</p>
            <ul>
                <li>{sections["storage"][3][0]}</li>
                <li>{sections["storage"][3][1]}</li>
                <li>{sections["storage"][3][2]}</li>
                <li>{sections["storage"][3][3]}</li>
                <li>{sections["storage"][3][4]}</li>
            </ul>
            <p>{sections["storage"][4]}</p>

            <h3>{sections["storage"][5]}</h3>
            <p>{sections["storage"][6]}</p>
        </section>

        <section>
            <h2>{sections["internet"][0]}</h2>
            <h3>{sections["internet"][1]}</h3>
            <p>{sections["internet"][2]}</p>

            <h3>{sections["internet"][3]}</h3>
            <p>{sections["internet"][4]}</p>
            <ul>
                <li>{sections["internet"][5][0]}</li>
                <li>{sections["internet"][5][1]}</li>
                <li>{sections["internet"][5][2]}</li>
            </ul>
            <p>{sections["internet"][6]}</p>

            <h3>{sections["internet"][7]}</h3>
            <p>{sections["internet"][8]}</p>
            <ul>
                <li>{sections["internet"][9][0]}</li>
                <li>{sections["internet"][9][1]}</li>
                <li>{sections["internet"][9][2]}</li>
                <li>{sections["internet"][9][3]}</li>
            </ul>
            <p>{sections["internet"][10]} <a href="https://policies.google.com/privacy" class="text-link" target="_blank" rel="noopener noreferrer">https://policies.google.com/privacy</a></p>

            <h3>{sections["internet"][11]}</h3>
            <p>{sections["internet"][12]}</p>
            <ul>
                <li>{sections["internet"][13][0]}</li>
                <li>{sections["internet"][13][1]}</li>
                <li>{sections["internet"][13][2]}</li>
                <li>{sections["internet"][13][3]}</li>
            </ul>
        </section>

        <section>
            <h2>{sections["iap"][0]}</h2>
            <h3>{sections["iap"][1]}</h3>
            <p>{sections["iap"][2]}</p>
            <ul>
                <li>{sections["iap"][3][0]}</li>
                <li>{sections["iap"][3][1]}</li>
                <li>{sections["iap"][3][2]}</li>
            </ul>
            <p>{sections["iap"][4]}</p>
        </section>

        <section>
            <h2>{sections["share"][0]}</h2>
            <h3>{sections["share"][1]}</h3>
            <p>{sections["share"][2]}</p>
            <ul>
                <li>{sections["share"][3][0]}</li>
                <li>{sections["share"][3][1]}</li>
                <li>{sections["share"][3][2]}</li>
            </ul>

            <h3>{sections["share"][4]}</h3>
            <p>{sections["share"][5]}</p>
            <p>{sections["share"][6]}</p>
            <ul>
                <li>{sections["share"][7][0]}</li>
                <li>{sections["share"][7][1]}</li>
                <li>{sections["share"][7][2]}</li>
                <li>{sections["share"][7][3]}</li>
            </ul>
            <p>{sections["share"][8]}</p>

            <h3>{sections["share"][9]}</h3>
            <p>{sections["share"][10]}</p>
            <ul>
                <li>{sections["share"][11][0]}</li>
                <li>{sections["share"][11][1]}</li>
                <li>{sections["share"][11][2]}</li>
            </ul>
        </section>

        <section>
            <h2>{sections["profiles"][0]}</h2>
            <h3>{sections["profiles"][1]}</h3>
            <p>{sections["profiles"][2]}</p>
            <ul>
                <li>{sections["profiles"][3][0]}</li>
                <li>{sections["profiles"][3][1]}</li>
                <li>{sections["profiles"][3][2]}</li>
                <li>{sections["profiles"][3][3]}</li>
            </ul>

            <h3>{sections["profiles"][4]}</h3>
            <p>{sections["profiles"][5]}</p>
        </section>

        <section>
            <h2>{sections["notifications"][0]}</h2>
            <h3>{sections["notifications"][1]}</h3>
            <p>{sections["notifications"][2]}</p>
            <ul>
                <li>{sections["notifications"][3][0]}</li>
                <li>{sections["notifications"][3][1]}</li>
                <li>{sections["notifications"][3][2]}</li>
                <li>{sections["notifications"][3][3]}</li>
            </ul>
        </section>

        <section>
            <h2>{sections["permissions"][0]}</h2>
            <p>{sections["permissions"][1]}</p>
            
            <h3>{sections["permissions"][2]}</h3>
            <ul>
                <li>{sections["permissions"][3][0]}</li>
                <li>{sections["permissions"][3][1]}</li>
            </ul>

            <h3>{sections["permissions"][4]}</h3>
            <ul>
                <li>{sections["permissions"][5][0]}</li>
                <li>{sections["permissions"][5][1]}</li>
            </ul>

            <h3>{sections["permissions"][6]}</h3>
            <ul>
                <li>{sections["permissions"][7][0]}</li>
                <li>{sections["permissions"][7][1]}</li>
            </ul>
        </section>

        <section>
            <h2>{sections["third_party"][0]}</h2>
            <h3>{sections["third_party"][1]}</h3>
            <p>{sections["third_party"][2]}</p>
            <p>{sections["third_party"][3]}</p>
            <ul>
                <li>{sections["third_party"][4][0]}</li>
                <li>{sections["third_party"][4][1]}</li>
                <li>{sections["third_party"][4][2]}</li>
                <li>{sections["third_party"][4][3]}</li>
                <li>{sections["third_party"][4][4]}</li>
            </ul>
        </section>

        <section>
            <h2>{sections["children"][0]}</h2>
            <p>{sections["children"][1][0]}</p>
            <p>{sections["children"][1][1]}</p>
        </section>

        <section>
            <h2>{sections["security"][0]}</h2>
            <h3>{sections["security"][1]}</h3>
            <p>{sections["security"][2]}</p>
            <ul>
                <li>{sections["security"][3][0]}</li>
                <li>{sections["security"][3][1]}</li>
                <li>{sections["security"][3][2]}</li>
            </ul>

            <h3>{sections["security"][4]}</h3>
            <p>{sections["security"][5]}</p>
            <ul>
                <li>{sections["security"][6][0]}</li>
                <li>{sections["security"][6][1]}</li>
                <li>{sections["security"][6][2]}</li>
            </ul>

            <h3>{sections["security"][7]}</h3>
            <p>{sections["security"][8]}</p>
            <ul>
                <li>{sections["security"][9][0]}</li>
                <li>{sections["security"][9][1]}</li>
                <li>{sections["security"][9][2]}</li>
            </ul>
        </section>

        <section>
            <h2>{sections["rights"][0]}</h2>
            <p>{sections["rights"][1]}</p>
            <ul>
                <li>{sections["rights"][2][0]}</li>
                <li>{sections["rights"][2][1]}</li>
                <li>{sections["rights"][2][2]}</li>
                <li>{sections["rights"][2][3]}</li>
            </ul>
        </section>

        <section>
            <h2>{sections["retention"][0]}</h2>
            <h3>{sections["retention"][1]}</h3>
            <p>{sections["retention"][2]}</p>
            <ul>
                <li>{sections["retention"][3][0]}</li>
                <li>{sections["retention"][3][1]}</li>
                <li>{sections["retention"][3][2]}</li>
            </ul>

            <h3>{sections["retention"][4]}</h3>
            <p>{sections["retention"][5]}</p>

            <h3>{sections["retention"][6]}</h3>
            <p>{sections["retention"][7]}</p>
        </section>

        <section>
            <h2>{sections["gdpr"][0]}</h2>
            <p>{sections["gdpr"][1]}</p>
            <ul>
                <li>{sections["gdpr"][2][0]}</li>
                <li>{sections["gdpr"][2][1]}</li>
                <li>{sections["gdpr"][2][2]}</li>
            </ul>
        </section>

        <section>
            <h2>{sections["ccpa"][0]}</h2>
            <ul>
                <li>{sections["ccpa"][1][0]}</li>
                <li>{sections["ccpa"][1][1]}</li>
                <li>{sections["ccpa"][1][2]}</li>
            </ul>
        </section>

        <section>
            <h2>{sections["transfers"][0]}</h2>
            <p>{sections["transfers"][1]}</p>
            <ul>
                <li>{sections["transfers"][2][0]}</li>
                <li>{sections["transfers"][2][1]}</li>
                <li>{sections["transfers"][2][2]}</li>
            </ul>
        </section>

        <section>
            <h2>{sections["changes"][0]}</h2>
            <p>{sections["changes"][1][0]}</p>
            <p>{sections["changes"][1][1]}</p>
            <ul>
                <li>{sections["changes"][2][0]}</li>
                <li>{sections["changes"][2][1]}</li>
                <li>{sections["changes"][2][2]}</li>
            </ul>
        </section>

        <section>
            <h2>{sections["contact"][0]}</h2>
            <p>{sections["contact"][1]}</p>
            <p>
                Email: <a href="mailto:info@jetztunddahanna.com" class="text-link">info@jetztunddahanna.com</a><br>
                Website: <a href="https://jetztunddahanna.com" class="text-link">jetztunddahanna.com</a>
            </p>
            <p>{sections["contact"][2]}</p>
        </section>

        <section>
            <h2>{sections["commitment"][0]}</h2>
            <p>{sections["commitment"][1]}</p>
        </section>

        <section>
            <h2>{sections["summary"][0]}</h2>
            <ul>
                <li>{sections["summary"][1][0]}</li>
                <li>{sections["summary"][1][1]}</li>
                <li>{sections["summary"][1][2]}</li>
                <li>{sections["summary"][1][3]}</li>
                <li>{sections["summary"][1][4]}</li>
                <li>{sections["summary"][1][5]}</li>
                <li>{sections["summary"][1][6]}</li>
            </ul>
        </section>
    </main>

    <footer class="site-footer">
        <div class="footer-links">
            <a href="../../legal/imprint.html">{t["footer_imprint"]}</a>
            <a href="../../legal/privacy.html">{t["footer_privacy"]}</a>
        </div>
    </footer>
    <script src="../../../site.js"></script>
{script}
</body>
</html>
'''


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Written: {path.replace(BASE + '/', '')}")


def main():
    for locale in NEW_LOCALES:
        t = TRANSLATIONS[locale]
        folder = LOCALE_DIRS[locale]
        root = os.path.join(BASE, folder)
        print(f"\n--- Generating locale: {locale} -> {folder}/ ---")

        write(os.path.join(root, "index.html"), make_index(locale, t))
        write(os.path.join(root, "about.html"), make_about(locale, t))
        write(os.path.join(root, "principles.html"), make_principles(locale, t))
        write(os.path.join(root, "contact.html"), make_contact(locale, t))
        write(os.path.join(root, "projects.html"), make_projects(locale, t))
        write(os.path.join(root, "legal", "imprint.html"), make_imprint(locale, t))
        write(os.path.join(root, "legal", "privacy.html"), make_privacy_site(locale, t))
        write(os.path.join(root, "projects", "loern.html"), make_loern(locale, t))
        write(os.path.join(root, "projects", "loern", "privacy.html"), make_loern_privacy(locale, t))

    print("\nDone. All new locales generated.")


if __name__ == "__main__":
    main()
