import 'dart:io';
import 'dart:ui' as ui;

import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:mocktail/mocktail.dart';
import 'package:loern/l10n/app_localizations.dart';
import 'package:loern/presentation/theme/app_theme.dart';
import 'package:loern/presentation/blocs/session/session_bloc.dart';
import 'package:loern/presentation/blocs/session/session_state.dart';
import 'package:loern/presentation/bloc/premium/premium_bloc.dart';
import 'package:loern/presentation/pages/session/session_page.dart';
import 'package:loern/presentation/widgets/session/flashcard_renderer.dart';
import 'package:loern/presentation/pages/session/session_complete_page.dart';
import 'package:loern/domain/entities/deck.dart';
import 'package:loern/domain/entities/learning_progress_card.dart';
import 'package:loern/domain/entities/learning_items/flashcard_item.dart';
import 'package:loern/domain/entities/learning_items/multiple_choice_item.dart';

class CaptureSession extends Mock implements SessionBloc {}

class CapturePremium extends Mock implements PremiumBloc {}

final examples = <String, List<String>>{
  'de': [
    'Unser Sonnensystem',
    'Warum gibt es auf der Erde Jahreszeiten?',
    'Die Erdachse ist geneigt. Dadurch treffen die Sonnenstrahlen im Laufe des Jahres unterschiedlich auf die Erdoberfläche.',
    'Welcher Planet ist für seinen Großen Roten Fleck bekannt?',
    'Mars',
    'Jupiter',
    'Saturn',
    'Venus',
  ],
  'en': [
    'Our solar system',
    'Why does Earth have seasons?',
    'Earth’s axis is tilted. This changes the angle of sunlight and the length of our days throughout the year.',
    'Which planet is known for its Great Red Spot?',
    'Mars',
    'Jupiter',
    'Saturn',
    'Venus',
  ],
  'fr': [
    'Notre système solaire',
    'Pourquoi y a-t-il des saisons sur Terre ?',
    'L’axe de la Terre est incliné. L’angle des rayons du Soleil et la durée du jour varient donc au fil de l’année.',
    'Quelle planète est connue pour sa Grande Tache rouge ?',
    'Mars',
    'Jupiter',
    'Saturne',
    'Vénus',
  ],
  'es': [
    'Nuestro sistema solar',
    '¿Por qué hay estaciones en la Tierra?',
    'El eje de la Tierra está inclinado. Por eso, el ángulo de la luz solar y la duración de los días cambian durante el año.',
    '¿Qué planeta es conocido por su Gran Mancha Roja?',
    'Marte',
    'Júpiter',
    'Saturno',
    'Venus',
  ],
  'it': [
    'Il nostro sistema solare',
    'Perché sulla Terra ci sono le stagioni?',
    'L’asse terrestre è inclinato. Per questo l’angolo della luce solare e la durata del giorno cambiano durante l’anno.',
    'Quale pianeta è noto per la Grande Macchia Rossa?',
    'Marte',
    'Giove',
    'Saturno',
    'Venere',
  ],
  'nl': [
    'Ons zonnestelsel',
    'Waarom heeft de aarde seizoenen?',
    'De aardas staat schuin. Daardoor veranderen de invalshoek van het zonlicht en de lengte van de dagen gedurende het jaar.',
    'Welke planeet staat bekend om de Grote Rode Vlek?',
    'Mars',
    'Jupiter',
    'Saturnus',
    'Venus',
  ],
  'sv': [
    'Vårt solsystem',
    'Varför har jorden årstider?',
    'Jordaxeln lutar. Därför förändras solljusets vinkel och dagarnas längd under året.',
    'Vilken planet är känd för sin stora röda fläck?',
    'Mars',
    'Jupiter',
    'Saturnus',
    'Venus',
  ],
  'pl': [
    'Nasz Układ Słoneczny',
    'Dlaczego na Ziemi występują pory roku?',
    'Oś Ziemi jest nachylona. Dlatego kąt padania promieni słonecznych i długość dnia zmieniają się w ciągu roku.',
    'Która planeta jest znana z Wielkiej Czerwonej Plamy?',
    'Mars',
    'Jowisz',
    'Saturn',
    'Wenus',
  ],
  'pt-br': [
    'Nosso Sistema Solar',
    'Por que a Terra tem estações do ano?',
    'O eixo da Terra é inclinado. Por isso, o ângulo da luz solar e a duração dos dias mudam ao longo do ano.',
    'Qual planeta é conhecido pela Grande Mancha Vermelha?',
    'Marte',
    'Júpiter',
    'Saturno',
    'Vênus',
  ],
  'pt-pt': [
    'O nosso Sistema Solar',
    'Porque existem estações do ano na Terra?',
    'O eixo da Terra é inclinado. Por isso, o ângulo da luz solar e a duração dos dias mudam ao longo do ano.',
    'Que planeta é conhecido pela Grande Mancha Vermelha?',
    'Marte',
    'Júpiter',
    'Saturno',
    'Vénus',
  ],
};
Future<void> fonts() async {
  final f = FontLoader('Roboto')
    ..addFont(
      Future.value(
        ByteData.sublistView(
          File(
            '${Platform.environment['CAPTURE_FLUTTER_ROOT']!}/bin/cache/artifacts/material_fonts/Roboto-Regular.ttf',
          ).readAsBytesSync(),
        ),
      ),
    );
  await f.load();
  final inter = FontLoader('Inter')
    ..addFont(
      Future.value(
        ByteData.sublistView(
          File(
            '${Platform.environment['CAPTURE_FLUTTER_ROOT']!}/bin/cache/artifacts/material_fonts/Roboto-Regular.ttf',
          ).readAsBytesSync(),
        ),
      ),
    );
  await inter.load();
  final emoji = FontLoader('Noto Color Emoji')
    ..addFont(
      Future.value(
        ByteData.sublistView(
          File('/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf')
              .readAsBytesSync(),
        ),
      ),
    );
  await emoji.load();
  final icons = FontLoader('MaterialIcons')
    ..addFont(
      Future.value(
        ByteData.sublistView(
          File(
            '${Platform.environment['CAPTURE_FLUTTER_ROOT']!}/bin/cache/artifacts/material_fonts/MaterialIcons-Regular.otf',
          ).readAsBytesSync(),
        ),
      ),
    );
  await icons.load();
}

void main() {
  testWidgets('render current app screens for website', (tester) async {
    await fonts();
    tester.view.physicalSize = const Size(1080, 2160);
    tester.view.devicePixelRatio = 2.5;
    for (final entry in examples.entries) {
      final language = entry.key, c = entry.value;
      final now = DateTime.now();
      final deck = Deck(id: 1, profileId: 1, name: c[0], importedAt: now);
      for (final screen in ['flashcard', 'choice', 'result']) {
        final session = CaptureSession(), premium = CapturePremium();
        final item = screen == 'choice'
            ? MultipleChoiceItem(
                id: 2,
                deckId: 1,
                question: c[3],
                options: c.sublist(4),
                correctIndices: const [1],
                createdAt: now,
              )
            : FlashcardItem(
                id: 1,
                deckId: 1,
                front: c[1],
                back: c[2],
                createdAt: now,
              );
        final SessionState state = screen == 'result'
            ? SessionCompleted(
                deck: deck,
                statistics: const SessionStatistics(
                  totalReviewed: 12,
                  againCount: 2,
                  goodCount: 10,
                  duration: Duration(minutes: 4, seconds: 32),
                  accuracy: 10 / 12,
                ),
              )
            : SessionInProgress(
                deck: deck,
                currentItem: item,
                currentCard: const LearningProgressCard(
                  learningItemId: 1,
                  profileId: 1,
                ),
                currentIndex: 4,
                totalCards: 12,
                reviewedCount: 4,
                againCount: 1,
                goodCount: 3,
                sessionStartTime: now.subtract(
                  const Duration(minutes: 2, seconds: 14),
                ),
                sessionDurationMinutes: 10,
                noTimeLimit: false,
              );
        when(() => session.state).thenReturn(state);
        when(() => session.stream).thenAnswer((_) => const Stream.empty());
        when(() => premium.state).thenReturn(PremiumInactive());
        when(() => premium.stream).thenAnswer((_) => const Stream.empty());
        final locale = language == 'pt-br'
            ? const Locale('pt', 'BR')
            : language == 'pt-pt'
            ? const Locale('pt')
            : Locale(language);
        final key = GlobalKey();
        await tester.pumpWidget(
          MultiBlocProvider(
            providers: [
              BlocProvider<SessionBloc>.value(value: session),
              BlocProvider<PremiumBloc>.value(value: premium),
            ],
            child: RepaintBoundary(
              key: key,
              child: MaterialApp(
                debugShowCheckedModeBanner: false,
                theme: (screen == 'result' ? AppTheme.dark() : AppTheme.light())
                    .copyWith(
                      textTheme:
                          (screen == 'result'
                                  ? AppTheme.dark()
                                  : AppTheme.light())
                              .textTheme
                              .apply(
                                fontFamily: 'Roboto',
                                fontFamilyFallback: const ['Noto Color Emoji'],
                              ),
                    ),
                locale: locale,
                localizationsDelegates: AppLocalizations.localizationsDelegates,
                supportedLocales: AppLocalizations.supportedLocales,
                home: screen == 'result'
                    ? const SessionCompletePage(deckId: 1)
                    : const SessionPage(deckId: 1),
              ),
            ),
          ),
        );
        await tester.pump();
        await tester.pump(const Duration(seconds: 3));
        await tester.pump();
        if (screen == 'flashcard') {
          await tester.tap(find.byType(FlashcardRenderer));
          await tester.pump();
          await tester.pump(const Duration(milliseconds: 500));
        }
        expect(tester.takeException(), isNull);
        final image = await tester.runAsync(
          () =>
              (key.currentContext!.findRenderObject() as RenderRepaintBoundary)
                  .toImage(pixelRatio: 2.5),
        );
        await expectLater(
          image,
          matchesGoldenFile('../build/website/$language/$screen.png'),
        );
        print('SAVED $language/$screen');
        await tester.pumpWidget(const SizedBox.shrink());
        await tester.pump();
        print('DISPOSED $language/$screen');
      }
    }
  });
}
