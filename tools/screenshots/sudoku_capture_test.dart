import 'dart:io';
import 'dart:ui' as ui;

import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:sudoku/app/theme/app_theme.dart';
import 'package:sudoku/data/ads/ads_service_provider.dart';
import 'package:sudoku/data/ads/null_ads_service.dart';
import 'package:sudoku/app/theme/app_color_theme.dart';
import 'package:sudoku/features/game/game_notifier.dart';
import 'package:sudoku/features/game/game_screen.dart';
import 'package:sudoku/features/home/home_screen.dart';
import 'package:sudoku/features/settings/settings_notifier.dart';
import 'package:sudoku/features/difficulty_selection/difficulty_selection_screen.dart';
import 'package:sudoku/localization/l10n/app_localizations.dart';
import 'package:sudoku/domain/stats/player_settings.dart';
import 'package:sudoku/domain/sudoku/entities/sudoku_game_state.dart';
import 'package:sudoku/domain/sudoku/entities/sudoku_difficulty.dart';
import 'package:sudoku/domain/sudoku/use_cases/game_engine.dart';
import 'package:sudoku/data/sudoku/generator/puzzle_generator.dart';

late SudokuGameState sample;

class CaptureGame extends GameNotifier {
  @override
  SudokuGameState? build() => sample;
}

class CaptureSettings extends SettingsNotifier {
  @override
  PlayerSettings build() => PlayerSettings.defaults.copyWith(
    privacyAccepted: true,
    colorTheme: 'sage',
  );
}

Future<void> fonts() async {
  final root = Directory(
    '${Platform.environment['CAPTURE_FLUTTER_ROOT']!}/bin/cache/artifacts/material_fonts',
  );
  for (final name in ['Roboto', 'MaterialIcons']) {
    final loader = FontLoader(name);
    for (final f in root.listSync().whereType<File>().where(
      (f) => name == 'Roboto'
          ? f.path.contains('Roboto-')
          : f.path.contains('MaterialIcons-Regular'),
    )) {
      loader.addFont(Future.value(ByteData.sublistView(f.readAsBytesSync())));
    }
    await loader.load();
  }
}

void main() {
  testWidgets('render current app screens for website', (tester) async {
    await fonts();
    tester.view.physicalSize = const Size(1080, 2160);
    tester.view.devicePixelRatio = 2.5;
    final puzzle = PuzzleGenerator().generate(
      SudokuDifficulty.easy,
      seed: 721390,
    );
    sample = GameEngine.start(
      puzzle: puzzle,
      errorHighlightingEnabled: true,
      selectionHighlightingEnabled: true,
      automaticNoteRemovalEnabled: true,
      now: DateTime.now(),
    );
    sample = sample.copyWith(
      selectedCell: 40,
      elapsedActive: const Duration(minutes: 2, seconds: 18),
    );
    for (final language in [
      'de',
      'en',
      'fr',
      'es',
      'it',
      'nl',
      'pl',
      'pt-br',
    ]) {
      final locale = language == 'pt-br'
          ? const Locale('pt', 'BR')
          : Locale(language);
      for (final screen in ['game', 'home', 'difficulty']) {
        final key = GlobalKey();
        final dark = screen == 'home';
        await tester.pumpWidget(
          ProviderScope(
            overrides: [
              adsServiceProvider.overrideWithValue(const NullAdsService()),
              gameProvider.overrideWith(CaptureGame.new),
              settingsProvider.overrideWith(CaptureSettings.new),
            ],
            child: RepaintBoundary(
              key: key,
              child: MaterialApp(
                debugShowCheckedModeBanner: false,
                theme: dark
                    ? AppTheme.darkFor(AppColorTheme.sage)
                    : AppTheme.lightFor(AppColorTheme.sage),
                locale: locale,
                localizationsDelegates: const [
                  AppLocalizations.delegate,
                  GlobalMaterialLocalizations.delegate,
                  GlobalWidgetsLocalizations.delegate,
                  GlobalCupertinoLocalizations.delegate,
                ],
                supportedLocales: AppLocalizations.supportedLocales,
                home: switch (screen) {
                  'game' => const GameScreen(),
                  'home' => const HomeScreen(),
                  _ => const DifficultySelectionScreen(),
                },
              ),
            ),
          ),
        );
        await tester.pump();
        await tester.pump(const Duration(milliseconds: 500));
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
